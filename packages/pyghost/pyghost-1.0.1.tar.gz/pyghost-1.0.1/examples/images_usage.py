#!/usr/bin/env python3
"""
Images Usage Examples - PyGhost

This script demonstrates comprehensive usage of the Images module for uploading
and managing images through the Ghost Admin API, including file validation,
multipart uploads, and batch operations.

Requirements:
- Set environment variables: GHOST_SITE_URL and GHOST_ADMIN_API_KEY
- Or modify the client initialization below with your actual credentials
- Sample image files for testing (will create test images if not available)

Example usage:
    python examples/images_usage.py
"""

import os
import sys
import tempfile
from typing import List, Dict
from io import BytesIO

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


def create_test_image(filename: str, width: int = 200, height: int = 200) -> str:
    """Create a simple test image for demonstration purposes."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Create a simple colored image with text
        image = Image.new('RGB', (width, height), color='lightblue')
        draw = ImageDraw.Draw(image)
        
        # Draw some simple shapes and text
        draw.rectangle([10, 10, width-10, height-10], outline='navy', width=3)
        draw.ellipse([width//4, height//4, 3*width//4, 3*height//4], fill='lightcoral', outline='darkred', width=2)
        
        # Add text
        try:
            font = ImageFont.load_default()
            text = "PyGhost\nTest Image"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = (width - text_width) // 2
            text_y = (height - text_height) // 2
            draw.text((text_x, text_y), text, fill='white', font=font)
        except:
            # Fallback if font loading fails
            draw.text((width//3, height//2), "PyGhost", fill='white')
        
        # Save to temp file
        temp_path = os.path.join(tempfile.gettempdir(), filename)
        image.save(temp_path, 'JPEG', quality=95)
        print(f"✅ Created test image: {temp_path}")
        return temp_path
        
    except ImportError:
        print("⚠️  PIL (Pillow) not available - creating simple text file as fallback")
        # Create a simple text file as fallback
        temp_path = os.path.join(tempfile.gettempdir(), filename.replace('.jpg', '.txt'))
        with open(temp_path, 'w') as f:
            f.write("This is a test file for PyGhost image upload demonstration.")
        return temp_path


def basic_image_upload(client: GhostClient) -> List[str]:
    """Demonstrate basic image upload operations."""
    print("\n📤 Basic Image Upload Operations")
    print("=" * 50)
    
    uploaded_urls = []
    
    try:
        # Create a test image
        test_image_path = create_test_image("pyghost_test_image.jpg")
        
        # Upload from file path
        print(f"Uploading image from file path...")
        result = client.images.upload(test_image_path)
        
        print(f"✅ Image uploaded successfully!")
        print(f"   URL: {result['url']}")
        print(f"   Reference: {result['ref']}")
        uploaded_urls.append(result['url'])
        
        # Upload from file object
        print(f"\nUploading image from file object...")
        with open(test_image_path, 'rb') as f:
            result2 = client.images.upload(f, "pyghost_file_object.jpg")
        
        print(f"✅ Image uploaded from file object!")
        print(f"   URL: {result2['url']}")
        print(f"   Reference: {result2['ref']}")
        uploaded_urls.append(result2['url'])
        
        # Clean up test file
        os.remove(test_image_path)
        
        return uploaded_urls
        
    except ValidationError as e:
        print(f"❌ Validation error: {e}")
        return uploaded_urls
    except GhostAPIError as e:
        print(f"❌ API error: {e}")
        return uploaded_urls
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return uploaded_urls


def image_validation_examples(client: GhostClient):
    """Demonstrate image validation features."""
    print("\n✅ Image Validation Examples")
    print("=" * 50)
    
    try:
        # Create test images with different properties
        test_files = []
        
        # Create a valid image
        valid_image = create_test_image("valid_image.jpg", 300, 200)
        test_files.append(valid_image)
        
        # Create a large image (for size validation demo)
        large_image = create_test_image("large_image.jpg", 800, 600)
        test_files.append(large_image)
        
        # Validate individual files
        print("Validating individual image files...")
        for i, file_path in enumerate(test_files):
            try:
                is_valid = client.images.validate_image_path(file_path)
                print(f"✅ File {i+1} validation: {is_valid}")
                
                # Get detailed file information
                info = client.images.get_image_info(file_path)
                print(f"   File: {info['filename']}")
                print(f"   Format: {info['format']}")
                print(f"   Size: {info['size_mb']} MB")
                print(f"   Supported: {info['is_supported']}")
                print(f"   Within size limit: {not info['exceeds_max_size']}")
                if 'width' in info and 'height' in info:
                    print(f"   Dimensions: {info['width']}x{info['height']}")
                
            except ValidationError as e:
                print(f"❌ File {i+1} validation failed: {e}")
        
        # Batch validation
        print(f"\nBatch validation of {len(test_files)} files...")
        batch_results = client.images.batch_validate(test_files)
        
        print(f"✅ Batch validation results:")
        print(f"   Total files: {batch_results['total_files']}")
        print(f"   Valid files: {batch_results['valid_count']}")
        print(f"   Invalid files: {batch_results['invalid_count']}")
        print(f"   Total size: {batch_results['total_size_mb']} MB")
        
        if batch_results['invalid']:
            print(f"   Invalid files:")
            for invalid in batch_results['invalid']:
                print(f"     • {invalid['path']}: {invalid['error']}")
        
        # Clean up test files
        for file_path in test_files:
            if os.path.exists(file_path):
                os.remove(file_path)
        
    except Exception as e:
        print(f"❌ Error in validation examples: {e}")


def multiple_image_upload(client: GhostClient) -> List[str]:
    """Demonstrate multiple image upload operations."""
    print("\n📤📤 Multiple Image Upload")
    print("=" * 50)
    
    uploaded_urls = []
    
    try:
        # Create multiple test images
        test_images = []
        for i in range(3):
            image_path = create_test_image(f"batch_image_{i+1}.jpg", 250 + i*50, 200 + i*30)
            test_images.append(image_path)
        
        print(f"Uploading {len(test_images)} images...")
        
        # Upload multiple images
        results = client.images.upload_multiple(test_images)
        
        print(f"✅ Successfully uploaded {len(results)} images:")
        for i, result in enumerate(results):
            print(f"   Image {i+1}:")
            print(f"     URL: {result['url']}")
            print(f"     Reference: {result['ref']}")
            uploaded_urls.append(result['url'])
        
        # Clean up test files
        for image_path in test_images:
            if os.path.exists(image_path):
                os.remove(image_path)
        
        return uploaded_urls
        
    except Exception as e:
        print(f"❌ Error uploading multiple images: {e}")
        return uploaded_urls


def url_upload_example(client: GhostClient) -> List[str]:
    """Demonstrate uploading images from URLs."""
    print("\n🌐 URL Upload Example")
    print("=" * 50)
    
    uploaded_urls = []
    
    # Test with a publicly available image URL
    test_urls = [
        "https://via.placeholder.com/300x200/4A90E2/FFFFFF?text=PyGhost+Test+1",
        "https://via.placeholder.com/400x250/50C878/FFFFFF?text=PyGhost+Test+2"
    ]
    
    for i, url in enumerate(test_urls):
        try:
            print(f"Uploading image from URL {i+1}: {url}")
            result = client.images.upload_from_url(url, f"url_image_{i+1}.png")
            
            print(f"✅ Image uploaded from URL!")
            print(f"   Original URL: {url}")
            print(f"   Ghost URL: {result['url']}")
            print(f"   Reference: {result['ref']}")
            uploaded_urls.append(result['url'])
            
        except Exception as e:
            print(f"❌ Error uploading from URL {i+1}: {e}")
    
    return uploaded_urls


def file_format_examples(client: GhostClient):
    """Demonstrate handling different file formats."""
    print("\n📁 File Format Examples")
    print("=" * 50)
    
    try:
        # Show supported formats
        print("Supported image formats:")
        for format_ext in sorted(client.images.SUPPORTED_FORMATS):
            content_type = client.images._get_content_type(f"test{format_ext}")
            print(f"   • {format_ext}: {content_type}")
        
        print(f"\nMaximum file size: {client.images.MAX_FILE_SIZE:,} bytes ({client.images.MAX_FILE_SIZE / (1024*1024):.1f} MB)")
        
        # Create test files with different formats
        test_formats = ['.jpg', '.png']  # Limit to formats we can easily create
        
        for format_ext in test_formats:
            try:
                print(f"\nTesting {format_ext.upper()} format...")
                
                if format_ext in ['.jpg', '.png']:
                    # Create test image
                    filename = f"format_test{format_ext}"
                    image_path = create_test_image(filename, 200, 150)
                    
                    # Get file info
                    info = client.images.get_image_info(image_path)
                    print(f"   File: {info['filename']}")
                    print(f"   Content-Type: {info['content_type']}")
                    print(f"   Size: {info['size_bytes']:,} bytes")
                    print(f"   Supported: {info['is_supported']}")
                    
                    # Upload the file
                    result = client.images.upload(image_path)
                    print(f"   ✅ Upload successful: {result['url']}")
                    
                    # Clean up
                    os.remove(image_path)
                
            except Exception as e:
                print(f"   ❌ Error with {format_ext}: {e}")
        
    except Exception as e:
        print(f"❌ Error in format examples: {e}")


def advanced_upload_features(client: GhostClient):
    """Demonstrate advanced upload features."""
    print("\n🚀 Advanced Upload Features")
    print("=" * 50)
    
    try:
        # Create a test image
        test_image = create_test_image("advanced_test.jpg", 400, 300)
        
        # Upload without validation (use with caution)
        print("Uploading without validation...")
        result = client.images.upload(test_image, validate=False)
        print(f"✅ Upload without validation successful: {result['url']}")
        
        # Demonstrate BytesIO upload
        print(f"\nUploading from BytesIO object...")
        
        # Read file into memory
        with open(test_image, 'rb') as f:
            image_data = f.read()
        
        # Create BytesIO object
        image_buffer = BytesIO(image_data)
        
        # Upload from buffer
        result2 = client.images.upload(image_buffer, "bytesio_image.jpg")
        print(f"✅ BytesIO upload successful: {result2['url']}")
        
        # Clean up
        os.remove(test_image)
        
    except Exception as e:
        print(f"❌ Error in advanced features: {e}")


def error_handling_examples(client: GhostClient):
    """Demonstrate comprehensive error handling."""
    print("\n⚠️  Error Handling Examples")
    print("=" * 50)
    
    # Test various error conditions
    
    # 1. Non-existent file
    try:
        print("Attempting to upload non-existent file...")
        client.images.upload("non_existent_file.jpg")
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except Exception as e:
        print(f"✅ Caught error (expected): {type(e).__name__}: {e}")
    
    # 2. File object without filename
    try:
        print("Attempting to upload file object without filename...")
        with open(__file__, 'rb') as f:  # Use this script as test file
            client.images.upload(f)  # Missing filename parameter
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except Exception as e:
        print(f"✅ Caught error (expected): {type(e).__name__}: {e}")
    
    # 3. Unsupported file format
    try:
        print("Attempting to upload unsupported file format...")
        # Create a text file
        temp_txt = os.path.join(tempfile.gettempdir(), "test.txt")
        with open(temp_txt, 'w') as f:
            f.write("This is not an image file")
        
        client.images.upload(temp_txt)
        os.remove(temp_txt)
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
        if os.path.exists(temp_txt):
            os.remove(temp_txt)
    except Exception as e:
        print(f"✅ Caught error (expected): {type(e).__name__}: {e}")
        if os.path.exists(temp_txt):
            os.remove(temp_txt)
    
    # 4. Empty file
    try:
        print("Attempting to upload empty file...")
        empty_file = os.path.join(tempfile.gettempdir(), "empty.jpg")
        open(empty_file, 'a').close()  # Create empty file
        
        client.images.upload(empty_file)
        os.remove(empty_file)
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
        if os.path.exists(empty_file):
            os.remove(empty_file)
    except Exception as e:
        print(f"✅ Caught error (expected): {type(e).__name__}: {e}")
        if os.path.exists(empty_file):
            os.remove(empty_file)
    
    # 5. Invalid URL
    try:
        print("Attempting to upload from invalid URL...")
        client.images.upload_from_url("not-a-valid-url")
    except ValidationError as e:
        print(f"✅ Caught validation error (expected): {e}")
    except Exception as e:
        print(f"✅ Caught error (expected): {type(e).__name__}: {e}")


def practical_usage_examples(uploaded_urls: List[str]):
    """Show practical usage examples with uploaded images."""
    print("\n💡 Practical Usage Examples")
    print("=" * 50)
    
    if not uploaded_urls:
        print("⚠️  No uploaded images available for practical examples")
        return
    
    print("Here are some practical ways to use your uploaded images:")
    
    # Show different usage contexts
    for i, url in enumerate(uploaded_urls[:3]):
        print(f"\n🖼️  Image {i+1}: {url}")
        
        # Post feature image example
        print(f"   📝 Use as post feature image:")
        print(f"      post_data = {{'feature_image': '{url}'}}")
        print(f"      client.posts.update(post_id, **post_data)")
        
        # Page cover image example
        print(f"   📄 Use as page cover image:")
        print(f"      page_data = {{'feature_image': '{url}'}}")
        print(f"      client.pages.update(page_id, **page_data)")
        
        # User profile image example
        print(f"   👤 Use as user profile image:")
        print(f"      user_data = {{'profile_image': '{url}'}}")
        print(f"      client.users.update(user_id, **user_data)")
        
        # HTML content example
        print(f"   📝 Use in post/page content:")
        print(f"      '<img src=\"{url}\" alt=\"Uploaded image\" />'")


def main() -> None:
    """Main function to run all image examples."""
    print("🖼️  PyGhost Images Module Examples")
    print("=" * 60)
    
    # Initialize client
    client = setup_client()
    if not client:
        return
    
    all_uploaded_urls = []
    
    try:
        # Basic upload operations
        basic_urls = basic_image_upload(client)
        all_uploaded_urls.extend(basic_urls)
        
        # Image validation
        image_validation_examples(client)
        
        # Multiple image upload
        multiple_urls = multiple_image_upload(client)
        all_uploaded_urls.extend(multiple_urls)
        
        # URL upload
        url_upload_urls = url_upload_example(client)
        all_uploaded_urls.extend(url_upload_urls)
        
        # File format examples
        file_format_examples(client)
        
        # Advanced features
        advanced_upload_features(client)
        
        # Error handling
        error_handling_examples(client)
        
        # Practical usage
        practical_usage_examples(all_uploaded_urls)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
    
    print("\n✅ Images module examples completed!")
    print(f"\n📊 Summary:")
    print(f"   • Uploaded {len(all_uploaded_urls)} images successfully")
    print(f"   • All images are now available in your Ghost media library")
    
    print("\nNext steps:")
    print("• Explore the Images module documentation")
    print("• Use uploaded images in your posts and pages")
    print("• Check out other PyGhost modules (Members, Users, Posts, etc.)")
    print("• Build your own media management workflows")
    
    if all_uploaded_urls:
        print(f"\n🔗 Your uploaded image URLs:")
        for i, url in enumerate(all_uploaded_urls):
            print(f"   {i+1}. {url}")


if __name__ == "__main__":
    main()
