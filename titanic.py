import pandas as pd
#%%
def load_raw_data():
    data = pd.read_csv('./data/spaceship-titanic.csv')
    data = data.dropna(axis=0) # drop 2087 observations
    
    assert data.isna().sum().sum() == 0
    
    continuous_features = [
        "Age",
        "RoomService",
        "FoodCourt",
        "ShoppingMall",
        "Spa",
        "VRDeck"
    ]
    
    categorical_features = [
        "HomePlanet",
        "CryoSleep",
        "Cabin",
        "Destination",
        "VIP",
        "Name",
        "Transported"
    ]
    
    integer_features = continuous_features
    
    ClfTarget = "Transported"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    