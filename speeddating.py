#%%
from scipy.io import arff
import pandas as pd
#%%
def load_raw_data():
    data, _ = arff.loadarff('./data/speeddating.arff') # output : data, meta
    data = pd.DataFrame(data)
    
    for column in data.select_dtypes([object]).columns:
        data[column] = data[column].str.decode('utf-8') # object decoding
    
    data = data.dropna(axis=0) # remove
    assert data.isna().sum().sum() == 0

    common_cols = [
        'd_age',
        'importance_same_race',
        'importance_same_religion',
        'pref_o_attractive',
        'pref_o_sincere',
        'pref_o_intelligence', 
        'pref_o_funny',
        'pref_o_ambitious',
        'pref_o_shared_interests',
        'attractive_o',
        'sinsere_o',
        'intelligence_o',
        'funny_o',
        'ambitous_o', 
        'shared_interests_o',
        'attractive_important', 
        'sincere_important',
        'intellicence_important',
        'funny_important',
        'ambtition_important',
        'shared_interests_important',
        'attractive',
        'sincere',  
        'intelligence',  
        'funny',
        'ambition', 
        'attractive_partner', 
        'sincere_partner',
        'intelligence_partner',  
        'funny_partner',
        'ambition_partner', 
        'shared_interests_partner',
        'sports',
        'tvsports',  
        'exercise', 
        'dining',  
        'museums',  
        'art',  
        'hiking',  
        'gaming',  
        'clubbing',  
        'reading',  
        'tv',  
        'theater',  
        'movies',  
        'concerts',  
        'music',  
        'shopping',  
        'yoga',
        'interests_correlate',
        'expected_happy_with_sd_people',
        'expected_num_interested_in_me',
        'expected_num_matches',
        'like',
        'guess_prob_liked',
    ] 

    continuous_features = [
        'wave',
        'age',
        'age_o',
        'met',
    ]  

    categorical_features = [
        'match',
        'has_null',
        'gender',
        'race',  
        'race_o',
        'samerace',
        'field',
        'decision',
        'decision_o',
    ]
    
    continuous_features += [x for x in common_cols]
    categorical_features += [f"d_{x}" for x in common_cols]
    integer_features = continuous_features

    ClfTarget = "match"
    return data, continuous_features, categorical_features, integer_features, ClfTarget
s