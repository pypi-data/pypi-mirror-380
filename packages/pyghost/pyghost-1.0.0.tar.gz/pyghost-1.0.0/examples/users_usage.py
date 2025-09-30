#!/usr/bin/env python3
"""
Users Usage Examples - PyGhost

This script demonstrates comprehensive usage of the Users module for managing
Ghost site staff and authors, including profile management, role assignments,
permissions, and user administration.

Requirements:
- Set environment variables: GHOST_SITE_URL and GHOST_ADMIN_API_KEY
- Or modify the client initialization below with your actual credentials
- Admin/Owner permissions required for most user management operations

Example usage:
    python examples/users_usage.py
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


def basic_user_operations(client: GhostClient):
    """Demonstrate basic user operations."""
    print("\n👤 Basic User Operations")
    print("=" * 50)
    
    try:
        # List all users
        print("Getting all users...")
        users = client.users.list(include="count.posts,roles")
        users_list = users.get('users', [])
        total_users = users.get('meta', {}).get('pagination', {}).get('total', 0)
        
        print(f"✅ Found {total_users} users on the site")
        
        # Display user information
        print(f"\n📋 User Overview:")
        for user in users_list[:5]:  # Show first 5 users
            roles = [role['name'] for role in user.get('roles', [])]
            post_count = user.get('count', {}).get('posts', 0)
            print(f"   • {user['name']} ({user['email']})")
            print(f"     Roles: {roles}")
            print(f"     Posts: {post_count}")
            print(f"     Status: {user['status']}")
            print(f"     Last seen: {user.get('last_seen', 'Never')[:10]}")
        
        return users_list[0] if users_list else None
        
    except GhostAPIError as e:
        print(f"❌ Error getting users: {e}")
        return None


def user_profile_management(client: GhostClient, user_data: Dict):
    """Demonstrate user profile management."""
    print("\n✏️  User Profile Management")
    print("=" * 50)
    
    user_id = user_data['id']
    original_name = user_data['name']
    
    try:
        # Update user profile information
        print(f"Updating profile for user: {original_name}")
        updated_user = client.users.update(
            user_id,
            name=f"{original_name} (Updated)",
            bio="Updated bio from PyGhost example - Senior content creator with expertise in technical writing",
            website="https://example-author.com",
            location="San Francisco, CA",
            twitter="@example_author"
        )
        
        print(f"✅ Updated user profile:")
        print(f"   Name: {updated_user['name']}")
        print(f"   Bio: {updated_user['bio'][:50]}...")
        print(f"   Website: {updated_user['website']}")
        print(f"   Location: {updated_user['location']}")
        print(f"   Twitter: @{updated_user['twitter']}")
        
        # Update SEO information
        print(f"\nUpdating SEO information...")
        seo_updated_user = client.users.update(
            user_id,
            meta_title=f"{original_name} - Technical Writer",
            meta_description="Experienced technical writer and content creator specializing in developer documentation."
        )
        
        print(f"✅ Updated SEO information:")
        print(f"   Meta Title: {seo_updated_user['meta_title']}")
        print(f"   Meta Description: {seo_updated_user['meta_description']}")
        
        # Restore original name
        print(f"\nRestoring original name...")
        client.users.update(user_id, name=original_name)
        print(f"✅ Restored original name: {original_name}")
        
    except GhostAPIError as e:
        print(f"❌ Error updating user profile: {e}")


def user_roles_and_permissions(client: GhostClient):
    """Demonstrate user roles and permissions management."""
    print("\n🔐 User Roles and Permissions")
    print("=" * 50)
    
    try:
        # Get available roles
        print("Getting available user roles...")
        roles = client.users.get_user_roles()
        
        print(f"✅ Available roles:")
        for role in roles:
            print(f"   • {role['name']}: {role['description']}")
        
        # Get users by role
        print(f"\nGetting users by role...")
        
        # Get owners
        owners = client.users.get_owners()
        print(f"✅ Site Owners: {len(owners)}")
        for owner in owners:
            print(f"   • {owner['name']} ({owner['email']})")
        
        # Get administrators
        administrators = client.users.get_administrators()
        print(f"✅ Administrators: {len(administrators)}")
        
        # Get editors
        editors = client.users.get_editors()
        print(f"✅ Editors: {len(editors)}")
        
        # Get authors
        authors = client.users.get_authors(include="count.posts")
        print(f"✅ Authors: {len(authors)}")
        for author in authors[:3]:  # Show first 3 authors
            post_count = author.get('count', {}).get('posts', 0)
            print(f"   • {author['name']}: {post_count} posts")
        
        # Get contributors
        contributors = client.users.get_contributors()
        print(f"✅ Contributors: {len(contributors)}")
        
        # Get user permissions (for first user)
        if owners:
            user_id = owners[0]['id']
            print(f"\nGetting permissions for user: {owners[0]['name']}")
            permissions = client.users.get_user_permissions(user_id)
            print(f"✅ User has {len(permissions)} permissions")
        
    except GhostAPIError as e:
        print(f"❌ Error managing roles and permissions: {e}")


def user_search_and_filtering(client: GhostClient):
    """Demonstrate user search and filtering capabilities."""
    print("\n🔍 User Search and Filtering")
    print("=" * 50)
    
    try:
        # Search users by email domain
        print("Searching for users by email pattern...")
        users_response = client.users.list(filter_="email:~gmail.com")
        gmail_users = users_response.get('users', [])
        print(f"✅ Found {len(gmail_users)} users with Gmail addresses")
        
        # Get active users only
        print(f"\nGetting active users...")
        active_users = client.users.get_active_users()
        print(f"✅ Found {len(active_users)} active users")
        
        # Search by specific email
        all_users = client.users.list()
        if all_users.get('users'):
            test_email = all_users['users'][0]['email']
            print(f"\nSearching for user by email: {test_email}")
            user = client.users.get_by_email(test_email)
            
            if user:
                print(f"✅ Found user: {user['name']}")
            else:
                print("❌ User not found")
        
        # Search by slug
        if all_users.get('users'):
            test_slug = all_users['users'][0]['slug']
            print(f"\nSearching for user by slug: {test_slug}")
            user = client.users.get_by_slug(test_slug)
            
            if user:
                print(f"✅ Found user: {user['name']}")
            else:
                print("❌ User not found")
        
        # Get users with post counts
        print(f"\nGetting users with post statistics...")
        authors_with_posts = client.users.list(
            include="count.posts",
            order="count.posts desc",
            limit=5
        )
        
        print(f"✅ Top content creators:")
        for user in authors_with_posts.get('users', []):
            post_count = user.get('count', {}).get('posts', 0)
            if post_count > 0:
                print(f"   • {user['name']}: {post_count} posts")
        
    except GhostAPIError as e:
        print(f"❌ Error searching users: {e}")


def notification_settings_management(client: GhostClient, user_data: Dict):
    """Demonstrate notification settings management."""
    print("\n🔔 Notification Settings Management")
    print("=" * 50)
    
    user_id = user_data['id']
    
    try:
        # Update notification preferences
        print(f"Updating notification settings for: {user_data['name']}")
        updated_user = client.users.update_notification_settings(
            user_id,
            comment_notifications=True,
            mention_notifications=True,
            milestone_notifications=False,
            free_member_signup_notification=True,
            paid_subscription_started_notification=True,
            paid_subscription_canceled_notification=False
        )
        
        print(f"✅ Updated notification settings:")
        print(f"   Comment notifications: {updated_user.get('comment_notifications', 'N/A')}")
        print(f"   Mention notifications: {updated_user.get('mention_notifications', 'N/A')}")
        print(f"   Milestone notifications: {updated_user.get('milestone_notifications', 'N/A')}")
        print(f"   Member signup notifications: {updated_user.get('free_member_signup_notification', 'N/A')}")
        print(f"   Subscription notifications: {updated_user.get('paid_subscription_started_notification', 'N/A')}")
        
    except GhostAPIError as e:
        print(f"❌ Error updating notification settings: {e}")


def user_analytics_and_statistics(client: GhostClient):
    """Demonstrate user analytics and statistics."""
    print("\n📊 User Analytics and Statistics")
    print("=" * 50)
    
    try:
        # Get user statistics
        print("Getting user statistics...")
        stats = client.users.get_user_statistics()
        
        print(f"✅ User Statistics:")
        print(f"   Total Users: {stats['total']}")
        print(f"   Owners: {stats['owners']}")
        print(f"   Administrators: {stats['administrators']}")
        print(f"   Editors: {stats['editors']}")
        print(f"   Authors: {stats['authors']}")
        print(f"   Contributors: {stats['contributors']}")
        
        # Get user activity overview
        print(f"\nGetting user activity overview...")
        active_authors = client.users.list(
            filter_="role:author+status:active",
            include="count.posts",
            order="last_seen desc",
            limit=5
        )
        
        print(f"✅ Recent Author Activity:")
        for user in active_authors.get('users', []):
            post_count = user.get('count', {}).get('posts', 0)
            last_seen = user.get('last_seen', 'Never')
            if last_seen != 'Never':
                last_seen = last_seen[:10]  # Just the date part
            print(f"   • {user['name']}: {post_count} posts, last seen {last_seen}")
        
        # Get content creation statistics
        print(f"\nContent creation overview...")
        all_users = client.users.list(include="count.posts")
        total_posts = sum(user.get('count', {}).get('posts', 0) for user in all_users.get('users', []))
        active_creators = len([u for u in all_users.get('users', []) if u.get('count', {}).get('posts', 0) > 0])
        
        print(f"✅ Content Statistics:")
        print(f"   Total posts across all users: {total_posts}")
        print(f"   Users with published content: {active_creators}")
        print(f"   Average posts per active creator: {total_posts / active_creators if active_creators > 0 else 0:.1f}")
        
    except GhostAPIError as e:
        print(f"❌ Error getting analytics: {e}")


def error_handling_examples(client: GhostClient):
    """Demonstrate proper error handling."""
    print("\n⚠️  Error Handling Examples")
    print("=" * 50)
    
    # Try to get non-existent user
    try:
        print("Attempting to get non-existent user...")
        client.users.get("non-existent-user-id")
    except Exception as e:
        print(f"✅ Caught error for non-existent user (expected): {type(e).__name__}")
    
    # Try to update with invalid email
    try:
        # Get a real user first
        users = client.users.list(limit=1)
        if users.get('users'):
            user_id = users['users'][0]['id']
            print("Attempting to update user with invalid email...")
            client.users.update(user_id, email="invalid-email-format")
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except Exception as e:
        print(f"✅ Caught error for invalid email (expected): {type(e).__name__}")
    
    # Try to delete owner (should fail)
    try:
        owners = client.users.get_owners()
        if owners:
            print("Attempting to delete site owner (should fail)...")
            client.users.delete(owners[0]['id'])
    except Exception as e:
        print(f"✅ Caught error trying to delete owner (expected): {type(e).__name__}")


def user_profile_examples(client: GhostClient):
    """Show examples of different user profile configurations."""
    print("\n👥 User Profile Examples")
    print("=" * 50)
    
    try:
        # Get users and show different profile configurations
        users = client.users.list(include="roles,count.posts")
        users_list = users.get('users', [])
        
        print("✅ User Profile Examples:")
        
        for user in users_list[:3]:  # Show first 3 users
            roles = [role['name'] for role in user.get('roles', [])]
            post_count = user.get('count', {}).get('posts', 0)
            
            print(f"\n   📝 {user['name']}")
            print(f"      Email: {user['email']}")
            print(f"      Slug: {user['slug']}")
            print(f"      Role(s): {', '.join(roles)}")
            print(f"      Posts: {post_count}")
            print(f"      Bio: {user.get('bio', 'No bio set')[:60]}...")
            print(f"      Website: {user.get('website', 'Not set')}")
            print(f"      Location: {user.get('location', 'Not set')}")
            
            # Social media
            social_media = []
            if user.get('twitter'):
                social_media.append(f"Twitter: @{user['twitter']}")
            if user.get('facebook'):
                social_media.append(f"Facebook: {user['facebook']}")
            
            if social_media:
                print(f"      Social: {', '.join(social_media)}")
            
            # SEO
            if user.get('meta_title') or user.get('meta_description'):
                print(f"      SEO Title: {user.get('meta_title', 'Not set')}")
                print(f"      SEO Description: {user.get('meta_description', 'Not set')[:40]}...")
        
    except GhostAPIError as e:
        print(f"❌ Error getting user profiles: {e}")


def main():
    """Main function to run all user examples."""
    print("👥 PyGhost Users Module Examples")
    print("=" * 60)
    
    # Initialize client
    client = setup_client()
    if not client:
        return
    
    try:
        # Basic operations
        first_user = basic_user_operations(client)
        
        # Profile management
        if first_user:
            user_profile_management(client, first_user)
            
            # Notification settings
            notification_settings_management(client, first_user)
        
        # Roles and permissions
        user_roles_and_permissions(client)
        
        # Search and filtering
        user_search_and_filtering(client)
        
        # Analytics
        user_analytics_and_statistics(client)
        
        # Profile examples
        user_profile_examples(client)
        
        # Error handling
        error_handling_examples(client)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
    
    print("\n✅ Users module examples completed!")
    print("\nNext steps:")
    print("• Explore the Users module documentation")
    print("• Check out other PyGhost modules (Members, Images, Posts, etc.)")
    print("• Build your own user management workflows")
    print("\n⚠️  Note: Many user management operations require Admin or Owner permissions")


if __name__ == "__main__":
    main()
