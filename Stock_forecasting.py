#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pickle
import numpy as np

# Title of the app
st.title("Apple Stock Price Forecasting")
st.write("Forecast Apple stock prices for a specified number of days based on historical data.")

# Function to load the model, scaler, and initial input sequence
#@st.cache_data
def load_model_and_scaler(model_path, scaler_path, x_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        with open(x_path, 'rb') as x_file:
            X = pickle.load(x_file)
        return model, scaler, X
    except Exception as e:
        st.error(f"Error loading files: {e}")
        return None, None, None

# Load the model, scaler, and initial sequence
model_path = r"lstm_model.pkl"
scaler_path = r"scaler"
x_path = r"X_scaled"
model, scaler, x = load_model_and_scaler(model_path, scaler_path, x_path)

# Input for the number of forecast days
steps = st.number_input(
    "Enter the number of days you want to forecast (post 2019-12-30):",
    min_value=1,
    value=30,
    step=1,
    help="Specify the number of future days to forecast."
)

# Function to generate forecast
def generate_forecast(model, scaler, x, steps):
    try:
        # Start with the last known sequence
        last_sequence = np.expand_dims(x[-1], axis=0)  # Shape (1, 90, 1)
        forecasted_values = []

        for _ in range(steps):
            # Predict the next value
            next_pred = model.predict(last_sequence)[0][-1]  # Assuming (1, 1)
            forecasted_values.append(next_pred)  # Collect prediction

            # Update the sequence with the new prediction
            next_input = np.array(next_pred).reshape(1, 1, 1)
            last_sequence = np.append(last_sequence[:, 1:, :], next_input, axis=1)  # Slide the window

        # Inverse scale the predictions to original scale
        forecasted_values_unscaled = scaler.inverse_transform(np.array(forecasted_values).reshape(-1, 1))
        return forecasted_values_unscaled
    except Exception as e:
        st.error(f"Error generating forecast: {e}")
        return None

# Button to trigger the forecast
if st.button("Generate Forecast"):
    if model and scaler and x is not None:
        forecast_result = generate_forecast(model, scaler, x, steps)
        if forecast_result is not None:
            # Display results in a table
            st.write(f"### Forecast for the next {steps} days:")
            forecast_table = {f"Day {i+1}": value[0] for i, value in enumerate(forecast_result)}
            st.dataframe(forecast_table, width=500, height=400)
    else:
        st.error("Model, scaler, or input sequence could not be loaded. Please check the file paths.")
