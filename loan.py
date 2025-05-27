#%%
import pandas as pd
#%%
def load_raw_data():    
    data = pd.read_csv('./data/Bank_Personal_Loan_Modelling.csv')
    
    continuous_features = [
        'Age',
        'Experience',
        'Income', 
        'CCAvg',
        'Mortgage',
    ]
    categorical_features = [
        'Family',
        'Personal Loan',
        'Securities Account',
        'CD Account',
        'Online',
        'CreditCard'
    ]
    integer_features = [
        'Age',
        'Experience',
        'Income', 
        'Mortgage'
    ]
    data = data[continuous_features + categorical_features]
    data = data.dropna()
    ClfTarget = "Personal Loan"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    