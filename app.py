import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Define file paths
MODEL_PATH = "best_IGE_model.pkl"
SCALER_PATH = "scaler.pkl"
IMAGE_PATH = "Haneef Picture.png"

# Placeholder for correct feature names
FEATURE_NAMES = [
    "gdp_per_capita", "gini_coefficient", "income_share_top_10_percent", 
    "income_share_bottom_10_percent", "educational_attainment", 
    "unemployment_rate", "healthcare_expenditure", "inflation_rate", 
    "urban_population_share", "foreign_direct_investment"
]

# Function to load objects (model/scaler)
def load_object(file_path, object_type="object"):
    try:
        obj = joblib.load(file_path)
        st.success(f"{object_type.capitalize()} loaded successfully from {file_path}.")
        return obj
    except FileNotFoundError:
        st.error(f"{object_type.capitalize()} file not found: {file_path}. Please ensure it is uploaded.")
        return None
    except Exception as e:
        st.error(f"Error loading {object_type}: {e}")
        return None

# Load the model and scaler
st.info("Loading the model and scaler...")
model = load_object(MODEL_PATH, "model")
scaler = load_object(SCALER_PATH, "scaler")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Resume", "Projects", "Intergenerational Income Mobility Predictor"])

# Home page
if page == "Home":
    st.title("Welcome to Haneefuddin Rasheed's Homepage")
    st.write("Hello! I am Haneefuddin Rasheed, a data scientist with a passion for understanding and predicting socio-economic trends.")
    
    # Display local image
    try:
        image = Image.open(IMAGE_PATH)
        st.image(image, caption="Haneefuddin Rasheed", use_container_width=True)
    except FileNotFoundError:
        st.error("Image file not found. Please ensure it is in the project directory.")

    st.write("### Contact Information")
    st.write("Email: h3rasheed@gmail.com")
    st.write("Phone: (226) 791-1310")
    st.write("Location: London, Ontario")

# Resume page
elif page == "Resume":
    st.title("Resume")
    st.write("## Haneefuddin Rasheed - Data Specialist")
    st.write("""
    ### Professional Experience
    **Business Intelligence Analyst**
    - Developed interactive dashboards visualizing HR metrics.
    - Conducted survival analysis to improve organizational stability.
    
    **Marketing and Sales Manager**
    - Led SaaS expansion into the Canadian market.
    - Forged strategic partnerships to enhance brand awareness.
    """)

# Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title("Intergenerational Income Mobility Predictor")
    
    if model and scaler:
        st.write("Enter the following socio-economic indicators:")
        
        inputs = []
        for feature in FEATURE_NAMES:
            value = st.number_input(f"Enter {feature.replace('_', ' ').title()}:", value=0.0)
            inputs.append(value)
        
        if st.button("Predict"):
            try:
                inputs_scaled = scaler.transform([inputs])  # Scale the inputs
                prediction = model.predict(inputs_scaled)
                st.success(f"Predicted outcome: {prediction[0]}")
            except Exception as e:
                st.error(f"Error during prediction: {e}")
    else:
        st.error("Model and/or scaler not loaded. Please check the files.")
