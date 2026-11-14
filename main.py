from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Mental Health Score Predictor",
    description="API for predicting mental health scores",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)
model = joblib.load("mental_health_pipeline_compressed.pkl")
class PredictionInput(BaseModel):
    Age: int
    Gender: str
    Country: str
    Academic_Level: str
    Most_Used_Platform: str
    Purpose_Of_Use: str
    Avg_Daily_Usage_Hours: float
    Daily_Unlocks: int
    Study_Hours: float
    Physical_Activity_Hours: float
    Sleep_Hours_Per_Night: float
    Stress_Level: str

top_countries = [
    "Canada", "USA", "India",
    "Australia", "UK", "Germany",
    "France", "Mexico", "Turkey"
]

@app.get("/")
def home():
    return {"message": "Mental Health Score Predictor API is running!"}
@app.post("/predict")
def predict(data: PredictionInput):

    input_data = data.model_dump()

    country = input_data["Country"]

    if country in top_countries:
        input_data["Grouped_country"] = country
    else:
        input_data["Grouped_country"] = "Other"

    df_input = pd.DataFrame([input_data])

    prediction = model.predict(df_input)

    return {
        "predicted_mental_health_score": round(float(prediction[0]), 2)
    }
