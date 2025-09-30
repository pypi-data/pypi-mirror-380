"""
Members module for Ghost Admin API.

This module provides functionality for managing Ghost members (subscribers) including
their subscriptions, newsletter preferences, labels, and tier associations.

.. module:: pyghost.members
   :synopsis: Ghost Admin API Members management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional

from .exceptions import ValidationError
from .enums import MemberStatus


class Members:
    """
    Members module for Ghost Admin API.

    Handles all member-related operations including creation, updates, subscription management,
    label assignment, and newsletter preferences for site subscribers.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> member = client.members.create(
        ...     email="subscriber@example.com",
        ...     name="John Subscriber",
        ...     labels=["VIP", "Newsletter"]
        ... )
    """

    def __init__(self, client):
        """
        Initialize Members module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def create(self,
               email: str,
               name: Optional[str] = None,
               note: Optional[str] = None,
               labels: Optional[List[str]] = None,
               newsletters: Optional[List[str]] = None,
               tiers: Optional[List[str]] = None,
               **kwargs) -> Dict:
        """
        Create a new member.

        :param email: Member email address (required, must be unique)
        :type email: str
        :param name: Member display name
        :type name: str, optional
        :param note: Internal note about the member
        :type note: str, optional
        :param labels: List of label names to assign to the member
        :type labels: List[str], optional
        :param newsletters: List of newsletter IDs to subscribe the member to
        :type newsletters: List[str], optional
        :param tiers: List of tier IDs to associate with the member
        :type tiers: List[str], optional
        :param kwargs: Additional member fields
        :type kwargs: dict

        :returns: Created member data
        :rtype: Dict
        :raises ValidationError: If validation fails (e.g., duplicate email)
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Create a basic member
            >>> member = client.members.create(
            ...     email="subscriber@example.com",
            ...     name="John Subscriber"
            ... )
            >>>
            >>> # Create a member with labels and newsletter subscriptions
            >>> premium_member = client.members.create(
            ...     email="premium@example.com",
            ...     name="Premium Subscriber",
            ...     note="VIP customer from email campaign",
            ...     labels=["VIP", "Premium", "Newsletter"],
            ...     newsletters=["newsletter_id_1", "newsletter_id_2"]
            ... )

        Note:
            - Email addresses must be unique across all members
            - Labels will be created automatically if they don't exist
            - Newsletter and tier IDs must reference existing resources
        """
        if not email:
            raise ValidationError("Email is required for member creation")

        member_data = {
            "email": email
        }

        # Add optional basic fields
        if name:
            member_data["name"] = name
        if note:
            member_data["note"] = note

        # Add labels (convert strings to label objects)
        if labels:
            member_data["labels"] = [
                {"name": label} if isinstance(label, str) else label
                for label in labels
            ]

        # Add newsletter subscriptions
        if newsletters:
            member_data["newsletters"] = [
                {"id": newsletter_id} if isinstance(newsletter_id, str) else newsletter_id
                for newsletter_id in newsletters
            ]

        # Add tier associations
        if tiers:
            member_data["tiers"] = [
                {"id": tier_id} if isinstance(tier_id, str) else tier_id
                for tier_id in tiers
            ]

        # Add any additional fields
        member_data.update(kwargs)

        response = self.client.post("members/", {"members": [member_data]})
        return response["members"][0] if response.get("members") else response

    def get(self, member_id: str, include: Optional[str] = None, **kwargs) -> Dict:
        """
        Get a specific member by ID.

        :param member_id: Member ID
        :type member_id: str
        :param include: Related data to include (e.g., 'newsletters,labels,tiers')
        :type include: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Member data
        :rtype: Dict
        :raises NotFoundError: If member not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> member = client.members.get("member_id_here", include="newsletters,labels")
        """
        params = kwargs
        if include:
            params["include"] = include

        response = self.client.get(f"members/{member_id}/", params=params)
        return response["members"][0] if response.get("members") else response

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List members with optional filtering and pagination.

        :param limit: Number of members to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string (e.g., 'status:paid', 'email:~gmail.com')
        :type filter_: str, optional
        :param include: Related data to include (e.g., 'newsletters,labels,tiers')
        :type include: str, optional
        :param order: Ordering specification (e.g., 'created_at desc', 'email asc')
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Members list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Get all members
            >>> members = client.members.list()
            >>>
            >>> # Get paid members only
            >>> paid_members = client.members.list(
            ...     filter_="status:paid",
            ...     include="newsletters,tiers",
            ...     order="created_at desc"
            ... )
            >>>
            >>> # Get members with specific email domain
            >>> gmail_members = client.members.list(filter_="email:~gmail.com")
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

        return self.client.get("members/", params=params)

    def update(self,
               member_id: str,
               email: Optional[str] = None,
               name: Optional[str] = None,
               note: Optional[str] = None,
               labels: Optional[List[str]] = None,
               newsletters: Optional[List[str]] = None,
               tiers: Optional[List[str]] = None,
               **kwargs) -> Dict:
        """
        Update an existing member.

        :param member_id: Member ID to update
        :type member_id: str
        :param email: New email address
        :type email: str, optional
        :param name: New member name
        :type name: str, optional
        :param note: New internal note
        :type note: str, optional
        :param labels: New list of label names (replaces existing labels)
        :type labels: List[str], optional
        :param newsletters: New list of newsletter IDs (replaces existing subscriptions)
        :type newsletters: List[str], optional
        :param tiers: New list of tier IDs (replaces existing tier associations)
        :type tiers: List[str], optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated member data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_member = client.members.update(
            ...     member_id="member_id",
            ...     name="Updated Name",
            ...     note="Updated customer status",
            ...     labels=["Premium", "Updated"]
            ... )

        Note:
            When updating labels, newsletters, or tiers, the entire list is replaced.
            To add/remove individual items, get current data first and modify the list.
        """
        member_data = {}

        # Add fields to update
        if email is not None:
            member_data["email"] = email
        if name is not None:
            member_data["name"] = name
        if note is not None:
            member_data["note"] = note

        # Update labels (replace existing)
        if labels is not None:
            member_data["labels"] = [
                {"name": label} if isinstance(label, str) else label
                for label in labels
            ]

        # Update newsletter subscriptions (replace existing)
        if newsletters is not None:
            member_data["newsletters"] = [
                {"id": newsletter_id} if isinstance(newsletter_id, str) else newsletter_id
                for newsletter_id in newsletters
            ]

        # Update tier associations (replace existing)
        if tiers is not None:
            member_data["tiers"] = [
                {"id": tier_id} if isinstance(tier_id, str) else tier_id
                for tier_id in tiers
            ]

        # Add any additional fields
        member_data.update(kwargs)

        response = self.client.put(f"members/{member_id}/", {"members": [member_data]})
        return response["members"][0] if response.get("members") else response

    def delete(self, member_id: str) -> bool:
        """
        Delete a member permanently.

        :param member_id: Member ID to delete
        :type member_id: str

        :returns: True if deletion was successful
        :rtype: bool
        :raises NotFoundError: If member not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> success = client.members.delete("member_id")
            >>> if success:
            ...     print("Member deleted successfully")

        Warning:
            This operation is permanent and cannot be undone. The member's subscription
            history and analytics data will also be lost.
        """
        self.client.delete(f"members/{member_id}/")
        return True

    def get_by_email(self, email: str, include: Optional[str] = None) -> Optional[Dict]:
        """
        Get a member by email address.

        :param email: Member email address
        :type email: str
        :param include: Related data to include
        :type include: str, optional

        :returns: Member data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> member = client.members.get_by_email("subscriber@example.com")
            >>> if member:
            ...     print(f"Found member: {member['name']}")
        """
        params = {"filter": f"email:{email}"}
        if include:
            params["include"] = include

        response = self.list(**params)
        members = response.get("members", [])
        return members[0] if members else None

    def add_labels(self, member_id: str, labels: List[str]) -> Dict:
        """
        Add labels to a member (preserves existing labels).

        :param member_id: Member ID
        :type member_id: str
        :param labels: List of label names to add
        :type labels: List[str]

        :returns: Updated member data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_member = client.members.add_labels(
            ...     "member_id",
            ...     ["New Label", "Another Label"]
            ... )
        """
        # Get current member data
        current_member = self.get(member_id, include="labels")
        existing_labels = current_member.get("labels", [])
        existing_label_names = {label["name"] for label in existing_labels}

        # Add new labels (avoid duplicates)
        for label in labels:
            if label not in existing_label_names:
                existing_labels.append({"name": label})

        # Update member with combined labels
        return self.update(member_id, labels=[label["name"] for label in existing_labels])

    def remove_labels(self, member_id: str, labels: List[str]) -> Dict:
        """
        Remove labels from a member.

        :param member_id: Member ID
        :type member_id: str
        :param labels: List of label names to remove
        :type labels: List[str]

        :returns: Updated member data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_member = client.members.remove_labels(
            ...     "member_id",
            ...     ["Old Label", "Expired Label"]
            ... )
        """
        # Get current member data
        current_member = self.get(member_id, include="labels")
        existing_labels = current_member.get("labels", [])

        # Remove specified labels
        labels_to_remove = set(labels)
        remaining_labels = [
            label for label in existing_labels
            if label["name"] not in labels_to_remove
        ]

        # Update member with remaining labels
        return self.update(member_id, labels=[label["name"] for label in remaining_labels])

    def subscribe_to_newsletters(self, member_id: str, newsletter_ids: List[str]) -> Dict:
        """
        Subscribe a member to additional newsletters (preserves existing subscriptions).

        :param member_id: Member ID
        :type member_id: str
        :param newsletter_ids: List of newsletter IDs to subscribe to
        :type newsletter_ids: List[str]

        :returns: Updated member data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_member = client.members.subscribe_to_newsletters(
            ...     "member_id",
            ...     ["newsletter_id_1", "newsletter_id_2"]
            ... )
        """
        # Get current member data
        current_member = self.get(member_id, include="newsletters")
        existing_newsletters = current_member.get("newsletters", [])
        existing_newsletter_ids = {newsletter["id"] for newsletter in existing_newsletters}

        # Add new newsletter subscriptions (avoid duplicates)
        for newsletter_id in newsletter_ids:
            if newsletter_id not in existing_newsletter_ids:
                existing_newsletters.append({"id": newsletter_id})

        # Update member with combined newsletters
        return self.update(member_id, newsletters=[newsletter["id"] for newsletter in existing_newsletters])

    def unsubscribe_from_newsletters(self, member_id: str, newsletter_ids: List[str]) -> Dict:
        """
        Unsubscribe a member from newsletters.

        :param member_id: Member ID
        :type member_id: str
        :param newsletter_ids: List of newsletter IDs to unsubscribe from
        :type newsletter_ids: List[str]

        :returns: Updated member data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_member = client.members.unsubscribe_from_newsletters(
            ...     "member_id",
            ...     ["newsletter_id_1"]
            ... )
        """
        # Get current member data
        current_member = self.get(member_id, include="newsletters")
        existing_newsletters = current_member.get("newsletters", [])

        # Remove specified newsletter subscriptions
        newsletters_to_remove = set(newsletter_ids)
        remaining_newsletters = [
            newsletter for newsletter in existing_newsletters
            if newsletter["id"] not in newsletters_to_remove
        ]

        # Update member with remaining newsletters
        return self.update(member_id, newsletters=[newsletter["id"] for newsletter in remaining_newsletters])

    def get_paid_members(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all paid members.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of paid member data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> paid_members = client.members.get_paid_members(include="tiers,subscriptions")
            >>> print(f"Found {len(paid_members)} paid members")
        """
        response = self.list(filter_=f"status:{MemberStatus.PAID.value}", include=include)
        return response.get("members", [])

    def get_free_members(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all free members.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of free member data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> free_members = client.members.get_free_members()
            >>> print(f"Found {len(free_members)} free members")
        """
        response = self.list(filter_=f"status:{MemberStatus.FREE.value}", include=include)
        return response.get("members", [])

    def get_members_by_label(self, label_name: str, include: Optional[str] = None) -> List[Dict]:
        """
        Get all members with a specific label.

        :param label_name: Label name to filter by
        :type label_name: str
        :param include: Related data to include
        :type include: str, optional

        :returns: List of member data with the specified label
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> vip_members = client.members.get_members_by_label("VIP")
            >>> print(f"Found {len(vip_members)} VIP members")
        """
        response = self.list(filter_=f"label:{label_name}", include=include)
        return response.get("members", [])

    def get_member_statistics(self) -> Dict:
        """
        Get basic member statistics.

        :returns: Dictionary with member statistics
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> stats = client.members.get_member_statistics()
            >>> print(f"Total: {stats['total']}, Paid: {stats['paid']}, Free: {stats['free']}")
        """
        # Get counts for different member types
        all_members = self.list(limit=1)
        paid_members = self.list(filter_=f"status:{MemberStatus.PAID.value}", limit=1)
        free_members = self.list(filter_=f"status:{MemberStatus.FREE.value}", limit=1)

        total_count = all_members.get("meta", {}).get("pagination", {}).get("total", 0)
        paid_count = paid_members.get("meta", {}).get("pagination", {}).get("total", 0)
        free_count = free_members.get("meta", {}).get("pagination", {}).get("total", 0)

        return {
            "total": total_count,
            "paid": paid_count,
            "free": free_count,
            "paid_percentage": (paid_count / total_count * 100) if total_count > 0 else 0
        }
