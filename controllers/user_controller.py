import os
import json

class UserController:
    def __init__(self, user_data_path="output/users/"):
        self.user_data_path = user_data_path
        os.makedirs(self.user_data_path, exist_ok=True)

    def get_user_profile(self, user_id):
        user_file = os.path.join(self.user_data_path, f"{user_id}.json")
        if not os.path.exists(user_file):
            raise FileNotFoundError(f"User profile for '{user_id}' does not exist.")
        with open(user_file, "r") as f:
            return json.load(f)

    def create_user_profile(self, user_id, preferences=None):
        user_file = os.path.join(self.user_data_path, f"{user_id}.json")
        if os.path.exists(user_file):
            raise FileExistsError(f"User profile for '{user_id}' already exists.")
        
        profile = {
            "user_id": user_id,
            "preferences": preferences or {},
            "creation_history": []
        }
        with open(user_file, "w") as f:
            json.dump(profile, f)
        return profile

    def update_preferences(self, user_id, preferences):
        profile = self.get_user_profile(user_id)
        profile["preferences"].update(preferences)
        self._save_profile(user_id, profile)
        return profile

    def log_avatar_creation(self, user_id, theme, style, traits=None, applied_style=None):
        profile = self.get_user_profile(user_id)
        profile["creation_history"].append({
            "theme": theme,
            "style": style,
            "traits": traits,
            "applied_style": applied_style
        })
        self._save_profile(user_id, profile)

    def _save_profile(self, user_id, profile):
        user_file = os.path.join(self.user_data_path, f"{user_id}.json")
        with open(user_file, "w") as f:
            json.dump(profile, f)
