import os
import shutil

class StorageService:
    def __init__(self, base_path="output/storage/"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def store_file(self, file_path, subdirectory="avatars"):
        """Moves a file to the storage subdirectory."""
        destination_path = os.path.join(self.base_path, subdirectory)
        os.makedirs(destination_path, exist_ok=True)
        filename = os.path.basename(file_path)
        new_path = os.path.join(destination_path, filename)
        shutil.move(file_path, new_path)
        print(f"File stored at {new_path}")
        return new_path

    def delete_file(self, file_path):
        """Deletes a file from the storage."""
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} deleted.")
        else:
            print(f"File {file_path} does not exist.")

    def list_files(self, subdirectory="avatars"):
        """Lists all files in the specified subdirectory."""
        directory = os.path.join(self.base_path, subdirectory)
        if os.path.exists(directory):
            return os.listdir(directory)
        else:
            print(f"Directory {directory} does not exist.")
            return []
