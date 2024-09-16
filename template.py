import os 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')

list_of_files = [
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    ".gitignore",
    "README.md",

    "app/__init__.py",
    "app/main.py",

    "app/models/__init__.py",
    "app/models/decision_tree.py",
    "app/models/random_forest.py",
    "app/models/xgboost_model.py",
    "app/models/lightgbm_model.py",

    "app/utils/__init__.py",
    "app/utils/data_preprocessing.py",
    "app/utils/model_utils.py",

    "app/api/__init__.py",
    "app/api/endpoints.py",

    "test/__init__.py",
    "test/test_model.py",
    "test/test_api.py",

    "artifact/.gitkeep"

]



for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    # for dir
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")
    # for files 
    if not os.path.exists(filepath) or os.path.getsize(filepath)==0:
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exist")





