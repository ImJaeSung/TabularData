#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/wdbc.data', header=None)
    data = data.drop(columns=[0]) # drop ID number
    columns = ["Diagnosis"]
    common_cols = [
        "radius",
        "texture",
        "perimeter",
        "area",
        "smoothness",
        "compactness",
        "concavity",
        "concave points",
        "symmetry",
        "fractal dimension",
    ]
    columns += [f"{x}1" for x in common_cols]
    columns += [f"{x}2" for x in common_cols]
    columns += [f"{x}3" for x in common_cols]
    data.columns = columns
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = []
    continuous_features += [f"{x}1" for x in common_cols]
    continuous_features += [f"{x}2" for x in common_cols]
    continuous_features += [f"{x}3" for x in common_cols]
    categorical_features = [
        "Diagnosis"
    ]
    integer_features = []
    ClfTarget = "Diagnosis"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    