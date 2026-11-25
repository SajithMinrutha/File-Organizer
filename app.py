from pathlib import Path


class App:
    def __init__(self, path):
        self.P = Path(path)

    def scan_for_subdirs(self):
        # scan for subdirectories
        print(f"\nscanning {self.P} for subdirectories...\n")

        subdirs_list = [entry for entry in self.P.iterdir() if entry.is_dir()]
        for subdir in subdirs_list:
            print(subdir)

    def scan_for_files(self):
        # scan for files
        print(f"\nscanning {self.P} for files...\n")

        self.files_list = [entry for entry in self.P.iterdir() if entry.is_file()]
        for files in self.files_list:
            print(files)

    def identify_file_extensions(self):
        # identify file extensions
        self.extensions = []
        print(f"\nidentifying file extensions in {self.P}")
        for file in self.files_list:
            self.extensions.append(file.suffix)

    def total_files_counter(self):
        total_files = len(self.extensions)
        print(f"\nTotal Files:{total_files} \n")

    def remove_duplicates(self):
        pass

    def list_files_by_type(self):
        pass
