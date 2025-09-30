#!/usr/bin/env python3
"""
Members Usage Examples - PyGhost

This script demonstrates comprehensive usage of the Members module for managing
Ghost subscribers, including CRUD operations, label management, newsletter subscriptions,
and analytics.

Requirements:
- Set environment variables: GHOST_SITE_URL and GHOST_ADMIN_API_KEY
- Or modify the client initialization below with your actual credentials

Example usage:
    python examples/members_usage.py
"""

import os
import sys
from typing import List, Dict

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyghost import GhostClient, ValidationError, GhostAPIError


def setup_client() -> GhostClient:
    """Initialize Ghost client with credentials."""
    site_url = os.getenv('GHOST_SITE_URL', 'https://your-site.ghost.io')
    admin_api_key = os.getenv('GHOST_ADMIN_API_KEY', 'your_key:your_secret')
    
    if site_url == 'https://your-site.ghost.io' or admin_api_key == 'your_key:your_secret':
        print("⚠️  Please set GHOST_SITE_URL and GHOST_ADMIN_API_KEY environment variables")
        print("   Or modify the credentials in this script")
        return None
    
    return GhostClient(site_url=site_url, admin_api_key=admin_api_key)


def basic_member_operations(client: GhostClient) -> Dict:
    """Demonstrate basic member CRUD operations."""
    print("\n🔰 Basic Member Operations")
    print("=" * 50)
    
    try:
        # Create a basic member
        print("Creating a new member...")
        member = client.members.create(
            email="subscriber@example.com",
            name="John Subscriber"
        )
        print(f"✅ Created member: {member['name']} ({member['email']})")
        print(f"   ID: {member['id']}")
        print(f"   Status: {member['status']}")
        print(f"   Created: {member['created_at']}")
        
        member_id = member['id']
        
        # Get member by ID
        print(f"\nRetrieving member by ID...")
        retrieved_member = client.members.get(member_id, include="labels,newsletters")
        print(f"✅ Retrieved member: {retrieved_member['name']}")
        print(f"   Labels: {len(retrieved_member.get('labels', []))}")
        print(f"   Newsletters: {len(retrieved_member.get('newsletters', []))}")
        
        # Update member
        print(f"\nUpdating member information...")
        updated_member = client.members.update(
            member_id,
            name="John Updated Subscriber",
            note="Updated from PyGhost example"
        )
        print(f"✅ Updated member: {updated_member['name']}")
        print(f"   Note: {updated_member['note']}")
        
        return updated_member
        
    except ValidationError as e:
        print(f"❌ Validation error: {e}")
        return None
    except GhostAPIError as e:
        print(f"❌ API error: {e}")
        return None


def member_label_management(client: GhostClient, member_id: str):
    """Demonstrate member label management."""
    print("\n🏷️  Member Label Management")
    print("=" * 50)
    
    try:
        # Add labels to member
        print("Adding labels to member...")
        labels_to_add = ["VIP", "Newsletter Subscriber", "Active"]
        updated_member = client.members.add_labels(member_id, labels_to_add)
        current_labels = [label['name'] for label in updated_member.get('labels', [])]
        print(f"✅ Added labels: {labels_to_add}")
        print(f"   Current labels: {current_labels}")
        
        # Remove specific labels
        print(f"\nRemoving some labels...")
        labels_to_remove = ["Active"]
        updated_member = client.members.remove_labels(member_id, labels_to_remove)
        remaining_labels = [label['name'] for label in updated_member.get('labels', [])]
        print(f"✅ Removed labels: {labels_to_remove}")
        print(f"   Remaining labels: {remaining_labels}")
        
    except GhostAPIError as e:
        print(f"❌ Error managing labels: {e}")


def newsletter_subscription_management(client: GhostClient, member_id: str):
    """Demonstrate newsletter subscription management."""
    print("\n📧 Newsletter Subscription Management")
    print("=" * 50)
    
    try:
        # First, get available newsletters
        print("Getting available newsletters...")
        newsletters_response = client.newsletters.list()
        newsletters = newsletters_response.get('newsletters', [])
        
        if newsletters:
            newsletter_ids = [newsletter['id'] for newsletter in newsletters[:2]]  # Use first 2
            newsletter_names = [newsletter['name'] for newsletter in newsletters[:2]]
            
            # Subscribe to newsletters
            print(f"Subscribing to newsletters: {newsletter_names}")
            updated_member = client.members.subscribe_to_newsletters(member_id, newsletter_ids)
            subscribed_newsletters = [nl['name'] for nl in updated_member.get('newsletters', [])]
            print(f"✅ Subscribed to newsletters: {subscribed_newsletters}")
            
            # Unsubscribe from one newsletter
            if len(newsletter_ids) > 1:
                print(f"Unsubscribing from: {newsletter_names[0]}")
                updated_member = client.members.unsubscribe_from_newsletters(member_id, [newsletter_ids[0]])
                remaining_newsletters = [nl['name'] for nl in updated_member.get('newsletters', [])]
                print(f"✅ Remaining subscriptions: {remaining_newsletters}")
        else:
            print("ℹ️  No newsletters found on this site")
            
    except GhostAPIError as e:
        print(f"❌ Error managing newsletter subscriptions: {e}")


def advanced_member_creation(client: GhostClient) -> Dict:
    """Demonstrate advanced member creation with full options."""
    print("\n🚀 Advanced Member Creation")
    print("=" * 50)
    
    try:
        # Get available newsletters and tiers for advanced creation
        newsletters_response = client.newsletters.list()
        newsletters = newsletters_response.get('newsletters', [])
        
        tiers_response = client.tiers.list()
        tiers = tiers_response.get('tiers', [])
        
        newsletter_ids = [nl['id'] for nl in newsletters[:1]] if newsletters else []
        tier_ids = [tier['id'] for tier in tiers[:1]] if tiers else []
        
        # Create advanced member
        print("Creating advanced member with labels, newsletters, and tiers...")
        advanced_member = client.members.create(
            email="premium@example.com",
            name="Premium Subscriber",
            note="High-value customer from marketing campaign",
            labels=["Premium", "Marketing Campaign", "High Value"],
            newsletters=newsletter_ids,
            tiers=tier_ids
        )
        
        print(f"✅ Created advanced member: {advanced_member['name']}")
        print(f"   Email: {advanced_member['email']}")
        print(f"   Status: {advanced_member['status']}")
        print(f"   Labels: {len(advanced_member.get('labels', []))}")
        print(f"   Newsletter subscriptions: {len(advanced_member.get('newsletters', []))}")
        print(f"   Tier associations: {len(advanced_member.get('tiers', []))}")
        
        return advanced_member
        
    except ValidationError as e:
        print(f"❌ Validation error: {e}")
        return None
    except GhostAPIError as e:
        print(f"❌ API error: {e}")
        return None


def member_search_and_filtering(client: GhostClient):
    """Demonstrate member search and filtering capabilities."""
    print("\n🔍 Member Search and Filtering")
    print("=" * 50)
    
    try:
        # List all members
        print("Getting all members...")
        all_members = client.members.list(limit=5, include="labels")
        total_members = all_members.get('meta', {}).get('pagination', {}).get('total', 0)
        print(f"✅ Total members on site: {total_members}")
        
        # Search by email domain
        print(f"\nSearching for members with 'example.com' domain...")
        gmail_members = client.members.list(filter_="email:~example.com", include="labels")
        example_members = gmail_members.get('members', [])
        print(f"✅ Found {len(example_members)} members with example.com emails")
        
        # Get paid members
        print(f"\nGetting paid members...")
        paid_members = client.members.get_paid_members(include="tiers")
        print(f"✅ Found {len(paid_members)} paid members")
        
        # Get free members
        print(f"\nGetting free members...")
        free_members = client.members.get_free_members()
        print(f"✅ Found {len(free_members)} free members")
        
        # Search by label
        print(f"\nSearching for VIP members...")
        vip_members = client.members.get_members_by_label("VIP")
        print(f"✅ Found {len(vip_members)} VIP members")
        
        # Get member by email
        print(f"\nSearching for specific member by email...")
        specific_member = client.members.get_by_email("subscriber@example.com")
        if specific_member:
            print(f"✅ Found member: {specific_member['name']} ({specific_member['email']})")
        else:
            print("ℹ️  Member not found")
            
    except GhostAPIError as e:
        print(f"❌ Error searching members: {e}")


def member_analytics_and_statistics(client: GhostClient):
    """Demonstrate member analytics and statistics."""
    print("\n📊 Member Analytics and Statistics")
    print("=" * 50)
    
    try:
        # Get member statistics
        print("Getting member statistics...")
        stats = client.members.get_member_statistics()
        
        print(f"✅ Member Statistics:")
        print(f"   Total Members: {stats['total']}")
        print(f"   Paid Members: {stats['paid']}")
        print(f"   Free Members: {stats['free']}")
        print(f"   Paid Percentage: {stats['paid_percentage']:.1f}%")
        
        # Get recent members
        print(f"\nGetting recent members...")
        recent_members = client.members.list(
            limit=5,
            order="created_at desc",
            include="labels"
        )
        
        print(f"✅ Recent Members:")
        for member in recent_members.get('members', [])[:3]:
            labels = [label['name'] for label in member.get('labels', [])]
            print(f"   • {member['name']} ({member['email']})")
            print(f"     Status: {member['status']}, Labels: {labels}")
            print(f"     Joined: {member['created_at'][:10]}")
        
    except GhostAPIError as e:
        print(f"❌ Error getting analytics: {e}")


def error_handling_examples(client: GhostClient):
    """Demonstrate proper error handling."""
    print("\n⚠️  Error Handling Examples")
    print("=" * 50)
    
    # Try to create member with duplicate email
    try:
        print("Attempting to create member with duplicate email...")
        client.members.create(email="subscriber@example.com", name="Duplicate")
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except GhostAPIError as e:
        print(f"✅ Caught API error (expected): {e}")
    
    # Try to get non-existent member
    try:
        print("Attempting to get non-existent member...")
        client.members.get("non-existent-id")
    except Exception as e:
        print(f"✅ Caught error for non-existent member (expected): {type(e).__name__}")
    
    # Try to create member with invalid email
    try:
        print("Attempting to create member with invalid email format...")
        client.members.create(email="invalid-email", name="Test")
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except Exception as e:
        print(f"✅ Caught error for invalid email (expected): {type(e).__name__}")


def cleanup_test_members(client: GhostClient, member_ids: List[str]):
    """Clean up test members created during examples."""
    print("\n🧹 Cleanup Test Members")
    print("=" * 50)
    
    for member_id in member_ids:
        try:
            # Get member info before deletion
            member = client.members.get(member_id)
            print(f"Deleting member: {member['name']} ({member['email']})")
            
            # Delete member
            success = client.members.delete(member_id)
            if success:
                print(f"✅ Successfully deleted member: {member['name']}")
            
        except Exception as e:
            print(f"⚠️  Could not delete member {member_id}: {e}")


def main() -> None:
    """Main function to run all member examples."""
    print("🎯 PyGhost Members Module Examples")
    print("=" * 60)
    
    # Initialize client
    client = setup_client()
    if not client:
        return
    
    created_member_ids = []
    
    try:
        # Basic operations
        basic_member = basic_member_operations(client)
        if basic_member:
            created_member_ids.append(basic_member['id'])
            
            # Label management
            member_label_management(client, basic_member['id'])
            
            # Newsletter management
            newsletter_subscription_management(client, basic_member['id'])
        
        # Advanced creation
        advanced_member = advanced_member_creation(client)
        if advanced_member:
            created_member_ids.append(advanced_member['id'])
        
        # Search and filtering
        member_search_and_filtering(client)
        
        # Analytics
        member_analytics_and_statistics(client)
        
        # Error handling
        error_handling_examples(client)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
    finally:
        # Cleanup
        if created_member_ids:
            cleanup_test_members(client, created_member_ids)
    
    print("\n✅ Members module examples completed!")
    print("\nNext steps:")
    print("• Explore the Members module documentation")
    print("• Check out other PyGhost modules (Users, Images, Posts, etc.)")
    print("• Build your own member management workflows")


if __name__ == "__main__":
    main()
