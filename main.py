import os

from src import Organizer


def main():
    current_path = os.getcwd()
    organizer = Organizer(current_path)
    organizer.move_files_to_directories()
    organizer.identify_file_extensions()
    organizer.total_files_counter()
    organizer.list_files_by_type()
    organizer.create_directories()
    organizer.test_print()
    # organizer.remove_dir()


if __name__ == "__main__":
    main()
