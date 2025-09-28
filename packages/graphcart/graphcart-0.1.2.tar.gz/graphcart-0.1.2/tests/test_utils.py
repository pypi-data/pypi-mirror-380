import pandas as pd
from visuals.utils import ensure_df

def test_ensure_df_from_list():
    out = ensure_df([[1,2],[3,4]])
    assert isinstance(out, pd.DataFrame)

def test_ensure_df_from_series():
    out = ensure_df([1,2,3])
    assert isinstance(out, pd.DataFrame)
    assert 'value' in out.columns
