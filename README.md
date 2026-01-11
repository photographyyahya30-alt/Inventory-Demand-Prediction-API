#  Inventory Demand Forecasting System

An end-to-end Machine Learning system designed to predict **inventory demand (units sold)** using historical retail data.

The system is built with:
- **FastAPI** for backend inference
- **XGBoost / AdaBoost** Machine Learning models
- **Streamlit** web application for user interaction

---

##  Problem Overview
Accurate demand forecasting helps businesses:
- **Reduce stock shortages**: Ensure products are available when customers want them.
- **Avoid overstocking**: Minimize capital tied up in excess inventory.
- **Improve inventory planning**: Data-driven decisions for supply chain management.

This project predicts the expected number of units sold based on product, store, pricing, promotions, weather, and seasonality data.

---

##  System Architecture
The system follows a modern decoupled architecture:
1. **Data Pipeline**: Preprocessing, Label Encoding, and Feature Engineering (Lags, Rolling Means).
2. **Model Provider**: Trained XGBoost models saved as artifacts.
3. **Backend API**: FastAPI serving the model predictions via REST endpoints.
4. **Frontend UI**: Streamlit dashboard for interactive visualization and manual prediction.

---

##  Technical Summary & Insights

### **Model Performance**
- **Algorithm**: XGBoost Regressor with Decision Tree base (Depth: 8).
- **R² Score**: ~0.36 (The model captures significant trends but leaves room for external data integration).
- **Stability**: High consistency between Training and Test sets, indicating no overfitting.

### **Key Features (What drives sales?)**
Based on our Feature Importance analysis:
1. **Inventory Level**: The strongest predictor (over 60% importance).
2. **Time Series Lags**: Previous day sales and 7-day averages are crucial.
3. **Price Competition**: Customers are highly sensitive to price differences vs competitors.



---

##  Getting Started

Follow these steps to get the project running on your local machine:

###  Clone the Repository
```bash
git clone [https://github.com/photographyyahya30-alt/Inventory-Demand-Prediction-API.git](https://github.com/photographyyahya30-alt/Inventory-Demand-Prediction-API.git)
cd Inventory-Demand-Prediction-API
