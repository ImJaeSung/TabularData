#%%
import pandas as pd
#%%
def load_raw_data():
    base = pd.read_csv('./data/covtype.csv')
    base = base.sample(frac=1, random_state=0).reset_index(drop=True)
    base = base.dropna(axis=0)
    data = base.iloc[:50000]
    
    continuous_features = [
        'Elevation', # target variable
        'Aspect', 
        'Slope',
        'Horizontal_Distance_To_Hydrology', 
        'Vertical_Distance_To_Hydrology',
        'Horizontal_Distance_To_Roadways',
        'Hillshade_9am',
        'Hillshade_Noon',
        'Hillshade_3pm',
        'Horizontal_Distance_To_Fire_Points',
    ]
    categorical_features = [
        'Cover_Type', # target variable
    ]
    integer_features = continuous_features
    
    ClfTarget = 'Cover_Type'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    