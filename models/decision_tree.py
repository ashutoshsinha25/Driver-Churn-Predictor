from utils.model_utils import load_model

class DecisionTreeModel:
    def __init__(self, model_path="artifacts/decision_tree.pkl"):
        self.model_obj = load_model(model_path)

    def __str__(self):
        return "Decision Tree Model"

    def predict(self, features):
        return self.model.predict(features)
    
    def pred_proba(self, features):
        return self.model.predict_proba(features)
    
    def get_feature_importance(self):
        if hasattr(self.model, 'feature_importances_'):
            return dict(zip(self.model.feature_names_in_, self.model.feature_importances_))
        return None
