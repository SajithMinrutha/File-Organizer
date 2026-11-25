import os

from src import Organizer


def main():
    current_path = os.getcwd()
    organizer = Organizer(current_path)

    organizer.scan_for_files()
    organizer.scan_for_subdirs()
    organizer.identify_file_extensions()
    organizer.total_files_counter()
    organizer.list_files_by_type()
    organizer.create_directories()
    organizer.check_file_types()
    organizer.test_print()


if __name__ == "__main__":
    main()
