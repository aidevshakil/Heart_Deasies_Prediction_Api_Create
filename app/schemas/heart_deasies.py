from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Union

class HeartDiseaseInput(BaseModel):
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "age": 52,
            "sex": 1,
            "dataset": 0,
            "cp": 0,
            "trestbps": 125,
            "chol": 212,
            "fbs": 0,
            "restecg": 1,
            "thalch": 168,
            "exang": 0,
            "oldpeak": 1.0,
            "slope": 2,
            "ca": 2,
            "thal": 3
        }
    })

    age: int = Field(..., ge=0, le=120, description="Age in years")
    sex: int = Field(..., ge=0, le=1, description="Gender (0=female, 1=male)")
    dataset: int = Field(..., ge=0, le=3, description="Dataset source")
    cp: int = Field(..., ge=0, le=3, description="Chest pain type")
    trestbps: float = Field(..., ge=0, description="Resting blood pressure")
    chol: float = Field(..., ge=0, description="Serum cholesterol")
    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar")
    restecg: int = Field(..., ge=0, le=2, description="Resting ECG results")
    thalch: float = Field(..., ge=0, description="Maximum heart rate")
    exang: int = Field(..., ge=0, le=1, description="Exercise induced angina")
    oldpeak: float = Field(..., description="ST depression induced by exercise")
    slope: int = Field(..., ge=0, le=2, description="Slope of peak exercise ST segment")
    ca: float = Field(..., ge=0, le=4, description="Number of major vessels")
    thal: float = Field(..., ge=0, le=3, description="Thalassemia")

class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="Numeric prediction class")
    condition: str = Field(..., description="Heart disease condition description")
    risk_level: str = Field(..., description="Risk level assessment")
    probability: Dict[str, float] = Field(..., description="Probability for each class")