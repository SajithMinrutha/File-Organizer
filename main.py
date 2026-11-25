from pathlib import Path

from src import Organizer


def main():
    target_directory = Path.cwd()

    organizer = Organizer(target_directory)
    organizer.scan_for_files()
    organizer.create_directories()
    organizer.move_files_to_directories()


if __name__ == "__main__":
    main()
