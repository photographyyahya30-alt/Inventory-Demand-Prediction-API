from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# =========================
# Load trained pipeline
# =========================
model = joblib.load("note_books/demand_forecast_model.pkl")

# =========================
# FastAPI app
# =========================
app = FastAPI(title="Inventory Demand Forecast API")


# =========================
#السمح بالطلبات من أي مصدر
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"], 
)
# =========================
# Input Schema (Pydantic)
# =========================
class InputData(BaseModel):
    Store_ID: str
    Product_ID: str
    Category: str
    Region: str
    Inventory_Level: int
    Units_Ordered: int
    Demand_Forecast: float
    Price: float
    Discount: float
    Weather_Condition: str
    Holiday_Promotion: int
    Competitor_Pricing: float
    Seasonality: str
    Month: int
    DayOfWeek: int

# =========================
# Prediction Endpoint
# =========================
@app.post("/predict")
def predict_units_sold(data: InputData):

    # Convert input to DataFrame
    input_df = pd.DataFrame([{
        "Store ID": data.Store_ID,
        "Product ID": data.Product_ID,
        "Category": data.Category,
        "Region": data.Region,
        "Inventory Level": data.Inventory_Level,
        "Units Ordered": data.Units_Ordered,
        "Demand Forecast": data.Demand_Forecast,
        "Price": data.Price,
        "Discount": data.Discount,
        "Weather Condition": data.Weather_Condition,
        "Holiday/Promotion": data.Holiday_Promotion,
        "Competitor Pricing": data.Competitor_Pricing,
        "Seasonality": data.Seasonality,
        "Month": data.Month,
        "DayOfWeek": data.DayOfWeek
    }])

    # Prediction
    prediction = model.predict(input_df)

    return {
        "predicted_units_sold": round(float(prediction[0]), 2)
    }

# =========================
# Health Check
# =========================
@app.get("/")
def root():
    return {"status": "Inventory Demand Forecast API is running"}
