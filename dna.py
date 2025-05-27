from scipy.io import arff
import pandas as pd
#%%
def load_raw_data():
    data, _ = arff.loadarff('./data/dna.arff') # output : data, meta
    data = pd.DataFrame(data)
    
    assert data.isna().sum().sum() == 0

    for column in data.select_dtypes([object]).columns:
        data[column] = data[column].str.decode('utf-8') # object decoding
    
    continuous_features = []
    
    categorical = [i for i in range(1, 180)]
    categorical_features = [f"A{x}" for x in categorical]
    categorical_features += ["class"]
    
    integer_features = []
        
    ClfTarget = 'class'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    