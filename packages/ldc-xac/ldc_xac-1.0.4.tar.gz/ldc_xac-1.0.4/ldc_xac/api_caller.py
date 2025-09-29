"""
External API Caller module for making HTTP requests with comprehensive logging.
"""

import json
import logging
import time
from typing import Dict, Optional
import requests
from .constants import ExternalAPILoggingConstants
from .config import MAX_REQUEST_BODY_SIZE

logger = logging.getLogger("ldc_xac")


class ExternalAPICaller:
    """
    A utility class for logging external API calls with request and response details.

    This class provides methods to log external API requests and responses in a structured format
    that matches the required logging schema for external APIs.
    """
    
    @staticmethod
    def _truncate_large_data(data, max_size=MAX_REQUEST_BODY_SIZE):
        """
        Truncate large data for logging purposes.
        
        Args:
            data: The data to potentially truncate
            max_size: Maximum size in characters
            
        Returns:
            str: Truncated data with indication if it was truncated
        """
        if data is None:
            return None
            
        data_str = str(data)
        if len(data_str) <= max_size:
            return data_str
        
        # Truncate and add indication
        truncated = data_str[:max_size]
        return f"{truncated}... [TRUNCATED - Original size: {len(data_str)} characters]"
    
    @staticmethod
    def log_external_api_request(
        url: str,
        method: str = "GET",
        api_code: Optional[str] = None,
        system: Optional[str] = None
    ) -> float:
        """
        Log external API request details.

        Args:
            url: The API endpoint URL
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            api_code: Custom API code identifier
            system: System identifier (e.g., "LDCS_LOS", "CRIF", "FMPP")

        Returns:
            float: Start time for calculating duration
        """
        start_time = time.time()

        try:
            # Prepare request log data
            request_log = {
                "descr": ExternalAPILoggingConstants.EXTERNAL_REQUEST,
                "system": system or ExternalAPILoggingConstants.EXTERNAL_SYSTEM,
                "api_code": api_code or ExternalAPILoggingConstants.API_CALL,
                "request_method": method.upper(),
                "request_url": url
            }

            logger.info(json.dumps(request_log))
        except Exception as e:
            # Logging should never break the main functionality
            logger.error(f"Failed to log external API request: {str(e)}")
        
        return start_time

    @staticmethod
    def log_external_api_response(
        url: str,
        response: requests.Response,
        start_time: float,
        api_code: Optional[str] = None,
        system: Optional[str] = None,
        params: Optional[Dict] = None,
        **kwargs
    ) -> None:
        """
        Log external API response details.

        Args:
            url: The API endpoint URL
            response: The requests.Response object
            start_time: Start time from log_external_api_request
            api_code: Custom API code identifier
            system: System identifier
            params: Request parameters
            **kwargs: Additional request arguments
        """
        try:
            end_time = time.time()
            time_taken_ms = round((end_time - start_time) * 1000, 2)

            # Prepare response log data
            response_log = {
                "descr": ExternalAPILoggingConstants.EXTERNAL_RESPONSE,
                "system": system or ExternalAPILoggingConstants.EXTERNAL_SYSTEM,
                "api_code": api_code or ExternalAPILoggingConstants.API_CALL,
                "response_code": response.status_code,
                "response_for_request": url,
                "time_taken_ms": time_taken_ms
            }

            # Log as warning if response code is 400 or above
            if response.status_code >= 400:
                # Log the entire original request data with size limits
                request_data = {}
                if params:
                    request_data['params'] = params
                if 'json' in kwargs:
                    request_data['json'] = ExternalAPICaller._truncate_large_data(kwargs['json'])
                if 'data' in kwargs:
                    request_data['data'] = ExternalAPICaller._truncate_large_data(kwargs['data'])
                
                response_log['request_data'] = request_data
                logger.warning(json.dumps(response_log))
            else:
                logger.info(json.dumps(response_log))
        except Exception as e:
            # Logging should never break the main functionality
            logger.error(f"Failed to log external API response: {str(e)}")
    
    @staticmethod
    def log_external_api_error(
        url: str,
        error: Exception,
        start_time: float,
        api_code: Optional[str] = None,
        system: Optional[str] = None
    ) -> None:
        """
        Log external API error details.

        Args:
            url: The API endpoint URL
            error: The exception that occurred
            start_time: Start time from log_external_api_request
            api_code: Custom API code identifier
            system: System identifier
        """
        try:
            end_time = time.time()
            time_taken_ms = round((end_time - start_time) * 1000, 2)

            # Prepare error log data
            error_log = {
                "descr": ExternalAPILoggingConstants.EXTERNAL_ERROR,
                "system": system or ExternalAPILoggingConstants.EXTERNAL_SYSTEM,
                "api_code": api_code or ExternalAPILoggingConstants.API_CALL,
                "response_code": None,
                "response_for_request": url,
                "time_taken_ms": time_taken_ms,
                "error_message": str(error),
                "error_type": type(error).__name__
            }

            logger.error(json.dumps(error_log))
        except Exception as e:
            # Logging should never break the main functionality
            logger.error(f"Failed to log external API error: {str(e)}")


def make_external_api_request(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict] = None,
    timeout: Optional[int] = 300,
    api_code: Optional[str] = None,
    system: Optional[str] = None,
    verify: bool = True,
    **kwargs
) -> requests.Response:
    """
    Make an external API request with comprehensive logging.

    Args:
        url: The API endpoint URL
        method: HTTP method (GET, POST, PUT, DELETE, etc.)
        headers: Request headers
        params: Query parameters
        timeout: Request timeout in seconds
        api_code: Custom API code identifier
        system: System identifier
        verify: SSL certificate verification (default: True)
        **kwargs: Additional arguments passed to requests.request

    Returns:
        requests.Response: The response object

    Raises:
        Exception: Any exception that occurs during the request
    """
    # Log request
    start_time = ExternalAPICaller.log_external_api_request(
        url=url,
        method=method,
        api_code=api_code,
        system=system
    )

    response = None
    try:
        # Make the request
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            verify=verify,
            **kwargs
        )

        # Log response
        ExternalAPICaller.log_external_api_response(
            url=url,
            response=response,
            start_time=start_time,
            api_code=api_code,
            system=system,
            params=params,
            **kwargs
        )

        return response

    except Exception as e:
        # Log error
        ExternalAPICaller.log_external_api_error(
            url=url,
            error=e,
            start_time=start_time,
            api_code=api_code,
            system=system
        )
        raise
