import pytest
import pandas as pd
import numpy as np


@pytest.fixture(scope="module")
def simple_dataframe():
    return pd.DataFrame({"A": [range(5)], "B": [range(0, 10, 2)]})


@pytest.fixture(scope="module")
def generated_dataframe():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list("ABCDE"))
    df['A Banana'] = np.random.randint(0, 100, size=(100))
    df['B Orange'] = np.random.randint(0, 100, size=(100))
    return df


@pytest.fixture(scope="module")
def boolean_dataframe():
    '''
    A dataframe with 1/0 in the columns
    '''
    df = pd.DataFrame({'A':[1,0,0,1],'B':[1,1,1,1], 'C':[0,0,0,0], 'D':[True,False,True,False]})
    return df


