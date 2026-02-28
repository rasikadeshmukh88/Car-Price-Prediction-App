import streamlit as st
import pandas as pd
import joblib
import numpy as np
model = joblib.load("car_price_model.joblib")
st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Predict the selling price of a used car using Machine Learning")
st.header("Enter Car Details")

name = st.text_input("Car Name", "Maruti Swift")

km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=45000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])

seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

owner = st.selectbox(
    "Owner Type",
    ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"]
)

mileage = st.number_input("Mileage (km/ltr)", min_value=5.0, max_value=50.0, value=22.0)

engine = st.number_input("Engine (CC)", min_value=500, max_value=5000, value=1197)

max_power = st.number_input("Max Power (bhp)", min_value=20.0, max_value=500.0, value=82.0)

seats = st.selectbox("Seats", [2, 4, 5, 6, 7])

car_age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)


input_data = pd.DataFrame({
    'name': [name],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner],
    'mileage(km/ltr/kg)': [mileage],
    'engine': [engine],
    'max_power': [max_power],
    'seats': [seats],
    'car_age': [car_age]
})
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Car Price: ₹ {int(prediction[0]):,}")
