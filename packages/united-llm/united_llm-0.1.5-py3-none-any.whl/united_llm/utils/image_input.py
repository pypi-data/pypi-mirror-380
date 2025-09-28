#!/usr/bin/env python3
"""
ImageInput utility for handling various image data formats in vision-enabled LLM operations.

Based on the united-llm_original implementation with simplified interface.
"""

import base64
import mimetypes
from pathlib import Path
from typing import Union, Optional
import requests
from urllib.parse import urlparse


class ImageInput:
    """
    Handles various image data formats for vision-enabled LLM operations.
    
    Supports:
    - URLs (http/https)
    - File paths (local files)
    - Base64 encoded data
    - Raw bytes
    """
    
    def __init__(self, data: Union[str, bytes], mime_type: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None):
        """
        Initialize ImageInput with image data.
        
        Args:
            data: Image data (URL, file path, base64 string, or bytes)
            mime_type: MIME type of the image (auto-detected if not provided)
            name: Optional name for the image
            description: Optional description of the image
        """
        self.name = name
        self.description = description
        self._original_data = data
        
        # Process the data and determine MIME type
        self.base64_data, self.mime_type = self._process_data(data, mime_type)
    
    def _process_data(self, data: Union[str, bytes], mime_type: Optional[str] = None) -> tuple[str, str]:
        """
        Process input data and convert to base64 format.
        
        Args:
            data: Input image data
            mime_type: Optional MIME type
            
        Returns:
            Tuple of (base64_data, mime_type)
        """
        if isinstance(data, bytes):
            # Raw bytes data
            b64_data = base64.b64encode(data).decode('utf-8')
            detected_mime = mime_type or 'image/jpeg'  # Default fallback
            return b64_data, detected_mime
        
        elif isinstance(data, str):
            # Check if it's a URL
            if data.startswith(('http://', 'https://')):
                return self._load_from_url(data, mime_type)
            
            # Check if it's a file path
            elif Path(data).exists():
                return self._load_from_file(data, mime_type)
            
            # Assume it's base64 data
            else:
                detected_mime = mime_type or 'image/jpeg'  # Default fallback
                # Validate base64 format
                try:
                    base64.b64decode(data)
                    return data, detected_mime
                except Exception as e:
                    raise ValueError(f"Invalid base64 data: {e}")
        
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")
    
    def _load_from_url(self, url: str, mime_type: Optional[str] = None) -> tuple[str, str]:
        """
        Load image from URL and convert to base64.
        
        Args:
            url: Image URL
            mime_type: Optional MIME type
            
        Returns:
            Tuple of (base64_data, mime_type)
        """
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Get MIME type from response headers or guess from URL
            if mime_type:
                detected_mime = mime_type
            else:
                detected_mime = response.headers.get('content-type', '')
                if not detected_mime or not detected_mime.startswith('image/'):
                    # Guess from URL extension
                    parsed_url = urlparse(url)
                    detected_mime, _ = mimetypes.guess_type(parsed_url.path)
                    detected_mime = detected_mime or 'image/jpeg'
            
            # Convert to base64
            b64_data = base64.b64encode(response.content).decode('utf-8')
            return b64_data, detected_mime
            
        except Exception as e:
            raise ValueError(f"Failed to load image from URL {url}: {e}")
    
    def _load_from_file(self, file_path: str, mime_type: Optional[str] = None) -> tuple[str, str]:
        """
        Load image from local file and convert to base64.
        
        Args:
            file_path: Path to image file
            mime_type: Optional MIME type
            
        Returns:
            Tuple of (base64_data, mime_type)
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"Image file not found: {file_path}")
            
            # Read file content
            with open(path, 'rb') as f:
                image_data = f.read()
            
            # Determine MIME type
            if mime_type:
                detected_mime = mime_type
            else:
                detected_mime, _ = mimetypes.guess_type(str(path))
                detected_mime = detected_mime or 'image/jpeg'
            
            # Convert to base64
            b64_data = base64.b64encode(image_data).decode('utf-8')
            return b64_data, detected_mime
            
        except Exception as e:
            raise ValueError(f"Failed to load image from file {file_path}: {e}")
    
    @classmethod
    def from_url(cls, url: str, name: Optional[str] = None, description: Optional[str] = None) -> 'ImageInput':
        """
        Create ImageInput from URL.
        
        Args:
            url: Image URL
            name: Optional name for the image
            description: Optional description
            
        Returns:
            ImageInput instance
        """
        return cls(data=url, name=name, description=description)
    
    @classmethod
    def from_file(cls, file_path: str, name: Optional[str] = None, description: Optional[str] = None) -> 'ImageInput':
        """
        Create ImageInput from local file.
        
        Args:
            file_path: Path to image file
            name: Optional name for the image
            description: Optional description
            
        Returns:
            ImageInput instance
        """
        return cls(data=file_path, name=name, description=description)
    
    @classmethod
    def from_base64(cls, base64_data: str, mime_type: str, name: Optional[str] = None, description: Optional[str] = None) -> 'ImageInput':
        """
        Create ImageInput from base64 data.
        
        Args:
            base64_data: Base64 encoded image data
            mime_type: MIME type of the image
            name: Optional name for the image
            description: Optional description
            
        Returns:
            ImageInput instance
        """
        return cls(data=base64_data, mime_type=mime_type, name=name, description=description)
    
    @classmethod
    def from_bytes(cls, image_bytes: bytes, mime_type: str, name: Optional[str] = None, description: Optional[str] = None) -> 'ImageInput':
        """
        Create ImageInput from raw bytes.
        
        Args:
            image_bytes: Raw image bytes
            mime_type: MIME type of the image
            name: Optional name for the image
            description: Optional description
            
        Returns:
            ImageInput instance
        """
        return cls(data=image_bytes, mime_type=mime_type, name=name, description=description)
    
    def to_base64(self) -> str:
        """
        Get the base64 encoded image data.
        
        Returns:
            Base64 encoded image data
        """
        return self.base64_data
    
    def get_mime_type(self) -> str:
        """
        Get the MIME type of the image.
        
        Returns:
            MIME type string
        """
        return self.mime_type
    
    def __repr__(self) -> str:
        """String representation of ImageInput."""
        return f"ImageInput(name={self.name}, mime_type={self.mime_type}, size={len(self.base64_data)} chars)"