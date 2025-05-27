import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/NCbirths.csv')
    data = data.drop(columns=["ID"]) # drop ID number
    data.dropna(axis=0, inplace=True)
    
    assert data.isna().sum().sum() == 0
    
    columns = list(data.columns)
    continuous_features = [
        "MomAge",
        "Weeks",
        "Gained",
        "BirthWeightOz",
        "BirthWeightGm",
    ]
    
    for i in continuous_features: 
        columns.remove(i)
    categorical_features = columns
    integer_features = [
        "MomAge", 
        "Weeks", 
        "Gained", 
        "BirthWeightOz"
    ]
    
    ClfTarget = 'MomRace'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    