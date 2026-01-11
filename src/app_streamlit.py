import streamlit as st
import requests

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Inventory Demand Forecast",
    layout="centered"
)

st.title("📦 Inventory Demand Forecast")
st.write("Predict expected units sold using ML model")

# =========================
# Input Form
# =========================
with st.form("prediction_form"):

    Store_ID = st.text_input("Store ID", "S001")
    Product_ID = st.text_input("Product ID", "P001")

    Category = st.selectbox(
        "Category",
        ["Groceries", "Electronics", "Clothing", "Toys"]
    )

    Region = st.selectbox(
        "Region",
        ["North", "South", "East", "West"]
    )

    Inventory_Level = st.number_input("Inventory Level", min_value=0, value=200)
    Units_Ordered = st.number_input("Units Ordered", min_value=0, value=50)
    Demand_Forecast = st.number_input("Demand Forecast", value=120.0)

    Price = st.number_input("Price", value=50.0)
    Discount = st.number_input("Discount (%)", value=10.0)

    Weather_Condition = st.selectbox(
        "Weather Condition",
        ["Sunny", "Rainy", "Cloudy", "Snowy"]
    )

    Holiday_Promotion = st.selectbox(
        "Holiday / Promotion",
        [0, 1]
    )

    Competitor_Pricing = st.number_input(
        "Competitor Pricing", value=48.0
    )

    Seasonality = st.selectbox(
        "Seasonality",
        ["Winter", "Spring", "Summer", "Autumn"]
    )

    Month = st.selectbox("Month", list(range(1, 13)))
    DayOfWeek = st.selectbox("Day of Week", list(range(0, 7)))

    submit = st.form_submit_button("🔮 Predict")

# =========================
# API Call
# =========================
if submit:
    payload = {
        "Store_ID": Store_ID,
        "Product_ID": Product_ID,
        "Category": Category,
        "Region": Region,
        "Inventory_Level": Inventory_Level,
        "Units_Ordered": Units_Ordered,
        "Demand_Forecast": Demand_Forecast,
        "Price": Price,
        "Discount": Discount,
        "Weather_Condition": Weather_Condition,
        "Holiday_Promotion": Holiday_Promotion,
        "Competitor_Pricing": Competitor_Pricing,
        "Seasonality": Seasonality,
        "Month": Month,
        "DayOfWeek": DayOfWeek
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"📈 Predicted Units Sold: {result['predicted_units_sold']}")
        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"🚨 Connection Error: {e}")
