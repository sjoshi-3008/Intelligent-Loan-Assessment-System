import joblib
import pandas as pd
import os
from src import config
from src.preprocessing import clean_and_encode

# --- THE CRITICAL FUNCTION ---
def make_prediction(input_data):
    """
    Takes a dictionary of applicant data and returns a prediction.
    """
    # 1. Load Model
    if not os.path.exists(config.MODEL_FILE):
        return "Error: Model not trained yet. Run src/train.py first.", 0.0
        
    try:
        model = joblib.load(config.MODEL_FILE)
    except Exception as e:
        return f"Error loading model: {e}", 0.0
    
    # 2. Convert Input to DataFrame
    df = pd.DataFrame([input_data])
    
    # 3. Preprocess (using saved encoders)
    # We use mode='predict' to use the encoders we saved during training
    df_processed = clean_and_encode(df, mode='predict')
    
    # 4. Predict
    try:
        # Get the class prediction (0 or 1)
        prediction = model.predict(df_processed)[0]
        
        # Get the confidence/probability
        prob = model.predict_proba(df_processed).max()
        
        # Map 1 -> Approved, 0 -> Rejected
        status = "Approved" if prediction == 1 else "Rejected"
        
        return status, prob
    except Exception as e:
        return f"Prediction Error: {str(e)}", 0.0