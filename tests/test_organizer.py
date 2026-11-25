from src import Organizer


def test_scan_for_files(tmp_path):
    (tmp_path / "photo.jpg").touch()
    (tmp_path / "report.pdf").touch()
    (tmp_path / "Images").mkdir()
    organizer = Organizer(tmp_path)
    result = organizer.scan_for_files()
    assert len(result) == 2
    assert all(file.is_file() for file in result)


def test_scan_for_subdirs(tmp_path):
    (tmp_path / "photo.jpg").touch()
    (tmp_path / "report.pdf").touch()
    (tmp_path / "Images").mkdir()
    organizer = Organizer(tmp_path)
    result = organizer.scan_for_subdirs()
    assert len(result) == 1
    assert all(subdir.is_dir() for subdir in result)
