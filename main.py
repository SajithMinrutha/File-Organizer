from app import App


def main():
    scan_directory = "."
    app = App(scan_directory)
    app.scan_for_files()
    app.scan_for_subdirs()
    app.identify_file_extensions()
    app.total_files_counter()


if __name__ == "__main__":
    main()
