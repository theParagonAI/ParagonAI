from PIL import Image

class OptimizationService:
    def __init__(self, compression_level=85):
        self.compression_level = compression_level

    def optimize_image(self, image, target_size=(256, 256)):
        """Resizes and compresses the image for optimization."""
        print("Optimizing image...")
        optimized_image = image.resize(target_size, Image.ANTIALIAS)
        return optimized_image

    def save_optimized_image(self, image, output_path, filename):
        """Saves the optimized image with compression."""
        filepath = os.path.join(output_path, filename)
        image.save(filepath, "JPEG", quality=self.compression_level)
        print(f"Optimized image saved at {filepath}")
        return filepath
