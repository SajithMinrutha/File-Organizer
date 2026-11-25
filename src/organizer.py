from pathlib import Path

from .categories import FILE_CATEGORIES


class Organizer:
    def __init__(self, path):
        self.path = Path(path)
        self.files_list = []
        self.subdirs_list = []
        self.extensions_list = []
        self.create_folders_list = []
        self.remove_duplicate_list = []
        self.categorized_dict = {}

    def scan_for_subdirs(self):
        print(f"\nscanning {self.path} for subdirectories...\n")
        self.subdirs_list = [entry for entry in self.path.iterdir() if entry.is_dir()]
        for subdir in self.subdirs_list:
            print(subdir.name)
        return self.subdirs_list

    def scan_for_files(self):
        print(f"\nscanning {self.path} for files...\n")
        self.files_list = [entry for entry in self.path.iterdir() if entry.is_file()]
        for files in self.files_list:  # remove later
            print(files.name)
        return self.files_list

    def identify_file_extensions(self):
        print(f"\nidentifying file extensions in {self.path}")
        for file in self.files_list:
            self.extensions_list.append(file.suffix.lower())
        return self.extensions_list

    def total_files_counter(self):
        total_files = len(self.files_list)
        print(f"\nTotal Files: {total_files}\n")
        return total_files

    def remove_duplicates(self):
        return set(self.extensions_list)

    def list_files_by_type(self):
        self.remove_duplicate_list = self.remove_duplicates()
        files_by_type = {}
        for ext in self.remove_duplicate_list:
            files_by_type[ext] = [
                file for file in self.files_list if file.suffix.lower() == ext
            ]
        return files_by_type

    def check_file_types(self):
        self.categorized_dict = {}

        for file in self.files_list:
            ext = file.suffix.lower()
            category = "Others"

            for folder_name, extensions_set in FILE_CATEGORIES.items():
                if ext in extensions_set:
                    category = folder_name
                    break

            self.categorized_dict.setdefault(category, []).append(file)

        self.create_folders_list = list(self.categorized_dict.keys())
        return self.categorized_dict

    def create_directories(self):
        self.check_file_types()

        for folder_name in self.categorized_dict:
            folder_path = self.path / folder_name

            if not folder_path.exists():
                folder_path.mkdir()
                print(f"Created directory: {folder_path}")
            else:
                print(f"Directory already exists: {folder_path}")

    def move_files_to_directories(self):
        if not self.categorized_dict:
            self.check_file_types()

        for folder_name, files in self.categorized_dict.items():
            destination_dir = self.path / folder_name

            for file in files:
                moved_file = file.move_into(destination_dir)

                print(f"Moved {file.name} to {folder_name}")
