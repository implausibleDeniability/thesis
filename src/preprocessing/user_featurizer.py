import numpy as np
import pandas as pd
from collections import namedtuple

class UserFeaturizer:
    numerical_feature_names = [
        "is_closed_profile",
        "sex_id",
        "age_is_present",
        "age",
    ]
    
    categorical_feature_names = [
        "city_id",
        "country_id",
        "sex_id",
        "political_pref_id",
        "life_main_id",
        "people_main_id",
        "alcohol_attitude_id",
    ]
    
    max_categories=10
    
    def build_feature_matrix(self, users: list[dict]):
        df = pd.DataFrame(users)
        numerical_features = np.array(df[self.numerical_feature_names].values, dtype=np.float32)
        categorical_features = np.array(df[self.categorical_feature_names].values, dtype=np.int32)
        categorical_features[np.bitwise_or(categorical_features > 10, categorical_features < 0)] = 0
        features = namedtuple('features', ['numerical', 'categorical'])
        return features(numerical_features, categorical_features)
