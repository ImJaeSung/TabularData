import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/vietnami.csv')
    
    assert data.isna().sum().sum() == 0
    
    continuous = [
        "pharvis",	
        "lnhhexp",
        "age", 
        "illness", 
        "illdays",	
        "actdays",	
        "commune",
    ]
    continuous_features = [f"con_{x}" for x in continuous]
    
    categorical = [
        "sex",
        "married",	
        "educ",		
        "injury",	
        "insurance",	
    ]
    categorical_features = [f"cat_{x}" for x in categorical]
    
    integer = [
        "pharvis",
        "illness", 
        "illdays",	
        "actdays",	
        "commune",
    ]
    integer_features = [f"con_{x}" for x in integer]
        
    ClfTarget = 'cat_insurance'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    