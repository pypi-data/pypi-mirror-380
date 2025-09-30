#!/usr/bin/env python3
"""
Newsletters Usage Examples

This example demonstrates how to use the Newsletters module of PyGhost
to manage newsletter configuration and styling on your Ghost site.
"""

import os
from pyghost import GhostClient

# Initialize the client
# Replace with your actual Ghost site URL and Admin API key
SITE_URL = os.getenv("GHOST_SITE_URL", "https://your-site.ghost.io")
ADMIN_API_KEY = os.getenv("GHOST_ADMIN_API_KEY", "your_key:your_secret")

client = GhostClient(site_url=SITE_URL, admin_api_key=ADMIN_API_KEY)


def create_newsletter_examples():
    """Demonstrate creating different types of newsletters"""
    print("=== Creating Newsletters ===")
    
    try:
        # Create a weekly newsletter with custom styling
        weekly_newsletter = client.newsletters.create(
            name="Weekly Digest",
            description="Our weekly roundup of the best content and updates",
            sender_name="Editorial Team",
            sender_reply_to="newsletter",
            title_font_category="serif",
            title_alignment="center",
            body_font_category="sans_serif",
            show_badge=False,
            show_header_icon=True,
            show_header_title=True,
            show_feature_image=True
        )
        print(f"✅ Created weekly newsletter: {weekly_newsletter['name']}")
        
        # Create a product updates newsletter
        product_newsletter = client.newsletters.create(
            name="Product Updates",
            description="Latest product news, features, and announcements",
            sender_name="Product Team",
            sender_reply_to="support",
            title_font_category="sans_serif",
            title_alignment="left",
            body_font_category="sans_serif",
            show_badge=True,
            subscribe_on_signup=False  # Don't auto-subscribe new members
        )
        print(f"✅ Created product newsletter: {product_newsletter['name']}")
        
        # Create a minimal newsletter with custom styling
        minimal_newsletter = client.newsletters.create(
            name="Minimal Updates",
            description="Clean, minimal newsletter for important updates only",
            sender_name="Admin",
            title_font_category="sans_serif",
            title_alignment="center",
            show_header_icon=False,
            show_header_name=False,
            show_badge=False,
            show_feature_image=False
        )
        print(f"✅ Created minimal newsletter: {minimal_newsletter['name']}")
        
        return weekly_newsletter, product_newsletter, minimal_newsletter
        
    except Exception as e:
        print(f"❌ Error creating newsletters: {e}")
        return None, None, None


def list_newsletters_examples() -> None:
    """Demonstrate different ways to list newsletters"""
    print("\n=== Listing Newsletters ===")
    
    try:
        # Get all newsletters
        all_newsletters = client.newsletters.list()
        print(f"📧 Total newsletters: {len(all_newsletters.get('newsletters', []))}")
        
        # Get only active newsletters
        active_newsletters = client.newsletters.list(filter_="status:active")
        print(f"📧 Active newsletters: {len(active_newsletters.get('newsletters', []))}")
        
        # Display newsletter information
        print("📧 Available newsletters:")
        for newsletter in all_newsletters.get('newsletters', []):
            status = newsletter.get('status', 'unknown')
            sender = newsletter.get('sender_name', 'Unknown')
            subscribers = newsletter.get('subscribe_on_signup', False)
            
            print(f"   - {newsletter['name']} ({status})")
            print(f"     Sender: {sender}")
            print(f"     Auto-subscribe: {'Yes' if subscribers else 'No'}")
            print(f"     Font: {newsletter.get('title_font_category', 'sans_serif')} title, {newsletter.get('body_font_category', 'sans_serif')} body")
            
    except Exception as e:
        print(f"❌ Error listing newsletters: {e}")


def update_newsletter_examples() -> None:
    """Demonstrate updating newsletter configuration"""
    print("\n=== Updating Newsletters ===")
    
    try:
        # Get a newsletter to update
        newsletters_list = client.newsletters.list(limit=1)
        if not newsletters_list.get('newsletters'):
            print("⚠️  No newsletters found to update")
            return
            
        newsletter = newsletters_list['newsletters'][0]
        newsletter_id = newsletter['id']
        
        # Update newsletter styling
        updated_newsletter = client.newsletters.update(
            newsletter_id=newsletter_id,
            title_alignment="left",
            show_header_icon=True,
            show_badge=False,
            footer_content="<p>Thanks for reading! Reply to this email with your thoughts.</p>"
        )
        print(f"✅ Updated styling for: {updated_newsletter['name']}")
        
        # Update sender information
        updated_sender = client.newsletters.update(
            newsletter_id=newsletter_id,
            sender_name="Updated Editorial Team",
            description="Updated newsletter description with new information"
        )
        print(f"✅ Updated sender info for: {updated_sender['name']}")
        
    except Exception as e:
        print(f"❌ Error updating newsletter: {e}")


def newsletter_management_examples() -> None:
    """Demonstrate newsletter management operations"""
    print("\n=== Newsletter Management ===")
    
    try:
        # Get newsletters for management
        newsletters_list = client.newsletters.list()
        newsletters = newsletters_list.get('newsletters', [])
        
        if len(newsletters) < 2:
            print("⚠️  Need at least 2 newsletters for management examples")
            return
        
        # Get a newsletter to manage (not the default one)
        newsletter_to_manage = None
        for newsletter in newsletters:
            if newsletter['name'] not in ['Default Newsletter', 'Weekly Digest']:
                newsletter_to_manage = newsletter
                break
        
        if not newsletter_to_manage:
            # Use the second newsletter if no others available
            newsletter_to_manage = newsletters[1] if len(newsletters) > 1 else newsletters[0]
            
        newsletter_id = newsletter_to_manage['id']
        
        # Archive a newsletter
        archived_newsletter = client.newsletters.archive(newsletter_id)
        print(f"📦 Archived newsletter: {archived_newsletter['name']}")
        
        # Activate the newsletter again
        activated_newsletter = client.newsletters.activate(newsletter_id)
        print(f"✅ Activated newsletter: {activated_newsletter['name']}")
        
        # Get active newsletters only
        active_newsletters = client.newsletters.get_active_newsletters()
        print(f"✅ Active newsletters count: {len(active_newsletters)}")
        
        # Get default newsletter
        default_newsletter = client.newsletters.get_default_newsletter()
        if default_newsletter:
            print(f"🏠 Default newsletter: {default_newsletter['name']}")
        
    except Exception as e:
        print(f"❌ Error in newsletter management: {e}")


def styling_examples():
    """Demonstrate different newsletter styling options"""
    print("\n=== Newsletter Styling Examples ===")
    
    try:
        # Create newsletters with different styling combinations
        
        # Modern serif newsletter
        serif_newsletter = client.newsletters.create(
            name="Serif Style Newsletter",
            description="Professional newsletter with serif fonts",
            sender_name="Editorial",
            title_font_category="serif",
            title_alignment="center",
            body_font_category="serif",
            show_header_icon=True,
            show_header_title=True,
            show_feature_image=True,
            show_badge=True
        )
        print(f"✅ Created serif newsletter: {serif_newsletter['name']}")
        
        # Minimal sans-serif newsletter
        minimal_newsletter = client.newsletters.create(
            name="Minimal Sans Newsletter", 
            description="Clean, modern newsletter with minimal styling",
            sender_name="Team",
            title_font_category="sans_serif",
            title_alignment="left",
            body_font_category="sans_serif",
            show_header_icon=False,
            show_header_title=False,
            show_header_name=True,
            show_feature_image=False,
            show_badge=False
        )
        print(f"✅ Created minimal newsletter: {minimal_newsletter['name']}")
        
        # Display styling comparison
        print("\n🎨 Styling Comparison:")
        newsletters = [serif_newsletter, minimal_newsletter]
        
        for newsletter in newsletters:
            print(f"\n   📧 {newsletter['name']}:")
            print(f"      Title font: {newsletter.get('title_font_category', 'sans_serif')}")
            print(f"      Body font: {newsletter.get('body_font_category', 'sans_serif')}")
            print(f"      Title alignment: {newsletter.get('title_alignment', 'center')}")
            print(f"      Show header icon: {newsletter.get('show_header_icon', True)}")
            print(f"      Show feature images: {newsletter.get('show_feature_image', True)}")
            print(f"      Show Ghost badge: {newsletter.get('show_badge', True)}")
        
        return serif_newsletter, minimal_newsletter
        
    except Exception as e:
        print(f"❌ Error creating styled newsletters: {e}")
        return None, None


def sender_configuration_examples() -> None:
    """Demonstrate sender email configuration"""
    print("\n=== Sender Configuration ===")
    
    try:
        # Get a newsletter to configure
        newsletters = client.newsletters.list().get('newsletters', [])
        if not newsletters:
            print("⚠️  No newsletters found for sender configuration")
            return
            
        newsletter = newsletters[0]
        newsletter_id = newsletter['id']
        
        # Update sender configuration
        updated_newsletter = client.newsletters.update(
            newsletter_id=newsletter_id,
            sender_name="Customer Success Team",
            sender_email="newsletter@example.com",  # This would need to be validated
            sender_reply_to="support"
        )
        print(f"✅ Updated sender configuration for: {updated_newsletter['name']}")
        
        # Note: In a real implementation, you would validate the sender email
        print("📝 Note: Sender email validation required for custom sender addresses")
        print("   Use client.newsletters.validate_sender_email() to validate custom emails")
        
        # Example of how you might validate (this would send a validation email)
        # validation_response = client.newsletters.validate_sender_email(
        #     newsletter_id, 
        #     "newsletter@example.com"
        # )
        # print(f"✅ Validation email sent for verification")
        
    except Exception as e:
        print(f"❌ Error configuring sender: {e}")


def newsletter_analytics_examples() -> None:
    """Demonstrate newsletter configuration analysis"""
    print("\n=== Newsletter Configuration Analysis ===")
    
    try:
        # Get all newsletters for analysis
        all_newsletters = client.newsletters.list()
        newsletters = all_newsletters.get('newsletters', [])
        
        if not newsletters:
            print("⚠️  No newsletters found for analysis")
            return
        
        print("📊 Newsletter Configuration Summary:")
        
        # Analyze font preferences
        serif_count = sum(1 for n in newsletters if n.get('title_font_category') == 'serif')
        sans_serif_count = len(newsletters) - serif_count
        
        print(f"   📝 Font Preferences:")
        print(f"      Serif titles: {serif_count}")
        print(f"      Sans-serif titles: {sans_serif_count}")
        
        # Analyze styling options
        with_badges = sum(1 for n in newsletters if n.get('show_badge', True))
        with_icons = sum(1 for n in newsletters if n.get('show_header_icon', True))
        with_features = sum(1 for n in newsletters if n.get('show_feature_image', True))
        
        print(f"   🎨 Visual Elements:")
        print(f"      Show Ghost badge: {with_badges}/{len(newsletters)}")
        print(f"      Show header icon: {with_icons}/{len(newsletters)}")
        print(f"      Show feature images: {with_features}/{len(newsletters)}")
        
        # Analyze subscription settings
        auto_subscribe = sum(1 for n in newsletters if n.get('subscribe_on_signup', True))
        
        print(f"   📧 Subscription Settings:")
        print(f"      Auto-subscribe new members: {auto_subscribe}/{len(newsletters)}")
        
        # Analyze sender configuration
        reply_to_newsletter = sum(1 for n in newsletters if n.get('sender_reply_to') == 'newsletter')
        reply_to_support = sum(1 for n in newsletters if n.get('sender_reply_to') == 'support')
        
        print(f"   👤 Sender Configuration:")
        print(f"      Reply-to newsletter: {reply_to_newsletter}")
        print(f"      Reply-to support: {reply_to_support}")
        
    except Exception as e:
        print(f"❌ Error in newsletter analysis: {e}")


def cleanup_examples() -> None:
    """Clean up example newsletters"""
    print("\n=== Cleanup ===")
    
    try:
        # Get newsletters created in this example
        all_newsletters = client.newsletters.list()
        
        for newsletter in all_newsletters.get('newsletters', []):
            # Only archive newsletters we created (be careful with existing ones)
            if newsletter['name'] in [
                'Weekly Digest', 'Product Updates', 'Minimal Updates',
                'Serif Style Newsletter', 'Minimal Sans Newsletter'
            ]:
                try:
                    client.newsletters.archive(newsletter['id'])
                    print(f"📦 Archived newsletter: {newsletter['name']}")
                except Exception as e:
                    print(f"⚠️  Could not archive {newsletter['name']}: {e}")
                
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")


def main() -> None:
    """Run all newsletter examples"""
    print("🚀 PyGhost Newsletters Module Examples")
    print("=" * 40)
    
    try:
        # Run examples
        create_newsletter_examples()
        list_newsletters_examples()
        update_newsletter_examples()
        newsletter_management_examples()
        styling_examples()
        sender_configuration_examples()
        newsletter_analytics_examples()
        
        # Optionally clean up (uncomment to clean up)
        # cleanup_examples()
        
        print("\n✅ All examples completed successfully!")
        print("\n📝 Tips for production use:")
        print("- Always test newsletter styling with sample content before going live")
        print("- Validate custom sender email addresses before using them")
        print("- Consider your audience when choosing fonts and styling")
        print("- Use meaningful names and descriptions for newsletters")
        print("- Archive rather than delete newsletters to preserve settings")
        
    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("Make sure you have:")
        print("1. Set GHOST_SITE_URL environment variable")
        print("2. Set GHOST_ADMIN_API_KEY environment variable")
        print("3. Valid Ghost Admin API credentials")
        print("4. Appropriate permissions to manage newsletters")


if __name__ == "__main__":
    main()
