# In order for this to work, the package needs to be installed
# pip install -e . should do the trick
from mlderes.dstoolkit import (
    remove_columns,
    replace_string_in_col_name,
    convert_to_bool,
    convert_from_bool,
    remove_duplicates,
)
import pandas as pd
from pandas.testing import assert_series_equal, assert_frame_equal


def test_replace_str_in_col_name(generated_dataframe):
    df_with_spaces = generated_dataframe.copy()
    df_actual = replace_string_in_col_name(df_with_spaces)
    assert list(df_actual.columns) == ["A", "B", "C", "D", "E", "ABanana", "BOrange"]

    df_actual = replace_string_in_col_name(
        df_with_spaces, find_val=" ", replace_val="_"
    )
    assert list(df_actual.columns) == ["A", "B", "C", "D", "E", "A_Banana", "B_Orange"]

    df_actual = replace_string_in_col_name(
        df_with_spaces, columns="A Banana", find_val=" ", replace_val="_"
    )
    assert list(df_actual.columns) == ["A", "B", "C", "D", "E", "A_Banana", "B Orange"]


def test_remove_columns(generated_dataframe):
    df_test = generated_dataframe.copy()
    df_actual = remove_columns(df_test, ["A", "C"])
    assert list(df_actual.columns) == list("BDE") + ["A Banana", "B Orange"]

    df_test = generated_dataframe.copy()
    df_actual = remove_columns(df_test, "A")
    assert list(df_actual.columns) == list("BCDE") + ["A Banana", "B Orange"]


def test_convert_to_bool(boolean_dataframe):
    df_test = boolean_dataframe.copy()
    df_test = convert_to_bool(df_test, columns="A")
    df_actual = pd.Series([True, False, False, True], dtype='boolean')
    assert_series_equal(df_test['A'], df_actual, check_names=False)

    df_test = convert_to_bool(boolean_dataframe.copy(), columns=["C", "B"])
    assert df_test["B"].all(bool_only=True), "Failed to convert two columns"
    df_actual = pd.Series([False, False, False, False], dtype='boolean')
    assert_series_equal(df_test['C'], df_actual, check_names=False)


def test_convert_from_bool(boolean_dataframe):
    df_test = boolean_dataframe.copy()
    df_actual = convert_from_bool(df_test, columns="D")
    assert_series_equal(df_actual['D'], pd.Series(data=[1, 0, 1, 0]),check_names=False)

def test_remove_duplicates():
    df_test = pd.DataFrame({'A':range(5)},index=[1,1,2,2,3])
    df_result = remove_duplicates(df_test)
    df_expected = pd.DataFrame({'A':[0,2,4]},index=[1,2,3])
    assert_frame_equal(df_result, df_expected)
    




