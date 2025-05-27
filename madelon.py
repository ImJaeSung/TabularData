#%%
from scipy.io import arff
import pandas as pd
#%%
def load_raw_data():
    data, _ = arff.loadarff('./data/phpfLuQE4.arff') # output : data, meta
    data = pd.DataFrame(data)
    
    assert data.isna().sum().sum() == 0

    for column in data.select_dtypes([object]).columns:
        data[column] = data[column].str.decode('utf-8') # object decoding
    
    continuous = [i for i in range(1, 501)]
    continuous_features = [f"V{x}" for x in continuous]
    
    categorical_features = ["Class"]
    integer_features = continuous_features
        
    ClfTarget = 'Class'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    