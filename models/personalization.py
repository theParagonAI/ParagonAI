from PIL import ImageDraw

class Personalization:
    def __init__(self):
        self.traits = {
            "glasses": self.add_glasses,
            "hat": self.add_hat,
            "beard": self.add_beard
        }

    def personalize_avatar(self, image, traits):
        print(f"Personalizing avatar with traits: {traits}")
        draw = ImageDraw.Draw(image)
        for trait in traits:
            if trait in self.traits:
                self.traits[trait](draw, image)
        return image

    def add_glasses(self, draw, image):
        width, height = image.size
        draw.rectangle([width//4, height//3, 3*width//4, height//3 + 20], outline="black", width=3)

    def add_hat(self, draw, image):
        width, height = image.size
        draw.rectangle([width//4, height//5, 3*width//4, height//5 + 30], fill="black")

    def add_beard(self, draw, image):
        width, height = image.size
        draw.arc([width//3, 2*height//3, 2*width//3, height], 0, 180, fill="black", width=3)
