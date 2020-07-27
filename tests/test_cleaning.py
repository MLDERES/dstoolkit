import pytest
import pandas as pd
from pathlib import Path
import time


# In order for this to work, the package needs to be installed
# pip install -e . should do the trick
from mlderes.dstoolkit import replace_string_in_col_name, remove_columns


def test_replace_str_in_col_name(df_with_spaces):
    df_actual = replace_string_in_col_name(df_with_spaces)
    assert list(df_actual.columns) == ['ABanana', 'BOrange']

    df_actual = replace_string_in_col_name(df_with_spaces,find_val = ' ', replace_val='_' )
    assert list(df_actual.columns) == ['A_Banana', 'B_Orange']

    df_actual = replace_string_in_col_name(df_with_spaces,columns='A Banana', find_val = ' ', 
        replace_val='_')
    assert list(df_actual.columns) == ['A_Banana', 'B Orange']

def test_remove_columns(generated_dataframe):
    df_test = generated_dataframe.copy()
    df_actual = remove_columns(df_test, ['A','C'])
    assert list(df_actual.columns) == list('BDE')

    df_test = generated_dataframe.copy()
    df_actual = remove_columns(df_test, 'A')
    assert list(df_actual.columns) == list('BCDE')



    
