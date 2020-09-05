import pytest
from pathlib import Path
import time

# In order for this to work, the package needs to be installed
# pip install -e . should do the trick
from mlderes.dstoolkit import DataFolder, get_latest_filename, get_latest_data_filename


@pytest.fixture
def default_dataroot():
    return "./tests/data"


@pytest.fixture
def default_dataroot_raw(default_dataroot):
    return DataFolder(default_dataroot).RAW


def test_datafolder(default_dataroot):
    dfolder = DataFolder(default_dataroot)
    assert dfolder.ROOT == Path(default_dataroot)
    assert dfolder.RAW == Path(default_dataroot) / "raw"


def test_get_latest_filename(tmp_path):
    r = tmp_path / "01.txt"
    r.write_text("something")
    time.sleep(1)
    s = tmp_path / "02.txt"
    s.write_text("something")
    s.touch()
    print(f'Files in the directory: {[_ for _ in tmp_path.glob("*")]}')
    print(f'Updated times: {[x.stat().st_mtime for x in tmp_path.glob("*")]}')
    assert get_latest_filename(tmp_path, "0", "txt") == "02.txt"
    with pytest.raises(AssertionError):
        assert get_latest_filename(tmp_path, "1", ".txt")

    latest = tmp_path / '02_latest.txt'
    latest.write_text('something')
    assert get_latest_filename(tmp_path, "02", "txt") == "02_latest.txt"


def test_get_latest_data_filename(tmp_path):
    r = tmp_path / "01.csv"
    r.write_text("something")
    time.sleep(1)
    r = tmp_path / "02.csv"
    r.write_text("something")
    assert get_latest_data_filename(tmp_path, "0") == "02.csv"
    with pytest.raises(AssertionError):
        assert get_latest_filename(tmp_path, "1", ".txt")


def test_write_data():
    assert 1


def test_read_latest():
    assert 1
