 #%%
import pandas as pd
#%%
def load_raw_data():       
    data = pd.read_csv('./data/clean2.data', header=None)
    assert data.isna().sum().sum() == 0
        
    column = [i for i in range(1, 167)]
    columns = [
        'molecule_name', 
        'conformation_name'
    ] + [
        f"f{x}" for x in column
    ] + [
        'class'
    ]

    data.columns = columns
    columns.remove('class') 
    columns.remove('molecule_name') 
    columns.remove('conformation_name')
    
    continuous_features = columns
    categorical_features = [
        'class', 
        'molecule_name', 
        'conformation_name'
    ]
    integer_features = continuous_features
        
    ClfTarget = 'class'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    
    
