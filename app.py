import streamlit as st
import joblib
import numpy as np
from PIL import Image
import os

# Helper function to safely load files
def safe_load(file_path, file_type="model"):
    try:
        return joblib.load(file_path)
    except Exception as e:
        st.error(f"Failed to load {file_type} from {file_path}. Please check the file format and dependencies.")
        st.stop()

# Paths to model and scaler files
model_path = 'best_IGE_model.pkl'
scaler_path = 'scaler.pkl'

# Check if model and scaler files exist
if os.path.exists(model_path) and os.path.exists(scaler_path):
    model = safe_load(model_path, "model")
    scaler = safe_load(scaler_path, "scaler")
else:
    st.error("Model or scaler files are missing. Ensure 'best_IGE_model.pkl' and 'scaler.pkl' are in the project directory.")
    st.stop()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Resume", "Projects", "Intergenerational Income Mobility Predictor"])

# Home page
if page == "Home":
    st.title('Welcome to Haneefuddin Rasheed\'s Homepage')
    st.write('Hello! I am Haneefuddin Rasheed, a data scientist with a passion for understanding and predicting socio-economic trends. This web application showcases my work and projects.')
    
    # Display local image
    try:
        image = Image.open('Haneef Picture.png')  # Ensure 'Haneef Picture.png' is in your project directory
        st.image(image, caption='Haneefuddin Rasheed', use_column_width=True)
    except FileNotFoundError:
        st.warning("Image file 'Haneef Picture.png' is missing. Please add it to the project directory.")
    
    st.write('### Contact Information')
    st.write('Email: h3rasheed@gmail.com')
    st.write('Phone: (226) 791-1310')
    st.write('Location: London, Ontario')

# Resume page
elif page == "Resume":
    st.title('Resume')
    
    # Display local resume file
    resume = 'HR_Resume.pdf'  
    try:
        with open(resume, 'rb') as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name=resume,
                mime='application/pdf'
            )
    except FileNotFoundError:
        st.warning("Resume file 'HR_Resume.pdf' is missing. Please add it to the project directory.")

    # Add your resume content here (truncated for brevity)
    st.write('### Professional Experience and Education')

# Projects page
elif page == "Projects":
    st.title('Projects')
    st.write('### General Projects')
    st.write('Links to other completed projects will be provided through my [GitHub profile](https://github.com/your_github_profile).')

# Intergenerational Income Mobility Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title('Intergenerational Income Mobility Predictor')
    st.write('Enter the socio-economic factors to predict intergenerational income mobility.')

    # Input fields for the features
    gdp_per_capita = st.number_input('GDP per Capita')
    gini_coefficient = st.number_input('Gini Coefficient')
    income_share_top_10 = st.number_input('Income Share of the Top 10%')
    poverty_headcount_ratio = st.number_input('Poverty Headcount Ratio')
    income_share_lowest_20 = st.number_input('Income Share Held by Lowest 20%')
    school_enrollment_primary = st.number_input('School Enrollment, Primary (% net)')
    school_enrollment_secondary = st.number_input('School Enrollment, Secondary (% net)')
    educational_attainment_primary = st.number_input('Educational Attainment, Primary')
    unemployment_total = st.number_input('Unemployment, Total (% of labor force)')

    # Predict button
    if st.button('Predict'):
        try:
            input_data = np.array([[gdp_per_capita, gini_coefficient, income_share_top_10, poverty_headcount_ratio, 
                                    income_share_lowest_20, school_enrollment_primary, school_enrollment_secondary, 
                                    educational_attainment_primary, unemployment_total]])
            input_data = scaler.transform(input_data)
            prediction = model.predict(input_data)
            st.write(f'Predicted Intergenerational Income Mobility: {prediction[0]}')
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
