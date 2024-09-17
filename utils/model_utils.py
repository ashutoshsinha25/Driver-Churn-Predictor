import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
# def save_model_and_preprocessor(model, preprocessor, model_filename, preprocessor_filename):
#     """
#     Save a trained model and its preprocessor to files.
#     """
#     joblib.dump(model, model_filename)
#     joblib.dump(preprocessor, preprocessor_filename)

def load_model(path):
    """
    Load a trained model and its preprocessor from files.
    """
    # obj = joblib.load(model_filename)
    model_pickle = open(path, "rb")
    obj = pickle.load(model_pickle)

    return obj

def evaluate_model(y_true, y_pred):
    """
    Evaluate model performance using various metrics.
    """
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1_score': f1_score(y_true, y_pred, average='weighted')
    }

def get_feature_importance(model, feature_names):
    """
    Get feature importances for tree-based models.
    """
    if hasattr(model, 'feature_importances_'):
        return dict(zip(feature_names, model.feature_importances_))
    else:
        return None