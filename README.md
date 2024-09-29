# Driver Churn Prediction with Flask

This project  predicts driver churn using a Flask application. The project utilizes various machine learning models to identify factors that contribute to driver churn and develop a model to predict which drivers are likely to churn.

## Demo Video
<video width="640" height="360" controls>
  <source src="demo video/driver_churn_test.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Project Structure

The project is organized into the following folders:

* `artifacts`: This folder stores artifacts generated during training, such as model pickles.
* `models`: This folder contains the code for the different machine learning models used in the project, including DT (decision tree), RF (random forest), XGB (XGBoost), and LGBM (LightGBM).
* `notebook`: This folder contains Jupyter notebooks used for data exploration, model training, and evaluation.
* `templates`: This folder stores the HTML templates used by the Flask application.
* `test`: This folder contains unit tests for the Flask application and the machine learning models.
* `utils`: This folder contains utility functions used throughout the project.
* `.gitignore`: This file specifies files and patterns to be ignored by Git.
* `Dockerfile`: This file contains instructions for building a Docker image for the Flask application.
* `README.md`: This file (the one you're currently reading!).
* `main.py`: This file is the entry point for the Flask application.
* `requirements.txt`: This file lists the Python dependencies required for the project.
* `setup.py`: This file is used to configure the project for packaging and distribution.
* `template.py`: This file contains the code for the Flask template used to render the prediction form.

## Running the Project

To run the project, follow these steps:

1. **Install dependencies:** Make sure you have Python and the required dependencies installed. You can install the dependencies by running the following command in the project directory:

   ```bash
   pip install -r requirements.txt

2. Run the Flask application: Start the Flask development server by running the following command:

    ```bash 
    python main.py

3. Running Unit Tests: 
   ```bash 
   pytest test_api.py
   pytest test_model.py

