#%%
import pandas as pd
#%%
def load_raw_data():
    base = pd.read_csv('./data/application_train.csv')
    data = base.sample(frac=1, random_state=0).reset_index(drop=True)
    
    continuous_features = [
        'AMT_INCOME_TOTAL', 
        'AMT_CREDIT', 
        'AMT_ANNUITY',
        'AMT_GOODS_PRICE',
        'REGION_POPULATION_RELATIVE', 
        'DAYS_BIRTH', 
        'DAYS_EMPLOYED', 
        'DAYS_REGISTRATION',
        'DAYS_ID_PUBLISH',
        'OWN_CAR_AGE',
    ]
    categorical_features = [
        'NAME_CONTRACT_TYPE',
        'CODE_GENDER',
        # 'FLAG_OWN_CAR',
        'FLAG_OWN_REALTY',
        'NAME_TYPE_SUITE',
        'NAME_INCOME_TYPE',
        'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS',
        'NAME_HOUSING_TYPE',
        'TARGET', # target variable
    ]
    integer_features = [
        'DAYS_BIRTH', 
        'DAYS_EMPLOYED', 
        'DAYS_ID_PUBLISH'
    ]
    ClfTarget = 'TARGET'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    