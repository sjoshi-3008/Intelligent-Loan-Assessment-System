import pandas as pd
import os
from src import config

def load_data():
    """Loads the training dataset."""
    # We refer to config.DATA_PATH which we just defined above
    if not os.path.exists(config.DATA_PATH):
        raise FileNotFoundError(f"File not found at: {config.DATA_PATH}")
    
    df = pd.read_csv(config.DATA_PATH)
    print(f"✅ Data Loaded Successfully. Shape: {df.shape}")
    return df

# Alias for compatibility
load_dataset = load_data