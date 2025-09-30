"""
Newsletters module for Ghost Admin API.

This module provides functionality for managing Ghost newsletters and email configuration.
Newsletters define email settings, styling, and subscriber management options.

.. module:: pyghost.newsletters
   :synopsis: Ghost Admin API Newsletters management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, Union

from .exceptions import ValidationError
from .enums import NewsletterStatus, NewsletterVisibility, NewsletterSenderReplyTo, get_enum_value


class Newsletters:
    """
    Newsletters module for Ghost Admin API.

    Handles all newsletter-related operations including creation, updates, and configuration
    of email newsletters with styling and sender settings.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> newsletter = client.newsletters.create(
        ...     name="Weekly Digest",
        ...     description="Our weekly newsletter with the latest updates",
        ...     sender_name="MyBlog Team",
        ...     sender_reply_to="newsletter"
        ... )
    """

    def __init__(self, client):
        """
        Initialize Newsletters module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def create(self,
               name: str,
               description: Optional[str] = None,
               sender_name: Optional[str] = None,
               sender_email: Optional[str] = None,
               sender_reply_to: NewsletterSenderReplyTo = NewsletterSenderReplyTo.NEWSLETTER,
               status: NewsletterStatus = NewsletterStatus.ACTIVE,
               visibility: NewsletterVisibility = NewsletterVisibility.MEMBERS,
               subscribe_on_signup: bool = True,
               show_header_icon: bool = True,
               show_header_title: bool = True,
               show_header_name: bool = True,
               title_font_category: str = "sans_serif",
               title_alignment: str = "center",
               show_feature_image: bool = True,
               body_font_category: str = "sans_serif",
               show_badge: bool = True,
               opt_in_existing: bool = False,
               **kwargs) -> Dict:
        """
        Create a new newsletter.

        :param name: Newsletter name (required)
        :type name: str
        :param description: Newsletter description
        :type description: str, optional
        :param sender_name: Sender name for emails
        :type sender_name: str, optional
        :param sender_email: Sender email address
        :type sender_email: str, optional
        :param sender_reply_to: Reply-to setting ('newsletter' or 'support')
        :type sender_reply_to: str
        :param status: Newsletter status ('active' or 'archived')
        :type status: str
        :param visibility: Newsletter visibility ('members')
        :type visibility: str
        :param subscribe_on_signup: Whether new members auto-subscribe
        :type subscribe_on_signup: bool
        :param show_header_icon: Show header icon in emails
        :type show_header_icon: bool
        :param show_header_title: Show header title in emails
        :type show_header_title: bool
        :param show_header_name: Show header name in emails
        :type show_header_name: bool
        :param title_font_category: Title font ('serif' or 'sans_serif')
        :type title_font_category: str
        :param title_alignment: Title alignment ('left', 'center', 'right')
        :type title_alignment: str
        :param show_feature_image: Show feature images in emails
        :type show_feature_image: bool
        :param body_font_category: Body font ('serif' or 'sans_serif')
        :type body_font_category: str
        :param show_badge: Show Ghost badge in emails
        :type show_badge: bool
        :param opt_in_existing: Opt-in existing members to new newsletter
        :type opt_in_existing: bool
        :param kwargs: Additional newsletter fields
        :type kwargs: dict

        :returns: Created newsletter data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> newsletter = client.newsletters.create(
            ...     name="Product Updates",
            ...     description="Monthly product updates and announcements",
            ...     sender_name="Product Team",
            ...     sender_reply_to="support",
            ...     title_font_category="serif",
            ...     show_badge=False
            ... )

        Note:
            When creating a newsletter with ``opt_in_existing=True``, all existing
            members will be automatically subscribed to the new newsletter.
        """
        # Convert enums to string values
        sender_reply_to_str = get_enum_value(sender_reply_to)
        status_str = get_enum_value(status)
        visibility_str = get_enum_value(visibility)

        # Validate enum values
        if sender_reply_to_str not in ["newsletter", "support"]:
            raise ValidationError("sender_reply_to must be NewsletterSenderReplyTo.NEWSLETTER or NewsletterSenderReplyTo.SUPPORT")

        if status_str not in ["active", "archived"]:
            raise ValidationError("status must be NewsletterStatus.ACTIVE or NewsletterStatus.ARCHIVED")

        if title_font_category not in ["serif", "sans_serif"]:
            raise ValidationError("title_font_category must be 'serif' or 'sans_serif'")

        if body_font_category not in ["serif", "sans_serif"]:
            raise ValidationError("body_font_category must be 'serif' or 'sans_serif'")

        newsletter_data = {
            "name": name,
            "sender_reply_to": sender_reply_to_str,
            "status": status_str,
            "visibility": visibility_str,
            "subscribe_on_signup": subscribe_on_signup,
            "show_header_icon": show_header_icon,
            "show_header_title": show_header_title,
            "show_header_name": show_header_name,
            "title_font_category": title_font_category,
            "title_alignment": title_alignment,
            "show_feature_image": show_feature_image,
            "body_font_category": body_font_category,
            "show_badge": show_badge
        }

        # Add optional fields
        if description:
            newsletter_data["description"] = description
        if sender_name:
            newsletter_data["sender_name"] = sender_name
        if sender_email:
            newsletter_data["sender_email"] = sender_email

        # Add any additional fields
        newsletter_data.update(kwargs)

        # Set up parameters
        params = {}
        if opt_in_existing:
            params["opt_in_existing"] = "true"

        response = self.client.post("newsletters/", {"newsletters": [newsletter_data]}, params=params)
        return response["newsletters"][0] if response.get("newsletters") else response

    def get(self, newsletter_id: str, **kwargs) -> Dict:
        """
        Get a specific newsletter by ID.

        :param newsletter_id: Newsletter ID
        :type newsletter_id: str
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Newsletter data
        :rtype: Dict
        :raises NotFoundError: If newsletter not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> newsletter = client.newsletters.get("newsletter_id_here")
        """
        params = kwargs
        response = self.client.get(f"newsletters/{newsletter_id}/", params=params)
        return response["newsletters"][0] if response.get("newsletters") else response

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List newsletters with optional filtering and pagination.

        :param limit: Number of newsletters to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string (e.g., 'status:active')
        :type filter_: str, optional
        :param order: Ordering specification
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Newsletters list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> newsletters = client.newsletters.list(filter_="status:active")
        """
        params = {}

        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
        if filter_:
            params["filter"] = filter_
        if order:
            params["order"] = order

        params.update(kwargs)

        return self.client.get("newsletters/", params=params)

    def update(self,
               newsletter_id: str,
               name: Optional[str] = None,
               description: Optional[str] = None,
               sender_name: Optional[str] = None,
               sender_email: Optional[str] = None,
               sender_reply_to: Optional[str] = None,
               status: Optional[Union[NewsletterStatus, str]] = None,
               visibility: Optional[Union[NewsletterVisibility, str]] = None,
               subscribe_on_signup: Optional[bool] = None,
               sort_order: Optional[int] = None,
               header_image: Optional[str] = None,
               show_header_icon: Optional[bool] = None,
               show_header_title: Optional[bool] = None,
               show_header_name: Optional[bool] = None,
               title_font_category: Optional[str] = None,
               title_alignment: Optional[str] = None,
               show_feature_image: Optional[bool] = None,
               body_font_category: Optional[str] = None,
               footer_content: Optional[str] = None,
               show_badge: Optional[bool] = None,
               **kwargs) -> Dict:
        """
        Update an existing newsletter.

        :param newsletter_id: Newsletter ID to update
        :type newsletter_id: str
        :param name: New newsletter name
        :type name: str, optional
        :param description: New newsletter description
        :type description: str, optional
        :param sender_name: New sender name
        :type sender_name: str, optional
        :param sender_email: New sender email
        :type sender_email: str, optional
        :param sender_reply_to: New reply-to setting ('newsletter' or 'support')
        :type sender_reply_to: str, optional
        :param status: New status ('active' or 'archived')
        :type status: str, optional
        :param visibility: New visibility setting
        :type visibility: str, optional
        :param subscribe_on_signup: New auto-subscribe setting
        :type subscribe_on_signup: bool, optional
        :param sort_order: Newsletter sort order
        :type sort_order: int, optional
        :param header_image: Header image URL
        :type header_image: str, optional
        :param show_header_icon: Show header icon setting
        :type show_header_icon: bool, optional
        :param show_header_title: Show header title setting
        :type show_header_title: bool, optional
        :param show_header_name: Show header name setting
        :type show_header_name: bool, optional
        :param title_font_category: Title font category ('serif' or 'sans_serif')
        :type title_font_category: str, optional
        :param title_alignment: Title alignment setting
        :type title_alignment: str, optional
        :param show_feature_image: Show feature image setting
        :type show_feature_image: bool, optional
        :param body_font_category: Body font category ('serif' or 'sans_serif')
        :type body_font_category: str, optional
        :param footer_content: Newsletter footer content
        :type footer_content: str, optional
        :param show_badge: Show Ghost badge setting
        :type show_badge: bool, optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated newsletter data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_newsletter = client.newsletters.update(
            ...     newsletter_id="newsletter_id",
            ...     name="Updated Newsletter Name",
            ...     description="Updated description",
            ...     show_badge=False
            ... )

        Note:
            Only provide the fields you want to update. Unspecified fields will remain unchanged.
        """
        # Validate enum values if provided
        if sender_reply_to and sender_reply_to not in ["newsletter", "support"]:
            raise ValidationError("sender_reply_to must be 'newsletter' or 'support'")

        if status and status not in ["active", "archived"]:
            raise ValidationError("status must be 'active' or 'archived'")

        if title_font_category and title_font_category not in ["serif", "sans_serif"]:
            raise ValidationError("title_font_category must be 'serif' or 'sans_serif'")

        if body_font_category and body_font_category not in ["serif", "sans_serif"]:
            raise ValidationError("body_font_category must be 'serif' or 'sans_serif'")

        newsletter_data = {}

        # Add fields to update
        if name is not None:
            newsletter_data["name"] = name
        if description is not None:
            newsletter_data["description"] = description
        if sender_name is not None:
            newsletter_data["sender_name"] = sender_name
        if sender_email is not None:
            newsletter_data["sender_email"] = sender_email
        if sender_reply_to is not None:
            newsletter_data["sender_reply_to"] = sender_reply_to
        if status is not None:
            newsletter_data["status"] = status
        if visibility is not None:
            newsletter_data["visibility"] = visibility
        if subscribe_on_signup is not None:
            newsletter_data["subscribe_on_signup"] = subscribe_on_signup
        if sort_order is not None:
            newsletter_data["sort_order"] = sort_order
        if header_image is not None:
            newsletter_data["header_image"] = header_image
        if show_header_icon is not None:
            newsletter_data["show_header_icon"] = show_header_icon
        if show_header_title is not None:
            newsletter_data["show_header_title"] = show_header_title
        if show_header_name is not None:
            newsletter_data["show_header_name"] = show_header_name
        if title_font_category is not None:
            newsletter_data["title_font_category"] = title_font_category
        if title_alignment is not None:
            newsletter_data["title_alignment"] = title_alignment
        if show_feature_image is not None:
            newsletter_data["show_feature_image"] = show_feature_image
        if body_font_category is not None:
            newsletter_data["body_font_category"] = body_font_category
        if footer_content is not None:
            newsletter_data["footer_content"] = footer_content
        if show_badge is not None:
            newsletter_data["show_badge"] = show_badge

        # Add any additional fields
        newsletter_data.update(kwargs)

        response = self.client.put(f"newsletters/{newsletter_id}/", {"newsletters": [newsletter_data]})
        return response["newsletters"][0] if response.get("newsletters") else response

    def archive(self, newsletter_id: str) -> Dict:
        """
        Archive a newsletter (set status='archived').

        Archived newsletters are no longer active but retain their configuration.

        :param newsletter_id: Newsletter ID to archive
        :type newsletter_id: str

        :returns: Updated newsletter data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> archived_newsletter = client.newsletters.archive("newsletter_id")
        """
        return self.update(newsletter_id, status=NewsletterStatus.ARCHIVED)

    def activate(self, newsletter_id: str) -> Dict:
        """
        Activate a newsletter (set status='active').

        Activated newsletters become available for sending emails.

        :param newsletter_id: Newsletter ID to activate
        :type newsletter_id: str

        :returns: Updated newsletter data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> active_newsletter = client.newsletters.activate("newsletter_id")
        """
        return self.update(newsletter_id, status=NewsletterStatus.ACTIVE)

    def get_default_newsletter(self) -> Optional[Dict]:
        """
        Get the default newsletter.

        Every Ghost site typically has a default newsletter. This is a convenience
        method to retrieve it.

        :returns: Default newsletter data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> default_newsletter = client.newsletters.get_default_newsletter()
            >>> if default_newsletter:
            ...     print(f"Default newsletter: {default_newsletter['name']}")
        """
        response = self.list(limit=1, order="created_at asc")
        newsletters = response.get("newsletters", [])
        return newsletters[0] if newsletters else None

    def validate_sender_email(self, newsletter_id: str, email: str) -> Dict:
        """
        Validate sender email address for a newsletter.

        This endpoint triggers email validation for the specified sender email.
        Ghost will send a validation email to confirm ownership.

        :param newsletter_id: Newsletter ID
        :type newsletter_id: str
        :param email: Email address to validate
        :type email: str

        :returns: Validation response
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> validation = client.newsletters.validate_sender_email(
            ...     "newsletter_id",
            ...     "sender@mydomain.com"
            ... )

        Note:
            After calling this method, check the specified email address for a
            validation email from Ghost. The email must be verified before it
            can be used as a sender email.
        """
        validation_data = {"email": email}
        response = self.client.post(f"newsletters/{newsletter_id}/verify-email/", validation_data)
        return response

    def get_active_newsletters(self) -> List[Dict]:
        """
        Get all active newsletters.

        Convenience method to retrieve all active newsletters.

        :returns: List of active newsletter data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> active_newsletters = client.newsletters.get_active_newsletters()
            >>> for newsletter in active_newsletters:
            ...     print(f"Active: {newsletter['name']}")
        """
        response = self.list(filter_="status:active")
        return response.get("newsletters", [])
