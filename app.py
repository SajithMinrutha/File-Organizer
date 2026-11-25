from pathlib import Path


class App:
    def __init__(self, path):
        self.P = Path(path)
        self.files_list = []
        self.subdirs_list = []
        self.extensions = []

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
        self.extensions = []
        print(f"\nidentifying file extensions in {self.P}")
        for file in self.files_list:
            self.extensions.append(file.suffix)
        return self.extensions

    def total_files_counter(self):
        total_files = len(self.files_list)
        print(f"\nTotal Files: {total_files}\n")
        return total_files

    def remove_duplicates(self):
        return set(self.extensions)

    def list_files_by_type(self):
        remove_duplicates = self.remove_duplicates()
        files_by_type = {}
        for ext in remove_duplicates:
            files_by_type[ext] = [
                file for file in self.files_list if file.suffix == ext
            ]
        return files_by_type

    def create_directories(self):
        pass
