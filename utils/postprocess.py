from PIL import ImageEnhance

def enhance_image(image, brightness=1.2, contrast=1.2):
    """Enhances the brightness and contrast of the image."""
    print("Enhancing image brightness and contrast...")
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)
    return image

def add_watermark(image, text="Paragon AI"):
    """Adds a watermark to the image."""
    print("Adding watermark to the image...")
    width, height = image.size
    watermark_text = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark_text)
    text_size = width // 15
    draw.text(
        (width - text_size * 5, height - text_size),
        text,
        fill=(255, 255, 255, 128),
        align="right"
    )
    return Image.alpha_composite(image.convert("RGBA"), watermark_text)
