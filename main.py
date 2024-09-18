from flask import Flask, render_template, request
from utils.data_preprocessing import DataPreprocessor
from models.decision_tree import DecisionTreeModel
from models.random_forest import RandomForestModel
from models.xgboost_model import XGBoostModel 
from models.lightgbm_model import LightGBModel


app = Flask(__name__)

def read_data(form_data):
    return {
        "Input_Model" : form_data['model_val'],
        'total_months': form_data['months_worked'],
        'age': int(form_data['age']),
        'gender': int(form_data['gender']),
        'city': form_data['city'],
        'education': int(form_data['education_level']),
        'income': float(form_data['income']),
        "joining_designation": float(form_data['joining_designation']),
        'grade': form_data['grade'],
        'total_business_val': float(form_data['total_business_value']),
        'quarterly_rating': int(form_data['quarterly_rating']),

        # to be dropped 
        'DOJ': form_data['joining_date'],
        "quarterly_rating_increased":int(form_data['quarterly_rating_increase']),
        "income_increased":int(form_data['income_increase']),
    }

def init_model(val):
    if val == "1":
        return DecisionTreeModel()
    elif val == "2":
        return RandomForestModel()
    elif val == "3":
        return XGBoostModel()
    else:
        return LightGBModel()


@app.route('/app', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Read data
        input_data = read_data(request.form)
        model_val = input_data['Input_Model']
        # Initialize the model
        model = init_model(model_val)
        model_name = model.__str__()
        # # Process data
        features = DataPreprocessor().process_data(input_data)
        # # # Make prediction
        prediction = model.model_obj.predict(features)
        # # # Get prediction probabilities
        probabilities = model.model_obj.predict_proba(features)[0]
        return render_template('result.html', prediction=prediction, probabilities=probabilities, model=model_name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)