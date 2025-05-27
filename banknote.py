#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/data_banknote_authentication.txt', header=None)
    data.columns = ["variance", "skewness", "curtosis", "entropy", "class"]
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = [
        "variance", "skewness", "curtosis", "entropy"
    ]
    categorical_features = [
        'class',
    ]
    integer_features = []
    ClfTarget = "class"
    return data, continuous_features, categorical_features, integer_features, ClfTarget