import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Internal imports
import src.config as config
from src.data_loader import load_data
from src.preprocessing import clean_and_encode

def run_training():
    print("--- Starting Training Pipeline ---")
    
    # 1. Load Data
    df = load_data()
    
    # 2. Preprocess
    print("Preprocessing data...")
    # We use 'train' mode to learn and save the encoders
    df_processed = clean_and_encode(df, mode='train')
    
    # 3. Split Data
    X = df_processed.drop(columns=[config.TARGET_COLUMN])
    y = df_processed[config.TARGET_COLUMN]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_SEED
    )
    
    # 4. Train Model (Random Forest)
    print("Training Random Forest Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=config.RANDOM_SEED)
    model.fit(X_train, y_train)
    
    # 5. Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    
    # THIS IS THE ACCURACY YOU WERE LOOKING FOR
    print(f"\n>>> MODEL ACCURACY: {acc:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, preds))
    
    # 6. Save Model
    if not os.path.exists(config.MODEL_DIR):
        os.makedirs(config.MODEL_DIR)
        
    joblib.dump(model, config.MODEL_PATH)
    print(f"Model saved to {config.MODEL_PATH}")

if __name__ == "__main__":
    run_training()