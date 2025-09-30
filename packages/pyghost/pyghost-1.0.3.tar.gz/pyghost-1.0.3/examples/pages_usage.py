#!/usr/bin/env python3
"""
Pages Usage Examples

This example demonstrates how to use the Pages module of PyGhost
to manage static pages on your Ghost site.
"""

import os
from datetime import datetime, timedelta
from pyghost import GhostClient

# Initialize the client
# Replace with your actual Ghost site URL and Admin API key
SITE_URL = os.getenv("GHOST_SITE_URL", "https://your-site.ghost.io")
ADMIN_API_KEY = os.getenv("GHOST_ADMIN_API_KEY", "your_key:your_secret")

client = GhostClient(site_url=SITE_URL, admin_api_key=ADMIN_API_KEY)


def create_page_examples() -> None:
    """Demonstrate creating different types of pages"""
    print("=== Creating Pages ===")
    
    try:
        # Create a basic page with HTML content
        about_page = client.pages.create(
            title="About Us",
            html="<h1>About Our Company</h1><p>We are a leading technology company...</p>",
            slug="about",
            meta_title="About Us - Company Information",
            meta_description="Learn more about our company, mission, and values.",
            tags=["company", "information"]
        )
        print(f"✅ Created about page: {about_page['title']}")
        
        # Create a page with Lexical JSON content
        privacy_page = client.pages.create(
            title="Privacy Policy",
            lexical='{"root":{"children":[{"children":[{"detail":0,"format":0,"mode":"normal","style":"","text":"Privacy Policy","type":"text","version":1}],"direction":"ltr","format":"","indent":0,"type":"heading","version":1,"tag":"h1"}],"direction":"ltr","format":"","indent":0,"type":"root","version":1}}',
            slug="privacy-policy",
            meta_title="Privacy Policy",
            visibility="public"
        )
        print(f"✅ Created privacy page: {privacy_page['title']}")
        
        # Create a page with custom excerpt and feature image
        services_page = client.pages.create(
            title="Our Services",
            html="<h1>Services We Offer</h1><p>Comprehensive solutions for your business needs.</p>",
            slug="services",
            excerpt="Discover the wide range of services we provide to help your business grow.",
            feature_image="https://example.com/services-hero.jpg",
            featured=True,
            tags=["services", "business"]
        )
        print(f"✅ Created services page: {services_page['title']}")
        
        return about_page, privacy_page, services_page
        
    except Exception as e:
        print(f"❌ Error creating pages: {e}")
        return None, None, None


def list_pages_examples() -> None:
    """Demonstrate different ways to list pages"""
    print("\n=== Listing Pages ===")
    
    try:
        # Get all pages
        all_pages = client.pages.list()
        print(f"📄 Total pages: {len(all_pages.get('pages', []))}")
        
        # Get only published pages
        published_pages = client.pages.list(filter_="status:published")
        print(f"📄 Published pages: {len(published_pages.get('pages', []))}")
        
        # Get pages with specific tags
        tagged_pages = client.pages.list(filter_="tag:company")
        print(f"📄 Pages tagged 'company': {len(tagged_pages.get('pages', []))}")
        
        # Get pages ordered by title
        ordered_pages = client.pages.list(order="title asc", limit=5)
        print("📄 Pages ordered by title:")
        for page in ordered_pages.get('pages', []):
            print(f"   - {page['title']}")
            
    except Exception as e:
        print(f"❌ Error listing pages: {e}")


def update_page_examples() -> None:
    """Demonstrate updating pages"""
    print("\n=== Updating Pages ===")
    
    try:
        # Get a page to update
        pages_list = client.pages.list(limit=1)
        if not pages_list.get('pages'):
            print("⚠️  No pages found to update")
            return
            
        page = pages_list['pages'][0]
        page_id = page['id']
        
        # Update page content and metadata
        updated_page = client.pages.update(
            page_id=page_id,
            title=f"{page['title']} (Updated)",
            html=f"{page.get('html', '')}<p><em>Last updated: {datetime.now().strftime('%Y-%m-%d')}</em></p>",
            meta_description="Updated page with new information and content.",
            updated_at=page['updated_at']  # Required for updates
        )
        print(f"✅ Updated page: {updated_page['title']}")
        
        # Update page tags
        updated_tags = client.pages.update(
            page_id=page_id,
            tags=["updated", "example"],
            updated_at=updated_page['updated_at']
        )
        print(f"✅ Updated page tags")
        
    except Exception as e:
        print(f"❌ Error updating page: {e}")


def publish_schedule_examples() -> None:
    """Demonstrate publishing and scheduling pages"""
    print("\n=== Publishing and Scheduling ===")
    
    try:
        # Create a draft page first
        draft_page = client.pages.create(
            title="Future Announcement",
            html="<h1>Coming Soon</h1><p>Exciting news will be announced here.</p>",
            slug="future-announcement",
            status="draft"
        )
        print(f"✅ Created draft page: {draft_page['title']}")
        
        # Publish the page immediately
        published_page = client.pages.publish(draft_page['id'])
        print(f"✅ Published page: {published_page['title']}")
        
        # Create another draft and schedule it
        scheduled_page = client.pages.create(
            title="Scheduled Update",
            html="<h1>Scheduled Content</h1><p>This content is scheduled for future publication.</p>",
            slug="scheduled-update",
            status="draft"
        )
        
        # Schedule for publication in 1 hour
        future_time = datetime.now() + timedelta(hours=1)
        scheduled_result = client.pages.schedule(
            scheduled_page['id'], 
            published_at=future_time.isoformat()
        )
        print(f"✅ Scheduled page for: {future_time.strftime('%Y-%m-%d %H:%M')}")
        
        # Unpublish a page (revert to draft)
        unpublished_page = client.pages.unpublish(published_page['id'])
        print(f"✅ Unpublished page: {unpublished_page['title']}")
        
    except Exception as e:
        print(f"❌ Error with publishing/scheduling: {e}")


def advanced_page_operations() -> None:
    """Demonstrate advanced page operations"""
    print("\n=== Advanced Operations ===")
    
    try:
        # Get page by slug
        about_page = client.pages.get_by_slug("about")
        if about_page:
            print(f"✅ Found page by slug: {about_page['title']}")
        
        # Get published pages only
        published_pages = client.pages.get_published_pages()
        print(f"✅ Published pages count: {len(published_pages)}")
        
        # Get draft pages only
        draft_pages = client.pages.get_draft_pages()
        print(f"✅ Draft pages count: {len(draft_pages)}")
        
        # Copy a page (create duplicate)
        if published_pages:
            source_page = published_pages[0]
            copied_page = client.pages.copy_page(
                source_page['id'],
                new_title=f"Copy of {source_page['title']}",
                new_slug=f"copy-{source_page['slug']}"
            )
            print(f"✅ Copied page: {copied_page['title']}")
        
    except Exception as e:
        print(f"❌ Error in advanced operations: {e}")


def cleanup_examples() -> None:
    """Clean up example pages"""
    print("\n=== Cleanup ===")
    
    try:
        # Get pages created in this example
        example_pages = client.pages.list(filter_="slug:about,privacy-policy,services,future-announcement,scheduled-update")
        
        for page in example_pages.get('pages', []):
            try:
                client.pages.delete(page['id'])
                print(f"🗑️  Deleted page: {page['title']}")
            except Exception as e:
                print(f"⚠️  Could not delete {page['title']}: {e}")
                
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")


def main() -> None:
    """Run all page examples"""
    print("🚀 PyGhost Pages Module Examples")
    print("=" * 40)
    
    try:
        # Run examples
        create_page_examples()
        list_pages_examples()
        update_page_examples()
        publish_schedule_examples()
        advanced_page_operations()
        
        # Optionally clean up (uncomment to clean up)
        # cleanup_examples()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("Make sure you have:")
        print("1. Set GHOST_SITE_URL environment variable")
        print("2. Set GHOST_ADMIN_API_KEY environment variable")
        print("3. Valid Ghost Admin API credentials")


if __name__ == "__main__":
    main()
