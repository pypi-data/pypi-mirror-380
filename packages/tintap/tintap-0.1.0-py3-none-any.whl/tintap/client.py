"""
tintap Python SDK Client

Main client class for interacting with the tintap AI audio detection API.
"""

import os
import requests
from typing import Union, Dict, Any, Optional, BinaryIO
from pathlib import Path

from .exceptions import (
    TintapError,
    TintapAPIError, 
    TintapConnectionError,
    TintapAuthError,
    TintapRateLimitError,
    TintapValidationError,
)


class TintapClient:
    """
    Client for tintap AI audio detection API.
    
    Provides methods to analyze audio files for AI-generated content detection.
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        endpoint: str = "http://localhost:3005/api",
        timeout: int = 120
    ):
        """
        Initialize the tintap client.
        
        Args:
            api_key: Your tintap API key. If not provided, will look for TINTAP_API_KEY env var.
            endpoint: API endpoint URL. Defaults to localhost:3005.
            timeout: Request timeout in seconds. Defaults to 120.
        """
        self.api_key = api_key or os.getenv("TINTAP_API_KEY")
        self.endpoint = endpoint.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set default headers
        if self.api_key:
            self.session.headers.update({
                "X-API-Key": self.api_key
            })
    
    def analyze_audio(
        self, 
        audio_file: Union[str, Path, BinaryIO, bytes],
        filename: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Analyze an audio file for AI-generated content detection.
        
        Args:
            audio_file: Path to audio file, file object, or bytes data
            filename: Filename for the audio file (required if passing bytes/file object)
            
        Returns:
            Dictionary containing analysis results with percentages and segments
            
        Raises:
            TintapAuthError: If API key is invalid
            TintapValidationError: If input parameters are invalid  
            TintapAPIError: If API returns an error
            TintapConnectionError: If connection fails
        """
        if not self.api_key:
            raise TintapAuthError("API key is required. Get one at https://tintap.ai")
        
        try:
            # Prepare file data
            files = self._prepare_file_data(audio_file, filename)
            
            # Make API request
            response = self.session.post(
                f"{self.endpoint}/analyze",
                files=files,
                timeout=self.timeout
            )
            
            # Handle response
            return self._handle_response(response)
            
        except requests.exceptions.ConnectionError as e:
            raise TintapConnectionError(f"Failed to connect to API: {str(e)}")
        except requests.exceptions.Timeout as e:
            raise TintapConnectionError(f"Request timeout: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise TintapConnectionError(f"Request failed: {str(e)}")
    
    def get_analysis(self, analysis_id: str) -> Dict[str, Any]:
        """
        Get analysis results by ID.
        
        Args:
            analysis_id: The analysis ID
            
        Returns:
            Dictionary containing analysis results
            
        Raises:
            TintapAuthError: If API key is invalid
            TintapAPIError: If API returns an error
            TintapConnectionError: If connection fails
        """
        if not self.api_key:
            raise TintapAuthError("API key is required. Get one at https://tintap.ai")
        
        try:
            response = self.session.get(
                f"{self.endpoint}/status/{analysis_id}",
                timeout=self.timeout
            )
            
            return self._handle_response(response)
            
        except requests.exceptions.ConnectionError as e:
            raise TintapConnectionError(f"Failed to connect to API: {str(e)}")
        except requests.exceptions.Timeout as e:
            raise TintapConnectionError(f"Request timeout: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise TintapConnectionError(f"Request failed: {str(e)}")
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get API information and health status.
        
        Returns:
            Dictionary containing API information
            
        Raises:
            TintapConnectionError: If connection fails
        """
        try:
            response = self.session.get(
                f"{self.endpoint}/info",
                timeout=30
            )
            
            return self._handle_response(response, require_auth=False)
            
        except requests.exceptions.ConnectionError as e:
            raise TintapConnectionError(f"Failed to connect to API: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise TintapConnectionError(f"Request failed: {str(e)}")
    
    def test_connection(self) -> bool:
        """
        Test connection to the API server.
        
        Returns:
            True if connection is successful, False otherwise
        """
        try:
            health_endpoint = self.endpoint.replace("/api", "/health")
            response = requests.get(health_endpoint, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def _prepare_file_data(
        self, 
        audio_file: Union[str, Path, BinaryIO, bytes],
        filename: Optional[str] = None
    ) -> Dict[str, tuple]:
        """Prepare file data for upload."""
        
        if isinstance(audio_file, (str, Path)):
            # File path
            file_path = Path(audio_file)
            if not file_path.exists():
                raise TintapValidationError(f"File not found: {file_path}")
            
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            filename = filename or file_path.name
            
        elif isinstance(audio_file, bytes):
            # Bytes data
            if not filename:
                raise TintapValidationError("Filename is required when passing bytes data")
            file_data = audio_file
            
        elif hasattr(audio_file, 'read'):
            # File-like object
            if not filename:
                filename = getattr(audio_file, 'name', 'audio_file')
            file_data = audio_file.read()
            
        else:
            raise TintapValidationError(
                "audio_file must be a file path, bytes data, or file-like object"
            )
        
        return {
            'file': (filename, file_data, 'audio/*')
        }
    
    def _handle_response(
        self, 
        response: requests.Response,
        require_auth: bool = True
    ) -> Dict[str, Any]:
        """Handle API response and raise appropriate exceptions."""
        
        if response.status_code == 401 and require_auth:
            raise TintapAuthError("Invalid API key")
        
        elif response.status_code == 429:
            raise TintapRateLimitError("Rate limit exceeded")
        
        elif response.status_code == 400:
            try:
                error_data = response.json()
                message = error_data.get("message", "Bad request")
            except:
                message = "Bad request"
            raise TintapValidationError(message)
        
        elif not response.ok:
            try:
                error_data = response.json()
                message = error_data.get("message", f"HTTP {response.status_code}")
            except:
                message = f"HTTP {response.status_code}: {response.reason}"
            
            raise TintapAPIError(
                message, 
                status_code=response.status_code,
                response=response
            )
        
        try:
            return response.json()
        except ValueError:
            raise TintapAPIError("Invalid JSON response from API")


def create_client(
    api_key: Optional[str] = None,
    endpoint: str = "http://localhost:3005/api", 
    timeout: int = 120
) -> TintapClient:
    """
    Create a new tintap client instance.
    
    Args:
        api_key: Your tintap API key
        endpoint: API endpoint URL
        timeout: Request timeout in seconds
        
    Returns:
        TintapClient instance
    """
    return TintapClient(api_key=api_key, endpoint=endpoint, timeout=timeout)