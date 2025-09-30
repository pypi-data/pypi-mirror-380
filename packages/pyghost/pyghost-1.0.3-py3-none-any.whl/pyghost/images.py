"""
Images module for Ghost Admin API.

This module provides functionality for uploading and managing images through the Ghost Admin API,
including support for various image formats and multipart file uploads.

.. module:: pyghost.images
   :synopsis: Ghost Admin API Images management

.. moduleauthor:: PyGhost Contributors
"""

import os
from typing import Dict, List, Optional, Union, BinaryIO

from .exceptions import ValidationError


class Images:
    """
    Images module for Ghost Admin API.

    Handles image upload operations including support for various image formats,
    file validation, and multipart form data uploads.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> with open("image.jpg", "rb") as f:
        ...     result = client.images.upload(f, "image.jpg")
        >>> print(f"Uploaded image URL: {result['url']}")
    """

    # Supported image formats
    SUPPORTED_FORMATS = {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp',
        '.svg', '.tiff', '.tif', '.ico', '.heic', '.heif'
    }

    # Maximum file size (in bytes) - Ghost typically allows up to 5MB
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

    def __init__(self, client):
        """
        Initialize Images module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def upload(self,
               file_data: Union[str, BinaryIO],
               filename: Optional[str] = None,
               validate: bool = True) -> Dict:
        """
        Upload an image file to Ghost.

        :param file_data: File path (string) or file-like object (binary mode)
        :type file_data: Union[str, BinaryIO]
        :param filename: Original filename (required if file_data is file-like object)
        :type filename: str, optional
        :param validate: Whether to validate file format and size
        :type validate: bool

        :returns: Upload response with URL and reference
        :rtype: Dict
        :raises ValidationError: If file validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Upload from file path
            >>> result = client.images.upload("/path/to/image.jpg")
            >>> print(f"Image URL: {result['url']}")
            >>>
            >>> # Upload from file object
            >>> with open("image.png", "rb") as f:
            ...     result = client.images.upload(f, "image.png")
            >>>
            >>> # Upload without validation (use with caution)
            >>> result = client.images.upload("image.jpg", validate=False)

        Note:
            - Supported formats: JPG, PNG, GIF, BMP, WebP, SVG, TIFF, ICO, HEIC, HEIF
            - Maximum file size is typically 5MB
            - Ghost automatically optimizes images for web delivery
        """
        # Handle file path vs file object
        if isinstance(file_data, str):
            if not os.path.exists(file_data):
                raise ValidationError(f"File not found: {file_data}")

            filename = filename or os.path.basename(file_data)

            with open(file_data, "rb") as f:
                return self._upload_file_object(f, filename, validate)
        else:
            if not filename:
                raise ValidationError("Filename is required when uploading file objects")

            return self._upload_file_object(file_data, filename, validate)

    def _upload_file_object(self, file_obj: BinaryIO, filename: str, validate: bool) -> Dict:
        """
        Internal method to upload file object.

        :param file_obj: File object in binary mode
        :type file_obj: BinaryIO
        :param filename: Original filename
        :type filename: str
        :param validate: Whether to validate file
        :type validate: bool

        :returns: Upload response
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails
        """
        if validate:
            self._validate_file(file_obj, filename)

        # Prepare multipart form data
        files = {
            'file': (filename, file_obj, self._get_content_type(filename))
        }

        # Make multipart upload request
        response = self.client.post_multipart("images/upload/", files=files)

        # Return the first image from the response
        if response.get("images") and len(response["images"]) > 0:
            return response["images"][0]

        return response

    def upload_multiple(self,
                        file_paths: List[str],
                        validate: bool = True) -> List[Dict]:
        """
        Upload multiple images.

        :param file_paths: List of file paths to upload
        :type file_paths: List[str]
        :param validate: Whether to validate files
        :type validate: bool

        :returns: List of upload responses
        :rtype: List[Dict]
        :raises ValidationError: If any file validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> files = ["/path/to/image1.jpg", "/path/to/image2.png"]
            >>> results = client.images.upload_multiple(files)
            >>> for result in results:
            ...     print(f"Uploaded: {result['url']}")

        Note:
            This method uploads files sequentially. For better performance with many files,
            consider using async upload patterns or batch processing.
        """
        results = []

        for file_path in file_paths:
            try:
                result = self.upload(file_path, validate=validate)
                results.append(result)
            except Exception as e:
                # Add filename context to error
                raise ValidationError(f"Failed to upload {file_path}: {str(e)}")

        return results

    def upload_from_url(self, url: str, filename: Optional[str] = None) -> Dict:
        """
        Upload an image from a URL.

        :param url: URL of the image to upload
        :type url: str
        :param filename: Filename to use (extracted from URL if not provided)
        :type filename: str, optional

        :returns: Upload response
        :rtype: Dict
        :raises ValidationError: If URL is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> result = client.images.upload_from_url(
            ...     "https://example.com/image.jpg",
            ...     "my-image.jpg"
            ... )

        Note:
            This method downloads the image from the URL and then uploads it to Ghost.
            For large images or unreliable connections, consider downloading separately first.
        """
        import requests

        if not url.startswith(('http://', 'https://')):
            raise ValidationError("URL must start with http:// or https://")

        # Extract filename from URL if not provided
        if not filename:
            filename = url.split('/')[-1]
            if '?' in filename:
                filename = filename.split('?')[0]
            if not filename or '.' not in filename:
                filename = "image.jpg"  # Default fallback

        try:
            # Download image from URL
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            # Upload the downloaded content
            return self._upload_file_object(response.raw, filename, validate=True)

        except requests.RequestException as e:
            raise ValidationError(f"Failed to download image from URL: {str(e)}")

    def _validate_file(self, file_obj: BinaryIO, filename: str) -> None:
        """
        Validate file format and size.

        :param file_obj: File object to validate
        :type file_obj: BinaryIO
        :param filename: Filename for format validation
        :type filename: str

        :raises ValidationError: If validation fails
        """
        # Validate file extension
        file_ext = os.path.splitext(filename.lower())[1]
        if file_ext not in self.SUPPORTED_FORMATS:
            raise ValidationError(
                f"Unsupported file format: {file_ext}. "
                f"Supported formats: {', '.join(sorted(self.SUPPORTED_FORMATS))}"
            )

        # Validate file size
        current_pos = file_obj.tell()
        file_obj.seek(0, 2)  # Seek to end
        file_size = file_obj.tell()
        file_obj.seek(current_pos)  # Reset position

        if file_size > self.MAX_FILE_SIZE:
            raise ValidationError(
                f"File size ({file_size:,} bytes) exceeds maximum allowed size "
                f"({self.MAX_FILE_SIZE:,} bytes)"
            )

        if file_size == 0:
            raise ValidationError("File is empty")

    def _get_content_type(self, filename: str) -> str:
        """
        Get appropriate content type for file.

        :param filename: Filename to determine content type for
        :type filename: str

        :returns: MIME content type
        :rtype: str
        """
        file_ext = os.path.splitext(filename.lower())[1]

        content_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp',
            '.svg': 'image/svg+xml',
            '.tiff': 'image/tiff',
            '.tif': 'image/tiff',
            '.ico': 'image/x-icon',
            '.heic': 'image/heic',
            '.heif': 'image/heif'
        }

        return content_types.get(file_ext, 'application/octet-stream')

    def validate_image_path(self, file_path: str) -> bool:
        """
        Validate an image file path without uploading.

        :param file_path: Path to image file
        :type file_path: str

        :returns: True if file is valid
        :rtype: bool
        :raises ValidationError: If validation fails

        Example:
            >>> if client.images.validate_image_path("/path/to/image.jpg"):
            ...     print("Image is valid for upload")
        """
        if not os.path.exists(file_path):
            raise ValidationError(f"File not found: {file_path}")

        filename = os.path.basename(file_path)

        with open(file_path, "rb") as f:
            self._validate_file(f, filename)

        return True

    def get_image_info(self, file_path: str) -> Dict:
        """
        Get information about an image file.

        :param file_path: Path to image file
        :type file_path: str

        :returns: Dictionary with image information
        :rtype: Dict
        :raises ValidationError: If file doesn't exist

        Example:
            >>> info = client.images.get_image_info("/path/to/image.jpg")
            >>> print(f"Size: {info['size_bytes']:,} bytes, Format: {info['format']}")
        """
        if not os.path.exists(file_path):
            raise ValidationError(f"File not found: {file_path}")

        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(filename.lower())[1]
        file_size = os.path.getsize(file_path)

        info = {
            "filename": filename,
            "format": file_ext,
            "size_bytes": file_size,
            "size_mb": round(file_size / (1024 * 1024), 2),
            "is_supported": file_ext in self.SUPPORTED_FORMATS,
            "exceeds_max_size": file_size > self.MAX_FILE_SIZE,
            "content_type": self._get_content_type(filename)
        }

        # Try to get image dimensions if PIL is available
        try:
            from PIL import Image
            with Image.open(file_path) as img:
                info["width"] = img.width
                info["height"] = img.height
                info["mode"] = img.mode
        except ImportError:
            # PIL not available, skip dimensions
            pass
        except Exception:
            # Error reading image, skip dimensions
            pass

        return info

    def batch_validate(self, file_paths: List[str]) -> Dict:
        """
        Validate multiple image files.

        :param file_paths: List of file paths to validate
        :type file_paths: List[str]

        :returns: Dictionary with validation results
        :rtype: Dict

        Example:
            >>> files = ["/path/to/image1.jpg", "/path/to/image2.png"]
            >>> results = client.images.batch_validate(files)
            >>> print(f"Valid: {len(results['valid'])}, Invalid: {len(results['invalid'])}")
        """
        valid = []
        invalid = []
        total_size = 0

        for file_path in file_paths:
            try:
                self.validate_image_path(file_path)
                file_size = os.path.getsize(file_path)
                valid.append({
                    "path": file_path,
                    "size_bytes": file_size
                })
                total_size += file_size
            except (ValidationError, OSError) as e:
                invalid.append({
                    "path": file_path,
                    "error": str(e)
                })

        return {
            "valid": valid,
            "invalid": invalid,
            "total_files": len(file_paths),
            "valid_count": len(valid),
            "invalid_count": len(invalid),
            "total_size_bytes": total_size,
            "total_size_mb": round(total_size / (1024 * 1024), 2)
        }
