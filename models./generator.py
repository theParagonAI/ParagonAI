from PIL import Image, ImageDraw

class AvatarGenerator:
    def generate_avatar(self, theme, style):
        print(f"Generating avatar with theme '{theme}' and style '{style}'...")
        image = Image.new("RGB", (512, 512), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((100, 250), f"{theme} - {style}", fill=(0, 0, 0))
        return image
