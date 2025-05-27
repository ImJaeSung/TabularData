#%%
import pandas as pd
#%%
def load_raw_data():
    base = pd.read_csv('./data/sigma_cabs.csv')
    base = base.sample(frac=1, random_state=0).reset_index(drop=True)
    data = base.dropna().reset_index().drop(columns='index')
    
    continuous_features = [
        'Trip_Distance', 
        'Life_Style_Index', 
        'Customer_Rating', 
        'Var1',
        'Var2',
        'Var3',
    ]
    categorical_features = [
        'Type_of_Cab',
        'Customer_Since_Months',
        'Confidence_Life_Style_Index',
        'Destination_Type',
        'Cancellation_Last_1Month',
        'Gender',
        'Surge_Pricing_Type', 
    ]
    integer_features = [
        'Var1',
        'Var2',
        'Var3'
    ]
    ClfTarget = 'Surge_Pricing_Type'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    