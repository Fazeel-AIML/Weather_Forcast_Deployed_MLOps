from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import joblib
import os
import boto3
from src.config.config import (
    MODEL_PATH, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET,
    NUMERICAL_COLUMNS, TARGET_COLUMN
)

# Initialize FastAPI app
app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Initialize S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def download_model_from_s3():
    """Download the latest model from S3 if it's not available locally."""
    if not os.path.exists(MODEL_PATH):
        try:
            print(f"📥 Downloading model from S3 bucket: {S3_BUCKET}")
            s3_client.download_file(S3_BUCKET, os.path.basename(MODEL_PATH), MODEL_PATH)
            print("✅ Model downloaded successfully from S3")
        except Exception as e:
            print(f"❌ Failed to download model: {e}")
            raise

# Download model on startup
download_model_from_s3()

# Load model
model = joblib.load(MODEL_PATH)

@app.get("/")
def home(request: Request):
    """Render the homepage with input form."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(
    request: Request,
    summary: int  = Form(...),
    temperature: float = Form(...),
    apparent_temperature: float = Form(...),
    humidity: float = Form(...),
    wind_speed: float = Form(...),
    wind_bearing: int = Form(...),
    visibility: float = Form(...),
    pressure: float = Form(...)
):
    """Make precipitation type prediction based on weather data."""
    
    # Create DataFrame with correct feature names
    input_data = pd.DataFrame([{
        "Summary":summary,
        "Temperature (C)": temperature,
        "Apparent Temperature (C)": apparent_temperature,
        "Humidity": humidity,
        "Wind Speed (km/h)": wind_speed,
        "Wind Bearing (degrees)": wind_bearing,
        "Visibility (km)": visibility,
        "Pressure (millibars)": pressure
    }])


    # Predict precipitation type (Rain/Snow)
    prediction = model.predict(input_data)[0]
    if str(prediction) == "0":
        prediction = "Expected Rain"
    elif str(prediction) == "1":
        prediction = "Expected Snow"
    else:
        prediction = "Clean"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": prediction}
    )
