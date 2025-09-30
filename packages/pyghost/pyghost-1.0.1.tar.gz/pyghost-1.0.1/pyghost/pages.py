"""
Pages module for Ghost Admin API.

This module provides functionality for managing Ghost pages (static content).
Pages are similar to posts but are typically used for static content like About, Contact, etc.

.. module:: pyghost.pages
   :synopsis: Ghost Admin API Pages management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, Union

from .exceptions import ValidationError
from .enums import PageStatus, ContentType, get_enum_value


class Pages:
    """
    Pages module for Ghost Admin API.

    Handles all page-related operations including CRUD, publishing, and scheduling.
    Pages are similar to posts but are typically used for static content.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> page = client.pages.create(
        ...     title="About Us",
        ...     content="This is our about page content",
        ...     status="published"
        ... )
    """

    def __init__(self, client):
        """
        Initialize Pages module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def create(self,
               title: str,
               content: Optional[str] = None,
               content_type: Union[ContentType, str] = ContentType.LEXICAL,
               status: Union[PageStatus, str] = PageStatus.DRAFT,
               tags: Optional[List[Union[str, Dict]]] = None,
               authors: Optional[List[Union[str, Dict]]] = None,
               excerpt: Optional[str] = None,
               featured: bool = False,
               feature_image: Optional[str] = None,
               meta_title: Optional[str] = None,
               meta_description: Optional[str] = None,
               **kwargs) -> Dict:
        """
        Create a new page.

        :param title: Page title (required)
        :type title: str
        :param content: Page content (Lexical JSON string or HTML)
        :type content: str, optional
        :param content_type: Content type ('lexical' or 'html')
        :type content_type: str
        :param status: Page status ('draft', 'published', 'scheduled')
        :type status: str
        :param tags: List of tag names or tag objects
        :type tags: List[Union[str, Dict]], optional
        :param authors: List of author emails/IDs or author objects
        :type authors: List[Union[str, Dict]], optional
        :param excerpt: Page excerpt
        :type excerpt: str, optional
        :param featured: Whether page is featured
        :type featured: bool
        :param feature_image: URL to feature image
        :type feature_image: str, optional
        :param meta_title: SEO meta title
        :type meta_title: str, optional
        :param meta_description: SEO meta description
        :type meta_description: str, optional
        :param kwargs: Additional page fields
        :type kwargs: dict

        :returns: Created page data
        :rtype: Dict
        :raises ValidationError: If content_type is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> page = client.pages.create(
            ...     title="Privacy Policy",
            ...     content="<h1>Our Privacy Policy</h1><p>We value your privacy...</p>",
            ...     content_type="html",
            ...     status="published"
            ... )
        """
        # Convert enums to string values
        content_type_str = get_enum_value(content_type)
        status_str = get_enum_value(status)

        page_data = {
            "title": title,
            "status": status_str,
            "featured": featured
        }

        # Handle content based on type
        if content:
            if content_type_str == "lexical":
                page_data["lexical"] = content
            elif content_type_str == "html":
                page_data["html"] = content
            else:
                raise ValidationError("content_type must be ContentType.LEXICAL or ContentType.HTML")

        # Add optional fields
        if excerpt:
            page_data["excerpt"] = excerpt
        if feature_image:
            page_data["feature_image"] = feature_image
        if meta_title:
            page_data["meta_title"] = meta_title
        if meta_description:
            page_data["meta_description"] = meta_description

        # Handle tags
        if tags:
            page_data["tags"] = self._format_tags(tags)

        # Handle authors
        if authors:
            page_data["authors"] = self._format_authors(authors)

        # Add any additional fields
        page_data.update(kwargs)

        # Determine endpoint params
        params = None
        if content_type_str == "html":
            params = {"source": "html"}

        response = self.client.post("pages/", {"pages": [page_data]}, params=params)
        return response["pages"][0] if response.get("pages") else response

    def get(self, page_id: str, **kwargs) -> Dict:
        """
        Get a specific page by ID.

        :param page_id: Page ID
        :type page_id: str
        :param kwargs: Additional query parameters (e.g., include, fields)
        :type kwargs: dict

        :returns: Page data
        :rtype: Dict
        :raises NotFoundError: If page not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> page = client.pages.get("page_id_here", include="tags,authors")
        """
        params = kwargs
        response = self.client.get(f"pages/{page_id}/", params=params)
        return response["pages"][0] if response.get("pages") else response

    def get_by_slug(self, slug: str, **kwargs) -> Dict:
        """
        Get a page by slug.

        :param slug: Page slug
        :type slug: str
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Page data
        :rtype: Dict
        :raises ValueError: If no page found with slug
        :raises GhostAPIError: If API request fails

        Example:
            >>> page = client.pages.get_by_slug("about-us")
        """
        params = {"slug": slug}
        params.update(kwargs)
        response = self.client.get("pages/", params=params)
        pages = response.get("pages", [])
        if not pages:
            raise ValueError(f"No page found with slug: {slug}")
        return pages[0]

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List pages with optional filtering and pagination.

        :param limit: Number of pages to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string
        :type filter_: str, optional
        :param include: Related data to include
        :type include: str, optional
        :param order: Ordering specification
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Pages list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> pages = client.pages.list(limit=10, filter_="status:published")
        """
        params = {}

        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        if filter_:
            params["filter"] = filter_
        if include:
            params["include"] = include
        if order:
            params["order"] = order

        params.update(kwargs)

        return self.client.get("pages/", params=params)

    def update(self,
               page_id: str,
               updated_at: str,
               title: Optional[str] = None,
               content: Optional[str] = None,
               content_type: Optional[Union[ContentType, str]] = None,
               status: Optional[Union[PageStatus, str]] = None,
               tags: Optional[List[Union[str, Dict]]] = None,
               authors: Optional[List[Union[str, Dict]]] = None,
               **kwargs) -> Dict:
        """
        Update an existing page.

        :param page_id: Page ID to update
        :type page_id: str
        :param updated_at: Current updated_at timestamp (for conflict resolution)
        :type updated_at: str
        :param title: New page title
        :type title: str, optional
        :param content: New page content
        :type content: str, optional
        :param content_type: Content type (ContentType.LEXICAL or ContentType.HTML)
        :type content_type: Union[ContentType, str], optional
        :param status: New page status (PageStatus.DRAFT, PageStatus.PUBLISHED, etc.)
        :type status: Union[PageStatus, str], optional
        :param tags: New tags list
        :type tags: List[Union[str, Dict]], optional
        :param authors: New authors list
        :type authors: List[Union[str, Dict]], optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated page data
        :rtype: Dict
        :raises ValidationError: If content_type is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_page = client.pages.update(
            ...     page_id="page_id",
            ...     updated_at="2024-01-01T00:00:00.000Z",
            ...     title="Updated Page Title"
            ... )
        """
        page_data = {"updated_at": updated_at}

        if title is not None:
            page_data["title"] = title

        if content is not None:
            content_type_str = get_enum_value(content_type) if content_type else None
            if content_type_str == "lexical":
                page_data["lexical"] = content
            elif content_type_str == "html":
                page_data["html"] = content
            elif content_type is None:
                # Default to lexical if not specified
                page_data["lexical"] = content
            else:
                raise ValidationError("content_type must be ContentType.LEXICAL or ContentType.HTML")

        if status is not None:
            page_data["status"] = get_enum_value(status)

        if tags is not None:
            page_data["tags"] = self._format_tags(tags)

        if authors is not None:
            page_data["authors"] = self._format_authors(authors)

        # Add any additional fields
        page_data.update(kwargs)

        # Determine endpoint params
        params = None
        if content_type == "html":
            params = {"source": "html"}

        response = self.client.put(f"pages/{page_id}/", {"pages": [page_data]}, params=params)
        return response["pages"][0] if response.get("pages") else response

    def publish(self, page_id: str, updated_at: str) -> Dict:
        """
        Publish a page immediately.

        :param page_id: Page ID to publish
        :type page_id: str
        :param updated_at: Current updated_at timestamp
        :type updated_at: str

        :returns: Updated page data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> published_page = client.pages.publish("page_id", "2024-01-01T00:00:00.000Z")
        """
        return self.update(page_id, updated_at, status=PageStatus.PUBLISHED)

    def unpublish(self, page_id: str, updated_at: str) -> Dict:
        """
        Unpublish a page (revert to draft).

        :param page_id: Page ID to unpublish
        :type page_id: str
        :param updated_at: Current updated_at timestamp
        :type updated_at: str

        :returns: Updated page data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> draft_page = client.pages.unpublish("page_id", "2024-01-01T00:00:00.000Z")
        """
        return self.update(page_id, updated_at, status=PageStatus.DRAFT)

    def delete(self, page_id: str) -> bool:
        """
        Delete a page permanently.

        :param page_id: Page ID to delete
        :type page_id: str

        :returns: True if deletion was successful
        :rtype: bool
        :raises GhostAPIError: If API request fails

        Example:
            >>> success = client.pages.delete("page_id")
        """
        self.client.delete(f"pages/{page_id}/")
        return True

    def copy(self, page_id: str) -> Dict:
        """
        Create a copy of an existing page.

        :param page_id: Page ID to copy
        :type page_id: str

        :returns: New page data (copy)
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> copied_page = client.pages.copy("original_page_id")
        """
        response = self.client.post(f"pages/{page_id}/copy")
        return response["pages"][0] if response.get("pages") else response

    def _format_tags(self, tags: List[Union[str, Dict]]) -> List[Dict]:
        """
        Format tags for API request.

        :param tags: List of tag names or tag objects
        :type tags: List[Union[str, Dict]]

        :returns: Formatted tags list
        :rtype: List[Dict]
        :raises ValidationError: If tag format is invalid
        """
        formatted_tags = []
        for tag in tags:
            if isinstance(tag, str):
                formatted_tags.append({"name": tag})
            elif isinstance(tag, dict):
                formatted_tags.append(tag)
            else:
                raise ValidationError(f"Invalid tag format: {tag}")
        return formatted_tags

    def _format_authors(self, authors: List[Union[str, Dict]]) -> List[Dict]:
        """
        Format authors for API request.

        :param authors: List of author emails/IDs or author objects
        :type authors: List[Union[str, Dict]]

        :returns: Formatted authors list
        :rtype: List[Dict]
        :raises ValidationError: If author format is invalid
        """
        formatted_authors = []
        for author in authors:
            if isinstance(author, str):
                # Assume it's an email if it contains @, otherwise treat as ID
                if "@" in author:
                    formatted_authors.append({"email": author})
                else:
                    formatted_authors.append({"id": author})
            elif isinstance(author, dict):
                formatted_authors.append(author)
            else:
                raise ValidationError(f"Invalid author format: {author}")
        return formatted_authors
