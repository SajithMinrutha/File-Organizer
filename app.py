from pathlib import Path


class App:
    def __init__(self, path):
        self.P = Path(path)

    def scan_for_subdirs(self):
        # scan for subdirectories
        print(f"scanning {self.P} for subdirectories...")

        subdirectory_list = [entry for entry in self.P.iterdir() if entry.is_dir()]
        for subdir in subdirectory_list:
            print(subdir)

    def get_path():
        pass
