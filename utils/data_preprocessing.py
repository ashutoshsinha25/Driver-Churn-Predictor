import pandas as pd
import joblib
import pickle 
from utils.model_utils import load_model

class DataPreprocessor:
    def __init__(self):
        self.scaler = load_model("scaler.pkl")
        self.encoder = load_model("encoder.pkl")
        self.te= ['city']
        

    def process_data(self, data):
        df = pd.DataFrame(data) if not isinstance(data, pd.DataFrame) else data.copy()
        # Date processing
        df['Dateofjoining'] = pd.to_datetime(df['Dateofjoining'], errors='coerce')
        df['LastWorkingDate'] = pd.to_datetime(df['LastWorkingDate'], errors='coerce')

        df['year'] = df['Dateofjoining'].dt.year
        df['month'] = df['Dateofjoining'].dt.month
        df['day'] = df['Dateofjoining'].dt.day

        df[self.te_cols] = self.target_encoder.transform(df[self.te_cols])

        return df

    def load_preprocessor(self, filename="artifacts/decision_tree.joblib"):
        return joblib.load(filename)
