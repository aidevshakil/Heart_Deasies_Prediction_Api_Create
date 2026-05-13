from fastapi import APIRouter, HTTPException
from app.schemas.heart_deasies import HeartDiseaseInput, PredictionResponse
from app.utils.util_model import HeartDiseasePredictor

router = APIRouter()
model = HeartDiseasePredictor()

@router.post("/predict", response_model=PredictionResponse, summary="Predict Heart Disease")
async def predict_heart_disease(input_data: HeartDiseaseInput):
    """
    Predict heart disease risk based on patient data
    
    - **Input**: Patient medical data
    - **Returns**: Prediction results including risk level and probabilities
    """
    try:
        prediction = model.predict(input_data.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}