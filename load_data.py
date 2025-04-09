import pandas as pd

def load_csv(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None