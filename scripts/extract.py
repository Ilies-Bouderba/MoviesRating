import pandas as pd
from config import RAW_DATA_PATH

def extract():
    print("Extracting raw data...")
    df = pd.read_csv(RAW_DATA_PATH)
    print("Raw data extracted successfully.")
    return df