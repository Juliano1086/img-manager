# Img-Manager

Img-Manager is a lightweight Python command-line utility designed to simplify image management tasks. It can recursively scan directories, convert PNG, JPG, and JPEG images to the WebP format, and optionally delete the original image files.

This tool is ideal for developers, website owners, and content creators who need a quick way to optimize image collections and reduce storage usage.

## Features

* Recursively scans directories and subdirectories
* Converts PNG, JPG, and JPEG images to WebP
* Displays conversion progress in real time
* Optionally deletes original image files
* Automatically installs Pillow if not available
* Simple interactive command-line interface
* Works on Windows, Linux, and macOS

## Requirements

* Python 3.8 or higher

## Install Dependencies

Before running the script, install the required packages:

```bash
pip install pillow pyfiglet
```

## Usage

Run the script:

```bash
python img_manager.py
```

You will see the following menu:

```text
1. Convert PNG/JPG to WebP
2. Delete PNG/JPG files
3. Exit
```

Enter the path to the directory you want to process when prompted.

## Example

```text
Select an option (1-3): 1
Enter the directory path: C:\Images

Found 25 image file(s) to convert.

[20.0%] Converted: image1.jpg
[40.0%] Converted: image2.png
...
```

## Why Use WebP?

WebP images typically provide:

* Smaller file sizes
* Faster website loading times
* Reduced storage consumption
* Better performance for web applications

## Author

Created by Juliano1086

## License

MIT License
