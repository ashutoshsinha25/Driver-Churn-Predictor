import pandas as pd
from utils.prediction_pipeline import PredictionPipeline
import joblib

class DataPreprocessor:
    def __init__(self, model_path):
        self.processor = self.load_preprocessor(model_path)
        self.model = self.processor.model
        self.scaler = self.processor.scaler
        self.encoder = self.processor.encoder
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

    @classmethod
    def load_preprocessor(cls, filename="artifacts/decision_tree.joblib"):
        return joblib.load(filename)