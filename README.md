# Driver Churn Prediction with Flask

This project  predicts driver churn using a Flask application. The project utilizes various machine learning models to identify factors that contribute to driver churn and develop a model to predict which drivers are likely to churn.

## Demo Video

https://github.com/user-attachments/assets/fccde530-34f8-447e-81e5-4325d7897324


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

1. **Create a virtual environment:**
   Choose one of the following methods to create a Python 3.9 environment:

   - **Using Conda:**
     ```bash
     conda create --name driver-churn-predictor python=3.9
     conda activate driver-churn-predictor
     ```

   - **Using Python `venv` module:**
     ```bash
     python3 -m venv driver-churn-env
     source driver-churn-env/bin/activate  # On Windows, use `driver-churn-env\Scripts\activate`
     ```

2. **Install dependencies:** After creating the virtual environment, install the required dependencies by running the following command in the project directory:

   ```bash
   pip install -r requirements.txt
   ```

   **Note for macOS users:** XGBoost requires `libomp` for parallel computation. You need to install `libomp` via Homebrew:
   
   ```bash
   brew install libomp
   ```

   If you encounter issues with `libomp` not being found, ensure that your environment is set up correctly by adding the following to your `.zshrc` or `.bashrc`:

   ```bash
   export LIBOMP_PATH=$(brew --prefix libomp)/lib
   export DYLD_LIBRARY_PATH=$LIBOMP_PATH:$DYLD_LIBRARY_PATH
   ```

   Reload your shell configuration:
   ```bash
   source ~/.zshrc   # for zsh users
   # or
   source ~/.bashrc  # for bash users
   ```

3. **Run the Flask application:** Start the Flask development server by running:

    ```bash 
    python main.py
    ```

4. **Running Unit Tests:**
   To run the unit tests for the project, use the following commands:
   
   ```bash
   pytest test_api.py
   pytest test_model.py
   ```

5. **Running with Docker:**

   - **Build the Docker image:** In your project root directory, run the following command:
     ```bash
     docker build -t driver-churn-predictor .
     ```

   - **Run the Docker container:** After building the image, run the container:
     ```bash
     docker run -p 8000:8000 driver-churn-predictor
     ```

   - **Access the application:** Open your web browser and navigate to `http://localhost:8000` to access the Flask application.
