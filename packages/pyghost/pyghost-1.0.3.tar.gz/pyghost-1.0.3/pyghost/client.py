import jwt
import json
import time
from typing import Dict, Optional
from urllib.parse import urljoin
import requests

from .exceptions import GhostAPIError, AuthenticationError, ValidationError, NotFoundError, RateLimitError
from .posts import Posts
from .pages import Pages
from .tiers import Tiers
from .newsletters import Newsletters
from .offers import Offers
from .members import Members
from .users import Users
from .images import Images
from .themes import Themes
from .webhooks import Webhooks


class GhostClient:
    """
    Main client for interacting with Ghost Admin API.

    Handles authentication, request/response processing, and error handling.
    Provides access to all Ghost Admin API modules including Posts, Pages,
    Tiers, Newsletters, Offers, Members, Users, Images, Themes, and Webhooks.

    :param site_url: Your Ghost site URL (e.g., 'https://mysite.ghost.io')
    :type site_url: str
    :param admin_api_key: Your Ghost Admin API key from Ghost Admin > Settings > Integrations
    :type admin_api_key: str
    :param api_version: API version to use (default: v5.0)
    :type api_version: str

    Attributes:
        posts (Posts): Posts management module
        pages (Pages): Pages management module
        tiers (Tiers): Subscription tiers management module
        newsletters (Newsletters): Newsletter configuration module
        offers (Offers): Discount offers management module
        members (Members): Member/subscriber management module
        users (Users): User/staff management module
        images (Images): Image upload and media management module
        themes (Themes): Theme upload and management module
        webhooks (Webhooks): Webhook creation and management module

    Example:
        >>> client = GhostClient(
        ...     site_url="https://mysite.ghost.io",
        ...     admin_api_key="your_key:your_secret"
        ... )
        >>> # Use different modules
        >>> posts = client.posts.list()
        >>> pages = client.pages.list()
        >>> tiers = client.tiers.list()
        >>> newsletters = client.newsletters.list()
        >>> offers = client.offers.list()
        >>> members = client.members.list()
        >>> users = client.users.list()
        >>> image_result = client.images.upload("path/to/image.jpg")
        >>> theme_result = client.themes.upload_from_file("theme.zip")
        >>> webhook = client.webhooks.create("post.published", "https://example.com/hook")
    """

    def __init__(self, site_url: str, admin_api_key: str, api_version: str = "v5.0"):
        """
        Initialize Ghost API client

        Args:
            site_url: Your Ghost site URL (e.g., 'https://mysite.ghost.io')
            admin_api_key: Your Ghost Admin API key (from Ghost Admin > Settings > Integrations)
            api_version: API version to use (default: v5.0)
        """
        self.site_url = site_url.rstrip('/')
        self.admin_api_key = admin_api_key
        self.api_version = api_version
        self.base_url = f"{self.site_url}/ghost/api/admin/"

        # Parse the admin API key
        self._parse_api_key()

        # Initialize session with default headers
        self.session = requests.Session()
        self.session.headers.update({
            'Accept-Version': self.api_version,
            'Content-Type': 'application/json',
            'User-Agent': 'PyGhost/1.0.0'
        })

        # Initialize API modules
        self.posts = Posts(self)
        self.pages = Pages(self)
        self.tiers = Tiers(self)
        self.newsletters = Newsletters(self)
        self.offers = Offers(self)
        self.members = Members(self)
        self.users = Users(self)
        self.images = Images(self)
        self.themes = Themes(self)
        self.webhooks = Webhooks(self)

    def _parse_api_key(self):
        """Parse the admin API key to extract key ID and secret"""
        try:
            key_id, secret = self.admin_api_key.split(':')
            self.key_id = key_id
            self.secret = bytes.fromhex(secret)
        except (ValueError, TypeError):
            raise AuthenticationError("Invalid admin API key format. Expected format: 'key_id:secret'")

    def _generate_jwt_token(self) -> str:
        """Generate JWT token for authentication"""
        iat = int(time.time())

        header = {'alg': 'HS256', 'typ': 'JWT', 'kid': self.key_id}
        payload = {
            'iat': iat,
            'exp': iat + 300,  # Token expires in 5 minutes
            'aud': '/admin/'
        }
        token = jwt.encode(payload, self.secret, algorithm='HS256', headers=header)
        return token

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None,
                      params: Optional[Dict] = None) -> Dict:
        """
        Make authenticated request to Ghost API

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (without base URL)
            data: Request body data
            params: Query parameters

        Returns:
            Response data as dictionary

        Raises:
            GhostAPIError: For API errors
            AuthenticationError: For auth failures
            ValidationError: For validation errors
            NotFoundError: For 404 errors
            RateLimitError: For rate limit errors
        """
        # Generate fresh JWT token for each request
        token = self._generate_jwt_token()
        headers = {'Authorization': f'Ghost {token}'}

        url = urljoin(self.base_url, endpoint.lstrip('/'))
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                json=data if data else None,
                params=params if params else None,
                timeout=30
            )

            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            raise GhostAPIError(f"Request failed: {str(e)}")

    def _handle_response(self, response: requests.Response) -> Dict:
        """Handle API response and raise appropriate exceptions"""
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            response_data = {'message': response.text or 'Unknown error'}

        if response.status_code == 200 or response.status_code == 201:
            return response_data
        elif response.status_code == 400:
            raise ValidationError(
                message=response_data.get('errors', [{}])[0].get('message', 'Validation failed'),
                status_code=response.status_code,
                response=response_data
            )
        elif response.status_code == 401:
            raise AuthenticationError(
                message=response_data.get('errors', [{}])[0].get('message', 'Authentication failed'),
                status_code=response.status_code,
                response=response_data
            )
        elif response.status_code == 404:
            raise NotFoundError(
                message=response_data.get('errors', [{}])[0].get('message', 'Resource not found'),
                status_code=response.status_code,
                response=response_data
            )
        elif response.status_code == 429:
            raise RateLimitError(
                message=response_data.get('errors', [{}])[0].get('message', 'Rate limit exceeded'),
                status_code=response.status_code,
                response=response_data
            )
        else:
            raise GhostAPIError(
                message=response_data.get('errors', [{}])[0].get('message', f'API error: {response.status_code}'),
                status_code=response.status_code,
                response=response_data
            )

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make GET request"""
        return self._make_request('GET', endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """Make POST request"""
        return self._make_request('POST', endpoint, data=data, params=params)

    def put(self, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """Make PUT request"""
        return self._make_request('PUT', endpoint, data=data, params=params)

    def delete(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make DELETE request"""
        return self._make_request('DELETE', endpoint, params=params)

    def post_multipart(self, endpoint: str, files: Optional[Dict] = None, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """
        Make POST request with multipart/form-data (for file uploads).

        :param endpoint: API endpoint
        :type endpoint: str
        :param files: Files to upload (format: {'field_name': (filename, file_obj, content_type)})
        :type files: Dict, optional
        :param data: Form data
        :type data: Dict, optional
        :param params: Query parameters
        :type params: Dict, optional

        :returns: Response data as dictionary
        :rtype: Dict
        :raises GhostAPIError: For API errors

        Example:
            >>> files = {'file': ('image.jpg', file_obj, 'image/jpeg')}
            >>> result = client.post_multipart('images/upload/', files=files)
        """
        # Generate fresh JWT token for each request
        token = self._generate_jwt_token()
        headers = {'Authorization': f'Ghost {token}'}
        # Remove Content-Type header for multipart uploads (requests will set it automatically)
        session_headers = self.session.headers.copy()
        if 'Content-Type' in session_headers:
            del session_headers['Content-Type']

        url = urljoin(self.base_url, endpoint.lstrip('/'))
        try:
            response = requests.request(
                method='POST',
                url=url,
                headers={**session_headers, **headers},
                files=files if files else None,
                data=data if data else None,
                params=params if params else None,
                timeout=30
            )

            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            raise GhostAPIError(f"Multipart request failed: {str(e)}")
