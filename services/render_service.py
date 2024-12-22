import os
from datetime import datetime

def save_avatar(image, output_path, filename):
    """Saves the generated avatar to the specified output path."""
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(output_path, f"{timestamp}_{filename}")
    image.save(filepath)
    print(f"Avatar saved at {filepath}")
    return filepath
