#!/usr/bin/env python3
"""
PyGhost Webhooks Module - Comprehensive Usage Examples

This example demonstrates the complete functionality of the PyGhost Webhooks module
including webhook creation, management, event handling, and monitoring.

Requirements:
- Set GHOST_SITE_URL and GHOST_ADMIN_API_KEY environment variables
- Admin permissions on your Ghost site
- A webhook endpoint URL for testing (can use webhook.site for testing)

Webhook Events Available:
- post.added, post.deleted, post.edited, post.published, post.unpublished
- post.scheduled, post.unscheduled
- page.added, page.deleted, page.edited, page.published, page.unpublished
- page.scheduled, page.unscheduled
- tag.added, tag.edited, tag.deleted
- user.activated, user.attached, user.detached
- member.added, member.edited, member.deleted
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import List, Dict

# Add the parent directory to the path to import pyghost
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyghost import GhostClient
from pyghost.exceptions import GhostAPIError, ValidationError, AuthenticationError


def demo_webhook_events():
    """Demonstrate webhook event information and validation."""
    print("\n" + "="*60)
    print("WEBHOOK EVENTS AND VALIDATION")
    print("="*60)
    
    try:
        # Initialize client for utility functions
        client = GhostClient("https://example.ghost.io", "dummy:key")
        
        # Get available webhook events
        print("📋 Available webhook events:")
        events = client.webhooks.get_webhook_events()
        
        # Group events by category
        event_categories = {}
        for event in events:
            category = event.split('.')[0]
            if category not in event_categories:
                event_categories[category] = []
            event_categories[category].append(event)
        
        for category, category_events in event_categories.items():
            print(f"\n📌 {category.upper()} Events:")
            for event in category_events:
                print(f"   • {event}")
        
        print(f"\n📊 Total events available: {len(events)}")
        
        # Test event validation
        print(f"\n🔍 Testing event validation:")
        test_events = [
            "post.published",    # Valid
            "member.added",      # Valid
            "invalid.event",     # Invalid
            "post.deleted",      # Valid
            "custom.event"       # Invalid
        ]
        
        for event in test_events:
            is_valid = client.webhooks.validate_webhook_event(event)
            status = "✅ Valid" if is_valid else "❌ Invalid"
            print(f"   {event}: {status}")
        
    except Exception as e:
        print(f"⚠️  Webhook events demo failed: {e}")


def demo_webhook_creation(client):
    """Demonstrate webhook creation functionality."""
    print("\n" + "="*60)
    print("WEBHOOK CREATION EXAMPLES")
    print("="*60)
    
    created_webhooks = []
    
    try:
        # Create a basic webhook
        print("📤 Creating a basic post publication webhook...")
        webhook1 = client.webhooks.create(
            event="post.published",
            target_url="https://webhook.site/unique-id-1",
            name="Post Publication Webhook"
        )
        created_webhooks.append(webhook1['id'])
        
        print(f"✅ Webhook created successfully!")
        print(f"   ID: {webhook1['id']}")
        print(f"   Event: {webhook1['event']}")
        print(f"   Target URL: {webhook1['target_url']}")
        print(f"   Name: {webhook1.get('name', 'No name')}")
        print(f"   Status: {webhook1.get('status', 'Unknown')}")
        
        # Create a webhook with secret
        print(f"\n📤 Creating webhook with secret for security...")
        webhook2 = client.webhooks.create(
            event="member.added",
            target_url="https://webhook.site/unique-id-2",
            name="New Member Webhook",
            secret="my-super-secret-key-123"
        )
        created_webhooks.append(webhook2['id'])
        
        print(f"✅ Webhook with secret created!")
        print(f"   ID: {webhook2['id']}")
        print(f"   Event: {webhook2['event']}")
        print(f"   Has secret: {'secret' in webhook2 and webhook2['secret'] is not None}")
        
        # Create webhook with API version
        print(f"\n📤 Creating webhook with specific API version...")
        webhook3 = client.webhooks.create(
            event="post.deleted",
            target_url="https://webhook.site/unique-id-3",
            name="Post Deletion Webhook",
            api_version="v5.0"
        )
        created_webhooks.append(webhook3['id'])
        
        print(f"✅ Webhook with API version created!")
        print(f"   ID: {webhook3['id']}")
        print(f"   API Version: {webhook3.get('api_version', 'Default')}")
        
        # Use convenience methods
        print(f"\n📤 Using convenience method for post webhook...")
        post_webhook = client.webhooks.create_post_webhook(
            target_url="https://webhook.site/unique-id-4",
            event="post.edited",
            name="Post Edit Tracker"
        )
        created_webhooks.append(post_webhook['id'])
        
        print(f"✅ Post webhook created with convenience method!")
        print(f"   Event: {post_webhook['event']}")
        print(f"   Name: {post_webhook['name']}")
        
        print(f"\n📤 Using convenience method for member webhook...")
        member_webhook = client.webhooks.create_member_webhook(
            target_url="https://webhook.site/unique-id-5",
            name="Member Activity Tracker"
        )
        created_webhooks.append(member_webhook['id'])
        
        print(f"✅ Member webhook created with convenience method!")
        print(f"   Event: {member_webhook['event']}")
        print(f"   Name: {member_webhook['name']}")
        
        return created_webhooks
        
    except Exception as e:
        print(f"⚠️  Webhook creation demo failed: {e}")
        return created_webhooks


def demo_webhook_management(client, webhook_ids: List[str]):
    """Demonstrate webhook management functionality."""
    print("\n" + "="*60)
    print("WEBHOOK MANAGEMENT EXAMPLES")
    print("="*60)
    
    try:
        if not webhook_ids:
            print("⚠️  No webhooks available for management demo")
            return
        
        # List all webhooks
        print("📋 Listing all webhooks...")
        webhooks_response = client.webhooks.list()
        webhooks = webhooks_response.get('webhooks', [])
        
        print(f"✅ Found {len(webhooks)} webhooks:")
        for webhook in webhooks[:5]:  # Show first 5
            print(f"   • {webhook.get('name', 'Unnamed')} ({webhook['event']}) -> {webhook['target_url']}")
        
        if len(webhooks) > 5:
            print(f"   ... and {len(webhooks) - 5} more")
        
        # Get specific webhook
        webhook_id = webhook_ids[0]
        print(f"\n🔍 Getting specific webhook: {webhook_id}")
        specific_webhook = client.webhooks.get(webhook_id)
        
        print(f"✅ Webhook details:")
        print(f"   Name: {specific_webhook.get('name', 'Unnamed')}")
        print(f"   Event: {specific_webhook['event']}")
        print(f"   Target URL: {specific_webhook['target_url']}")
        print(f"   Status: {specific_webhook.get('status', 'Unknown')}")
        print(f"   Created: {specific_webhook.get('created_at', 'Unknown')}")
        print(f"   Last triggered: {specific_webhook.get('last_triggered_at', 'Never')}")
        
        # Update webhook
        print(f"\n✏️ Updating webhook...")
        updated_webhook = client.webhooks.update(
            webhook_id=webhook_id,
            name="Updated Webhook Name",
            target_url="https://webhook.site/updated-endpoint"
        )
        
        print(f"✅ Webhook updated successfully!")
        print(f"   New name: {updated_webhook.get('name', 'Unnamed')}")
        print(f"   New URL: {updated_webhook['target_url']}")
        
        # Get webhooks by event type
        print(f"\n🔍 Getting webhooks for 'post.published' event...")
        post_webhooks = client.webhooks.get_webhooks_by_event("post.published")
        print(f"✅ Found {len(post_webhooks)} webhooks for post.published event")
        
        # Get active webhooks
        print(f"\n🔍 Getting active webhooks...")
        active_webhooks = client.webhooks.get_active_webhooks()
        print(f"✅ Found {len(active_webhooks)} active webhooks")
        
    except Exception as e:
        print(f"⚠️  Webhook management demo failed: {e}")


def demo_webhook_statistics(client):
    """Demonstrate webhook statistics and monitoring."""
    print("\n" + "="*60)
    print("WEBHOOK STATISTICS AND MONITORING")
    print("="*60)
    
    try:
        # Get webhook statistics
        print("📊 Getting webhook statistics...")
        stats = client.webhooks.get_webhook_statistics()
        
        print(f"✅ Webhook Statistics:")
        print(f"   Total webhooks: {stats['total']}")
        print(f"   Active webhooks: {stats['active']}")
        print(f"   Last triggered: {stats['last_triggered'] or 'Never'}")
        
        if stats['events']:
            print(f"\n📋 Webhooks by event type:")
            for event, count in stats['events'].items():
                print(f"   • {event}: {count} webhook(s)")
        
        # List webhooks with filtering
        print(f"\n🔍 Listing webhooks with limit...")
        limited_response = client.webhooks.list(limit=3)
        limited_webhooks = limited_response.get('webhooks', [])
        
        print(f"✅ Retrieved {len(limited_webhooks)} webhooks (limited to 3)")
        for webhook in limited_webhooks:
            status = webhook.get('status', 'unknown')
            last_triggered = webhook.get('last_triggered_at', 'Never')
            print(f"   • {webhook.get('name', 'Unnamed')}: {status} (last: {last_triggered})")
        
    except Exception as e:
        print(f"⚠️  Webhook statistics demo failed: {e}")


def demo_webhook_cleanup(client, webhook_ids: List[str]):
    """Demonstrate webhook cleanup and bulk operations."""
    print("\n" + "="*60)
    print("WEBHOOK CLEANUP AND BULK OPERATIONS")
    print("="*60)
    
    try:
        if not webhook_ids:
            print("⚠️  No webhooks available for cleanup demo")
            return
        
        # Delete individual webhook
        if len(webhook_ids) > 0:
            webhook_to_delete = webhook_ids[0]
            print(f"🗑️  Deleting individual webhook: {webhook_to_delete}")
            success = client.webhooks.delete(webhook_to_delete)
            
            if success:
                print(f"✅ Webhook deleted successfully!")
                webhook_ids.remove(webhook_to_delete)
            
        # Bulk delete remaining webhooks
        if len(webhook_ids) > 1:
            print(f"\n🗑️  Bulk deleting {len(webhook_ids)} webhooks...")
            bulk_results = client.webhooks.bulk_delete_webhooks(webhook_ids)
            
            print(f"✅ Bulk deletion completed!")
            print(f"   Successful: {len(bulk_results['successful'])}")
            print(f"   Failed: {len(bulk_results['failed'])}")
            print(f"   Total processed: {bulk_results['total']}")
            
            if bulk_results['failed']:
                print(f"   Failed deletions:")
                for failed in bulk_results['failed']:
                    print(f"     • {failed['id']}: {failed['error']}")
        
        elif len(webhook_ids) == 1:
            # Delete the last webhook individually
            last_webhook = webhook_ids[0]
            print(f"🗑️  Deleting last webhook: {last_webhook}")
            client.webhooks.delete(last_webhook)
            print(f"✅ Last webhook deleted!")
        
    except Exception as e:
        print(f"⚠️  Webhook cleanup demo failed: {e}")


def demo_error_handling():
    """Demonstrate error handling for webhook operations."""
    print("\n" + "="*60)
    print("ERROR HANDLING EXAMPLES")
    print("="*60)
    
    try:
        # Initialize client
        client = GhostClient("https://example.ghost.io", "dummy:key")
        
        # Test empty event error
        print("🔍 Testing empty event error...")
        try:
            client.webhooks.create("", "https://example.com/webhook")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test empty target URL error
        print("\n🔍 Testing empty target URL error...")
        try:
            client.webhooks.create("post.published", "")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test invalid event type
        print("\n🔍 Testing invalid event type...")
        try:
            client.webhooks.get_webhooks_by_event("invalid.event")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test empty webhook ID
        print("\n🔍 Testing empty webhook ID...")
        try:
            client.webhooks.get("")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test empty webhook IDs list for bulk delete
        print("\n🔍 Testing empty webhook IDs for bulk delete...")
        try:
            client.webhooks.bulk_delete_webhooks([])
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test update with no fields
        print("\n🔍 Testing update with no fields...")
        try:
            client.webhooks.update("webhook_id")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
    except Exception as e:
        print(f"⚠️  Error handling demo failed: {e}")


def demo_webhook_best_practices():
    """Demonstrate webhook best practices and tips."""
    print("\n" + "="*60)
    print("WEBHOOK BEST PRACTICES AND TIPS")
    print("="*60)
    
    print("💡 Webhook Best Practices:")
    print()
    print("🔐 Security:")
    print("   • Always use HTTPS endpoints for webhook URLs")
    print("   • Include a secret for webhook verification")
    print("   • Validate webhook signatures in your endpoint")
    print("   • Use API versioning to ensure compatibility")
    print()
    print("⚡ Performance:")
    print("   • Keep webhook endpoints fast (< 5 seconds response time)")
    print("   • Return HTTP 200 status for successful processing")
    print("   • Implement proper error handling and logging")
    print("   • Use queues for heavy processing")
    print()
    print("🔄 Reliability:")
    print("   • Implement idempotency in your webhook handlers")
    print("   • Handle duplicate webhook deliveries gracefully")
    print("   • Monitor webhook delivery success rates")
    print("   • Set up alerting for failed webhooks")
    print()
    print("🧪 Testing:")
    print("   • Use webhook.site or similar tools for testing")
    print("   • Test with different event types")
    print("   • Verify webhook payload structure")
    print("   • Test error scenarios and timeouts")
    print()
    print("📊 Monitoring:")
    print("   • Track webhook delivery metrics")
    print("   • Monitor endpoint response times")
    print("   • Log webhook payloads for debugging")
    print("   • Set up health checks for webhook endpoints")
    
    # Show example webhook payload structure
    print(f"\n📋 Example webhook payload structure:")
    example_payload = {
        "post": {
            "current": {
                "id": "5f04028cc9b839282b0eb5e3",
                "title": "Welcome to Ghost",
                "slug": "welcome",
                "status": "published",
                "created_at": "2020-07-07T05:05:16.000Z",
                "updated_at": "2020-07-07T05:05:16.000Z",
                "published_at": "2020-07-07T05:05:16.000Z"
            }
        }
    }
    
    print(json.dumps(example_payload, indent=2))


def main():
    """Main demonstration function."""
    print("🔗 PyGhost Webhooks Module - Comprehensive Usage Examples")
    print("=" * 60)
    
    # Configuration
    SITE_URL = os.getenv("GHOST_SITE_URL")
    API_KEY = os.getenv("GHOST_ADMIN_API_KEY")
    
    if not SITE_URL or not API_KEY:
        print("⚠️  Please set the required environment variables:")
        print("   export GHOST_SITE_URL='https://your-site.ghost.io'")
        print("   export GHOST_ADMIN_API_KEY='your_key_id:your_secret_hex'")
        print()
        print("🔧 Running offline demonstrations that don't require API access...")
        
        # Run demonstrations that don't require API connection
        demo_webhook_events()
        demo_error_handling()
        demo_webhook_best_practices()
        
        print("\n💡 To run webhook management examples, configure your Ghost API credentials.")
        print("💡 For testing, you can use https://webhook.site to create test endpoints.")
        return
    
    try:
        # Initialize the PyGhost client
        print(f"🚀 Initializing PyGhost client for {SITE_URL}...")
        client = GhostClient(site_url=SITE_URL, admin_api_key=API_KEY)
        print("✅ Client initialized successfully!")
        
        # Run all demonstrations
        demo_webhook_events()
        
        # Create webhooks for testing
        created_webhook_ids = demo_webhook_creation(client)
        
        # Manage webhooks
        demo_webhook_management(client, created_webhook_ids)
        demo_webhook_statistics(client)
        
        # Best practices
        demo_webhook_best_practices()
        
        # Error handling
        demo_error_handling()
        
        # Clean up created webhooks
        demo_webhook_cleanup(client, created_webhook_ids)
        
        print("\n🎉 All webhook examples completed successfully!")
        print("\n💡 Next steps:")
        print("   • Set up webhook endpoints for your applications")
        print("   • Implement webhook signature verification")
        print("   • Create automated workflows based on Ghost events")
        print("   • Monitor webhook delivery and performance")
        print("   • Explore Ghost's webhook event documentation")
        
    except AuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("   Please check your Ghost site URL and API key")
        
    except GhostAPIError as e:
        print(f"❌ Ghost API error: {e}")
        print("   Please check your Ghost site configuration and permissions")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("   Please check your configuration and network connection")


if __name__ == "__main__":
    main()
