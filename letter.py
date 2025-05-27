#%%
import pandas as pd
#%%
def load_raw_data():    
    data = pd.read_csv('./data/letter-recognition.data', header=None)
    columns = [
        "lettr",
        "x-box",
        "y-box",
        "width",
        "high",
        "onpix",
        "x-bar",
        "y-bar",
        "x2bar",
        "y2bar",
        "xybar",
        "x2ybr",
        "xy2br",
        "x-ege",
        "xegvy",
        "y-ege",
        "yegvx",
    ]
    data.columns = columns
    
    assert data.isna().sum().sum() == 0
    
    columns.remove("lettr")
    continuous_features = columns
    categorical_features = [
        "lettr"
    ]
    integer_features = columns
    ClfTarget = "lettr"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
    