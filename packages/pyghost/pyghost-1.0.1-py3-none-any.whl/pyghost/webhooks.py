"""
Webhooks module for Ghost Admin API.

This module provides functionality for managing Ghost webhooks including
webhook creation, updating, deletion, and event management.

.. module:: pyghost.webhooks
   :synopsis: Ghost Admin API Webhooks management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, Union

from .enums import WebhookEvent, WebhookStatus, get_enum_value


class Webhooks:
    """
    Webhooks module for Ghost Admin API.

    Handles all webhook-related operations including webhook creation, updates,
    deletion, and event management for Ghost sites.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(
        ...     site_url="https://mysite.ghost.io",
        ...     admin_api_key="key:secret"
        ... )
        >>> webhook = client.webhooks.create(
        ...     event="post.published",
        ...     target_url="https://example.com/webhook"
        ... )

    Note:
        Webhooks allow Ghost to send HTTP requests to external URLs when
        specific events occur, enabling real-time integrations.
    """

    def __init__(self, client):
        """
        Initialize the Webhooks module.

        :param client: The GhostClient instance
        :type client: GhostClient
        """
        self.client = client

    def create(self, event: Union[WebhookEvent, str], target_url: str, name: Optional[str] = None,
               secret: Optional[str] = None, api_version: Optional[str] = None,
               integration_id: Optional[str] = None) -> Dict:
        """
        Create a new webhook.

        :param event: The event that triggers the webhook
        :type event: Union[WebhookEvent, str]
        :param target_url: The URL to send the webhook payload to
        :type target_url: str
        :param name: Optional name for the webhook
        :type name: str, optional
        :param secret: Optional secret for webhook verification
        :type secret: str, optional
        :param api_version: API version for the webhook
        :type api_version: str, optional
        :param integration_id: Integration ID (required for token authentication)
        :type integration_id: str, optional

        :returns: Created webhook data
        :rtype: Dict
        :raises ValidationError: If required parameters are missing or invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> webhook = client.webhooks.create(
            ...     event="post.published",
            ...     target_url="https://example.com/webhook",
            ...     name="My Webhook",
            ...     secret="my-secret-key"
            ... )
            >>> print(f"Created webhook: {webhook['id']}")
        """
        if not event:
            raise ValueError("Event cannot be empty")
        if not target_url:
            raise ValueError("Target URL cannot be empty")

        # Convert enum to string value
        event_str = get_enum_value(event)

        webhook_data = {
            "event": event_str,
            "target_url": target_url
        }

        # Add optional fields if provided
        if name is not None:
            webhook_data["name"] = name
        if secret is not None:
            webhook_data["secret"] = secret
        if api_version is not None:
            webhook_data["api_version"] = api_version
        if integration_id is not None:
            webhook_data["integration_id"] = integration_id

        data = {"webhooks": [webhook_data]}

        response = self.client.post("webhooks", data=data)
        return response.get("webhooks", [{}])[0]

    def list(self, limit: Optional[int] = None,
             filter_: Optional[str] = None) -> Dict:
        """
        List all webhooks.

        :param limit: Maximum number of webhooks to return
        :type limit: int, optional
        :param filter_: Filter string for webhook queries
        :type filter_: str, optional

        :returns: Dictionary containing webhooks list and metadata
        :rtype: Dict
        :raises GhostAPIError: If the API request fails

        Example:
            >>> webhooks = client.webhooks.list(limit=10)
            >>> for webhook in webhooks['webhooks']:
            ...     print(f"Webhook: {webhook['event']} -> {webhook['target_url']}")
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if filter_ is not None:
            params["filter"] = filter_

        return self.client.get("webhooks", params=params)

    def get(self, webhook_id: str) -> Dict:
        """
        Get a specific webhook by ID.

        :param webhook_id: The webhook ID
        :type webhook_id: str

        :returns: Webhook data
        :rtype: Dict
        :raises ValidationError: If webhook ID is invalid
        :raises GhostAPIError: If the API request fails or webhook not found

        Example:
            >>> webhook = client.webhooks.get("webhook_id_here")
            >>> print(f"Webhook event: {webhook['event']}")
        """
        if not webhook_id:
            raise ValueError("Webhook ID cannot be empty")

        response = self.client.get(f"webhooks/{webhook_id}")
        return response.get("webhooks", [{}])[0]

    def update(self, webhook_id: str, event: Optional[str] = None,
               target_url: Optional[str] = None, name: Optional[str] = None,
               secret: Optional[str] = None, api_version: Optional[str] = None) -> Dict:
        """
        Update an existing webhook.

        :param webhook_id: The webhook ID to update
        :type webhook_id: str
        :param event: New event for the webhook
        :type event: str, optional
        :param target_url: New target URL for the webhook
        :type target_url: str, optional
        :param name: New name for the webhook
        :type name: str, optional
        :param secret: New secret for the webhook
        :type secret: str, optional
        :param api_version: New API version for the webhook
        :type api_version: str, optional

        :returns: Updated webhook data
        :rtype: Dict
        :raises ValidationError: If webhook ID is invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> updated_webhook = client.webhooks.update(
            ...     webhook_id="webhook_id_here",
            ...     target_url="https://new-url.com/webhook",
            ...     name="Updated Webhook Name"
            ... )
        """
        if not webhook_id:
            raise ValueError("Webhook ID cannot be empty")

        webhook_data = {}

        # Add fields to update if provided
        if event is not None:
            webhook_data["event"] = event
        if target_url is not None:
            webhook_data["target_url"] = target_url
        if name is not None:
            webhook_data["name"] = name
        if secret is not None:
            webhook_data["secret"] = secret
        if api_version is not None:
            webhook_data["api_version"] = api_version

        if not webhook_data:
            raise ValueError("At least one field must be provided for update")

        data = {"webhooks": [webhook_data]}

        response = self.client.put(f"webhooks/{webhook_id}", data=data)
        return response.get("webhooks", [{}])[0]

    def delete(self, webhook_id: str) -> bool:
        """
        Delete a webhook.

        :param webhook_id: The webhook ID to delete
        :type webhook_id: str

        :returns: True if deletion was successful
        :rtype: bool
        :raises ValidationError: If webhook ID is invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> success = client.webhooks.delete("webhook_id_here")
            >>> if success:
            ...     print("Webhook deleted successfully")
        """
        if not webhook_id:
            raise ValueError("Webhook ID cannot be empty")

        self.client.delete(f"webhooks/{webhook_id}")
        return True

    def test_webhook(self, webhook_id: str) -> Dict:
        """
        Test a webhook by triggering it manually (if supported).

        Note: This is a utility method. The Ghost Admin API may not provide
        a direct webhook testing endpoint.

        :param webhook_id: The webhook ID to test
        :type webhook_id: str

        :returns: Test result information
        :rtype: Dict
        :raises NotImplementedError: If webhook testing is not available

        Example:
            >>> result = client.webhooks.test_webhook("webhook_id_here")
            >>> print(f"Test result: {result['status']}")
        """
        raise NotImplementedError(
            "Webhook testing is not available through the Ghost Admin API. "
            "Webhooks are triggered automatically by Ghost events."
        )

    def get_webhook_events(self) -> List[str]:
        """
        Get list of available webhook events.

        :returns: List of available webhook event types
        :rtype: List[str]

        Example:
            >>> events = client.webhooks.get_webhook_events()
            >>> print(f"Available events: {', '.join(events)}")
        """
        return [
            "post.added",
            "post.deleted",
            "post.edited",
            "post.published",
            "post.unpublished",
            "post.scheduled",
            "post.unscheduled",
            "page.added",
            "page.deleted",
            "page.edited",
            "page.published",
            "page.unpublished",
            "page.scheduled",
            "page.unscheduled",
            "tag.added",
            "tag.edited",
            "tag.deleted",
            "user.activated",
            "user.attached",
            "user.detached",
            "member.added",
            "member.edited",
            "member.deleted"
        ]

    def validate_webhook_event(self, event: str) -> bool:
        """
        Validate if an event type is supported for webhooks.

        :param event: The event type to validate
        :type event: str

        :returns: True if event is valid, False otherwise
        :rtype: bool

        Example:
            >>> is_valid = client.webhooks.validate_webhook_event("post.published")
            >>> print(f"Valid event: {is_valid}")
        """
        available_events = self.get_webhook_events()
        return event in available_events

    def get_webhooks_by_event(self, event: str) -> List[Dict]:
        """
        Get all webhooks for a specific event type.

        :param event: The event type to filter by
        :type event: str

        :returns: List of webhooks for the specified event
        :rtype: List[Dict]
        :raises GhostAPIError: If the API request fails

        Example:
            >>> webhooks = client.webhooks.get_webhooks_by_event("post.published")
            >>> print(f"Found {len(webhooks)} webhooks for post.published")
        """
        if not self.validate_webhook_event(event):
            raise ValueError(f"Invalid webhook event: {event}")

        response = self.list(filter_=f"event:{event}")
        return response.get("webhooks", [])

    def get_active_webhooks(self) -> List[Dict]:
        """
        Get all active webhooks.

        :returns: List of active webhooks
        :rtype: List[Dict]
        :raises GhostAPIError: If the API request fails

        Example:
            >>> active_webhooks = client.webhooks.get_active_webhooks()
            >>> print(f"Found {len(active_webhooks)} active webhooks")
        """
        response = self.list(filter_=f"status:{WebhookStatus.AVAILABLE.value}")
        return response.get("webhooks", [])

    def get_webhook_statistics(self) -> Dict:
        """
        Get webhook statistics and summary information.

        :returns: Webhook statistics
        :rtype: Dict
        :raises GhostAPIError: If the API request fails

        Example:
            >>> stats = client.webhooks.get_webhook_statistics()
            >>> print(f"Total webhooks: {stats['total']}")
            >>> print(f"Active webhooks: {stats['active']}")
        """
        response = self.list()
        webhooks = response.get("webhooks", [])

        stats = {
            "total": len(webhooks),
            "active": len([w for w in webhooks if w.get("status") == WebhookStatus.AVAILABLE.value]),
            "events": {},
            "last_triggered": None
        }

        # Count webhooks by event type
        for webhook in webhooks:
            event = webhook.get("event", "unknown")
            stats["events"][event] = stats["events"].get(event, 0) + 1

            # Track most recent trigger
            last_triggered = webhook.get("last_triggered_at")
            if last_triggered:
                if not stats["last_triggered"] or last_triggered > stats["last_triggered"]:
                    stats["last_triggered"] = last_triggered

        return stats

    def create_post_webhook(self, target_url: str, event: Union[WebhookEvent, str] = "post.published",
                            name: Optional[str] = None, secret: Optional[str] = None) -> Dict:
        """
        Convenience method to create a post-related webhook.

        :param target_url: The URL to send the webhook payload to
        :type target_url: str
        :param event: The post event type (default: "post.published")
        :type event: Union[WebhookEvent, str]
        :param name: Optional name for the webhook
        :type name: str, optional
        :param secret: Optional secret for webhook verification
        :type secret: str, optional

        :returns: Created webhook data
        :rtype: Dict
        :raises ValidationError: If parameters are invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> webhook = client.webhooks.create_post_webhook(
            ...     target_url="https://example.com/post-published",
            ...     name="Post Publication Webhook"
            ... )
        """
        post_events = [e for e in self.get_webhook_events() if e.startswith("post.")]
        if event not in post_events:
            raise ValueError(f"Invalid post event: {event}. Available: {', '.join(post_events)}")

        return self.create(
            event=event,
            target_url=target_url,
            name=name or f"Post {event.split('.')[1].title()} Webhook",
            secret=secret
        )

    def create_member_webhook(self, target_url: str, event: Union[WebhookEvent, str] = "member.added",
                              name: Optional[str] = None, secret: Optional[str] = None) -> Dict:
        """
        Convenience method to create a member-related webhook.

        :param target_url: The URL to send the webhook payload to
        :type target_url: str
        :param event: The member event type (default: "member.added")
        :type event: Union[WebhookEvent, str]
        :param name: Optional name for the webhook
        :type name: str, optional
        :param secret: Optional secret for webhook verification
        :type secret: str, optional

        :returns: Created webhook data
        :rtype: Dict
        :raises ValidationError: If parameters are invalid
        :raises GhostAPIError: If the API request fails

        Example:
            >>> webhook = client.webhooks.create_member_webhook(
            ...     target_url="https://example.com/new-member",
            ...     name="New Member Webhook"
            ... )
        """
        member_events = [e for e in self.get_webhook_events() if e.startswith("member.")]
        if event not in member_events:
            raise ValueError(f"Invalid member event: {event}. Available: {', '.join(member_events)}")

        return self.create(
            event=event,
            target_url=target_url,
            name=name or f"Member {event.split('.')[1].title()} Webhook",
            secret=secret
        )

    def bulk_delete_webhooks(self, webhook_ids: List[str]) -> Dict:
        """
        Delete multiple webhooks in bulk.

        :param webhook_ids: List of webhook IDs to delete
        :type webhook_ids: List[str]

        :returns: Bulk deletion results
        :rtype: Dict
        :raises ValidationError: If webhook IDs are invalid
        :raises GhostAPIError: If any API requests fail

        Example:
            >>> results = client.webhooks.bulk_delete_webhooks([
            ...     "webhook_id_1",
            ...     "webhook_id_2"
            ... ])
            >>> print(f"Deleted: {results['successful']}")
            >>> print(f"Failed: {results['failed']}")
        """
        if not webhook_ids:
            raise ValueError("Webhook IDs list cannot be empty")

        results = {
            "successful": [],
            "failed": [],
            "total": len(webhook_ids)
        }

        for webhook_id in webhook_ids:
            try:
                self.delete(webhook_id)
                results["successful"].append(webhook_id)
            except Exception as e:
                results["failed"].append({"id": webhook_id, "error": str(e)})

        return results
