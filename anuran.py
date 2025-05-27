#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/Frogs_MFCCs.csv')
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = [x for x in data.columns if x.startswith("MFCCs_")]
    categorical_features = [
        'Family',
        'Genus',
        'Species'
    ]
    integer_features = []
    ClfTarget = "Species"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    