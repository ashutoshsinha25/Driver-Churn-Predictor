import joblib 
from sklearn.tree import DecisionTreeClassifier
from utils.data_preprocessing import DataPreprocessor

class DecisionTreeModel:

    def __init__(self, model_path="artifacts/decision_tree.joblib"):
        self.model = DataPreprocessor(model_path)

    def predict(self, features):
        return self.model.predict(features)
    
    def predict_proba(self, features):
        return self.model.predict_proba(features)
    
    def get_feature_importance(self):
        if hasattr(self.model, 'feature_importances_'):
            return dict(zip(self.model.feature_names_in_, self.model.feature_importances_))
        return None
