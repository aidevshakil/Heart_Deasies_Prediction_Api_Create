import joblib
import pandas as pd
from pathlib import Path
from typing import Dict, Any

class HeartDiseasePredictor:
    HEART_DISEASE_CATEGORIES = {
        0: "No heart disease (Healthy)",
        1: "Mild heart disease",
        2: "Moderate heart disease",
        3: "Severe heart disease",
        4: "Very severe heart disease"
    }

    def __init__(self):
        model_path = Path("C:/Users/USER/Desktop/mealPlaneAPICreate/models/LogisticRegression_20250311_150614.joblib")
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found at {model_path}")
        self.model = joblib.load(model_path)
        self.features = [
            "age", "sex", "dataset", "cp", "trestbps", "chol",
            "fbs", "restecg", "thalch", "exang", "oldpeak",
            "slope", "ca", "thal"
        ]

    def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Create DataFrame with correct feature order
            input_df = pd.DataFrame([input_data], columns=self.features)
            
            # Make prediction
            prediction = self.model.predict(input_df)[0]
            probability = self.model.predict_proba(input_df)[0]
            
            return {
                'prediction': int(prediction),
                'condition': self.HEART_DISEASE_CATEGORIES[prediction],
                'probability': {
                    self.HEART_DISEASE_CATEGORIES[i]: float(p) 
                    for i, p in enumerate(probability)
                },
                'risk_level': 'High' if prediction > 0 else 'Low'
            }
        except Exception as e:
            raise ValueError(f"Prediction error: {str(e)}")