#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/winequality-white.csv', delimiter=";")
    columns = list(data.columns)
    columns.remove("quality")
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = columns
    categorical_features = [
        "quality"
    ]
    integer_features = []
    ClfTarget = "quality"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    