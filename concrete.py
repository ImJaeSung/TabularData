#%%
import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/Concrete_Data.csv')
    columns = [
        "Cement",
        "Blast Furnace Slag",
        "Fly Ash",
        "Water",
        "Superplasticizer",
        "Coarse Aggregate",
        "Fine Aggregate",
        "Age",
        "Concrete compressive strength"
    ]
    data.columns = columns
    
    assert data.isna().sum().sum() == 0
    
    columns.remove("Age")
    continuous_features = columns
    categorical_features = [
        "Age",
    ]
    integer_features = []
    ClfTarget = "Age"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    