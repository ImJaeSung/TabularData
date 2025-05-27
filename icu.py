import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/icu.csv')
    
    assert data.isna().sum().sum() == 0
    
    columns = list(data.columns)
    columns.remove("Unit")
    
    continuous_features = columns
    
    categorical_features = [
        "Unit"
    ]
    
    integer_features = continuous_features
    
    ClfTarget = "Unit"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    