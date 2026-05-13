from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease risk levels",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)