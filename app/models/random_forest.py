import joblib 
from sklearn.ensemble import RandomForestClassifier

class RandomForestModel:

    def __init__(self, model_path='models/random_forest.joblib'):
        self.model=self.load_model(model_path)

    def load_model(self, model_path):
        try:
            return joblib.load(model_path)
        except FileNotFoundError:
            print(f"Model file not found at {model_path}. Initializing a new model.")
            return RandomForestClassifier()
        except Exception as e:
            print(f"Error loading the model: {e}. Initializing a new model.")
            return RandomForestClassifier()
    
    def predict(self, features):
        return self.model.predict(features)
    
    def predict_proba(self, features):
        return self.model.predict_proba(features)
    
    def get_feature_importance(self):
        return dict(zip(self.model.feature_names_in_ , self.model.feature_importances_))
