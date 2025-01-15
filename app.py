import streamlit as st
import joblib
import numpy as np

# Define file paths
MODEL_PATH = "best_IGE_model.pkl"
SCALER_PATH = "scaler.pkl"

# Function to load objects (model/scaler)
def load_object(file_path, object_type="object"):
    try:
        obj = joblib.load(file_path)
        st.success(f"{object_type.capitalize()} loaded successfully from {file_path}.")
        return obj
    except FileNotFoundError:
        st.error(f"{object_type.capitalize()} file not found: {file_path}. Please ensure it is uploaded.")
    except Exception as e:
        st.error(f"Error loading {object_type}: {e}")
        return None

# Streamlit app
st.title("IGE Model Prediction App")

st.info("Attempting to load the model and scaler...")
model = load_object(MODEL_PATH, "model")
scaler = load_object(SCALER_PATH, "scaler")

if not model or not scaler:
    st.error("Model or scaler failed to load. Please check the files.")
else:
    st.success("Model and scaler are ready for predictions!")

# Input section
st.header("Enter Input Features")

try:
    # Replace with the actual feature names used during model training
    feature_1 = st.number_input("Feature 1", value=0.0, step=0.1, format="%.2f")
    feature_2 = st.number_input("Feature 2", value=0.0, step=0.1, format="%.2f")
    feature_3 = st.number_input("Feature 3", value=0.0, step=0.1, format="%.2f")

    # Combine input features into an array
    features = np.array([[feature_1, feature_2, feature_3]])

    if st.button("Predict"):
        if scaler and model:
            scaled_features = scaler.transform(features)  # Scale the features
            prediction = model.predict(scaled_features)  # Make prediction
            st.success(f"Prediction: {prediction[0]}")
        else:
            st.error("Cannot make predictions because model or scaler is missing.")
except Exception as e:
    st.error(f"An error occurred while processing inputs: {e}")
