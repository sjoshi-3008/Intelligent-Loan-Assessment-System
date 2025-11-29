import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib
import os
from src import config

def clean_and_encode(df, mode='train'):
    """
    Cleans data and encodes categorical variables.
    mode: 'train' (fits encoders) or 'predict' (uses saved encoders)
    """
    df = df.copy()
    
    # 1. Drop Loan_ID
    if config.ID_COLUMN in df.columns:
        df = df.drop(columns=[config.ID_COLUMN])
        
    # 2. Handle Missing Values
    # Categorical -> Mode
    cat_imputer = SimpleImputer(strategy='most_frequent')
    # Numerical -> Mean
    num_imputer = SimpleImputer(strategy='mean')

    # We only apply imputation if the columns exist in the dataframe
    # This handles the case where 'df' might be just one row for prediction
    
    # Numerical Imputation
    present_num_cols = [c for c in config.NUMERICAL_COLS if c in df.columns]
    if present_num_cols:
        # If training, fit the imputer. In real prod code, we'd save this imputer too.
        # For simplicity, we refit on train, and just transform on predict (assuming mean is close enough or recomputing)
        # A better approach for prod is saving the imputer like the encoder.
        # Here we stick to simple fillna for robustness if not saving imputer:
        for col in present_num_cols:
             df[col] = df[col].fillna(df[col].mean())

    # Categorical Imputation
    present_cat_cols = [c for c in config.CATEGORICAL_COLS if c in df.columns]
    for col in present_cat_cols:
         df[col] = df[col].fillna(df[col].mode()[0])

    # 3. Fix 'Dependents' column
    if 'Dependents' in df.columns:
        df['Dependents'] = df['Dependents'].replace('3+', '4')

    # 4. Encoding
    encoders = {}
    
    if mode == 'predict' and os.path.exists(config.ENCODER_FILE):
        encoders = joblib.load(config.ENCODER_FILE)
    
    # Loop through categorical columns and encode them
    # We rely on the config list to know which cols are categorical
    for col in config.CATEGORICAL_COLS:
        if col in df.columns:
            # Convert to string to ensure consistency
            df[col] = df[col].astype(str)
            
            if mode == 'train':
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
                encoders[col] = le
            else:
                if col in encoders:
                    le = encoders[col]
                    # Safe transform: if unknown label, assign 0 (or mode)
                    # This lambda checks if value is in classes, else puts 0
                    df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else 0)
    
    # Save encoders if in training mode
    if mode == 'train':
        if not os.path.exists(config.MODEL_DIR):
            os.makedirs(config.MODEL_DIR)
        joblib.dump(encoders, config.ENCODER_FILE)
        
    return df