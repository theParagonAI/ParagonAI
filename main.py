from controllers.avatar_controller import AvatarController
from config.settings import get_config
from utils.logging import log

def main():
    log("Starting Paragon AI...")
    
    config = get_config()
    controller = AvatarController(config)
    
    print("Welcome to Paragon AI!")
    theme = input("Enter the theme (e.g., futuristic, fantasy): ")
    style = input("Enter the style (e.g., pixel art, realistic): ")
    
    try:
        avatar_path = controller.create_avatar(theme, style)
        print(f"Avatar successfully created and saved to: {avatar_path}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
