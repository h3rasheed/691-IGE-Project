import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Feature names used during model training
FEATURE_NAMES = ["age", "education", "income", "employment", "region", "family_size", 
                 "parent_income", "parent_education", "parent_employment", "parent_region"]

# Helper function to load the model and scaler
@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load("best_IGE_model.pkl")
        st.success("Model loaded successfully from best_IGE_model.pkl.")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        model = None
    try:
        scaler = joblib.load("scaler.pkl")
        st.success("Scaler loaded successfully from scaler.pkl.")
    except Exception as e:
        st.error(f"Error loading scaler: {e}")
        scaler = None
    return model, scaler

# Load the model and scaler
st.info("Loading the model and scaler...")
model, scaler = load_model_and_scaler()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Resume", "Projects", "Intergenerational Income Mobility Predictor"])

# Home page
if page == "Home":
    st.title("Welcome to Haneefuddin Rasheed's Homepage")
    st.write("Hello! I am Haneefuddin Rasheed, a data scientist with a passion for understanding and predicting socio-economic trends. This web application showcases my work and projects.")
    image = Image.open("Haneef Picture.png")
    st.image(image, caption="Haneefuddin Rasheed", use_container_width=True)
    st.write("### Contact Information")
    st.write("Email: h3rasheed@gmail.com")
    st.write("Phone: (226) 791-1310")
    st.write("Location: London, Ontario")

# Resume page
elif page == "Resume":
    st.title("Resume")
    st.write("### HANEEF RASHEED")
    st.write("### DATA SPECIALIST")
    st.write("Professional Experience and details directly provided here in text format.")
    st.write("...")

# Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title("Intergenerational Income Mobility Predictor")
    
    if not model or not scaler:
        st.error("Model and/or scaler not loaded. Please check the files.")
    else:
        st.subheader("Enter the following details for prediction:")
        
        # User inputs
        inputs = []
        for feature in FEATURE_NAMES:
            value = st.number_input(f"Enter {feature.capitalize()}:", value=0.0)
            inputs.append(value)

        if st.button("Predict"):
            try:
                inputs_scaled = scaler.transform([inputs])  # Scale the inputs
                prediction = model.predict(inputs_scaled)[0]
                
                # Display the prediction
                st.success(f"Predicted IGE Value: {prediction:.2f}")
                
                # Interpretation section
                st.write("### How to Interpret the Predicted IGE Value:")
                st.write(
                    "- **IGE (Intergenerational Income Elasticity)** measures the relationship between parents' income and their children's income.\n"
                    "- A value closer to **0** suggests high income mobility, indicating that a child's income is less dependent on their parents' income.\n"
                    "- A value closer to **1** suggests low income mobility, meaning that a child's income is strongly influenced by their parents' income."
                )
            except Exception as e:
                st.error(f"Error during prediction: {e}")
