#!/usr/bin/env python3
"""
PyGhost Themes Module - Comprehensive Usage Examples

This example demonstrates the complete functionality of the PyGhost Themes module
including theme upload, activation, validation, and management.

Requirements:
- Set GHOST_SITE_URL and GHOST_ADMIN_API_KEY environment variables
- Have a valid Ghost theme ZIP file for testing
- Admin permissions on your Ghost site

Example theme ZIP structure:
my-theme.zip
├── package.json
├── index.hbs
├── post.hbs
├── page.hbs
├── assets/
│   ├── css/
│   └── js/
└── partials/
"""

import os
import sys
import tempfile
import zipfile
import json
from datetime import datetime

# Add the parent directory to the path to import pyghost
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyghost import GhostClient
from pyghost.exceptions import GhostAPIError, ValidationError, AuthenticationError


def create_sample_theme_zip() -> str:
    """
    Create a sample Ghost theme ZIP file for demonstration purposes.
    
    Returns:
        str: Path to the created theme ZIP file
    """
    # Create a temporary directory for the theme
    with tempfile.TemporaryDirectory() as temp_dir:
        theme_dir = os.path.join(temp_dir, "sample-theme")
        os.makedirs(theme_dir)
        
        # Create package.json
        package_json = {
            "name": "pyghost-sample-theme",
            "description": "A sample theme created by PyGhost for demonstration",
            "version": "1.0.0",
            "engines": {
                "ghost": ">=5.0.0"
            },
            "keywords": ["ghost", "theme", "pyghost", "demo"],
            "author": "PyGhost Contributors",
            "config": {
                "posts_per_page": 5,
                "image_sizes": {
                    "xs": {"width": 150},
                    "s": {"width": 300},
                    "m": {"width": 600},
                    "l": {"width": 1000},
                    "xl": {"width": 2000}
                }
            }
        }
        
        with open(os.path.join(theme_dir, "package.json"), "w") as f:
            json.dump(package_json, f, indent=2)
        
        # Create basic template files
        templates = {
            "index.hbs": """<!DOCTYPE html>
<html>
<head>
    <title>{{@site.title}}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <header>
        <h1>{{@site.title}}</h1>
        <p>{{@site.description}}</p>
    </header>
    <main>
        {{#foreach posts}}
            <article>
                <h2><a href="{{url}}">{{title}}</a></h2>
                <p>{{excerpt}}</p>
                <time>{{date}}</time>
            </article>
        {{/foreach}}
    </main>
</body>
</html>""",
            
            "post.hbs": """<!DOCTYPE html>
<html>
<head>
    <title>{{title}} - {{@site.title}}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <article>
        <header>
            <h1>{{title}}</h1>
            <time>{{date}}</time>
            {{#if tags}}
                <div class="tags">
                    {{#foreach tags}}
                        <span class="tag">{{name}}</span>
                    {{/foreach}}
                </div>
            {{/if}}
        </header>
        <div class="content">
            {{content}}
        </div>
    </article>
</body>
</html>""",
            
            "page.hbs": """<!DOCTYPE html>
<html>
<head>
    <title>{{title}} - {{@site.title}}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <article>
        <header>
            <h1>{{title}}</h1>
        </header>
        <div class="content">
            {{content}}
        </div>
    </article>
</body>
</html>"""
        }
        
        # Write template files
        for filename, content in templates.items():
            with open(os.path.join(theme_dir, filename), "w") as f:
                f.write(content)
        
        # Create assets directory with a simple CSS file
        assets_dir = os.path.join(theme_dir, "assets", "css")
        os.makedirs(assets_dir)
        
        css_content = """
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    border-bottom: 1px solid #eee;
    padding-bottom: 20px;
    margin-bottom: 40px;
}

article {
    margin-bottom: 40px;
}

.tags {
    margin-top: 10px;
}

.tag {
    background: #f0f0f0;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.9em;
    margin-right: 8px;
}
"""
        
        with open(os.path.join(assets_dir, "style.css"), "w") as f:
            f.write(css_content)
        
        # Create the ZIP file
        zip_path = os.path.join(tempfile.gettempdir(), f"pyghost-sample-theme-{datetime.now().strftime('%Y%m%d-%H%M%S')}.zip")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(theme_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, theme_dir)
                    zipf.write(file_path, arcname)
        
        return zip_path


def demo_theme_validation():
    """Demonstrate theme validation functionality."""
    print("\n" + "="*60)
    print("THEME VALIDATION EXAMPLES")
    print("="*60)
    
    try:
        # Create a sample theme for validation
        print("📦 Creating sample theme for validation...")
        sample_theme_path = create_sample_theme_zip()
        print(f"✅ Created sample theme: {os.path.basename(sample_theme_path)}")
        
        # Initialize client for validation (doesn't require API connection)
        client = GhostClient("https://example.ghost.io", "dummy:key")
        
        # Validate theme structure
        print("\n🔍 Validating theme structure...")
        validation_result = client.themes.validate_theme_structure(sample_theme_path)
        print(f"✅ Theme validation successful!")
        print(f"   Valid: {validation_result['valid']}")
        print(f"   Templates found: {len(validation_result['templates'])}")
        
        # Get theme information
        print("\n📋 Extracting theme information...")
        theme_info = client.themes.get_theme_info(sample_theme_path)
        print(f"✅ Theme info extracted:")
        print(f"   Name: {theme_info['name']}")
        print(f"   Version: {theme_info['version']}")
        print(f"   Description: {theme_info['description']}")
        print(f"   Templates: {theme_info['template_count']}")
        if theme_info.get('author'):
            print(f"   Author: {theme_info['author']}")
        
        # Test format validation
        print("\n🔍 Testing format validation...")
        valid_formats = client.themes.get_supported_formats()
        print(f"📁 Supported formats: {', '.join(valid_formats)}")
        
        # Test various file formats
        test_files = ["theme.zip", "theme.tar.gz", "theme.rar", "theme.txt"]
        for test_file in test_files:
            is_valid = client.themes.validate_theme_format(test_file)
            status = "✅ Valid" if is_valid else "❌ Invalid"
            print(f"   {test_file}: {status}")
        
        # Clean up
        os.unlink(sample_theme_path)
        print(f"\n🧹 Cleaned up sample theme file")
        
    except Exception as e:
        print(f"⚠️  Theme validation demo failed: {e}")


def demo_theme_upload_and_management(client):
    """Demonstrate theme upload and management functionality."""
    print("\n" + "="*60)
    print("THEME UPLOAD AND MANAGEMENT EXAMPLES")
    print("="*60)
    
    try:
        # Create a sample theme for upload
        print("📦 Creating sample theme for upload...")
        sample_theme_path = create_sample_theme_zip()
        theme_name = os.path.basename(sample_theme_path).replace('.zip', '')
        print(f"✅ Created sample theme: {theme_name}")
        
        # Upload theme from file path
        print(f"\n📤 Uploading theme from file: {os.path.basename(sample_theme_path)}")
        uploaded_theme = client.themes.upload_from_file(sample_theme_path)
        print(f"✅ Theme uploaded successfully!")
        print(f"   Theme name: {uploaded_theme.get('name', 'Unknown')}")
        print(f"   Active: {uploaded_theme.get('active', False)}")
        
        if uploaded_theme.get('templates'):
            print(f"   Templates: {len(uploaded_theme['templates'])}")
            for template in uploaded_theme['templates'][:3]:  # Show first 3
                print(f"     - {template.get('filename', 'Unknown')}: {template.get('name', 'No name')}")
        
        # Activate the uploaded theme
        theme_name = uploaded_theme.get('name')
        if theme_name:
            print(f"\n🚀 Activating theme: {theme_name}")
            activated_theme = client.themes.activate(theme_name)
            print(f"✅ Theme activated successfully!")
            print(f"   Active status: {activated_theme.get('active', False)}")
        
        # Upload and activate in one step
        print(f"\n📤🚀 Uploading and activating theme in one step...")
        sample_theme_path_2 = create_sample_theme_zip()
        uploaded_and_activated = client.themes.upload_from_file(sample_theme_path_2, activate=True)
        print(f"✅ Theme uploaded and activated!")
        print(f"   Theme name: {uploaded_and_activated.get('name', 'Unknown')}")
        print(f"   Active: {uploaded_and_activated.get('active', False)}")
        
        # Clean up sample files
        os.unlink(sample_theme_path)
        os.unlink(sample_theme_path_2)
        print(f"\n🧹 Cleaned up sample theme files")
        
    except Exception as e:
        print(f"⚠️  Theme upload demo failed: {e}")
        print("   This might be due to permissions or Ghost site configuration")


def demo_theme_file_object_upload(client):
    """Demonstrate theme upload from file-like objects."""
    print("\n" + "="*60)
    print("THEME FILE OBJECT UPLOAD EXAMPLES")
    print("="*60)
    
    try:
        # Create a sample theme
        sample_theme_path = create_sample_theme_zip()
        
        # Upload from file object
        print("📤 Uploading theme from file object...")
        with open(sample_theme_path, 'rb') as theme_file:
            uploaded_theme = client.themes.upload_from_file_object(theme_file)
        
        print(f"✅ Theme uploaded from file object!")
        print(f"   Theme name: {uploaded_theme.get('name', 'Unknown')}")
        print(f"   Package info available: {'package' in uploaded_theme}")
        
        # Clean up
        os.unlink(sample_theme_path)
        print(f"\n🧹 Cleaned up sample theme file")
        
    except Exception as e:
        print(f"⚠️  File object upload demo failed: {e}")


def demo_advanced_theme_features():
    """Demonstrate advanced theme management features."""
    print("\n" + "="*60)
    print("ADVANCED THEME FEATURES")
    print("="*60)
    
    try:
        # Initialize client for utility functions
        client = GhostClient("https://example.ghost.io", "dummy:key")
        
        # Test backup functionality (will show not implemented message)
        print("💾 Testing theme backup functionality...")
        try:
            backup_path = client.themes.create_theme_backup("current-theme", "/tmp/")
        except NotImplementedError as e:
            print(f"ℹ️  {e}")
        
        # Show supported formats
        print(f"\n📁 Supported theme formats:")
        formats = client.themes.get_supported_formats()
        for fmt in formats:
            print(f"   • {fmt}")
        
        print(f"\n💡 Theme management tips:")
        print(f"   • Always backup your current theme before uploading a new one")
        print(f"   • Test themes on a staging site first")
        print(f"   • Ensure themes are compatible with your Ghost version")
        print(f"   • Validate theme structure before uploading")
        print(f"   • Use semantic versioning in your package.json")
        
    except Exception as e:
        print(f"⚠️  Advanced features demo failed: {e}")


def demo_error_handling():
    """Demonstrate error handling for theme operations."""
    print("\n" + "="*60)
    print("ERROR HANDLING EXAMPLES")
    print("="*60)
    
    try:
        # Initialize client
        client = GhostClient("https://example.ghost.io", "dummy:key")
        
        # Test file not found error
        print("🔍 Testing file not found error...")
        try:
            client.themes.upload_from_file("/nonexistent/theme.zip")
        except FileNotFoundError as e:
            print(f"✅ Correctly caught FileNotFoundError: {e}")
        
        # Test invalid file format
        print("\n🔍 Testing invalid file format...")
        try:
            client.themes.upload_from_file("invalid_theme.txt")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test empty theme name for activation
        print("\n🔍 Testing empty theme name for activation...")
        try:
            client.themes.activate("")
        except ValueError as e:
            print(f"✅ Correctly caught ValueError: {e}")
        
        # Test invalid theme structure validation
        print("\n🔍 Testing invalid theme validation...")
        # Create an invalid theme (empty ZIP)
        invalid_theme_path = os.path.join(tempfile.gettempdir(), "invalid_theme.zip")
        with zipfile.ZipFile(invalid_theme_path, 'w') as zipf:
            zipf.writestr("empty.txt", "This is not a valid theme")
        
        try:
            client.themes.validate_theme_structure(invalid_theme_path)
        except ValidationError as e:
            print(f"✅ Correctly caught ValidationError: {e}")
        finally:
            if os.path.exists(invalid_theme_path):
                os.unlink(invalid_theme_path)
        
    except Exception as e:
        print(f"⚠️  Error handling demo failed: {e}")


def main():
    """Main demonstration function."""
    print("🎨 PyGhost Themes Module - Comprehensive Usage Examples")
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
        demo_theme_validation()
        demo_advanced_theme_features()
        demo_error_handling()
        
        print("\n💡 To run upload and management examples, configure your Ghost API credentials.")
        return
    
    try:
        # Initialize the PyGhost client
        print(f"🚀 Initializing PyGhost client for {SITE_URL}...")
        client = GhostClient(site_url=SITE_URL, admin_api_key=API_KEY)
        print("✅ Client initialized successfully!")
        
        # Run all demonstrations
        demo_theme_validation()
        demo_theme_upload_and_management(client)
        demo_theme_file_object_upload(client)
        demo_advanced_theme_features()
        demo_error_handling()
        
        print("\n🎉 All theme examples completed successfully!")
        print("\n💡 Next steps:")
        print("   • Create your own custom Ghost themes")
        print("   • Use PyGhost to automate theme deployment")
        print("   • Integrate theme management into your CI/CD pipeline")
        print("   • Explore the Ghost theme development documentation")
        
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
