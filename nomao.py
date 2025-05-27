#%%
from scipy.io import arff
import pandas as pd
#%%
def load_raw_data():
    data, _ = arff.loadarff('./data/nomao.arff') # output : data, meta
    data = pd.DataFrame(data)
    
    assert data.isna().sum().sum() == 0

    for column in data.select_dtypes([object]).columns:
        data[column] = data[column].str.decode('utf-8') # object decoding
    
    categorical = [
        7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 
        47, 48, 55, 56, 63, 64, 71, 72, 79, 80, 
        87,  88, 92, 96, 100, 104, 108, 112, 116 
    ]
    continuous = [i for i in range(1, 119)]
    continuous = [x for x in continuous if x not in categorical]

    continuous_features = [f"V{x}" for x in continuous]
    categorical_features = [f"V{x}" for x in categorical] + ['Class']
    integer_features = []
        
    ClfTarget = 'Class'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    