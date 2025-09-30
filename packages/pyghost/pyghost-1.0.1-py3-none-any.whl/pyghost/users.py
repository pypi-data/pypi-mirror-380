"""
Users module for Ghost Admin API.

This module provides functionality for managing Ghost users (site staff/authors)
including
their roles, permissions, profiles, and invitation management.

.. module:: pyghost.users
   :synopsis: Ghost Admin API Users management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, Union

from .enums import UserRole, UserStatus, get_enum_value


class Users:
    """
    Users module for Ghost Admin API.

    Handles all user-related operations including profile management, role assignments,
    permissions, invitations, and user administration for site staff and authors.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(
        ...     site_url="https://mysite.ghost.io",
        ...     admin_api_key="key:secret"
        ... )
        >>> user = client.users.update(
        ...     user_id="user123",
        ...     name="John Author",
        ...     bio="Senior content writer"
        ... )

    Note:
        Users are different from Members. Users are site staff (owners, administrators,
        editors, authors, contributors) while Members are subscribers/customers.
    """

    def __init__(self, client):
        """
        Initialize Users module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def get(self, user_id: str, include: Optional[str] = None, **kwargs) -> Dict:
        """
        Get a specific user by ID.

        :param user_id: User ID
        :type user_id: str
        :param include: Related data to include (e.g., 'count.posts,permissions,roles')
        :type include: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: User data
        :rtype: Dict
        :raises NotFoundError: If user not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> user = client.users.get("user_id", include="count.posts,roles")
            >>> print(f"User {user['name']} has {user['count']['posts']} posts")
        """
        params = kwargs
        if include:
            params["include"] = include

        response = self.client.get(f"users/{user_id}/", params=params)
        return response["users"][0] if response.get("users") else response

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List users with optional filtering and pagination.

        :param limit: Number of users to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string (e.g., 'status:active', 'role:author')
        :type filter_: str, optional
        :param include: Related data to include (e.g., 'count.posts,permissions,roles')
        :type include: str, optional
        :param order: Ordering specification (e.g., 'created_at desc', 'name asc')
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Users list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Get all users
            >>> users = client.users.list()
            >>>
            >>> # Get active authors only
            >>> authors = client.users.list(
            ...     filter_="role:author+status:active",
            ...     include="count.posts",
            ...     order="name asc"
            ... )
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

        return self.client.get("users/", params=params)

    def update(self,
               user_id: str,
               name: Optional[str] = None,
               email: Optional[str] = None,
               bio: Optional[str] = None,
               website: Optional[str] = None,
               location: Optional[str] = None,
               facebook: Optional[str] = None,
               twitter: Optional[str] = None,
               profile_image: Optional[str] = None,
               cover_image: Optional[str] = None,
               meta_title: Optional[str] = None,
               meta_description: Optional[str] = None,
               roles: Optional[List[UserRole]] = None,
               **kwargs) -> Dict:
        """
        Update an existing user's profile and settings.

        :param user_id: User ID to update
        :type user_id: str
        :param name: Display name
        :type name: str, optional
        :param email: Email address
        :type email: str, optional
        :param bio: User biography
        :type bio: str, optional
        :param website: Website URL
        :type website: str, optional
        :param location: User location
        :type location: str, optional
        :param facebook: Facebook profile URL
        :type facebook: str, optional
        :param twitter: Twitter handle (with or without @)
        :type twitter: str, optional
        :param profile_image: Profile image URL
        :type profile_image: str, optional
        :param cover_image: Cover image URL
        :type cover_image: str, optional
        :param meta_title: SEO meta title
        :type meta_title: str, optional
        :param meta_description: SEO meta description
        :type meta_description: str, optional
        :param roles: List of role IDs to assign to the user
        :type roles: List[str], optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated user data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_user = client.users.update(
            ...     user_id="user123",
            ...     name="John Author",
            ...     bio="Senior content writer with 5 years experience",
            ...     website="https://johnauthor.com",
            ...     twitter="@johnauthor"
            ... )

        Note:
            - Only site owners can update user roles
            - Users can only update their own profiles unless they have admin
              permissions
        """
        user_data = {}

        # Add basic profile fields
        if name is not None:
            user_data["name"] = name
        if email is not None:
            user_data["email"] = email
        if bio is not None:
            user_data["bio"] = bio
        if website is not None:
            user_data["website"] = website
        if location is not None:
            user_data["location"] = location

        # Add social media fields
        if facebook is not None:
            user_data["facebook"] = facebook
        if twitter is not None:
            # Normalize Twitter handle
            user_data["twitter"] = twitter.lstrip("@") if twitter else twitter

        # Add image fields
        if profile_image is not None:
            user_data["profile_image"] = profile_image
        if cover_image is not None:
            user_data["cover_image"] = cover_image

        # Add SEO fields
        if meta_title is not None:
            user_data["meta_title"] = meta_title
        if meta_description is not None:
            user_data["meta_description"] = meta_description

        # Add roles (requires appropriate permissions)
        if roles is not None:
            user_data["roles"] = [
                {"id": get_enum_value(role)} if hasattr(role, 'value') else {"id": role}
                for role in roles
            ]

        # Add any additional fields
        user_data.update(kwargs)

        response = self.client.put(f"users/{user_id}/", {"users": [user_data]})
        return response["users"][0] if response.get("users") else response

    def delete(self, user_id: str) -> bool:
        """
        Delete a user permanently.

        :param user_id: User ID to delete
        :type user_id: str

        :returns: True if deletion was successful
        :rtype: bool
        :raises NotFoundError: If user not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> success = client.users.delete("user_id")
            >>> if success:
            ...     print("User deleted successfully")

        Warning:
            - This operation is permanent and cannot be undone
            - User's posts will remain but will be marked as authored by deleted user
            - Only owners can delete users
            - Cannot delete the site owner
        """
        self.client.delete(f"users/{user_id}/")
        return True

    def get_by_email(self, email: str, include: Optional[str] = None) -> Optional[Dict]:
        """
        Get a user by email address.

        :param email: User email address
        :type email: str
        :param include: Related data to include
        :type include: str, optional

        :returns: User data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> user = client.users.get_by_email("author@example.com")
            >>> if user:
            ...     print(f"Found user: {user['name']}")
        """
        params = {"filter": f"email:{email}"}
        if include:
            params["include"] = include

        response = self.list(**params)
        users = response.get("users", [])
        return users[0] if users else None

    def get_by_slug(self, slug: str, include: Optional[str] = None) -> Optional[Dict]:
        """
        Get a user by slug.

        :param slug: User slug
        :type slug: str
        :param include: Related data to include
        :type include: str, optional

        :returns: User data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> user = client.users.get_by_slug("john-author")
            >>> if user:
            ...     print(f"Found user: {user['name']}")
        """
        params = {"filter": f"slug:{slug}"}
        if include:
            params["include"] = include

        response = self.list(**params)
        users = response.get("users", [])
        return users[0] if users else None

    def get_owners(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all users with Owner role.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of owner user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> owners = client.users.get_owners()
            >>> print(f"Site has {len(owners)} owners")
        """
        response = self.list(filter_=f"role:{UserRole.OWNER.value}", include=include)
        return response.get("users", [])

    def get_administrators(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all users with Administrator role.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of administrator user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> admins = client.users.get_administrators()
            >>> print(f"Site has {len(admins)} administrators")
        """
        response = self.list(filter_=f"role:{UserRole.ADMINISTRATOR.value}", include=include)
        return response.get("users", [])

    def get_editors(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all users with Editor role.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of editor user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> editors = client.users.get_editors()
            >>> print(f"Site has {len(editors)} editors")
        """
        response = self.list(filter_=f"role:{UserRole.EDITOR.value}", include=include)
        return response.get("users", [])

    def get_authors(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all users with Author role.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of author user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> authors = client.users.get_authors(include="count.posts")
            >>> for author in authors:
            ...     print(f"{author['name']}: {author['count']['posts']} posts")
        """
        response = self.list(filter_=f"role:{UserRole.AUTHOR.value}", include=include)
        return response.get("users", [])

    def get_contributors(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all users with Contributor role.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of contributor user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> contributors = client.users.get_contributors()
            >>> print(f"Site has {len(contributors)} contributors")
        """
        response = self.list(filter_=f"role:{UserRole.CONTRIBUTOR.value}", include=include)
        return response.get("users", [])

    def get_active_users(self, include: Optional[str] = None) -> List[Dict]:
        """
        Get all active users.

        :param include: Related data to include
        :type include: str, optional

        :returns: List of active user data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> active_users = client.users.get_active_users()
            >>> print(f"Site has {len(active_users)} active users")
        """
        response = self.list(filter_=f"status:{UserStatus.ACTIVE.value}", include=include)
        return response.get("users", [])

    def update_notification_settings(
            self,
            user_id: str,
            comment_notifications: Optional[bool] = None,
            free_member_signup_notification: Optional[bool] = None,
            paid_subscription_started_notification: Optional[bool] = None,
            paid_subscription_canceled_notification: Optional[bool] = None,
            mention_notifications: Optional[bool] = None,
            milestone_notifications: Optional[bool] = None) -> Dict:
        """
        Update user notification preferences.

        :param user_id: User ID
        :type user_id: str
        :param comment_notifications: Enable comment notifications
        :type comment_notifications: bool, optional
        :param free_member_signup_notification: Enable free member signup
            notifications
        :type free_member_signup_notification: bool, optional
        :param paid_subscription_started_notification: Enable paid subscription
            start notifications
        :type paid_subscription_started_notification: bool, optional
        :param paid_subscription_canceled_notification: Enable subscription
            cancellation notifications
        :type paid_subscription_canceled_notification: bool, optional
        :param mention_notifications: Enable mention notifications
        :type mention_notifications: bool, optional
        :param milestone_notifications: Enable milestone notifications
        :type milestone_notifications: bool, optional

        :returns: Updated user data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_user = client.users.update_notification_settings(
            ...     "user_id",
            ...     comment_notifications=True,
            ...     mention_notifications=False,
            ...     milestone_notifications=True
            ... )
        """
        notification_data = {}

        if comment_notifications is not None:
            notification_data["comment_notifications"] = comment_notifications
        if free_member_signup_notification is not None:
            notification_data["free_member_signup_notification"] = \
                free_member_signup_notification
        if paid_subscription_started_notification is not None:
            notification_data["paid_subscription_started_notification"] = \
                paid_subscription_started_notification
        if paid_subscription_canceled_notification is not None:
            notification_data["paid_subscription_canceled_notification"] = \
                paid_subscription_canceled_notification
        if mention_notifications is not None:
            notification_data["mention_notifications"] = mention_notifications
        if milestone_notifications is not None:
            notification_data["milestone_notifications"] = milestone_notifications

        return self.update(user_id, **notification_data)

    def change_password(self, user_id: str, old_password: str,
                        new_password: str) -> Dict:
        """
        Change a user's password.

        :param user_id: User ID
        :type user_id: str
        :param old_password: Current password
        :type old_password: str
        :param new_password: New password
        :type new_password: str

        :returns: Updated user data
        :rtype: Dict
        :raises ValidationError: If old password is incorrect or new password is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_user = client.users.change_password(
            ...     "user_id",
            ...     "old_password",
            ...     "new_secure_password"
            ... )

        Note:
            - Users can only change their own password unless they have admin
              permissions
            - Password must meet minimum security requirements
        """
        password_data = {
            "password": [{
                "user_id": user_id,
                "oldPassword": old_password,
                "newPassword": new_password
            }]
        }

        return self.client.put("users/password/", password_data)

    def get_user_roles(self) -> List[Dict]:
        """
        Get all available user roles.

        :returns: List of role data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> roles = client.users.get_user_roles()
            >>> for role in roles:
            ...     print(f"Role: {role['name']} - {role['description']}")
        """
        response = self.client.get("roles/")
        return response.get("roles", [])

    def get_user_permissions(self, user_id: str) -> List[Dict]:
        """
        Get permissions for a specific user.

        :param user_id: User ID
        :type user_id: str

        :returns: List of permission data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> permissions = client.users.get_user_permissions("user_id")
            >>> print(f"User has {len(permissions)} permissions")
        """
        user = self.get(user_id, include="permissions,roles")
        return user.get("permissions", [])

    def get_user_statistics(self) -> Dict:
        """
        Get basic user statistics.

        :returns: Dictionary with user statistics by role
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> stats = client.users.get_user_statistics()
            >>> print(f"Authors: {stats['authors']}, Editors: {stats['editors']}")
        """
        # Get counts for different user roles
        all_users = self.list(limit=1)
        owners = self.get_owners()
        administrators = self.get_administrators()
        editors = self.get_editors()
        authors = self.get_authors()
        contributors = self.get_contributors()

        total_count = all_users.get("meta", {}).get("pagination", {}).get("total", 0)

        return {
            "total": total_count,
            "owners": len(owners),
            "administrators": len(administrators),
            "editors": len(editors),
            "authors": len(authors),
            "contributors": len(contributors)
        }
