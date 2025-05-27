#%%
from scipy.io import arff
import pandas as pd
#%%
def load_raw_data():
    data, _ = arff.loadarff('./data/yeast.arff') # output : data, meta
    data = pd.DataFrame(data)
    
    assert data.isna().sum().sum() == 0

    for column in data.select_dtypes([object]).columns:
        data[column] = data[column].str.decode('utf-8') # object decoding
    
    continuous = [i for i in range(1, 104)]
    continuous_features = [f"attr{x}" for x in continuous]
    
    categorical = [i for i in range(1, 15)]
    categorical_features = [f"class{x}" for x in categorical]
    integer_features = []
        
    ClfTarget = 'class14'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    