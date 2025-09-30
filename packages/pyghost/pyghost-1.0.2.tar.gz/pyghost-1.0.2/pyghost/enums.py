"""
Enums for PyGhost library to provide type-safe constants for Ghost Admin API.

This module contains enums for all fixed options used throughout the Ghost Admin API,
making the library more user-friendly and preventing typos in string literals.
"""

from enum import Enum


class PostStatus(Enum):
    """Post status options."""
    DRAFT = "draft"
    PUBLISHED = "published"
    SCHEDULED = "scheduled"
    SENT = "sent"


class PageStatus(Enum):
    """Page status options."""
    DRAFT = "draft"
    PUBLISHED = "published"
    SCHEDULED = "scheduled"


class ContentType(Enum):
    """Content format types for posts and pages."""
    LEXICAL = "lexical"
    HTML = "html"


class TierVisibility(Enum):
    """Tier visibility options."""
    PUBLIC = "public"
    NONE = "none"


class NewsletterStatus(Enum):
    """Newsletter status options."""
    ACTIVE = "active"
    ARCHIVED = "archived"


class NewsletterVisibility(Enum):
    """Newsletter visibility options."""
    MEMBERS = "members"
    PAID = "paid"


class NewsletterSenderReplyTo(Enum):
    """Newsletter sender reply-to options."""
    NEWSLETTER = "newsletter"
    SUPPORT = "support"


class OfferType(Enum):
    """Offer discount type options."""
    PERCENT = "percent"
    FIXED = "fixed"


class OfferDuration(Enum):
    """Offer duration options."""
    ONCE = "once"
    FOREVER = "forever"
    REPEATING = "repeating"


class OfferStatus(Enum):
    """Offer status options."""
    ACTIVE = "active"
    ARCHIVED = "archived"


class OfferCadence(Enum):
    """Offer cadence options for repeating offers."""
    MONTH = "month"
    YEAR = "year"


class Currency(Enum):
    """Supported currency codes."""
    USD = "usd"
    EUR = "eur"
    GBP = "gbp"
    AUD = "aud"
    CAD = "cad"
    JPY = "jpy"
    CHF = "chf"
    SEK = "sek"
    NOK = "nok"
    DKK = "dkk"
    PLN = "pln"
    CZK = "czk"
    HUF = "huf"
    BGN = "bgn"
    RON = "ron"
    HRK = "hrk"
    RSD = "rsd"
    BAM = "bam"
    MKD = "mkd"
    ALL = "all"
    ISK = "isk"
    TRY = "try"
    RUB = "rub"
    UAH = "uah"
    BYN = "byn"
    MDL = "mdl"
    GEL = "gel"
    AMD = "amd"
    AZN = "azn"
    KZT = "kzt"
    UZS = "uzs"
    KGS = "kgs"
    TJS = "tjs"
    TMT = "tmt"
    MNT = "mnt"
    CNY = "cny"
    HKD = "hkd"
    TWD = "twd"
    KRW = "krw"
    THB = "thb"
    VND = "vnd"
    IDR = "idr"
    MYR = "myr"
    SGD = "sgd"
    PHP = "php"
    INR = "inr"
    PKR = "pkr"
    BDT = "bdt"
    LKR = "lkr"
    NPR = "npr"
    BTN = "btn"
    MVR = "mvr"
    AFN = "afn"
    IRR = "irr"
    IQD = "iqd"
    SYP = "syp"
    LBP = "lbp"
    JOD = "jod"
    KWD = "kwd"
    BHD = "bhd"
    QAR = "qar"
    AED = "aed"
    OMR = "omr"
    YER = "yer"
    SAR = "sar"
    ILS = "ils"
    EGP = "egp"
    LYD = "lyd"
    TND = "tnd"
    DZD = "dzd"
    MAD = "mad"
    MRU = "mru"
    SLL = "sll"
    GHS = "ghs"
    NGN = "ngn"
    XOF = "xof"
    XAF = "xaf"
    KES = "kes"
    UGX = "ugx"
    TZS = "tzs"
    RWF = "rwf"
    BIF = "bif"
    ETB = "etb"
    ERN = "ern"
    DJF = "djf"
    SOS = "sos"
    ZAR = "zar"
    NAD = "nad"
    BWP = "bwp"
    SZL = "szl"
    LSL = "lsl"
    MZN = "mzn"
    MWK = "mwk"
    ZMW = "zmw"
    AOA = "aoa"
    CDF = "cdf"
    XDR = "xdr"


class WebhookEvent(Enum):
    """Webhook event types."""
    # Post events
    POST_ADDED = "post.added"
    POST_DELETED = "post.deleted"
    POST_EDITED = "post.edited"
    POST_PUBLISHED = "post.published"
    POST_UNPUBLISHED = "post.unpublished"
    POST_SCHEDULED = "post.scheduled"
    POST_UNSCHEDULED = "post.unscheduled"
    POST_TAG_ATTACHED = "post.tag.attached"
    POST_TAG_DETACHED = "post.tag.detached"

    # Page events
    PAGE_ADDED = "page.added"
    PAGE_DELETED = "page.deleted"
    PAGE_EDITED = "page.edited"
    PAGE_PUBLISHED = "page.published"
    PAGE_UNPUBLISHED = "page.unpublished"
    PAGE_SCHEDULED = "page.scheduled"
    PAGE_UNSCHEDULED = "page.unscheduled"
    PAGE_TAG_ATTACHED = "page.tag.attached"
    PAGE_TAG_DETACHED = "page.tag.detached"

    # Member events
    MEMBER_ADDED = "member.added"
    MEMBER_DELETED = "member.deleted"
    MEMBER_EDITED = "member.edited"
    MEMBER_PAID = "member.paid"

    # Subscription events
    SUBSCRIPTION_ACTIVATED = "subscription.activated"
    SUBSCRIPTION_CANCELLED = "subscription.cancelled"
    SUBSCRIPTION_UPDATED = "subscription.updated"

    # Tag events
    TAG_ADDED = "tag.added"
    TAG_DELETED = "tag.deleted"
    TAG_EDITED = "tag.edited"


class WebhookStatus(Enum):
    """Webhook status options."""
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class MemberStatus(Enum):
    """Member status options."""
    FREE = "free"
    PAID = "paid"
    COMPED = "comped"


class UserRole(Enum):
    """User role options."""
    OWNER = "Owner"
    ADMINISTRATOR = "Administrator"
    EDITOR = "Editor"
    AUTHOR = "Author"
    CONTRIBUTOR = "Contributor"


class UserStatus(Enum):
    """User status options."""
    ACTIVE = "active"
    INVITED = "invited"
    INACTIVE = "inactive"


class ImageFormat(Enum):
    """Supported image formats for upload."""
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    GIF = "gif"
    WEBP = "webp"
    SVG = "svg"
    BMP = "bmp"
    TIFF = "tiff"
    ICO = "ico"


# Convenience function to get enum value
def get_enum_value(enum_item):
    """
    Get the string value from an enum item.

    Args:
        enum_item: Enum item or string value

    Returns:
        String value of the enum
    """
    if isinstance(enum_item, Enum):
        return enum_item.value
    return enum_item


# Export all enums for easy importing
__all__ = [
    'PostStatus',
    'PageStatus',
    'ContentType',
    'TierVisibility',
    'NewsletterStatus',
    'NewsletterVisibility',
    'NewsletterSenderReplyTo',
    'OfferType',
    'OfferDuration',
    'OfferStatus',
    'OfferCadence',
    'Currency',
    'WebhookEvent',
    'WebhookStatus',
    'MemberStatus',
    'UserRole',
    'UserStatus',
    'ImageFormat',
    'get_enum_value'
]
