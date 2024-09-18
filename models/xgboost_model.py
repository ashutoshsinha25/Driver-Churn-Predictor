from utils.model_utils import load_model

class XGBoostModel:
    def __init__(self, model_path="artifacts/xgboost.pkl"):
        self.model_obj = load_model(model_path)

    def __str__(self):
        return "Extreme Gradient Boosted Machine [xgboost]"

    def predict(self, features):
        return self.model.predict(features)
    
    def predict_proba(self, features):
        return self.model.predict_proba(features)
    
    def get_feature_importance(self):
        if hasattr(self.model, 'feature_importances_'):
            return dict(zip(self.model.feature_names_in_, self.model.feature_importances_))
        return None