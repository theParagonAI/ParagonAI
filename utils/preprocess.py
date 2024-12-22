from PIL import Image

def resize_image(image, target_size=(512, 512)):
    """Resizes the input image to the target size."""
    print(f"Resizing image to {target_size}...")
    return image.resize(target_size, Image.ANTIALIAS)

def normalize_input(input_string):
    """Normalizes user input by trimming and converting to lowercase."""
    print(f"Normalizing input: '{input_string}'")
    return input_string.strip().lower()
