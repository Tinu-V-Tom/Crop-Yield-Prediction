import streamlit as st
import pickle

# Load the model and preprocesser from pickle files
with open("dtr.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("preprocesser.pkl", "rb") as preprocessor_file:
    preprocesser = pickle.load(preprocessor_file)

# Title of the app
st.title("Crop Yield Prediction Per Country")

# Subtitle
st.subheader("Input All Features Here")

# Input fields
year = st.number_input("Year", min_value=1900, max_value=2100, value=2023)
average_rainfall = st.number_input("Average Rainfall (mm/year)", min_value=0.0, value=0.0)
pesticides = st.number_input("Pesticides (tonnes)", min_value=0.0, value=0.0)
average_temperature = st.number_input("Average Temperature (°C)", min_value=-50.0, max_value=50.0, value=0.0)
area = st.text_input("Area")
item = st.text_input("Item")

# Prediction button
if st.button("Predict"):
    # Create a DataFrame or appropriate input format for your model
    import pandas as pd
    input_data = pd.DataFrame({
        'Year': [year],
        'average_rain_fall_mm_per_year': [average_rainfall],
        'pesticides_tonnes': [pesticides],
        'avg_temp': [average_temperature],
        'Area': [area],
        'Item': [item]
    })

    # Preprocess the input data
    preprocessed_data = preprocesser.transform(input_data)

    # Make the prediction
    prediction = model.predict(preprocessed_data)

# Display the prediction
    st.write(f"Predicted Yield: {prediction[0]}")
