import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Define file paths
MODEL_PATH = "best_IGE_model.pkl"
SCALER_PATH = "scaler.pkl"
IMAGE_PATH = "Haneef Picture.png"
RESUME_PATH = "HR_Resume.pdf"

# Correct feature names
FEATURE_NAMES = [
    "parent_income", "education_years", "region_code", "employment_status", "gender", "age"
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
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Resume", "Projects", "Intergenerational Income Mobility Predictor"]
)

# Home page
if page == "Home":
    st.title("Welcome to Haneefuddin Rasheed's Homepage")
    st.write(
        "Hello! I am Haneefuddin Rasheed, a data scientist with a passion for understanding "
        "and predicting socio-economic trends. This web application showcases my work and projects."
    )
    
    # Display local image
    try:
        image = Image.open(IMAGE_PATH)  # Ensure 'Haneef Picture.png' is in your project directory
        st.image(image, caption="Haneefuddin Rasheed", use_column_width=True)
    except FileNotFoundError:
        st.error(f"Image file not found: {IMAGE_PATH}. Please ensure it is in the project directory.")
    
    st.write("### Contact Information")
    st.write("Email: h3rasheed@gmail.com")
    st.write("Phone: (226) 791-1310")
    st.write("Location: London, Ontario")

# Resume page
elif page == "Resume":
    st.title("Resume")
    
    # Display local resume file
    try:
        with open(RESUME_PATH, "rb") as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="Haneef_Rasheed_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error(f"Resume file not found: {RESUME_PATH}. Please ensure it is in the project directory.")
    
    st.write("## HANEEF RASHEED")
    st.write("### DATA SPECIALIST")
    st.write("### Professional Experience")
    st.write("**Business Intelligence Analyst**")
    st.write("London, ON | 2023 – 2024")
    st.write("""
    - Led a Span of Control Optimization project aimed at reducing high turnover rates among clinical leaders 
      by providing HR executives with actionable insights through prescriptive analytics.
    ...
    """)

# Intergenerational Income Mobility Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title("Intergenerational Income Mobility Predictor")
    st.write(
        "This tool predicts intergenerational income mobility based on factors such as parental income, education level, "
        "region, employment status, gender, and age."
    )
    
    # User input
    try:
        parent_income = st.number_input("Parent Income (in USD)", min_value=0, value=50000, step=1000)
        education_years = st.number_input("Years of Education", min_value=0, max_value=30, value=12)
        region_code = st.selectbox("Region Code", options=[1, 2, 3, 4, 5])  # Adjust options as needed
        employment_status = st.selectbox("Employment Status", options=["Unemployed", "Employed", "Self-Employed"])
        gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
        age = st.slider("Age", min_value=18, max_value=80, value=30)
        
        # Encode inputs if necessary
        employment_mapping = {"Unemployed": 0, "Employed": 1, "Self-Employed": 2}
        gender_mapping = {"Male": 0, "Female": 1, "Other": 2}
        
        employment_status_encoded = employment_mapping[employment_status]
        gender_encoded = gender_mapping[gender]

        # Input feature array
        features = np.array([[parent_income, education_years, region_code, employment_status_encoded, gender_encoded, age]])
        
        # Scale features
        if scaler:
            features_scaled = scaler.transform(features)
        else:
            st.warning("Scaler not available. Proceeding with unscaled features.")
            features_scaled = features
        
        # Predict
        if model:
            prediction = model.predict(features_scaled)
            st.write(f"### Predicted Income: ${prediction[0]:,.2f}")
        else:
            st.error("Model not available. Unable to make predictions.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
