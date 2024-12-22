from models.generator import AvatarGenerator
from models.style_transfer import StyleTransfer
from models.personalization import Personalization
from services.render_service import save_avatar
from utils.validation import validate_input

class AvatarController:
    def __init__(self, config):
        self.generator = AvatarGenerator()
        self.style_transfer = StyleTransfer()
        self.personalization = Personalization()
        self.output_path = config["output_path"]
        self.valid_themes = config["valid_themes"]
        self.valid_styles = config["valid_styles"]

    def create_avatar(self, theme, style, traits=None, applied_style=None):
        if not validate_input(theme, style, self.valid_themes, self.valid_styles):
            raise ValueError("Invalid theme or style.")

        print(f"Creating avatar with theme: '{theme}', style: '{style}'")
        
        # Generate base avatar
        avatar = self.generator.generate_avatar(theme, style)

        # Apply optional traits
        if traits:
            print(f"Applying traits: {traits}")
            avatar = self.personalization.personalize_avatar(avatar, traits)

        # Apply style transfer
        if applied_style:
            print(f"Applying style: '{applied_style}'")
            avatar = self.style_transfer.apply_style(avatar, applied_style)

        # Save avatar to output path
        filename = f"{theme}_{style}_{applied_style or 'base'}.png"
        avatar_path = save_avatar(avatar, self.output_path, filename)
        return avatar_path
