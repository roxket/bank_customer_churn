
# Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Feature engineering
def feature_engineering(df, numeric_features):
    for col in numeric_features:
        df[col+'_log'] = np.log1p(df[col])
        df[col+'_sqrt'] = np.sqrt(df[col])
        df[col+'_sq'] = np.square(df[col])
    
    return df

# One-hot encoding for categorical features
def one_hot_encoding(df, col):
    df = pd.get_dummies(df, columns=col)
    return df

# Promising Transformations
def promising_transformations(df):
    return np.sqrt(np.log1p(df['Credit_Limit']))

# Standarization
def standarization(train_data, val_data, test_data):
    scaler = StandardScaler()
    train_data = scaler.fit_transform(train_data)
    val_data = scaler.transform(val_data)
    test_data = scaler.transform(test_data)
    return train_data, val_data, test_data