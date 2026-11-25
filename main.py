from os import getcwd

from src import Organizer


def main():
    current_path = getcwd()
    organizer = Organizer(current_path)

    organizer.scan_for_files()
    organizer.identify_file_extensions()
    organizer.total_files_counter()
    organizer.list_files_by_type()

    organizer.check_file_types()
    organizer.create_directories()
    organizer.move_files_to_directories()


if __name__ == "__main__":
    main()
