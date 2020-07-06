from pathlib import Path
import datetime as dt

DATA_FOLDER = Path('data')


class DataFolder():
    
    def __init__(self, root_data_folder):
        root_data_folder = _ensure_path(root_data_folder)
        self._raw = root_data_folder / 'raw'
        self._processed = root_data_folder / 'processed'
        self._external = root_data_folder / 'external'
        self._interim = root_data_folder / 'interim'
        self._root = root_data_folder

    def get_root(self):
        return self._root
    
    def get_procesed(self):
        return self._processed
    
    def get_raw(self):
        return self._raw
    
    def get_interim(self):
        return self._interim
    
    def get_external(self):
        return self._external
    
    DATA_ROOT = property(get_root)
    DATA_RAW = property(get_raw)
    DATA_PROCESSED = property(get_procesed)
    DATA_EXTERNAL = property(get_external)
    DATA_INTERIM = property(get_interim)


def _ensure_path(f):
    return f if isinstance(Path) else Path(f)


def get_latest_file(file_path, filename_like, file_ext):
    """
    Find absolute path to the file with the latest timestamp given the datasource name
    and file extension in the path
    
    Parameters
    ----------
    path : Path
        Folder to look for the file
    datasource : str
        Stem name of the file
    file_ext : str
        The name file extension to be looking for
    
    Returns
    -------
    str
        The absolute path of the file, if it exists or None

    """
    file_ext = file_ext if '.' in file_ext else f'.{file_ext}'
    file_path = _ensure_path(file_path)
    all_files = [f for f in file_path.glob(f'{filename_like}*{file_ext}',)]
    assert len(all_files) > 0, f'Unable to find any files like {file_path / filename_like}{file_ext}'
    fname = max(all_files, key=lambda x: x.stat().st_mtime).name
    return fname

def get_latest_data_filename(datasource_name, folder, file_ext='.csv'):
    """
    Utility method for finding .csv files
    
    Parameters
    ----------
    path : Path
        Folder to look for the file
    datasource : str
        Stem name of the file
    file_ext : str
        The name file extension to be looking for
    
    Returns
    -------
    str
        The absolute path of the file, if it exists or None

    """
    return get_latest_file(folder, datasource_name, file_ext)

def make_ts_filename(dir_name, src_name, suffix, with_ts=True):
    """
    Get a path with the filename specified by src_name with or without a timestamp, 
    in the appropriate directory.

    The filename created will have the form 'src_name'_[MMdd_HHmmss].'suffix' or
    else the timestamp will be replace with 'latest'.  See examples
    
    Parameters
    ----------
    dir_name : str or Path
        The directory where the file will live
    
    src_name: str
        The stem of the filename

    suffix : str
        The file suffix
    
    with_ts : bool, default True
        if True, use the current datetime as a timestamp (MMddHHmmss) to version the file
        if False the file version will be latest
        the 
    
    Returns
    -------
    A PosixPath representing the full path to the new filename created by the function

    Examples
    --------
    >>> make_ts_filename('/usr/tmp','hello','csv', with_ts=False)
    PosixPath('/usr/tmp/hello_latest.csv')

    """
    NOW = dt.datetime.now()
    dir_name = _ensure_path(dir_name)
    filename_suffix = f'{TODAY.month:02d}{TODAY.day:02d}_{NOW.hour:02d}{NOW.minute:02}{NOW.second:02d}' \
        if with_ts else "latest"
    fn = f'{src_name}_{filename_suffix}'
    suffix = suffix if '.' in suffix else f'.{suffix}'
    filename = (dir_name / fn).with_suffix(suffix)
    return filename


def write_data(df, datasource_name, folder, with_ts=True, **kwargs):
    """
    Export the dataset to a file
    Parameters
    ----------
    df : pandas.DataFrame 
        the dataset to write
    datasource_name : str
        the basefilename to write
    folder : str or Path
        the folder where the file will finally live
    
    with_ts : bool
        If True, then append the month, day and hour, minute, second to the filename to be written
        otherwise append the suffix 'latest' to the basename
    
    ```***kwargs```
        Keyword arguments supported by `DataFrame.to_csv`
        idx : str or int
            the name of the index or the column number
    
    return: the name of the file written
    """
    fn = make_ts_filename(folder, src_name=datasource_name, suffix='.csv')

    if 'float_format' not in kwargs.keys():
        kwargs['float_format'] = '%.3f'
    df.to_csv(fn, **kwargs)
    return fn

# def read_latest(datasource_name, folder, **kwargs):
#     """
#     Get the most recent version of a file (assumes a .csv file)
#     :param datasource_name: name of the file to get the data from (one of KAGGLE, IMDB, TNUMBERS, K_AND_IMDB, COMBINED)
#     :param folder: the subpath to the data, likely interim or processed
#     :return:
#     """
#     read_path = folder
#     fname = get_latest_data_filename(datasource_name, folder)
#     logging.info(f"read from {fname}")
#     return pd.read_csv(read_path / fname, index_col=0, infer_datetime_format=True, true_values=TRUE_VALUES,
#                        false_values=FALSE_VALUES, **kwargs)


# def write_excel(data, filename='combined', data_version=False, folder=INTERIM, with_ts=True, **kwargs):
#     """
#     Write multiple data items to a single Excel file.  Where the data is a dictionary of
#     datasources and dataframes
#     :param data: dictionary of sheet names and dataframes
#     :param filename: the name of the excel file to save
#     :param folder: folder to store the excel file
#     :param with_ts: if true, add a timestamp to the filename
#     :param kwargs: other arguments to be passed to the pandas to_excel function
#     :return: the filename of the excel file that was written
#     """
#     logger = logging.getLogger(__name__)
#     logger.info(f"writing {len(data)} to excel... {folder}")
#     fn = make_ts_filename(DATA_PATH / folder, filename, suffix='.xlsx', with_ts=with_ts)

#     if 'float_format' not in kwargs.keys():
#         kwargs['float_format'] = '%.3f'
#     if type(data_version) is bool:
#         data_version = f'_{TODAY.month:02d}{TODAY.day:02d}' if data_version else ''

#     with pd.ExcelWriter(fn) as writer:
#         for datasource, df in data.items():
#             if type(df) is not pd.DataFrame:
#                 continue
#             df.to_excel(writer, sheet_name=f'{datasource}{data_version}', **kwargs)
#     logger.info(f"finished writing df to file... {filename}")
#     return filename



# def get_file_version_from_name(fn):
#     return fn.split('_')[1]




if __name__ == "__main__":
    import doctest
    doctest.testmod()