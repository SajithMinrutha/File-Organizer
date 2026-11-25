import os

from app import App


def main():
    current_path = os.getcwd()
    app = App(current_path)

    app.scan_for_files()
    app.scan_for_subdirs()
    app.identify_file_extensions()
    app.total_files_counter()
    app.list_files_by_type()


if __name__ == "__main__":
    main()
