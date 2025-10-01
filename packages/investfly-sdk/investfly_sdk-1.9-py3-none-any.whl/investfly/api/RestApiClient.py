import logging
import warnings
import json
import time
from typing import Dict, Any, Optional, Union

import requests
from requests import Response

from investfly.models.CommonModels import Session

warnings.simplefilter("ignore")


class RestApiClient:

    """
    Internal class to make REST API requests. Users of the SDK do not use this class directly.
    Please use investfly.api.InvestflyApiClient` instead
    """

    # Timeout constant for all HTTP requests (connection, read, etc.)
    DEFAULT_TIMEOUT: float = 10.0

    def __init__(self, baseUrl: str, logEnabled: bool = False) -> None:
        self.headers: Dict[str, str] = {}
        self.headers['client-mode'] = 'api'
        self.baseUrl = baseUrl
        self.logEnabled = logEnabled
        self.log = logging.getLogger(self.__class__.__name__)

    def _log_request(self, method: str, url: str, headers: Dict[str, str], 
                    auth: Optional[tuple] = None,
                    data: Optional[Union[str, Dict[str, Any]]] = None,
                    json_data: Optional[Dict[str, Any]] = None) -> None:
        """Log HTTP request details"""
        if not self.logEnabled:
            return
            
        log_data = {
            "method": method.upper(),
            "url": url,
            "headers": headers,
            "auth": "***" if auth else None,
            "data": data,
            "json": json_data
        }
        
        # Remove sensitive headers from logging
        sensitive_headers = ['investfly-client-token', 'authorization']
        safe_headers = {k: v for k, v in headers.items() 
                       if k.lower() not in sensitive_headers}
        log_data["headers"] = safe_headers
        
        self.log.info(f"HTTP REQUEST: {json.dumps(log_data, indent=2, default=str)}")
    
    def _log_response(self, response: Response, response_time: float) -> None:
        """Log HTTP response details"""
        if not self.logEnabled:
            return
            
        try:
            # Check if response is JSON based on content-type
            content_type = response.headers.get('content-type', '').lower()
            if 'application/json' in content_type:
                try:
                    # Parse JSON and store as object (not string) for proper formatting
                    response_body = response.json()
                except (json.JSONDecodeError, ValueError):
                    # Keep as text if JSON parsing fails
                    response_body = response.text
            else:
                # For non-JSON responses, keep as text
                response_body = response.text
        except Exception as e:
            response_body = f"<Error reading response body: {str(e)}>"
        
        # Remove sensitive headers from response logging
        safe_response_headers = dict(response.headers)
        sensitive_response_headers = ['investfly-client-token', 'investfly-client-id']
        for header in sensitive_response_headers:
            if header in safe_response_headers:
                safe_response_headers[header] = "***"
        
        log_data = {
            "status_code": response.status_code,
            "headers": safe_response_headers,
            "response_time_ms": round(response_time * 1000, 2),
            "body": response_body
        }
        
        self.log.info(f"HTTP RESPONSE: {json.dumps(log_data, indent=2, default=str)}")

    def login(self, username: str, password: str) -> Session:
        url = self.baseUrl + "/user/login"
        auth = (username, password)
        self._log_request("POST", url, self.headers, auth=auth)
        
        start_time = time.time()
        try:
            res = requests.post(url, auth=auth, headers=self.headers, verify=False, timeout=self.DEFAULT_TIMEOUT)
            response_time = time.time() - start_time
            self._log_response(res, response_time)
            
            if res.status_code == 200:
                self.headers['investfly-client-id'] = res.headers['investfly-client-id']
                self.headers['investfly-client-token'] = res.headers['investfly-client-token']
                dict_obj = res.json()
                session = Session.fromJsonDict(dict_obj)
                return session
            else:
                raise RestApiClient.getException(res)
        except Exception as e:
            response_time = time.time() - start_time
            if self.logEnabled:
                self.log.error(f"HTTP REQUEST FAILED: {str(e)} (after {round(response_time * 1000, 2)}ms)")
            raise

    def logout(self):
        url = self.baseUrl + "/user/logout"
        self._log_request("POST", url, self.headers)
        
        start_time = time.time()
        try:
            res = requests.post(url, headers=self.headers, verify=False, timeout=self.DEFAULT_TIMEOUT)
            response_time = time.time() - start_time
            self._log_response(res, response_time)
            
            del self.headers['investfly-client-id']
            del self.headers['investfly-client-token']
        except Exception as e:
            response_time = time.time() - start_time
            if self.logEnabled:
                self.log.error(f"HTTP REQUEST FAILED: {str(e)} (after {round(response_time * 1000, 2)}ms)")
            # Still try to clean up headers even if request failed
            if 'investfly-client-id' in self.headers:
                del self.headers['investfly-client-id']
            if 'investfly-client-token' in self.headers:
                del self.headers['investfly-client-token']
            raise

    def doGet(self, url: str) -> Any:
        full_url = self.baseUrl + url
        self._log_request("GET", full_url, self.headers)
        
        start_time = time.time()
        try:
            res = requests.get(full_url, headers=self.headers, verify=False, timeout=self.DEFAULT_TIMEOUT)
            response_time = time.time() - start_time
            self._log_response(res, response_time)
            
            # This does not actually return JSON string, but instead returns Python Dictionary/List etc
            if res.status_code == 200:
                contentType: str = res.headers['Content-Type']
                if "json" in contentType:
                    return res.json()
                else:
                    return res.text
            else:
                raise RestApiClient.getException(res)
        except Exception as e:
            response_time = time.time() - start_time
            if self.logEnabled:
                self.log.error(f"HTTP REQUEST FAILED: {str(e)} (after {round(response_time * 1000, 2)}ms)")
            raise

    def doPost(self, url: str, obj: Dict[str, Any]) -> Any:
        full_url = self.baseUrl + url
        self._log_request("POST", full_url, self.headers, json_data=obj)
        
        start_time = time.time()
        try:
            res: Response = requests.post(full_url, json=obj, headers=self.headers, verify=False, timeout=self.DEFAULT_TIMEOUT)
            response_time = time.time() - start_time
            self._log_response(res, response_time)
            
            if res.status_code == 200:
                contentType: str = res.headers['Content-Type']
                if "json" in contentType:
                    return res.json()
                else:
                    return res.text
            else:
                raise RestApiClient.getException(res)
        except Exception as e:
            response_time = time.time() - start_time
            if self.logEnabled:
                self.log.error(f"HTTP REQUEST FAILED: {str(e)} (after {round(response_time * 1000, 2)}ms)")
            raise
        
    def doPostCode(self, url: str, code: str) -> Any:
        full_url = self.baseUrl + url
        self._log_request("POST", full_url, self.headers, data=code)
        
        start_time = time.time()
        try:
            res: Response = requests.post(full_url, data=code, headers=self.headers, verify=False, timeout=self.DEFAULT_TIMEOUT)
            response_time = time.time() - start_time
            self._log_response(res, response_time)
            
            if res.status_code == 200:
                contentType: str = res.headers['Content-Type']
                if "json" in contentType:
                    return res.json()
                else:
                    return res.text
            else:
                raise RestApiClient.getException(res)
        except Exception as e:
            response_time = time.time() - start_time
            if self.logEnabled:
                self.log.error(f"HTTP REQUEST FAILED: {str(e)} (after {round(response_time * 1000, 2)}ms)")
            raise

    @staticmethod
    def getException(res: Response):
        try:
            # Server returns valid JSON in case of any exceptions that may occor while processing request
            errorObj: Dict[str, Any] = res.json()
            if 'message' in errorObj.keys():
                return Exception(errorObj.get('message'))
            else:
                return Exception(str(errorObj))
        except requests.exceptions.JSONDecodeError:
            # Just in case, there are other errors
            return Exception(res.text)
