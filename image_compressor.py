from PIL import Image
import os


class ImageCompressor:
    def __init__(self, quality: int = 80) -> None:
        """
        Initialize the ImageCompressor with a specified quality.

        :param quality: compression quality (from 0 to 100)
        """
        self.quality = quality

    def compress_jpg(self, input_path: str, output_path: str) -> None:
        """
        Compress an image in JPEG format.

        :param input_path: path to the input file
        :param output_path: path to the output file
        """
        try:
            # Check if the directory for the output file exists
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print(f"Created directory: {output_dir}")

            # Open the input image and compress it
            with Image.open(input_path) as img:
                convert = img.convert("RGB")
                convert.save(output_path, "JPEG", quality=self.quality)
            print(f"Image successfully compressed and saved at: {output_path}")
        except Exception as e:
            print(f"Error during image compression: {e}")

    def compress_jpg_files(self, input_path: str, output_dir: str) -> None:
        """
        Compress multiple images in a directory or a single image.

        :param input_path: path to the input file or directory
        :param output_dir: path to the output directory
        """
        if os.path.isdir(input_path):
            # Process all files in the directory
            for filename in os.listdir(input_path):
                file_path = os.path.join(input_path, filename)
                if os.path.isfile(file_path):
                    name, ext = os.path.splitext(filename)
                    output_path = os.path.join(output_dir, f"{name}.jpg")
                    self.compress_jpg(file_path, output_path)

        # Process a single file
        if os.path.isfile(input_path):
            name, ext = os.path.splitext(os.path.basename(input_path))
            output_path = os.path.join(output_dir, f"{name}.jpg")
            self.compress_jpg(input_path, output_path)

        print(f"Input path {input_path} is neither a file nor a directory.")
