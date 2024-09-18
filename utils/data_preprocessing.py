import pandas as pd
import joblib
# import pickle 
from utils.model_utils import load_model

class DataPreprocessor:
    def __init__(self):
        self.scaler = load_model("./artifacts/scaler.pkl")
        self.encoder = load_model("./artifacts/encoder.pkl")
        self.te_cols= 'city'
        

    def process_data(self, data):
        # ensuring data values are list 
        for key, value in data.items():
            data[key] = [value]

        df = pd.DataFrame(data)
        # Date processing
        df['DOJ'] = pd.to_datetime(df['DOJ'])
        df['year'] = df['DOJ'].dt.year
        df['month'] = df['DOJ'].dt.month
        df['day'] = df['DOJ'].dt.day
        df.drop(columns='DOJ',inplace=True)

        df = df.loc[: , ["total_months","age","gender","city","education","income",\
                         "joining_designation","grade", "total_business_val","quarterly_rating",\
                            "year", "month", "day", "quarterly_rating_increased", "income_increased"]]
        df[self.te_cols] = self.encoder.transform(df[self.te_cols])
        df = self.scaler.transform(df)
        return df

    def load_preprocessor(self, filename="artifacts/decision_tree.joblib"):
        return joblib.load(filename)
