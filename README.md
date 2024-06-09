Image Compression Project
This project provides tools for compressing images in JPEG format using Python. It includes:

1.image_compressor.py: Contains the ImageCompressor class with methods for compressing
single images and directories of images using the Pillow library.

  - compress_jpg(input_path, output_path): Compresses a single image.
  - compress_jpg_files(input_path, output_dir): Compresses all images in a specified directory or a single image file.
  
2.main.py: Demonstrates how to use the ImageCompressor class to compress images.

Features:
  - Efficient image compression with customizable quality.
  - Handles both individual files and directories of images.

Usage:
  - Clone the repository.
  - Modify main.py with your input and output paths.
  - Run main.py to compress your images.

Requirements:
  - Python
  - Pillow library

Example:
  - compressor = ImageCompressor(quality=17)
  - compressor.compress_jpg_files(input_path, output_dir)
