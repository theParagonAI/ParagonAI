import unittest
from PIL import Image, ImageDraw
from models.personalization import Personalization

class TestPersonalization(unittest.TestCase):
    def setUp(self):
        self.personalization = Personalization()
        self.image = Image.new("RGB", (512, 512), color=(200, 200, 255))

    def test_add_glasses(self):
        traits = ["glasses"]
        personalized_image = self.personalization.personalize_avatar(self.image, traits)
        self.assertIsInstance(personalized_image, Image.Image)
        print("Glasses trait applied successfully!")

    def test_add_hat(self):
        traits = ["hat"]
        personalized_image = self.personalization.personalize_avatar(self.image, traits)
        self.assertIsInstance(personalized_image, Image.Image)
        print("Hat trait applied successfully!")

    def test_multiple_traits(self):
        traits = ["glasses", "beard"]
        personalized_image = self.personalization.personalize_avatar(self.image, traits)
        self.assertIsInstance(personalized_image, Image.Image)
        print("Multiple traits applied successfully!")

    def test_invalid_trait(self):
        with self.assertRaises(KeyError):
            self.personalization.personalize_avatar(self.image, ["invalid_trait"])

if __name__ == "__main__":
    unittest.main()
