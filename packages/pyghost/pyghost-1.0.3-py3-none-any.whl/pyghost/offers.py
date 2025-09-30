"""
Offers module for Ghost Admin API.

This module provides functionality for managing Ghost discount offers and promotions.
Offers allow creating discount codes for subscription tiers with various pricing strategies.

.. module:: pyghost.offers
   :synopsis: Ghost Admin API Offers management

.. moduleauthor:: PyGhost Contributors
"""

from typing import Dict, List, Optional, Union

from .exceptions import ValidationError
from .enums import OfferType, OfferDuration, OfferStatus, OfferCadence, Currency, get_enum_value


class Offers:
    """
    Offers module for Ghost Admin API.

    Handles all offer-related operations including creation, updates, and management
    of discount offers for subscription tiers.

    :param client: The GhostClient instance
    :type client: GhostClient

    Example:
        >>> client = GhostClient(site_url="https://mysite.ghost.io", admin_api_key="key:secret")
        >>> offer = client.offers.create(
        ...     name="Black Friday Sale",
        ...     code="BLACKFRIDAY2024",
        ...     display_title="50% Off Annual Plans",
        ...     display_description="Limited time offer - 50% off all annual subscriptions",
        ...     type="percent",
        ...     amount=50,
        ...     duration="once",
        ...     tier_id="tier_id_here"
        ... )
    """

    def __init__(self, client):
        """
        Initialize Offers module.

        :param client: GhostClient instance for API communication
        :type client: GhostClient
        """
        self.client = client

    def create(self,
               name: str,
               code: str,
               display_title: str,
               display_description: str,
               type: Union[OfferType, str],
               amount: Union[int, float],
               duration: Union[OfferDuration, str],
               tier_id: str,
               cadence: Union[OfferCadence, str] = OfferCadence.MONTH,
               currency: Optional[Union[Currency, str]] = None,
               currency_restriction: bool = False,
               duration_in_months: Optional[int] = None,
               **kwargs) -> Dict:
        """
        Create a new discount offer.

        :param name: Offer name (internal identifier)
        :type name: str
        :param code: Offer code (what users enter)
        :type code: str
        :param display_title: Public display title
        :type display_title: str
        :param display_description: Public display description
        :type display_description: str
        :param type: Discount type (OfferType.PERCENT or OfferType.FIXED)
        :type type: Union[OfferType, str]
        :param amount: Discount amount (percentage or fixed amount)
        :type amount: Union[int, float]
        :param duration: Duration type ('once', 'forever', 'repeating')
        :type duration: str
        :param tier_id: Target tier ID for the offer
        :type tier_id: str
        :param cadence: Billing cadence ('month' or 'year')
        :type cadence: str
        :param currency: Currency code (required for fixed discounts)
        :type currency: str, optional
        :param currency_restriction: Whether to restrict to specific currency
        :type currency_restriction: bool
        :param duration_in_months: Duration in months (for 'repeating' duration)
        :type duration_in_months: int, optional
        :param kwargs: Additional offer fields
        :type kwargs: dict

        :returns: Created offer data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Create percentage discount
            >>> percent_offer = client.offers.create(
            ...     name="Summer Sale",
            ...     code="SUMMER2024",
            ...     display_title="30% Off Premium",
            ...     display_description="Save 30% on your first year",
            ...     type="percent",
            ...     amount=30,
            ...     duration="once",
            ...     tier_id="premium_tier_id",
            ...     cadence="year"
            ... )
            >>>
            >>> # Create fixed amount discount
            >>> fixed_offer = client.offers.create(
            ...     name="New Customer Discount",
            ...     code="WELCOME10",
            ...     display_title="$10 Off First Month",
            ...     display_description="Welcome bonus for new subscribers",
            ...     type="fixed",
            ...     amount=1000,  # $10.00 in cents
            ...     duration="once",
            ...     tier_id="basic_tier_id",
            ...     cadence="month",
            ...     currency="usd"
            ... )

        Note:
            - For ``type="percent"``, amount should be 0-100 (percentage)
            - For ``type="fixed"``, amount should be in smallest currency unit (e.g., cents)
            - Duration ``"once"`` applies to first payment only
            - Duration ``"forever"`` applies to all payments
            - Duration ``"repeating"`` applies for specified months
        """
        # Convert enums to string values
        type_str = get_enum_value(type)
        duration_str = get_enum_value(duration)
        cadence_str = get_enum_value(cadence)
        currency_str = get_enum_value(currency) if currency else None

        # Validate required enum values
        if type_str not in ["percent", "fixed"]:
            raise ValidationError("type must be OfferType.PERCENT or OfferType.FIXED")

        if duration_str not in ["once", "forever", "repeating"]:
            raise ValidationError("duration must be OfferDuration.ONCE, OfferDuration.FOREVER, or OfferDuration.REPEATING")

        if cadence_str not in ["month", "year"]:
            raise ValidationError("cadence must be OfferCadence.MONTH or OfferCadence.YEAR")

        # Validate fixed discount requirements
        if type_str == "fixed" and not currency_str:
            raise ValidationError("currency is required for fixed discount type")

        # Validate repeating duration requirements
        if duration_str == "repeating" and duration_in_months is None:
            raise ValidationError("duration_in_months is required for repeating duration")

        offer_data = {
            "name": name,
            "code": code,
            "display_title": display_title,
            "display_description": display_description,
            "type": type_str,
            "amount": amount,
            "duration": duration_str,
            "cadence": cadence_str,
            "currency_restriction": currency_restriction,
            "status": OfferStatus.ACTIVE.value,  # New offers are active by default
            "tier": {"id": tier_id}
        }

        # Add optional fields
        if currency_str:
            offer_data["currency"] = currency_str
        if duration_in_months is not None:
            offer_data["duration_in_months"] = duration_in_months

        # Add any additional fields
        offer_data.update(kwargs)

        response = self.client.post("offers/", {"offers": [offer_data]})
        return response["offers"][0] if response.get("offers") else response

    def get(self, offer_id: str, include: Optional[str] = None, **kwargs) -> Dict:
        """
        Get a specific offer by ID.

        :param offer_id: Offer ID
        :type offer_id: str
        :param include: Related data to include (e.g., 'tier')
        :type include: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Offer data
        :rtype: Dict
        :raises NotFoundError: If offer not found
        :raises GhostAPIError: If API request fails

        Example:
            >>> offer = client.offers.get("offer_id_here", include="tier")
        """
        params = kwargs
        if include:
            params["include"] = include

        response = self.client.get(f"offers/{offer_id}/", params=params)
        return response["offers"][0] if response.get("offers") else response

    def list(self,
             limit: Optional[int] = None,
             page: Optional[int] = None,
             filter_: Optional[str] = None,
             include: Optional[str] = None,
             order: Optional[str] = None,
             **kwargs) -> Dict:
        """
        List offers with optional filtering and pagination.

        :param limit: Number of offers to return
        :type limit: int, optional
        :param page: Page number for pagination
        :type page: int, optional
        :param filter_: Ghost filter string (e.g., 'status:active', 'type:percent')
        :type filter_: str, optional
        :param include: Related data to include (e.g., 'tier')
        :type include: str, optional
        :param order: Ordering specification
        :type order: str, optional
        :param kwargs: Additional query parameters
        :type kwargs: dict

        :returns: Offers list with pagination metadata
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Get all active offers
            >>> offers = client.offers.list(filter_="status:active", include="tier")
            >>>
            >>> # Get percentage discounts only
            >>> percent_offers = client.offers.list(filter_="type:percent")
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

        return self.client.get("offers/", params=params)

    def update(self,
               offer_id: str,
               name: Optional[str] = None,
               code: Optional[str] = None,
               display_title: Optional[str] = None,
               display_description: Optional[str] = None,
               type: Optional[str] = None,
               amount: Optional[Union[int, float]] = None,
               duration: Optional[str] = None,
               cadence: Optional[str] = None,
               currency: Optional[str] = None,
               currency_restriction: Optional[bool] = None,
               duration_in_months: Optional[int] = None,
               status: Optional[Union[OfferStatus, str]] = None,
               **kwargs) -> Dict:
        """
        Update an existing offer.

        :param offer_id: Offer ID to update
        :type offer_id: str
        :param name: New offer name
        :type name: str, optional
        :param code: New offer code
        :type code: str, optional
        :param display_title: New display title
        :type display_title: str, optional
        :param display_description: New display description
        :type display_description: str, optional
        :param type: New discount type ('percent' or 'fixed')
        :type type: str, optional
        :param amount: New discount amount
        :type amount: Union[int, float], optional
        :param duration: New duration ('once', 'forever', 'repeating')
        :type duration: str, optional
        :param cadence: New cadence ('month' or 'year')
        :type cadence: str, optional
        :param currency: New currency code
        :type currency: str, optional
        :param currency_restriction: New currency restriction setting
        :type currency_restriction: bool, optional
        :param duration_in_months: New duration in months
        :type duration_in_months: int, optional
        :param status: New status ('active' or 'archived')
        :type status: str, optional
        :param kwargs: Additional fields to update
        :type kwargs: dict

        :returns: Updated offer data
        :rtype: Dict
        :raises ValidationError: If validation fails
        :raises GhostAPIError: If API request fails

        Example:
            >>> updated_offer = client.offers.update(
            ...     offer_id="offer_id",
            ...     display_title="Limited Time: 40% Off!",
            ...     amount=40,
            ...     status="active"
            ... )

        Note:
            Only provide the fields you want to update. Unspecified fields will remain unchanged.
        """
        # Validate enum values if provided
        if type and type not in ["percent", "fixed"]:
            raise ValidationError("type must be 'percent' or 'fixed'")

        if duration and duration not in ["once", "forever", "repeating"]:
            raise ValidationError("duration must be 'once', 'forever', or 'repeating'")

        if cadence and cadence not in ["month", "year"]:
            raise ValidationError("cadence must be 'month' or 'year'")

        if status and status not in ["active", "archived"]:
            raise ValidationError("status must be 'active' or 'archived'")

        offer_data = {}

        # Add fields to update
        if name is not None:
            offer_data["name"] = name
        if code is not None:
            offer_data["code"] = code
        if display_title is not None:
            offer_data["display_title"] = display_title
        if display_description is not None:
            offer_data["display_description"] = display_description
        if type is not None:
            offer_data["type"] = type
        if amount is not None:
            offer_data["amount"] = amount
        if duration is not None:
            offer_data["duration"] = duration
        if cadence is not None:
            offer_data["cadence"] = cadence
        if currency is not None:
            offer_data["currency"] = currency
        if currency_restriction is not None:
            offer_data["currency_restriction"] = currency_restriction
        if duration_in_months is not None:
            offer_data["duration_in_months"] = duration_in_months
        if status is not None:
            offer_data["status"] = status

        # Add any additional fields
        offer_data.update(kwargs)

        response = self.client.put(f"offers/{offer_id}/", {"offers": [offer_data]})
        return response["offers"][0] if response.get("offers") else response

    def archive(self, offer_id: str) -> Dict:
        """
        Archive an offer (set status='archived').

        Archived offers are no longer available for new redemptions but
        existing redemptions remain valid.

        :param offer_id: Offer ID to archive
        :type offer_id: str

        :returns: Updated offer data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> archived_offer = client.offers.archive("offer_id")
        """
        return self.update(offer_id, status=OfferStatus.ARCHIVED)

    def activate(self, offer_id: str) -> Dict:
        """
        Activate an offer (set status='active').

        Activated offers become available for new redemptions.

        :param offer_id: Offer ID to activate
        :type offer_id: str

        :returns: Updated offer data
        :rtype: Dict
        :raises GhostAPIError: If API request fails

        Example:
            >>> active_offer = client.offers.activate("offer_id")
        """
        return self.update(offer_id, status=OfferStatus.ACTIVE)

    def get_by_code(self, code: str) -> Optional[Dict]:
        """
        Get an offer by its code.

        :param code: Offer code to search for
        :type code: str

        :returns: Offer data or None if not found
        :rtype: Dict or None
        :raises GhostAPIError: If API request fails

        Example:
            >>> offer = client.offers.get_by_code("SUMMER2024")
            >>> if offer:
            ...     print(f"Found offer: {offer['display_title']}")
        """
        response = self.list(filter_=f"code:{code}", limit=1)
        offers = response.get("offers", [])
        return offers[0] if offers else None

    def get_active_offers(self, tier_id: Optional[str] = None) -> List[Dict]:
        """
        Get all active offers, optionally filtered by tier.

        :param tier_id: Filter by specific tier ID
        :type tier_id: str, optional

        :returns: List of active offer data
        :rtype: List[Dict]
        :raises GhostAPIError: If API request fails

        Example:
            >>> # Get all active offers
            >>> active_offers = client.offers.get_active_offers()
            >>>
            >>> # Get active offers for specific tier
            >>> tier_offers = client.offers.get_active_offers(tier_id="premium_tier")
        """
        filter_str = "status:active"
        if tier_id:
            filter_str += f"+tier.id:{tier_id}"

        response = self.list(filter_=filter_str, include="tier")
        return response.get("offers", [])

    def calculate_discount(self, offer_data: Dict, original_price: int) -> Dict:
        """
        Calculate the discounted price for an offer.

        :param offer_data: Offer data containing type and amount
        :type offer_data: Dict
        :param original_price: Original price in smallest currency unit
        :type original_price: int

        :returns: Discount calculation details
        :rtype: Dict

        Example:
            >>> offer = client.offers.get("offer_id")
            >>> calculation = client.offers.calculate_discount(offer, 2999)  # $29.99
            >>> print(f"Original: ${calculation['original_price']/100:.2f}")
            >>> print(f"Discount: ${calculation['discount_amount']/100:.2f}")
            >>> print(f"Final: ${calculation['final_price']/100:.2f}")

        Note:
            Returns a dictionary with keys:
            - ``original_price``: Original price
            - ``discount_amount``: Amount of discount
            - ``final_price``: Price after discount
            - ``discount_type``: Type of discount applied
        """
        discount_type = offer_data.get("type")
        discount_amount_config = offer_data.get("amount", 0)

        if discount_type == "percent":
            discount_amount = int(original_price * (discount_amount_config / 100))
        elif discount_type == "fixed":
            discount_amount = int(discount_amount_config)
        else:
            discount_amount = 0

        # Ensure discount doesn't exceed original price
        discount_amount = min(discount_amount, original_price)
        final_price = max(0, original_price - discount_amount)

        return {
            "original_price": original_price,
            "discount_amount": discount_amount,
            "final_price": final_price,
            "discount_type": discount_type,
            "discount_percentage": (discount_amount / original_price * 100) if original_price > 0 else 0
        }

    def generate_offer_url(self, offer_code: str, site_url: str) -> str:
        """
        Generate the public URL for an offer.

        :param offer_code: The offer code
        :type offer_code: str
        :param site_url: Your Ghost site URL
        :type site_url: str

        :returns: Complete offer URL
        :rtype: str

        Example:
            >>> offer_url = client.offers.generate_offer_url("SUMMER2024", "https://mysite.com")
            >>> print(f"Share this URL: {offer_url}")
            # Output: https://mysite.com/summer2024

        Note:
            The generated URL follows Ghost's standard format: ``{site_url}/{code}``
        """
        site_url = site_url.rstrip('/')
        code_slug = offer_code.lower().replace('_', '-')
        return f"{site_url}/{code_slug}"
