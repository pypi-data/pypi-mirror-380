#!/usr/bin/env python3
"""
Offers Usage Examples

This example demonstrates how to use the Offers module of PyGhost
to manage discount offers and promotional codes on your Ghost site.
"""

import os

from pyghost import GhostClient

# Initialize the client
# Replace with your actual Ghost site URL and Admin API key
SITE_URL = os.getenv("GHOST_SITE_URL", "https://your-site.ghost.io")
ADMIN_API_KEY = os.getenv("GHOST_ADMIN_API_KEY", "your_key:your_secret")

client = GhostClient(site_url=SITE_URL, admin_api_key=ADMIN_API_KEY)


def create_offer_examples() -> None:
    """Demonstrate creating different types of offers"""
    print("=== Creating Discount Offers ===")

    try:
        # First, get available tiers to create offers for
        tiers = client.tiers.list()
        available_tiers = tiers.get('tiers', [])

        if not available_tiers:
            print("⚠️  No tiers found. Please create tiers first.")
            return None, None, None

        # Find a paid tier for our offers
        paid_tier = None
        for tier in available_tiers:
            if tier.get('monthly_price', 0) > 0:
                paid_tier = tier
                break

        if not paid_tier:
            print("⚠️  No paid tiers found. Creating offers for first available tier.")
            paid_tier = available_tiers[0]

        tier_id = paid_tier['id']

        # Create a percentage discount offer
        percent_offer = client.offers.create(
            name="Black Friday Sale",
            code="BLACKFRIDAY2024",
            display_title="Black Friday Special - 50% Off!",
            display_description="Limited time offer - Save 50% on your first year subscription",
            type="percent",
            amount=50,  # 50% discount
            duration="once",  # Apply only to first payment
            tier_id=tier_id,
            cadence="year"  # Apply to yearly subscriptions
        )
        print(f"✅ Created percentage offer: {percent_offer['display_title']}")

        # Create a fixed amount discount offer
        fixed_offer = client.offers.create(
            name="New Customer Welcome",
            code="WELCOME10",
            display_title="$10 Off Your First Month",
            display_description="Welcome bonus for new subscribers - $10 off your first payment",
            type="fixed",
            amount=1000,  # $10.00 in cents
            duration="once",
            tier_id=tier_id,
            cadence="month",
            currency="usd"
        )
        print(f"✅ Created fixed discount offer: {fixed_offer['display_title']}")

        # Create a forever discount offer
        forever_offer = client.offers.create(
            name="Loyal Customer Discount",
            code="LOYAL25",
            display_title="25% Off Forever",
            display_description="Exclusive discount for loyal customers - 25% off all payments",
            type="percent",
            amount=25,
            duration="forever",  # Apply to all payments
            tier_id=tier_id,
            cadence="month"
        )
        print(f"✅ Created forever discount offer: {forever_offer['display_title']}")

        return percent_offer, fixed_offer, forever_offer

    except Exception as e:
        print(f"❌ Error creating offers: {e}")
        return None, None, None


def list_offers_examples() -> None:
    """Demonstrate different ways to list offers"""
    print("\n=== Listing Offers ===")

    try:
        # Get all offers
        all_offers = client.offers.list(include="tier")
        print(f"🎫 Total offers: {len(all_offers.get('offers', []))}")

        # Get only active offers
        active_offers = client.offers.list(filter_="status:active")
        print(f"🎫 Active offers: {len(active_offers.get('offers', []))}")

        # Get percentage discounts only
        percent_offers = client.offers.list(filter_="type:percent")
        print(f"🎫 Percentage offers: {len(percent_offers.get('offers', []))}")

        # Get fixed amount discounts only
        fixed_offers = client.offers.list(filter_="type:fixed")
        print(f"🎫 Fixed amount offers: {len(fixed_offers.get('offers', []))}")

        # Display offer information
        print("🎫 Available offers:")
        for offer in all_offers.get('offers', []):
            offer_type = offer.get('type', 'unknown')
            amount = offer.get('amount', 0)
            duration = offer.get('duration', 'unknown')
            cadence = offer.get('cadence', 'month')

            if offer_type == "percent":
                discount_display = f"{amount}% off"
            elif offer_type == "fixed":
                currency = offer.get('currency', 'USD').upper()
                discount_display = f"${amount / 100:.2f} {currency} off"
            else:
                discount_display = "Unknown discount"

            print(f"   - {offer['code']}: {discount_display} ({duration}, {cadence})")
            print(f"     {offer['display_title']}")

    except Exception as e:
        print(f"❌ Error listing offers: {e}")


def update_offer_examples() -> None:
    """Demonstrate updating offers"""
    print("\n=== Updating Offers ===")

    try:
        # Get an offer to update
        offers_list = client.offers.list(limit=1)
        if not offers_list.get('offers'):
            print("⚠️  No offers found to update")
            return

        offer = offers_list['offers'][0]
        offer_id = offer['id']

        # Update offer display information
        updated_offer = client.offers.update(
            offer_id=offer_id,
            display_title=f"{offer['display_title']} - Limited Time!",
            display_description=f"{offer.get('display_description', '')} Hurry, this offer won't last long!"
        )
        print(f"✅ Updated display text for: {updated_offer['code']}")

        # Update offer discount amount
        if offer.get('type') == 'percent':
            updated_discount = client.offers.update(
                offer_id=offer_id,
                amount=min(offer.get('amount', 0) + 5, 100)  # Increase by 5%, max 100%
            )
            print(f"✅ Updated discount amount for: {updated_discount['code']}")

    except Exception as e:
        print(f"❌ Error updating offer: {e}")


def offer_management_examples() -> None:
    """Demonstrate offer management operations"""
    print("\n=== Offer Management ===")

    try:
        # Get offers for management
        offers_list = client.offers.list()
        offers = offers_list.get('offers', [])

        if not offers:
            print("⚠️  No offers found for management operations")
            return

        # Use the first offer for management examples
        offer_id = offers[0]['id']

        # Archive an offer
        archived_offer = client.offers.archive(offer_id)
        print(f"📦 Archived offer: {archived_offer['code']}")

        # Activate the offer again
        activated_offer = client.offers.activate(offer_id)
        print(f"✅ Activated offer: {activated_offer['code']}")

        # Get active offers only
        active_offers = client.offers.get_active_offers()
        print(f"✅ Active offers count: {len(active_offers)}")

        # Get offer by code
        if offers:
            offer_code = offers[0]['code']
            found_offer = client.offers.get_by_code(offer_code)
            if found_offer:
                print(f"🔍 Found offer by code '{offer_code}': {found_offer['display_title']}")

    except Exception as e:
        print(f"❌ Error in offer management: {e}")


def discount_calculation_examples() -> None:
    """Demonstrate discount calculation utilities"""
    print("\n=== Discount Calculations ===")

    try:
        # Get offers for calculation examples
        offers_list = client.offers.list()
        offers = offers_list.get('offers', [])

        if not offers:
            print("⚠️  No offers found for calculation examples")
            return

        # Example prices to test (in cents)
        test_prices = [999, 1999, 4999, 9999]  # $9.99, $19.99, $49.99, $99.99

        print("💰 Discount Calculation Examples:")

        for offer in offers[:3]:  # Test first 3 offers
            print(f"\n   🎫 Offer: {offer['code']} ({offer.get('type', 'unknown')} - {offer.get('amount', 0)})")

            for original_price in test_prices:
                calculation = client.offers.calculate_discount(offer, original_price)

                original = calculation['original_price'] / 100
                discount = calculation['discount_amount'] / 100
                final = calculation['final_price'] / 100
                percentage = calculation['discount_percentage']

                print(f"      ${original:.2f} → ${final:.2f} (save ${discount:.2f}, {percentage:.1f}% off)")

        # Comparison of different offer types
        if len(offers) >= 2:
            print(f"\n   📊 Offer Comparison (on $29.99 subscription):")
            test_price = 2999  # $29.99

            for offer in offers[:2]:
                calc = client.offers.calculate_discount(offer, test_price)
                savings = calc['discount_amount'] / 100
                final_price = calc['final_price'] / 100

                print(f"      {offer['code']}: Final price ${final_price:.2f} (save ${savings:.2f})")

    except Exception as e:
        print(f"❌ Error in discount calculations: {e}")


def offer_url_examples() -> None:
    """Demonstrate offer URL generation"""
    print("\n=== Offer URL Generation ===")

    try:
        # Get offers for URL generation
        offers_list = client.offers.list(limit=3)
        offers = offers_list.get('offers', [])

        if not offers:
            print("⚠️  No offers found for URL generation")
            return

        print("🔗 Generated Offer URLs:")

        for offer in offers:
            offer_code = offer['code']
            # Use the site URL from client configuration
            offer_url = client.offers.generate_offer_url(offer_code, SITE_URL)

            print(f"   🎫 {offer['display_title']}")
            print(f"      Code: {offer_code}")
            print(f"      URL: {offer_url}")
            print(f"      Share this link to let customers redeem the offer")

    except Exception as e:
        print(f"❌ Error generating offer URLs: {e}")


def advanced_offer_examples():
    """Demonstrate advanced offer features"""
    print("\n=== Advanced Offer Features ===")

    try:
        # Get tiers for advanced examples
        tiers = client.tiers.list()
        available_tiers = tiers.get('tiers', [])

        if len(available_tiers) < 1:
            print("⚠️  Need at least 1 tier for advanced examples")
            return

        tier_id = available_tiers[0]['id']

        # Create a repeating discount offer (applies for X months)
        repeating_offer = client.offers.create(
            name="3-Month Promo",
            code="PROMO3M",
            display_title="25% Off for 3 Months",
            display_description="Get 25% off your subscription for the first 3 months",
            type="percent",
            amount=25,
            duration="repeating",
            duration_in_months=3,  # Apply for 3 months
            tier_id=tier_id,
            cadence="month"
        )
        print(f"✅ Created repeating offer: {repeating_offer['code']}")

        # Create offers for different currencies
        if len(available_tiers) > 0:
            # EUR offer
            eur_offer = client.offers.create(
                name="European Special",
                code="EURSPECIAL",
                display_title="€5 Off First Month",
                display_description="Special discount for European customers",
                type="fixed",
                amount=500,  # €5.00 in cents
                duration="once",
                tier_id=tier_id,
                cadence="month",
                currency="eur",
                currency_restriction=True
            )
            print(f"✅ Created EUR offer: {eur_offer['code']}")

        # Get offers for a specific tier
        tier_offers = client.offers.get_active_offers(tier_id=tier_id)
        print(f"🎯 Offers for specific tier: {len(tier_offers)}")

        return repeating_offer

    except Exception as e:
        print(f"❌ Error creating advanced offers: {e}")
        return None


def offer_analytics_examples() -> None:
    """Demonstrate offer analytics and insights"""
    print("\n=== Offer Analytics ===")

    try:
        # Get all offers for analysis
        all_offers = client.offers.list(include="tier")
        offers = all_offers.get('offers', [])

        if not offers:
            print("⚠️  No offers found for analysis")
            return

        print("📊 Offer Portfolio Analysis:")

        # Analyze offer types
        percent_count = sum(1 for o in offers if o.get('type') == 'percent')
        fixed_count = sum(1 for o in offers if o.get('type') == 'fixed')

        print(f"   💹 Discount Types:")
        print(f"      Percentage discounts: {percent_count}")
        print(f"      Fixed amount discounts: {fixed_count}")

        # Analyze duration types
        once_count = sum(1 for o in offers if o.get('duration') == 'once')
        forever_count = sum(1 for o in offers if o.get('duration') == 'forever')
        repeating_count = sum(1 for o in offers if o.get('duration') == 'repeating')

        print(f"   ⏰ Duration Types:")
        print(f"      One-time discounts: {once_count}")
        print(f"      Forever discounts: {forever_count}")
        print(f"      Repeating discounts: {repeating_count}")

        # Analyze cadence preferences
        monthly_count = sum(1 for o in offers if o.get('cadence') == 'month')
        yearly_count = sum(1 for o in offers if o.get('cadence') == 'year')

        print(f"   📅 Cadence Targeting:")
        print(f"      Monthly subscriptions: {monthly_count}")
        print(f"      Yearly subscriptions: {yearly_count}")

        # Analyze discount amounts for percentage offers
        percent_offers = [o for o in offers if o.get('type') == 'percent']
        if percent_offers:
            amounts = [o.get('amount', 0) for o in percent_offers]
            avg_discount = sum(amounts) / len(amounts)
            max_discount = max(amounts)
            min_discount = min(amounts)

            print(f"   📈 Percentage Discount Analysis:")
            print(f"      Average discount: {avg_discount:.1f}%")
            print(f"      Highest discount: {max_discount}%")
            print(f"      Lowest discount: {min_discount}%")

        # Active vs archived offers
        active_count = sum(1 for o in offers if o.get('status') == 'active')
        archived_count = len(offers) - active_count

        print(f"   📊 Offer Status:")
        print(f"      Active offers: {active_count}")
        print(f"      Archived offers: {archived_count}")

    except Exception as e:
        print(f"❌ Error in offer analytics: {e}")


def cleanup_examples() -> None:
    """Clean up example offers"""
    print("\n=== Cleanup ===")

    try:
        # Get offers created in this example
        all_offers = client.offers.list()

        example_codes = [
            'BLACKFRIDAY2024', 'WELCOME10', 'LOYAL25',
            'PROMO3M', 'EURSPECIAL'
        ]

        for offer in all_offers.get('offers', []):
            if offer['code'] in example_codes:
                try:
                    client.offers.archive(offer['id'])
                    print(f"📦 Archived offer: {offer['code']}")
                except Exception as e:
                    print(f"⚠️  Could not archive {offer['code']}: {e}")

    except Exception as e:
        print(f"❌ Error during cleanup: {e}")


def main() -> None:
    """Run all offer examples"""
    print("🚀 PyGhost Offers Module Examples")
    print("=" * 40)

    try:
        # Run examples
        create_offer_examples()
        list_offers_examples()
        update_offer_examples()
        offer_management_examples()
        discount_calculation_examples()
        offer_url_examples()
        advanced_offer_examples()
        offer_analytics_examples()

        # Optionally clean up (uncomment to clean up)
        # cleanup_examples()

        print("\n✅ All examples completed successfully!")
        print("\n📝 Tips for production use:")
        print("- Test offer calculations thoroughly before launching")
        print("- Use clear, descriptive offer codes that customers can easily remember")
        print("- Consider the business impact of forever vs. one-time discounts")
        print("- Monitor offer usage and adjust strategies based on performance")
        print("- Archive expired offers rather than deleting them")
        print("- Use currency-specific offers for international customers")

    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("Make sure you have:")
        print("1. Set GHOST_SITE_URL environment variable")
        print("2. Set GHOST_ADMIN_API_KEY environment variable")
        print("3. Valid Ghost Admin API credentials")
        print("4. At least one subscription tier created on your Ghost site")


if __name__ == "__main__":
    main()
