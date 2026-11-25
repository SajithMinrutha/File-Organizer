from pathlib import Path

from .categories import FILE_CATEGORIES


# handle empty extensions
class Organizer:
    def __init__(self, path):
        self.P = Path(path)
        self.files_list = []
        self.subdirs_list = []
        self.extensions_list = []
        self.create_folders_list = []

    def scan_for_subdirs(self):
        print(f"\nscanning {self.P} for subdirectories...\n")
        self.subdirs_list = [entry for entry in self.P.iterdir() if entry.is_dir()]
        for subdir in self.subdirs_list:
            print(subdir.name)
        return self.subdirs_list

    def scan_for_files(self):
        print(f"\nscanning {self.P} for files...\n")
        self.files_list = [entry for entry in self.P.iterdir() if entry.is_file()]
        for files in self.files_list:
            print(files.name)
        return self.files_list

    def identify_file_extensions(self):
        print(f"\nidentifying file extensions in {self.P}")
        for file in self.files_list:
            self.extensions_list.append(file.suffix)
        return self.extensions_list

    def total_files_counter(self):
        total_files = len(self.files_list)
        print(f"\nTotal Files: {total_files}\n")
        return total_files

    def remove_duplicates(self):
        return set(self.extensions_list)

    def list_files_by_type(self):
        remove_duplicates = self.remove_duplicates()
        files_by_type = {}
        for ext in remove_duplicates:
            files_by_type[ext] = [
                file for file in self.files_list if file.suffix == ext
            ]
        return files_by_type

    def check_file_types(self):
        for key, extensions_set in FILE_CATEGORIES.items():
            print(key, extensions_set)
            for ext in self.extensions_list:
                if ext in extensions_set:
                    self.create_folders_list.append(key)
        return self.create_folders_list

    def create_directories(self):
        self.check_file_types()

    def test_print(self):
        print(self.create_folders_list)
