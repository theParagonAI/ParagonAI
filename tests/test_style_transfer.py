import unittest
from PIL import Image
from models.style_transfer import StyleTransfer

class TestStyleTransfer(unittest.TestCase):
    def setUp(self):
        self.style_transfer = StyleTransfer()
        self.image = Image.new("RGB", (512, 512), color=(255, 200, 200))

    def test_apply_pixel_art_style(self):
        styled_image = self.style_transfer.apply_style(self.image, "pixel art")
        self.assertEqual(styled_image.size, (512, 512))
        print("Pixel art style applied successfully!")

    def test_apply_watercolor_style(self):
        styled_image = self.style_transfer.apply_style(self.image, "watercolor")
        self.assertIsNotNone(styled_image)
        print("Watercolor style applied successfully!")

    def test_invalid_style(self):
        with self.assertRaises(ValueError):
            self.style_transfer.apply_style(self.image, "nonexistent_style")

if __name__ == "__main__":
    unittest.main()
