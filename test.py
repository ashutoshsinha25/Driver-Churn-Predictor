# from app.models.decision_tree import DecisionTreeModel
import joblib 
import pandas as pd 
import inspect

def get_init_attributes(cls):
    init_method = cls.__init__
    source = inspect.getsource(init_method)
    attributes = set()
    for line in source.split('\n'):
        if line.strip().startswith('self.'):
            parts = line.split('=')
            if len(parts) > 1:
                attribute = parts[0].strip().replace('self.', '')
                attributes.add(attribute)
    
    return attributes

class PredictionPipeline:
  def __init__(self, model, scaler, encoder):
    self.model = model 
    self.scaler = scaler 
    self.encoder = encoder
  
  def predict(self, X):
    X_en = self.encoder.transform(X)
    X_scaled = self.scaler.transform(X_en)
    return self.model.predict(X_scaled)
  

path = "artifacts/decision_tree.joblib"
model = joblib.load(path)

attributes = get_init_attributes(model)
print(attributes)