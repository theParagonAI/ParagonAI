import unittest
from PIL import Image
from models.generator import AvatarGenerator

class TestAvatarGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AvatarGenerator()

    def test_generate_avatar(self):
        theme = "futuristic"
        style = "pixel art"
        avatar = self.generator.generate_avatar(theme, style)
        self.assertIsInstance(avatar, Image.Image)
        self.assertEqual(avatar.size, (512, 512))
        print("Avatar generated successfully!")

    def test_invalid_generate_avatar(self):
        theme = ""
        style = ""
        with self.assertRaises(Exception):
            self.generator.generate_avatar(theme, style)

if __name__ == "__main__":
    unittest.main()
