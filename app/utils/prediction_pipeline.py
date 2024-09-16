class PredictionPipeline:
  def __init__(self, model, scaler, encoder):
    self.model = model 
    self.scaler = scaler 
    self.encoder = encoder
  
  def predict(self, X):
    X_en = self.encoder.transform(X)
    X_scaled = self.scaler.transform(X_en)
    return self.model.predict(X_scaled)