   #%%
import pandas as pd
#%%
def load_raw_data(): 
    data = pd.read_csv('./data/kc_house_data.csv')
    
    continuous_features = [
        'price', 
        'sqft_living',
        'sqft_lot',
        'sqft_above',
        'sqft_basement',
        'yr_built',
        'yr_renovated',
        'lat',
        'long',
        'sqft_living15',
        'sqft_lot15',
    ]
    categorical_features = [
        'bedrooms',
        'bathrooms',
        'floors',
        'waterfront',
        'view',
        'condition',
        'grade', 
    ]
    integer_features = [
        'price',
        'sqft_living',
        'sqft_lot',
        'sqft_above',
        'sqft_basement',
        'yr_built',
        'yr_renovated',
        'sqft_living15',
        'sqft_lot15',
    ]
    ClfTarget = "grade"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    