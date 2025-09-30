#!/usr/bin/env python3
"""
Tiers Usage Examples

This example demonstrates how to use the Tiers module of PyGhost
to manage subscription tiers and pricing on your Ghost site.
"""

import os
from pyghost import GhostClient

# Initialize the client
# Replace with your actual Ghost site URL and Admin API key
SITE_URL = os.getenv("GHOST_SITE_URL", "https://your-site.ghost.io")
ADMIN_API_KEY = os.getenv("GHOST_ADMIN_API_KEY", "your_key:your_secret")

client = GhostClient(site_url=SITE_URL, admin_api_key=ADMIN_API_KEY)


def create_tier_examples():
    """Demonstrate creating different types of subscription tiers"""
    print("=== Creating Subscription Tiers ===")
    
    try:
        # Create a basic monthly tier
        basic_tier = client.tiers.create(
            name="Basic Plan",
            description="Perfect for individuals getting started",
            monthly_price=999,  # $9.99 in cents
            yearly_price=9999,  # $99.99 in cents (save ~17%)
            currency="usd",
            benefits=[
                "Access to all posts",
                "Weekly newsletter",
                "Comment on posts"
            ]
        )
        print(f"✅ Created basic tier: {basic_tier['name']}")
        
        # Create a premium tier with more features
        premium_tier = client.tiers.create(
            name="Premium Plan",
            description="For professionals who need advanced features",
            monthly_price=1999,  # $19.99
            yearly_price=19999,  # $199.99
            currency="usd",
            benefits=[
                "Everything in Basic",
                "Premium content access",
                "Monthly video calls",
                "Priority support",
                "Download resources"
            ],
            visibility="public"
        )
        print(f"✅ Created premium tier: {premium_tier['name']}")
        
        # Create a free tier
        free_tier = client.tiers.create(
            name="Free Membership",
            description="Get started with free access",
            monthly_price=0,
            yearly_price=0,
            currency="usd",
            benefits=[
                "Access to free posts",
                "Join the community"
            ],
            type="free"
        )
        print(f"✅ Created free tier: {free_tier['name']}")
        
        return basic_tier, premium_tier, free_tier
        
    except Exception as e:
        print(f"❌ Error creating tiers: {e}")
        return None, None, None


def list_tiers_examples():
    """Demonstrate different ways to list tiers"""
    print("\n=== Listing Tiers ===")
    
    try:
        # Get all tiers
        all_tiers = client.tiers.list()
        print(f"💳 Total tiers: {len(all_tiers.get('tiers', []))}")
        
        # Get only active tiers
        active_tiers = client.tiers.list(filter_="active:true")
        print(f"💳 Active tiers: {len(active_tiers.get('tiers', []))}")
        
        # Get tiers with pricing information
        paid_tiers = client.tiers.list(filter_="type:paid")
        print(f"💳 Paid tiers: {len(paid_tiers.get('tiers', []))}")
        
        # Display tier information
        print("💳 Available tiers:")
        for tier in all_tiers.get('tiers', []):
            monthly = tier.get('monthly_price', 0)
            yearly = tier.get('yearly_price', 0)
            currency = tier.get('currency', 'USD').upper()
            
            if monthly > 0:
                monthly_display = f"${monthly/100:.2f}"
                yearly_display = f"${yearly/100:.2f}" if yearly > 0 else "N/A"
                print(f"   - {tier['name']}: {monthly_display}/{currency} monthly, {yearly_display} yearly")
            else:
                print(f"   - {tier['name']}: Free")
            
    except Exception as e:
        print(f"❌ Error listing tiers: {e}")


def update_tier_examples():
    """Demonstrate updating tiers"""
    print("\n=== Updating Tiers ===")
    
    try:
        # Get a tier to update
        tiers_list = client.tiers.list(filter_="name:'Basic Plan'")
        if not tiers_list.get('tiers'):
            print("⚠️  No 'Basic Plan' tier found to update")
            return
            
        tier = tiers_list['tiers'][0]
        tier_id = tier['id']
        
        # Update pricing and benefits
        updated_tier = client.tiers.update(
            tier_id=tier_id,
            monthly_price=1199,  # Increase to $11.99
            yearly_price=11999,  # $119.99 yearly
            benefits=[
                "Access to all posts",
                "Weekly newsletter", 
                "Comment on posts",
                "Early access to content"  # New benefit
            ]
        )
        print(f"✅ Updated pricing for: {updated_tier['name']}")
        
        # Update tier description
        updated_description = client.tiers.update(
            tier_id=tier_id,
            description="Enhanced plan for individuals with premium features"
        )
        print(f"✅ Updated description for: {updated_description['name']}")
        
    except Exception as e:
        print(f"❌ Error updating tier: {e}")


def tier_management_examples():
    """Demonstrate tier management operations"""
    print("\n=== Tier Management ===")
    
    try:
        # Get tiers for management operations
        tiers_list = client.tiers.list()
        tiers = tiers_list.get('tiers', [])
        
        if not tiers:
            print("⚠️  No tiers found for management operations")
            return
        
        # Find a tier to manage
        tier_to_manage = None
        for tier in tiers:
            if tier['name'] != 'Free Membership':  # Don't archive the free tier
                tier_to_manage = tier
                break
        
        if not tier_to_manage:
            print("⚠️  No suitable tier found for management operations")
            return
            
        tier_id = tier_to_manage['id']
        
        # Archive a tier
        archived_tier = client.tiers.archive(tier_id)
        print(f"📦 Archived tier: {archived_tier['name']}")
        
        # Activate the tier again
        activated_tier = client.tiers.activate(tier_id)
        print(f"✅ Activated tier: {activated_tier['name']}")
        
        # Get active tiers only
        active_tiers = client.tiers.get_active_tiers()
        print(f"✅ Active tiers count: {len(active_tiers)}")
        
        # Get paid tiers only
        paid_tiers = client.tiers.get_paid_tiers()
        print(f"💰 Paid tiers count: {len(paid_tiers)}")
        
    except Exception as e:
        print(f"❌ Error in tier management: {e}")


def pricing_analysis_examples():
    """Demonstrate pricing analysis utilities"""
    print("\n=== Pricing Analysis ===")
    
    try:
        # Get all paid tiers for analysis
        paid_tiers = client.tiers.get_paid_tiers()
        
        if not paid_tiers:
            print("⚠️  No paid tiers found for analysis")
            return
        
        print("💰 Pricing Analysis:")
        for tier in paid_tiers:
            monthly = tier.get('monthly_price', 0)
            yearly = tier.get('yearly_price', 0)
            currency = tier.get('currency', 'USD').upper()
            
            # Calculate yearly savings
            yearly_from_monthly = monthly * 12
            yearly_savings = yearly_from_monthly - yearly if yearly > 0 else 0
            savings_percent = (yearly_savings / yearly_from_monthly * 100) if yearly_from_monthly > 0 else 0
            
            print(f"\n   📊 {tier['name']}:")
            print(f"      Monthly: ${monthly/100:.2f} {currency}")
            if yearly > 0:
                print(f"      Yearly: ${yearly/100:.2f} {currency}")
                print(f"      Yearly savings: ${yearly_savings/100:.2f} ({savings_percent:.1f}%)")
            
            # Benefits count
            benefits_count = len(tier.get('benefits', []))
            print(f"      Benefits: {benefits_count} features")
        
        # Calculate tier value comparison
        if len(paid_tiers) >= 2:
            basic_tier = min(paid_tiers, key=lambda t: t.get('monthly_price', 0))
            premium_tier = max(paid_tiers, key=lambda t: t.get('monthly_price', 0))
            
            price_diff = premium_tier['monthly_price'] - basic_tier['monthly_price']
            benefits_diff = len(premium_tier.get('benefits', [])) - len(basic_tier.get('benefits', []))
            
            print(f"\n   📈 Tier Comparison:")
            print(f"      Price difference: ${price_diff/100:.2f}/month")
            print(f"      Additional benefits: {benefits_diff}")
        
    except Exception as e:
        print(f"❌ Error in pricing analysis: {e}")


def currency_examples():
    """Demonstrate multi-currency tier creation"""
    print("\n=== Multi-Currency Examples ===")
    
    try:
        # Create tiers in different currencies
        eur_tier = client.tiers.create(
            name="European Plan",
            description="Pricing optimized for European customers",
            monthly_price=899,  # €8.99
            yearly_price=8999,  # €89.99
            currency="eur",
            benefits=[
                "All premium content",
                "EU-compliant data handling",
                "European support hours"
            ]
        )
        print(f"✅ Created EUR tier: {eur_tier['name']}")
        
        gbp_tier = client.tiers.create(
            name="UK Plan", 
            description="Pricing for UK customers",
            monthly_price=799,  # £7.99
            yearly_price=7999,  # £79.99
            currency="gbp",
            benefits=[
                "All premium content",
                "UK support team",
                "Local payment methods"
            ]
        )
        print(f"✅ Created GBP tier: {gbp_tier['name']}")
        
        return eur_tier, gbp_tier
        
    except Exception as e:
        print(f"❌ Error creating multi-currency tiers: {e}")
        return None, None


def cleanup_examples():
    """Clean up example tiers"""
    print("\n=== Cleanup ===")
    
    try:
        # Get tiers created in this example
        example_tiers = client.tiers.list()
        
        for tier in example_tiers.get('tiers', []):
            # Only delete tiers we created (be careful not to delete existing tiers)
            if tier['name'] in ['Basic Plan', 'Premium Plan', 'Free Membership', 'European Plan', 'UK Plan']:
                try:
                    # Archive instead of delete for safety
                    client.tiers.archive(tier['id'])
                    print(f"📦 Archived tier: {tier['name']}")
                except Exception as e:
                    print(f"⚠️  Could not archive {tier['name']}: {e}")
                
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")


def main():
    """Run all tier examples"""
    print("🚀 PyGhost Tiers Module Examples")
    print("=" * 40)
    
    try:
        # Run examples
        create_tier_examples()
        list_tiers_examples()
        update_tier_examples()
        tier_management_examples()
        pricing_analysis_examples()
        currency_examples()
        
        # Optionally clean up (uncomment to clean up)
        # cleanup_examples()
        
        print("\n✅ All examples completed successfully!")
        print("\n📝 Tips for production use:")
        print("- Always test pricing changes in a staging environment")
        print("- Consider the impact on existing subscribers when updating tiers")
        print("- Use appropriate currency codes for your target markets")
        print("- Archive rather than delete tiers to preserve subscriber history")
        
    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("Make sure you have:")
        print("1. Set GHOST_SITE_URL environment variable")
        print("2. Set GHOST_ADMIN_API_KEY environment variable")
        print("3. Valid Ghost Admin API credentials")


if __name__ == "__main__":
    main()
