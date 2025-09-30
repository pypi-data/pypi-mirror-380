"""
Tiers module for Ghost Admin API.

This module provides functionality for managing Ghost subscription tiers and pricing.
Tiers define different membership levels with associated benefits and pricing options.

.. module:: pyghost.tiers
   :synopsis: Ghost Admin API Tiers management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional

from .exceptions import ValidationError
from .enums import TierVisibility, Currency, get_enum_value


class Tiers:
    """
    Tiers module for Ghost Admin API.

    Handles all tier-related operations including creation, updates, and retrieval
    of subscription tiers with pricing and benefits management.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> tier = client.tiers.create(
        ...     name="Premium",
        ...     description="Access to premium content",
        ...     monthly_price=999,
        ...     yearly_price=9999,
        ...     currency="usd",
        ...     benefits=["Premium articles", "Email support"]
        ... )
    """

    def __init__(self, client):
        """
        Initialize Tiers module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def create(self,
               name: str,
               description: Optional[str] = None,
               monthly_price: Optional[int] = None,
               yearly_price: Optional[int] = None,
               currency: Currency = Currency.USD,
               benefits: Optional[List[str]] = None,
               visibility: TierVisibility = TierVisibility.PUBLIC,
               welcome_page_url: Optional[str] = None,
               **kwargs) -> Dict:
        """
        Create a new subscription tier.

        :param name: Tier name (required)
        :type name: str
        :param description: Tier description
        :type description: str, optional
        :param monthly_price: Monthly price in smallest currency unit (e.g., cents)
        :type monthly_price: int, optional
        :param yearly_price: Yearly price in smallest currency unit (e.g., cents)
        :type yearly_price: int, optional
        :param currency: Currency code (ISO 4217)
        :type currency: Currency
        :param benefits: List of benefit descriptions
        :type benefits: List[str], optional
        :param visibility: Tier visibility
        :type visibility: TierVisibility
        :param welcome_page_url: URL for welcome page after subscription
        :type welcome_page_url: str, optional
        :param kwargs: Additional tier fields
        :type kwargs: dict

        :returns: Created tier data
        :rtype: Dict
        :raises ValidationError: If visibility value is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> tier = client.tiers.create(
            ...     name="Gold",
            ...     description="Premium access with exclusive content",
            ...     monthly_price=1999,  # $19.99 in cents
            ...     yearly_price=19999,  # $199.99 in cents
            ...     currency="usd",
            ...     benefits=["Exclusive articles", "Priority support", "Monthly webinars"],
            ...     visibility="public"
            ... )

        Note:
            Prices should be specified in the smallest currency unit (e.g., cents for USD).
            For example, $9.99 should be passed as 999.
        """
        # Convert enums to string values
        currency_str = get_enum_value(currency)
        visibility_str = get_enum_value(visibility)

        if visibility_str not in ["public", "none"]:
            raise ValidationError("visibility must be TierVisibility.PUBLIC or TierVisibility.NONE")

        tier_data = {
            "name": name,
            "currency": currency_str,
            "visibility": visibility_str,
            "active": True  # New tiers are active by default
        }

        # Add optional fields
        if description:
            tier_data["description"] = description
        if monthly_price is not None:
            tier_data["monthly_price"] = monthly_price
        if yearly_price is not None:
            tier_data["yearly_price"] = yearly_price
        if benefits:
            tier_data["benefits"] = benefits
        if welcome_page_url:
            tier_data["welcome_page_url"] = welcome_page_url

        # Add any additional fields
        tier_data.update(kwargs)

        response = self.client.post("tiers/", {"tiers": [tier_data]})
        return response["tiers"][0] if response.get("tiers") else response

    def get(self, tier_id: str, include: Optional[str] = None, **kwargs) -> Dict:
        """
        Get a specific tier by ID.

        :param tier_id: Tier ID
        :type tier_id: str
        :param include: Related data to include (e.g., 'monthly_price,yearly_price,benefits')
        :type include: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Tier data
        :rtype: Dict
        :raises NotFoundError: If tier not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> tier = client.tiers.get("tier_id_here", include="monthly_price,yearly_price,benefits")
        """
        params = kwargs
        if include:
            params["include"] = include

        response = self.client.get(f"tiers/{tier_id}/", params=params)
        return response["tiers"][0] if response.get("tiers") else response

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List tiers with optional filtering and pagination.

        :param limit: Number of tiers to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string (e.g., 'type:paid', 'active:true', 'visibility:public')
        :type filter_: str, optional
        :param include: Related data to include (e.g., 'monthly_price,yearly_price,benefits')
        :type include: str, optional
        :param order: Ordering specification
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Tiers list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Get all paid tiers with pricing info
            >>> tiers = client.tiers.list(
            ...     filter_="type:paid",
            ...     include="monthly_price,yearly_price,benefits"
            ... )
            >>>
            >>> # Get only active public tiers
            >>> active_tiers = client.tiers.list(filter_="active:true+visibility:public")

        Note:
            Common filter options:
            - ``type:free|paid`` - Filter by tier type
            - ``visibility:public|none`` - Filter by visibility
            - ``active:true|false`` - Filter by active status
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

        return self.client.get("tiers/", params=params)

    def update(self,
               tier_id: str,
               name: Optional[str] = None,
               description: Optional[str] = None,
               monthly_price: Optional[int] = None,
               yearly_price: Optional[int] = None,
               currency: Optional[str] = None,
               benefits: Optional[List[str]] = None,
               visibility: Optional[str] = None,
               active: Optional[bool] = None,
               welcome_page_url: Optional[str] = None,
               **kwargs) -> Dict:
        """
        Update an existing tier.

        :param tier_id: Tier ID to update
        :type tier_id: str
        :param name: New tier name
        :type name: str, optional
        :param description: New tier description
        :type description: str, optional
        :param monthly_price: New monthly price in smallest currency unit
        :type monthly_price: int, optional
        :param yearly_price: New yearly price in smallest currency unit
        :type yearly_price: int, optional
        :param currency: New currency code
        :type currency: str, optional
        :param benefits: New benefits list
        :type benefits: List[str], optional
        :param visibility: New visibility setting ('public' or 'none')
        :type visibility: str, optional
        :param active: Whether tier is active
        :type active: bool, optional
        :param welcome_page_url: New welcome page URL
        :type welcome_page_url: str, optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated tier data
        :rtype: Dict
        :raises ValidationError: If visibility value is invalid
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_tier = client.tiers.update(
            ...     tier_id="tier_id",
            ...     name="Platinum Plus",
            ...     monthly_price=2999,  # $29.99
            ...     benefits=["All premium features", "1-on-1 support", "Early access"]
            ... )

        Note:
            Only provide the fields you want to update. Unspecified fields will remain unchanged.
        """
        if visibility and visibility not in ["public", "none"]:
            raise ValidationError("visibility must be 'public' or 'none'")

        tier_data = {}

        # Add fields to update
        if name is not None:
            tier_data["name"] = name
        if description is not None:
            tier_data["description"] = description
        if monthly_price is not None:
            tier_data["monthly_price"] = monthly_price
        if yearly_price is not None:
            tier_data["yearly_price"] = yearly_price
        if currency is not None:
            tier_data["currency"] = currency
        if benefits is not None:
            tier_data["benefits"] = benefits
        if visibility is not None:
            tier_data["visibility"] = visibility
        if active is not None:
            tier_data["active"] = active
        if welcome_page_url is not None:
            tier_data["welcome_page_url"] = welcome_page_url

        # Add any additional fields
        tier_data.update(kwargs)

        response = self.client.put(f"tiers/{tier_id}/", {"tiers": [tier_data]})
        return response["tiers"][0] if response.get("tiers") else response

    def archive(self, tier_id: str) -> Dict:
        """
        Archive a tier (set active=False).

        Archived tiers are no longer available for new subscriptions but existing
        subscribers retain access.

        :param tier_id: Tier ID to archive
        :type tier_id: str

        :returns: Updated tier data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> archived_tier = client.tiers.archive("tier_id")
        """
        return self.update(tier_id, active=False)

    def activate(self, tier_id: str) -> Dict:
        """
        Activate a tier (set active=True).

        Activated tiers become available for new subscriptions.

        :param tier_id: Tier ID to activate
        :type tier_id: str

        :returns: Updated tier data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> active_tier = client.tiers.activate("tier_id")
        """
        return self.update(tier_id, active=True)

    def get_free_tier(self) -> Optional[Dict]:
        """
        Get the default free tier.

        Every Ghost site has a default free tier. This is a convenience method
        to retrieve it without needing to know its ID.

        :returns: Free tier data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> free_tier = client.tiers.get_free_tier()
            >>> if free_tier:
            ...     print(f"Free tier: {free_tier['name']}")
        """
        response = self.list(filter_="type:free", limit=1)
        tiers = response.get("tiers", [])
        return tiers[0] if tiers else None

    def get_paid_tiers(self, include_archived: bool = False) -> List[Dict]:
        """
        Get all paid tiers.

        Convenience method to retrieve all paid subscription tiers.

        :param include_archived: Whether to include archived tiers
        :type include_archived: bool

        :returns: List of paid tier data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> paid_tiers = client.tiers.get_paid_tiers()
            >>> for tier in paid_tiers:
            ...     print(f"Tier: {tier['name']} - ${tier.get('monthly_price', 0)/100:.2f}/month")
        """
        filter_str = "type:paid"
        if not include_archived:
            filter_str += "+active:true"

        response = self.list(
            filter_=filter_str,
            include="monthly_price,yearly_price,benefits"
        )
        return response.get("tiers", [])

    def calculate_savings(self, tier_data: Dict) -> Optional[Dict]:
        """
        Calculate yearly vs monthly savings for a tier.

        :param tier_data: Tier data containing monthly_price and yearly_price
        :type tier_data: Dict

        :returns: Savings calculation or None if prices not available
        :rtype: Dict or None

        Example:
            >>> tier = client.tiers.get("tier_id", include="monthly_price,yearly_price")
            >>> savings = client.tiers.calculate_savings(tier)
            >>> if savings:
            ...     print(f"Save {savings['percentage']:.1f}% with yearly billing")

        Note:
            Returns a dictionary with keys:
            - ``monthly_total``: Total cost for 12 months of monthly billing
            - ``yearly_total``: Total cost for yearly billing
            - ``savings_amount``: Absolute savings amount
            - ``percentage``: Percentage savings
        """
        monthly_price = tier_data.get("monthly_price")
        yearly_price = tier_data.get("yearly_price")

        if not monthly_price or not yearly_price:
            return None

        monthly_total = monthly_price * 12
        savings_amount = monthly_total - yearly_price
        percentage = (savings_amount / monthly_total) * 100 if monthly_total > 0 else 0

        return {
            "monthly_total": monthly_total,
            "yearly_total": yearly_price,
            "savings_amount": savings_amount,
            "percentage": percentage
        }
