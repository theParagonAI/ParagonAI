from PIL import Image, ImageFilter

class StyleTransfer:
    def __init__(self):
        self.available_styles = ["pixel art", "watercolor", "sketch", "oil painting"]

    def apply_style(self, image, style):
        if style not in self.available_styles:
            raise ValueError(f"Style '{style}' is not supported.")
        
        print(f"Applying '{style}' style to the avatar...")
        if style == "pixel art":
            return image.resize((64, 64)).resize(image.size, resample=Image.NEAREST)
        elif style == "watercolor":
            return image.filter(ImageFilter.BLUR)
        elif style == "sketch":
            return image.filter(ImageFilter.CONTOUR)
        elif style == "oil painting":
            return image.filter(ImageFilter.EDGE_ENHANCE)
        else:
            return image
