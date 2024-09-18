from flask import Flask, render_template, request
from utils.data_preprocessing import DataPreprocessor
from models.decision_tree import DecisionTreeModel


app = Flask(__name__)

def read_data(form_data):
    return {
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
        #year
        #month 
        #date
        "quarterly_rating_increased":int(form_data['quarterly_rating_increase']),
        "income_increased":int(form_data['income_increase']),
    }

def init_model():
    return DecisionTreeModel()

# Initialize the model
model = init_model()

@app.route('/app', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Read data
        input_data = read_data(request.form)
        # print(f"Input data: {input_data}", flush=True)
        # # print(input_data)
        # Process data
        features = DataPreprocessor().process_data(input_data)
        # # Make prediction
        prediction = model.model_obj.predict(features)
        # # Get prediction probabilities
        probabilities = model.model_obj.predict_proba(features)[0]
        # prediction=1
        # probabilities=[0.15, 0.85]
        return render_template('result.html', prediction=prediction, probabilities=probabilities)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)