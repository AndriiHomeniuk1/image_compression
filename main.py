from image_compressor import ImageCompressor


input_path = ""  # specify file or a directory
output_dir = ""

# Create an instance of ImageCompressor with the desired quality
compressor = ImageCompressor(quality=17)

# Use the instance to compress the image or images in the directory
compressor.compress_jpg_files(input_path, output_dir)
