#%%
import pandas as pd
#%%
def load_raw_data():
    base = pd.read_csv('./data/adult.csv')
    base = base.sample(frac=1, random_state=0).reset_index(drop=True)
    base = base[(base == '?').sum(axis=1) == 0]
    data = base.dropna()
    
    continuous_features = [
        'age', # target variable
        'educational-num',
        'capital-gain', 
        'capital-loss', 
        'hours-per-week',
    ]
    categorical_features = [
        'workclass',
        'education',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'gender',
        'native-country',
        'income', # target variable
    ]
    integer_features = continuous_features
    
    ClfTarget = 'income'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    