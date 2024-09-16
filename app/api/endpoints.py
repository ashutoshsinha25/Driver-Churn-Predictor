from flask import Blueprint, request, jsonify
from app.models.decision_tree import DecisionTreeModel
# from app.models.random_forest import RandomForestModel
# from app.models.xgboost_model import XGBoostModel
# from app.models.lightgbm_model import LightGBMModel
# from app.utils.data_preprocessing import DataPreprocessor

api_bp = Blueprint('api', __name__)


model_mapping = {
    "dt": DecisionTreeModel()

}
@api_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    model_name = data.get('model', 'dt')

    if model_name not in model_mapping:
        return jsonify({'error': 'Invalid model name'}), 400
    
    features = data.get('features')
    if not features:
        return jsonify({'error': 'No features provided'}), 400
    
    obj = model_mapping[model_name]
    preprocessed_features = obj.process_data(features)
    prediction = obj.model.predict(preprocessed_features)
    probability = obj.model.predict_proba(preprocessed_features)[:, 1]
    
    return jsonify({
        'prediction': prediction.tolist(),
        'probability': probability.tolist()
    })

@api_bp.route('/models', methods=['GET'])
def get_models():
    return jsonify({'models': list(model_mapping.keys())})