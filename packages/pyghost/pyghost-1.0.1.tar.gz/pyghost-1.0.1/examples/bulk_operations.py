#!/usr/bin/env python3
"""
Bulk operations examples for PyGhost library

This example demonstrates:
- Creating multiple posts efficiently
- Bulk updating posts
- Content migration patterns
- Error handling for batch operations
"""

import json
import os
import sys
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyghost import GhostClient
from pyghost.exceptions import GhostAPIError


def create_lexical_content(text: str) -> str:
    """Helper function to create basic Lexical content"""
    return json.dumps({
        "root": {
            "children": [
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": text,
                            "type": "extended-text",
                            "version": 1
                        }
                    ],
                    "direction": "ltr",
                    "format": "",
                    "indent": 0,
                    "type": "paragraph",
                    "version": 1
                }
            ],
            "direction": "ltr",
            "format": "",
            "indent": 0,
            "type": "root",
            "version": 1
        }
    })


def main() -> None:
    # Configuration
    SITE_URL = "https://your-site.ghost.io"  # Replace with your Ghost site URL
    API_KEY = "your_key_id:your_secret_hex"  # Replace with your Admin API key
    
    try:
        client = GhostClient(site_url=SITE_URL, admin_api_key=API_KEY)
        print("✅ Ghost client initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize client: {e}")
        return
    
    # Example 1: Create multiple posts in sequence
    print("\n📚 Creating multiple posts...")
    
    posts_data = [
        {
            "title": "PyGhost Tutorial: Getting Started",
            "content": "Learn how to get started with PyGhost, the Python wrapper for Ghost Admin API.",
            "tags": ["tutorial", "python", "getting-started"],
            "status": "draft"
        },
        {
            "title": "PyGhost Tutorial: Advanced Usage",
            "content": "Explore advanced features of PyGhost including bulk operations and error handling.",
            "tags": ["tutorial", "python", "advanced"],
            "status": "draft"
        },
        {
            "title": "PyGhost Tutorial: Best Practices",
            "content": "Best practices for using PyGhost in production environments.",
            "tags": ["tutorial", "python", "best-practices"],
            "status": "draft"
        }
    ]
    
    created_posts = []
    
    for i, post_data in enumerate(posts_data, 1):
        try:
            post = client.posts.create(
                title=post_data["title"],
                content=create_lexical_content(post_data["content"]),
                content_type="lexical",
                status=post_data["status"],
                tags=post_data["tags"],
                excerpt=post_data["content"][:150] + "..." if len(post_data["content"]) > 150 else post_data["content"]
            )
            created_posts.append(post)
            print(f"  ✅ Created post {i}/3: '{post['title']}'")
            
        except GhostAPIError as e:
            print(f"  ❌ Failed to create post {i}/3: {e}")
            continue
    
    print(f"\n📊 Successfully created {len(created_posts)} out of {len(posts_data)} posts")
    
    # Example 2: Bulk update posts (publish all draft tutorial posts)
    print("\n🔄 Bulk updating tutorial posts...")
    
    try:
        # Find all tutorial posts that are drafts
        tutorial_posts = client.posts.list(
            filter_="tag:tutorial+status:draft",
            include="tags"
        )
        
        draft_tutorials = tutorial_posts.get('posts', [])
        print(f"Found {len(draft_tutorials)} draft tutorial posts")
        
        published_count = 0
        for post in draft_tutorials:
            try:
                updated_post = client.posts.publish(
                    post_id=post['id'],
                    updated_at=post['updated_at']
                )
                published_count += 1
                print(f"  ✅ Published: '{post['title']}'")
                
            except GhostAPIError as e:
                print(f"  ❌ Failed to publish '{post['title']}': {e}")
        
        print(f"\n📈 Successfully published {published_count} tutorial posts")
        
    except GhostAPIError as e:
        print(f"❌ Error retrieving tutorial posts: {e}")
    
    # Example 3: Schedule posts for a content calendar
    print("\n📅 Scheduling posts for content calendar...")
    
    try:
        # Get some draft posts to schedule
        draft_posts_response = client.posts.list(
            filter_="status:draft",
            limit=3
        )
        draft_posts = draft_posts_response.get('posts', [])
        
        if not draft_posts:
            print("No draft posts available for scheduling")
        else:
            base_date = datetime.now() + timedelta(days=1)
            
            for i, post in enumerate(draft_posts):
                try:
                    # Schedule each post 2 days apart
                    schedule_date = base_date + timedelta(days=i * 2)
                    
                    scheduled_post = client.posts.schedule(
                        post_id=post['id'],
                        updated_at=post['updated_at'],
                        publish_at=schedule_date
                    )
                    
                    print(f"  ⏰ Scheduled '{post['title']}' for {schedule_date.strftime('%Y-%m-%d')}")
                    
                except GhostAPIError as e:
                    print(f"  ❌ Failed to schedule '{post['title']}': {e}")
    
    except GhostAPIError as e:
        print(f"❌ Error retrieving draft posts: {e}")
    
    # Example 4: Content migration simulation
    print("\n🚚 Simulating content migration...")
    
    # Simulate importing content from an external source
    external_content = [
        {
            "title": "Migrated Post 1: Introduction to APIs",
            "html_content": "<h2>Welcome to APIs</h2><p>This post was migrated from another CMS.</p>",
            "published_date": "2024-01-15T10:00:00Z",
            "tags": ["migration", "api", "introduction"],
            "author_email": "migration@example.com"
        },
        {
            "title": "Migrated Post 2: Database Best Practices",
            "html_content": "<h2>Database Tips</h2><p>Essential database practices for developers.</p>",
            "published_date": "2024-01-16T14:30:00Z",
            "tags": ["migration", "database", "best-practices"],
            "author_email": "migration@example.com"
        }
    ]
    
    migrated_count = 0
    for content in external_content:
        try:
            # Create as published post with specific publication date
            post = client.posts.create(
                title=content["title"],
                content=content["html_content"],
                content_type="html",
                status="published",
                tags=content["tags"],
                authors=[content["author_email"]],
                published_at=content["published_date"]
            )
            
            migrated_count += 1
            print(f"  ✅ Migrated: '{content['title']}'")
            
        except GhostAPIError as e:
            print(f"  ❌ Failed to migrate '{content['title']}': {e}")
    
    print(f"\n📦 Successfully migrated {migrated_count} posts")
    
    # Example 5: Error handling and recovery
    print("\n🛡️ Demonstrating error handling...")
    
    # Simulate some error conditions
    error_scenarios = [
        {
            "name": "Invalid post ID",
            "action": lambda: client.posts.get("invalid-post-id")
        },
        {
            "name": "Empty title validation",
            "action": lambda: client.posts.create(title="", content="Test content")
        }
    ]
    
    for scenario in error_scenarios:
        try:
            scenario["action"]()
            print(f"  ⚠️ Expected error for '{scenario['name']}' but none occurred")
        except GhostAPIError as e:
            print(f"  ✅ Correctly handled '{scenario['name']}': {type(e).__name__}")
    
    print("\n🎉 Bulk operations examples completed!")
    print("\n💡 Tips for production use:")
    print("   - Implement proper retry logic with exponential backoff")
    print("   - Use rate limiting to avoid API limits")
    print("   - Always validate data before bulk operations")
    print("   - Keep track of operation results for rollback if needed")


if __name__ == "__main__":
    main()
