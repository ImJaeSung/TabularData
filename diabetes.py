import pandas as pd
#%%
def load_raw_data():    
    data = pd.read_csv('./data/diabetes.csv')
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
    ]
    categorical_features = ["Outcome"]
    integer_features = continuous_features
    
    ClfTarget = 'Outcome'
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    s