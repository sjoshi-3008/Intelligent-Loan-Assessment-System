import os

# Base Paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
MODEL_DIR = os.path.join(PROJECT_ROOT, 'models')

# --- PATHS ---
DATA_PATH = os.path.join(DATA_DIR, 'loan_data.csv')
TRAIN_DATA = DATA_PATH 
TEST_DATA_PATH = os.path.join(DATA_DIR, 'test_data.csv')

MODEL_PATH = os.path.join(MODEL_DIR, 'loan_model.pkl')
MODEL_FILE = MODEL_PATH
ENCODER_PATH = os.path.join(MODEL_DIR, 'encoders.pkl')
ENCODER_FILE = ENCODER_PATH

# --- CONFIGURATION ---
RANDOM_SEED = 42
TEST_SIZE = 0.2
TARGET_COLUMN = 'Loan_Status'
TARGET = TARGET_COLUMN

# --- MISSING VARIABLES (Added these to fix your error) ---
ID_COLUMN = 'Loan_ID'
ID_COL = ID_COLUMN

CATEGORICAL_COLS = [
    'Gender', 'Married', 'Dependents', 'Education', 
    'Self_Employed', 'Property_Area', 'Credit_History'
]

NUMERICAL_COLS = [
    'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
    'Loan_Amount_Term'
]