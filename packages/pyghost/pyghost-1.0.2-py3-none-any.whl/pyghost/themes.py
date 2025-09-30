"""
Themes module for Ghost Admin API.

This module provides functionality for managing Ghost themes including
theme upload, activation, and theme information retrieval.

.. module:: pyghost.themes
   :synopsis: Ghost Admin API Themes management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, BinaryIO
import os
import zipfile


class Themes:
    """
    Themes module for Ghost Admin API.

    Handles all theme-related operations including theme upload, activation,
    and theme management for Ghost sites.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(
        ...     site_url="https://mysite.ghost.io",
        ...     admin_api_key="key:secret"
        ... )
        >>> uploaded_theme = client.themes.upload_from_file("my-theme.zip")
        >>> activated_theme = client.themes.activate(uploaded_theme['name'])

    Note:
        Theme uploads require multipart/form-data and must be valid Ghost theme
        ZIP files containing a package.json and theme templates.
    """

    def __init__(self, client):
        """
        Initialize the Themes module.

        :param client: The GhostClient instance
        :type client: GhostClient
        """
        self.client = client

    def upload_from_file(self, file_path: str, activate: bool = False) -> Dict:
        """
        Upload a theme from a local file path.

        :param file_path: Path to the theme ZIP file
        :type file_path: str
        :param activate: Whether to activate the theme after upload
        :type activate: bool, optional

        :returns: Uploaded theme data
        :rtype: Dict
        :raises FileNotFoundError: If the theme file doesn't exist
        :raises ValidationError: If the theme file is invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> theme = client.themes.upload_from_file(
            ...     "/path/to/my-theme.zip",
            ...     activate=True
            ... )
            >>> print(f"Uploaded theme: {theme['name']}")
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Theme file not found: {file_path}")

        if not file_path.lower().endswith('.zip'):
            raise ValueError("Theme file must be a ZIP archive")

        # Validate ZIP file structure
        self._validate_theme_zip(file_path)

        with open(file_path, 'rb') as theme_file:
            return self.upload_from_file_object(theme_file, activate=activate)

    def upload_from_file_object(self, file_obj: BinaryIO,
                                activate: bool = False) -> Dict:
        """
        Upload a theme from a file-like object.

        :param file_obj: File-like object containing theme ZIP data
        :type file_obj: BinaryIO
        :param activate: Whether to activate the theme after upload
        :type activate: bool, optional

        :returns: Uploaded theme data
        :rtype: Dict
        :raises ValidationError: If the theme data is invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> with open("my-theme.zip", "rb") as f:
            ...     theme = client.themes.upload_from_file_object(f)
        """
        files = {'file': file_obj}

        response = self.client.post_multipart(
            endpoint="themes/upload",
            files=files
        )
        uploaded_theme = response.get('themes', [{}])[0]

        if activate and uploaded_theme.get('name'):
            return self.activate(uploaded_theme['name'])

        return uploaded_theme

    def activate(self, theme_name: str) -> Dict:
        """
        Activate a theme by name.

        :param theme_name: Name of the theme to activate
        :type theme_name: str

        :returns: Activated theme data
        :rtype: Dict
        :raises ValidationError: If theme name is invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> activated_theme = client.themes.activate("my-theme")
            >>> print(f"Active theme: {activated_theme['name']}")
        """
        if not theme_name:
            raise ValueError("Theme name cannot be empty")

        endpoint = f"themes/{theme_name}/activate"

        response = self.client.put(endpoint)
        return response.get('themes', [{}])[0]

    def get_active_theme(self) -> Optional[Dict]:
        """
        Get the currently active theme.

        :returns: Active theme data or None if no active theme found
        :rtype: Optional[Dict]
        :raises GhostAPIError: If the API request fails

        Example:
            >>> active_theme = client.themes.get_active_theme()
            >>> if active_theme:
            ...     print(f"Current theme: {active_theme['name']}")
        """
        # Note: Ghost API doesn't have a direct endpoint to list themes
        # This is a utility method that would need to be implemented
        # based on site configuration or other available endpoints

        # For now, return None as this endpoint may not be available
        # in the current Ghost Admin API
        return None

    def validate_theme_structure(self, theme_path: str) -> Dict:
        """
        Validate a theme's structure and return information about it.

        :param theme_path: Path to the theme ZIP file
        :type theme_path: str

        :returns: Theme validation information
        :rtype: Dict
        :raises FileNotFoundError: If the theme file doesn't exist
        :raises ValidationError: If the theme structure is invalid

        Example:
            >>> validation = client.themes.validate_theme_structure(
            ...     "/path/to/theme.zip"
            ... )
            >>> print(f"Theme valid: {validation['valid']}")
            >>> print(f"Templates: {len(validation['templates'])}")
        """
        if not os.path.exists(theme_path):
            raise FileNotFoundError(f"Theme file not found: {theme_path}")

        return self._validate_theme_zip(theme_path)

    def get_theme_info(self, theme_path: str) -> Dict:
        """
        Extract theme information from a theme ZIP file.

        :param theme_path: Path to the theme ZIP file
        :type theme_path: str

        :returns: Theme information including package.json data
        :rtype: Dict
        :raises FileNotFoundError: If the theme file doesn't exist
        :raises ValidationError: If the theme structure is invalid

        Example:
            >>> info = client.themes.get_theme_info("/path/to/theme.zip")
            >>> print(f"Theme name: {info['name']}")
            >>> print(f"Version: {info['version']}")
            >>> print(f"Templates: {len(info['templates'])}")
        """
        if not os.path.exists(theme_path):
            raise FileNotFoundError(f"Theme file not found: {theme_path}")

        return self._extract_theme_info(theme_path)

    def create_theme_backup(self, theme_name: str,
                            backup_path: str) -> str:
        """
        Create a backup of the current theme (placeholder method).

        Note: This is a utility method for theme management.
        The Ghost Admin API doesn't provide direct theme download,
        so this would need to be implemented using other methods.

        :param theme_name: Name of the theme to backup
        :type theme_name: str
        :param backup_path: Path where to save the backup
        :type backup_path: str

        :returns: Path to the created backup file
        :rtype: str
        :raises NotImplementedError: This feature is not yet implemented

        Example:
            >>> backup_file = client.themes.create_theme_backup(
            ...     "current-theme",
            ...     "/backups/"
            ... )
        """
        raise NotImplementedError(
            "Theme backup functionality is not available through the Ghost Admin API. "
            "Please use Ghost CLI or manual file system operations for theme backups."
        )

    def _validate_theme_zip(self, theme_path: str) -> Dict:
        """
        Validate the structure of a theme ZIP file.

        :param theme_path: Path to the theme ZIP file
        :type theme_path: str

        :returns: Validation results
        :rtype: Dict
        :raises ValidationError: If the theme structure is invalid
        """
        validation_result = {
            'valid': False,
            'errors': [],
            'warnings': [],
            'package_json': None,
            'templates': []
        }

        try:
            with zipfile.ZipFile(theme_path, 'r') as zip_file:
                file_list = zip_file.namelist()

                # Check for package.json
                package_json_files = [f for f in file_list if f.endswith('package.json')]
                if not package_json_files:
                    validation_result['errors'].append("Missing package.json file")
                else:
                    # Try to read and parse package.json
                    try:
                        import json
                        package_json_content = zip_file.read(package_json_files[0])
                        validation_result['package_json'] = json.loads(package_json_content)
                    except (json.JSONDecodeError, UnicodeDecodeError) as e:
                        validation_result['errors'].append(f"Invalid package.json: {e}")

                # Check for template files
                template_files = [f for f in file_list if f.endswith('.hbs')]
                if not template_files:
                    validation_result['warnings'].append("No Handlebars template files found")
                else:
                    validation_result['templates'] = template_files

                # Check for required files
                required_files = ['index.hbs']
                for required_file in required_files:
                    if not any(f.endswith(required_file) for f in file_list):
                        validation_result['errors'].append(f"Missing required file: {required_file}")

                # Set valid status
                validation_result['valid'] = len(validation_result['errors']) == 0

        except zipfile.BadZipFile:
            validation_result['errors'].append("Invalid ZIP file format")
        except Exception as e:
            validation_result['errors'].append(f"Validation error: {str(e)}")

        if not validation_result['valid']:
            from .exceptions import ValidationError
            raise ValidationError(f"Theme validation failed: {', '.join(validation_result['errors'])}")

        return validation_result

    def _extract_theme_info(self, theme_path: str) -> Dict:
        """
        Extract theme information from package.json and file structure.

        :param theme_path: Path to the theme ZIP file
        :type theme_path: str

        :returns: Theme information
        :rtype: Dict
        """
        validation_result = self._validate_theme_zip(theme_path)

        theme_info = {
            'name': 'unknown',
            'version': 'unknown',
            'description': '',
            'templates': validation_result['templates'],
            'template_count': len(validation_result['templates']),
            'valid': validation_result['valid']
        }

        if validation_result['package_json']:
            pkg = validation_result['package_json']
            theme_info.update({
                'name': pkg.get('name', 'unknown'),
                'version': pkg.get('version', 'unknown'),
                'description': pkg.get('description', ''),
                'author': pkg.get('author', ''),
                'keywords': pkg.get('keywords', []),
                'config': pkg.get('config', {})
            })

        return theme_info

    def get_supported_formats(self) -> List[str]:
        """
        Get list of supported theme file formats.

        :returns: List of supported file extensions
        :rtype: List[str]

        Example:
            >>> formats = client.themes.get_supported_formats()
            >>> print(f"Supported formats: {', '.join(formats)}")
        """
        return ['.zip']

    def validate_theme_format(self, file_path: str) -> bool:
        """
        Validate if a file has a supported theme format.

        :param file_path: Path to the theme file
        :type file_path: str

        :returns: True if format is supported, False otherwise
        :rtype: bool

        Example:
            >>> is_valid = client.themes.validate_theme_format("theme.zip")
            >>> print(f"Valid format: {is_valid}")
        """
        supported_formats = self.get_supported_formats()
        file_extension = os.path.splitext(file_path.lower())[1]
        return file_extension in supported_formats
