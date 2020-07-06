import pytest
import pandas as pd
from pathlib import Path

import mutil
from mutil import DataFolder, get_latest_file


@pytest.fixture
def simple_dataframe():
    return pd.DataFrame({'A':[range(5)],'B':[range(0,10,2)]})

@pytest.fixture
def default_dataroot():
    return './tests/data'

@pytest.fixture
def default_dataroot_raw(default_dataroot):
    return DataFolder(default_dataroot).RAW


def test_datafolder(default_dataroot):
    dfolder = DataFolder(default_dataroot)
    assert dfolder.ROOT == Path(default_dataroot)
    assert dfolder.RAW == Path(default_dataroot)/'raw'

def test_get_latest_file(tmp_path):
    r = tmp_path / '01.csv'
    r.write_text('something')
    r = tmp_path/ '02.csv'
    r.write_text('something')
    print([_ for _ in r.glob('*')])
    assert get_latest_file(tmp_path,'0','csv') == '02.csv'
    with pytest.raises(AssertionError):
        assert get_latest_file(tmp_path,'1','.csv')


def test_get_latest_file(tmp_path):
    r = tmp_path / '01.csv'
    r.write_text('something')
    r = tmp_path/ '02.csv'
    r.write_text('something')
    print([_ for _ in r.glob('*')])
    assert get_latest_file(tmp_path,'0','csv') == '02.csv'



