import os 
import joblib 
from utils.data_preprocessing import DataPreprocessor
# from utils.prediction_pipeline import PredictionPipeline
# path = "artifacts/decision_tree.joblib"
# processor_obj = DataPreprocessor(path)
# prediction = processor_obj.model.predict([data])
# print(prediction)


from flask import Flask, jsonify
from flask_cors import CORS
from app.api.endpoints import api_bp
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
