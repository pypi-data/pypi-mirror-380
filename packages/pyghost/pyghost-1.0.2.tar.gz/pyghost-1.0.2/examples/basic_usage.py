#!/usr/bin/env python3
"""
Basic usage examples for PyGhost library

This example demonstrates the fundamental operations:
- Creating posts with different content types
- Reading and listing posts
- Updating posts
- Publishing and scheduling
"""

import json
import os
from datetime import datetime, timedelta

# Add parent directory to path for imports
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyghost import GhostClient
from pyghost.exceptions import GhostAPIError, ValidationError


def main() -> None:
    # Configuration - replace with your actual values
    SITE_URL = "https://your-site.ghost.io"  # Replace with your Ghost site URL
    API_KEY = "your_key_id:your_secret_hex"  # Replace with your Admin API key
    
    # Initialize the client
    try:
        client = GhostClient(site_url=SITE_URL, admin_api_key=API_KEY)
        print("✅ Ghost client initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize client: {e}")
        return
    
    # Example 1: Create a simple draft post with Lexical content
    print("\n📝 Creating a draft post...")
    
    # Simple Lexical content structure
    lexical_content = {
        "root": {
            "children": [
                {
                    "children": [
                        {
                            "detail": 0,
                            "format": 0,
                            "mode": "normal",
                            "style": "",
                            "text": "Welcome to PyGhost! This is a sample post created using the PyGhost library.",
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
    }
    
    try:
        draft_post = client.posts.create(
            title="My First PyGhost Post",
            content=json.dumps(lexical_content),
            content_type="lexical",
            status="draft",
            tags=["python", "ghost", "api", "tutorial"],
            excerpt="This is a sample post created with PyGhost library"
        )
        print(f"✅ Created draft post: '{draft_post['title']}' (ID: {draft_post['id']})")
        
        # Save the post ID for later examples
        post_id = draft_post['id']
        updated_at = draft_post['updated_at']
        
    except ValidationError as e:
        print(f"❌ Validation error creating post: {e}")
        return
    except GhostAPIError as e:
        print(f"❌ API error creating post: {e}")
        return
    
    # Example 2: Create an HTML post and publish immediately
    print("\n📄 Creating and publishing an HTML post...")
    
    html_content = """
    <h2>PyGhost HTML Example</h2>
    <p>This post was created with <strong>HTML content</strong> and published immediately.</p>
    <ul>
        <li>Easy to use API</li>
        <li>Modular design</li>
        <li>Full error handling</li>
    </ul>
    <p>Check out the <a href="https://github.com/your-username/pyghost">PyGhost repository</a> for more information!</p>
    """
    
    try:
        html_post = client.posts.create(
            title="PyGhost HTML Example",
            content=html_content.strip(),
            content_type="html",
            status="published",
            tags=["html", "example"],
            featured=True,
            excerpt="An example post using HTML content with PyGhost"
        )
        print(f"✅ Created and published HTML post: '{html_post['title']}' (ID: {html_post['id']})")
        
    except GhostAPIError as e:
        print(f"❌ Error creating HTML post: {e}")
    
    # Example 3: Read and list posts
    print("\n📋 Listing recent posts...")
    
    try:
        # Get the latest 5 posts
        posts_response = client.posts.list(limit=5, include="tags,authors")
        posts = posts_response.get('posts', [])
        
        print(f"Found {len(posts)} posts:")
        for post in posts:
            status_emoji = {"published": "🟢", "draft": "🟡", "scheduled": "🟠"}.get(post['status'], "⚪")
            tags_list = [tag['name'] for tag in post.get('tags', [])]
            tags_str = f" (Tags: {', '.join(tags_list)})" if tags_list else ""
            print(f"  {status_emoji} {post['title']} - {post['status']}{tags_str}")
            
    except GhostAPIError as e:
        print(f"❌ Error listing posts: {e}")
    
    # Example 4: Update the draft post
    print(f"\n✏️ Updating the draft post (ID: {post_id})...")
    
    try:
        updated_post = client.posts.update(
            post_id=post_id,
            updated_at=updated_at,
            title="My Updated PyGhost Post",
            content=json.dumps({
                "root": {
                    "children": [
                        {
                            "children": [
                                {
                                    "detail": 0,
                                    "format": 0,
                                    "mode": "normal",
                                    "style": "",
                                    "text": "This post has been updated! PyGhost makes it easy to modify your content programmatically.",
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
            }),
            tags=["python", "ghost", "api", "updated"]
        )
        print(f"✅ Updated post: '{updated_post['title']}'")
        
        # Update the timestamp for next operations
        updated_at = updated_post['updated_at']
        
    except GhostAPIError as e:
        print(f"❌ Error updating post: {e}")
    
    # Example 5: Schedule the post for future publication
    print(f"\n⏰ Scheduling the post for publication...")
    
    try:
        # Schedule for 1 hour from now
        future_date = datetime.now() + timedelta(hours=1)
        
        scheduled_post = client.posts.schedule(
            post_id=post_id,
            updated_at=updated_at,
            publish_at=future_date
        )
        print(f"✅ Scheduled post for: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Update timestamp
        updated_at = scheduled_post['updated_at']
        
    except GhostAPIError as e:
        print(f"❌ Error scheduling post: {e}")
    
    # Example 6: Publish the post immediately
    print(f"\n🚀 Publishing the post immediately...")
    
    try:
        published_post = client.posts.publish(
            post_id=post_id,
            updated_at=updated_at
        )
        print(f"✅ Published post: '{published_post['title']}'")
        print(f"   URL: {published_post.get('url', 'N/A')}")
        
    except GhostAPIError as e:
        print(f"❌ Error publishing post: {e}")
    
    print("\n🎉 Basic usage examples completed!")
    print("\n💡 Next steps:")
    print("   - Replace SITE_URL and API_KEY with your actual values")
    print("   - Explore the other example files for more advanced usage")
    print("   - Check the README.md for complete API reference")


if __name__ == "__main__":
    main()
