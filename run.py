import sys
from pathlib import Path

from src import Organizer


def main():
    if getattr(sys, "frozen", False):
        target_directory = Path(sys.executable).resolve().parent
    else:
        target_directory = Path(__file__).resolve().parent

    organizer = Organizer(target_directory)
    organizer.scan_for_files()
    organizer.create_directories()
    organizer.move_files_to_directories()


if __name__ == "__main__":
    main()
