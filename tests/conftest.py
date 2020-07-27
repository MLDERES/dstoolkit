import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope='module')
def simple_dataframe():
    return pd.DataFrame({'A': [range(5)], 'B': [range(0, 10, 2)]})

@pytest.fixture(scope='module')
def generated_dataframe():
    return pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))

@pytest.fixture(scope='module')
def df_with_spaces():
    return pd.DataFrame({'A Banana': range(5), 'B Orange': range(0, 10, 2)})

        

