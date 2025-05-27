#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/abalone.data', header=None)
    columns = [
        "Sex",
        "Length",
        "Diameter",
        "Height",
        "Whole weight",
        "Shucked weight",
        "Viscera weight",
        "Shell weight",
        "Rings",
    ]
    data.columns = columns
    
    assert data.isna().sum().sum() == 0
    
    columns.remove("Sex")
    columns.remove("Rings")
    continuous_features = columns
    categorical_features = [
        "Sex",
        "Rings"
    ]
    integer_features = []
    ClfTarget = "Rings"
                
    return data, continuous_features, categorical_features, integer_features, ClfTarget