import os
import sys
from pathlib import Path
import sys

# Optional dependencies: handle missing packages with a clear message
try:
    from PIL import Image
except ModuleNotFoundError:
    # Try to install Pillow automatically
    print("'Pillow' library not found. Attempting to install automatically...")
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        from PIL import Image
        print("Pillow installed successfully.")
    except Exception:
        print("Error: failed to install 'Pillow'. Please install manually with: pip install pillow")
        sys.exit(1)

try:
    import pyfiglet
except ModuleNotFoundError:
    print("Warning: 'pyfiglet' library not found. ASCII banner will be omitted. Install with: pip install pyfiglet")
    pyfiglet = None

def convert_to_webp(directory_path):
    """Convert all PNG and JPG images in directory and subdirectories to WebP format."""
    
    # Validate directory path
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return
    
    # Find all PNG and JPG files recursively
    extensions = ['*.png', '*.jpg', '*.jpeg']
    image_files = []
    for ext in extensions:
        image_files.extend(list(Path(directory_path).rglob(ext)))
    
    if not image_files:
        print("No PNG or JPG files found in the specified directory.")
        return
    
    total_files = len(image_files)
    print(f"\nFound {total_files} image file(s) to convert.\n")
    
    successful = 0
    failed = 0
    
    for index, img_file in enumerate(image_files, 1):
        try:
            # Open image
            img = Image.open(img_file)
            
            # Create output path with .webp extension
            webp_file = img_file.with_suffix('.webp')
            
            # Convert and save as WebP
            img.convert('RGB').save(webp_file, 'WEBP', quality=80)
            
            successful += 1
            
            # Calculate and display progress
            percentage = (index / total_files) * 100
            print(f"[{percentage:.1f}%] Converted: {img_file.name}")
            
        except Exception as e:
            failed += 1
            print(f"[Error] Failed to convert {img_file.name}: {str(e)}")
    
    # Display final summary
    print(f"\n{'='*50}")
    print(f"Conversion Complete!")
    print(f"Successfully converted: {successful}/{total_files}")
    print(f"Failed: {failed}/{total_files}")
    print(f"{'='*50}\n")

def delete_image_files(directory_path):
    """Delete all PNG and JPG images in directory and subdirectories."""
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    extensions = ['*.png', '*.jpg', '*.jpeg']
    image_files = []
    for ext in extensions:
        image_files.extend(list(Path(directory_path).rglob(ext)))

    if not image_files:
        print("No PNG or JPG files found to delete.")
        return

    confirm = input(f"Are you sure you want to delete {len(image_files)} PNG/JPG files? (y/N): ").lower()
    if confirm != 'y':
        print("Operation cancelled.")
        return

    deleted = 0
    for img_file in image_files:
        try:
            os.remove(img_file)
            deleted += 1
            print(f"Deleted: {img_file.name}")
        except Exception as e:
            print(f"[Error] Failed to delete {img_file.name}: {str(e)}")

    print(f"\nDeletion Complete! {deleted} files removed.")

def main():
    if pyfiglet:
        ascii_banner = pyfiglet.figlet_format("Img-manager")
        print(ascii_banner)
    print("Version: 1.0")
    print("Created by: Juliano1086")
    print("-" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Convert PNG/JPG to WebP")
        print("2. Delete PNG/JPG files")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '3':
            break
        elif choice in ['1', '2']:
            directory_path = input("Enter the directory path: ").strip()
            if not os.path.isdir(directory_path):
                print(f"Error: Directory '{directory_path}' does not exist.")
                continue
            
            if choice == '1':
                convert_to_webp(directory_path)
            else:
                delete_image_files(directory_path)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
