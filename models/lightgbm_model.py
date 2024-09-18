from utils.model_utils import load_model

class LightGBModel:
    def __init__(self, model_path="artifacts/lightgbm.pkl"):
        self.model_obj = load_model(model_path)

    def __str__(self):
        return "Light Gradient Boosting Machine [lightGBM]"
    
    def predict(self, features):
        return self.model.predict(features)
    
    def predict_proba(self, features):
        return self.model.predict_proba(features)
    
    def get_feature_importance(self):
        if hasattr(self.model, 'feature_importances_'):
            return dict(zip(self.model.feature_names_in_, self.model.feature_importances_))
        return None