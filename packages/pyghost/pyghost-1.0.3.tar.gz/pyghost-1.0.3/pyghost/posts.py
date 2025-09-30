from typing import Dict, List, Optional, Union
from datetime import datetime

from .exceptions import ValidationError
from .enums import PostStatus, ContentType, get_enum_value


class Posts:
    """
    Posts module for Ghost Admin API

    Handles all post-related operations including CRUD, publishing, scheduling, and email management.
    """

    def __init__(self, client):
        """
        Initialize Posts module

        Args:
            client: GhostClient instance
        """
        self.client = client

    def create(self,
               title: str,
               content: Optional[str] = None,
               content_type: Union[ContentType, str] = ContentType.HTML,
               status: Union[PostStatus, str] = PostStatus.DRAFT,
               tags: Optional[List[Union[str, Dict]]] = None,
               authors: Optional[List[Union[str, Dict]]] = None,
               excerpt: Optional[str] = None,
               featured: bool = False,
               feature_image: Optional[str] = None,
               meta_title: Optional[str] = None,
               meta_description: Optional[str] = None,
               **kwargs) -> Dict:
        """
        Create a new post

        Args:
            title: Post title (required)
            content: Post content (Lexical JSON string or HTML)
            content_type: Content type (ContentType.LEXICAL or ContentType.HTML)
            status: Post status (PostStatus.DRAFT, PostStatus.PUBLISHED, etc.)
            tags: List of tag names/objects
            authors: List of author emails/IDs/objects
            excerpt: Post excerpt
            featured: Whether post is featured
            feature_image: URL to feature image
            meta_title: SEO meta title
            meta_description: SEO meta description
            **kwargs: Additional post fields

        Returns:
            Created post data
        """
        # Convert enums to string values
        content_type_str = get_enum_value(content_type)
        status_str = get_enum_value(status)

        post_data = {
            "title": title,
            "status": status_str,
            "featured": featured
        }

        # Handle content based on type
        if content:
            if content_type_str == "lexical":
                post_data["lexical"] = content
            elif content_type_str == "html":
                post_data["html"] = content
            else:
                raise ValidationError("content_type must be ContentType.LEXICAL or ContentType.HTML")

        # Add optional fields
        if excerpt:
            post_data["excerpt"] = excerpt
        if feature_image:
            post_data["feature_image"] = feature_image
        if meta_title:
            post_data["meta_title"] = meta_title
        if meta_description:
            post_data["meta_description"] = meta_description

        # Handle tags
        if tags:
            post_data["tags"] = self._format_tags(tags)

        # Handle authors
        if authors:
            post_data["authors"] = self._format_authors(authors)

        # Add any additional fields
        post_data.update(kwargs)

        # Determine endpoint params
        params = None
        if content_type_str == "html":
            params = {"source": "html"}

        response = self.client.post("posts/", {"posts": [post_data]}, params=params)
        return response["posts"][0] if response.get("posts") else response

    def get(self, post_id: str, **kwargs) -> Dict:
        """
        Get a specific post by ID

        Args:
            post_id: Post ID
            **kwargs: Additional query parameters (e.g., include, fields)

        Returns:
            Post data
        """
        params = kwargs
        response = self.client.get(f"posts/{post_id}/", params=params)
        return response["posts"][0] if response.get("posts") else response

    def get_by_slug(self, slug: str, **kwargs) -> Dict:
        """
        Get a post by slug

        Args:
            slug: Post slug
            **kwargs: Additional query parameters

        Returns:
            Post data
        """
        params = {"slug": slug}
        params.update(kwargs)
        response = self.client.get("posts/", params=params)
        posts = response.get("posts", [])
        if not posts:
            raise ValueError(f"No post found with slug: {slug}")
        return posts[0]

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List posts with optional filtering and pagination

        Args:
            limit: Number of posts to return
            page: Page number for pagination
            filter_: Ghost filter string
            include: Related data to include
            order: Ordering specification
            **kwargs: Additional query parameters

        Returns:
            Posts list with pagination metadata
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

        return self.client.get("posts/", params=params)

    def update(self,
               post_id: str,
               updated_at: str,
               title: Optional[str] = None,
               content: Optional[str] = None,
               content_type: Optional[Union[ContentType, str]] = None,
               status: Optional[Union[PostStatus, str]] = None,
               tags: Optional[List[Union[str, Dict]]] = None,
               authors: Optional[List[Union[str, Dict]]] = None,
               **kwargs) -> Dict:
        """
        Update an existing post

        Args:
            post_id: Post ID to update
            updated_at: Current updated_at timestamp (for conflict resolution)
            title: New post title
            content: New post content
            content_type: Content type (ContentType.LEXICAL or ContentType.HTML)
            status: New post status (PostStatus.DRAFT, PostStatus.PUBLISHED, etc.)
            tags: New tags list
            authors: New authors list
            **kwargs: Additional fields to update

        Returns:
            Updated post data
        """
        post_data = {"updated_at": updated_at}

        if title is not None:
            post_data["title"] = title

        if content is not None:
            content_type_str = get_enum_value(content_type) if content_type else None
            if content_type_str == "lexical":
                post_data["lexical"] = content
            elif content_type_str == "html":
                post_data["html"] = content
            elif content_type is None:
                # Default to lexical if not specified
                post_data["lexical"] = content
            else:
                raise ValidationError("content_type must be ContentType.LEXICAL or ContentType.HTML")

        if status is not None:
            post_data["status"] = get_enum_value(status)

        if tags is not None:
            post_data["tags"] = self._format_tags(tags)

        if authors is not None:
            post_data["authors"] = self._format_authors(authors)

        # Add any additional fields
        post_data.update(kwargs)

        # Determine endpoint params
        params = None
        if content_type and get_enum_value(content_type) == "html":
            params = {"source": "html"}

        response = self.client.put(f"posts/{post_id}/", {"posts": [post_data]}, params=params)
        return response["posts"][0] if response.get("posts") else response

    def publish(self, post_id: str, updated_at: str) -> Dict:
        """
        Publish a post immediately

        Args:
            post_id: Post ID to publish
            updated_at: Current updated_at timestamp

        Returns:
            Updated post data
        """
        return self.update(post_id, updated_at, status=PostStatus.PUBLISHED)

    def schedule(self, post_id: str, updated_at: str, publish_at: Union[str, datetime]) -> Dict:
        """
        Schedule a post for future publication

        Args:
            post_id: Post ID to schedule
            updated_at: Current updated_at timestamp
            publish_at: Publication datetime (ISO string or datetime object)

        Returns:
            Updated post data
        """
        if isinstance(publish_at, datetime):
            publish_at = publish_at.isoformat()

        return self.update(post_id, updated_at, status=PostStatus.SCHEDULED, published_at=publish_at)

    def unpublish(self, post_id: str, updated_at: str) -> Dict:
        """
        Unpublish a post (revert to draft)

        Args:
            post_id: Post ID to unpublish
            updated_at: Current updated_at timestamp

        Returns:
            Updated post data
        """
        return self.update(post_id, updated_at, status=PostStatus.DRAFT)

    def delete(self, post_id: str) -> bool:
        """
        Delete a post permanently

        Args:
            post_id: Post ID to delete

        Returns:
            True if deletion was successful
        """
        self.client.delete(f"posts/{post_id}/")
        return True

    def _format_tags(self, tags: List[Union[str, Dict]]) -> List[Dict]:
        """
        Format tags for API request

        Args:
            tags: List of tag names or tag objects

        Returns:
            Formatted tags list
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
        Format authors for API request

        Args:
            authors: List of author emails/IDs or author objects

        Returns:
            Formatted authors list
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
