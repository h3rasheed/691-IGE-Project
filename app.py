import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Feature names (including the 10th feature "Parental Wealth")
FEATURE_NAMES = [
    "gdp_per_capita",
    "gini_coefficient",
    "income_share_top_10",
    "poverty_headcount_ratio",
    "income_share_lowest_20",
    "school_enrollment_primary",
    "school_enrollment_secondary",
    "educational_attainment_primary",
    "unemployment_total",
    "parental_wealth",  # Contextual and quantifiable feature
]

# Helper function to load the model and scaler
@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load("best_IGE_model.pkl")
        st.success("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        model = None

    try:
        scaler = joblib.load("scaler.pkl")
        st.success("Scaler loaded successfully.")
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
    st.title("Welcome to Haneef Rasheed's Homepage")
    st.write("Hello! I am Haneef Rasheed, a data scientist with a passion for understanding and predicting socio-economic trends. This web application showcases my work and projects.")

    # Display local image
    try:
        image = Image.open("Haneef Picture.png")
        st.image(image, caption="Haneef Rasheed", use_container_width=True)
    except FileNotFoundError:
        st.warning("Image file 'Haneef Picture.png' not found. Please ensure it is in the project directory.")

    st.write("### Contact Information")
    st.write("Email: h3rasheed@gmail.com")
    st.write("Phone: (226) 791-1310")
    st.write("Location: London, Ontario")

# Resume page
elif page == "Resume":
    st.title("Resume")
    st.write("## Haneef Rasheed")
    st.write("### Data Specialist")

    # Professional Experience
    st.write("### Professional Experience")

    st.write("**Business Intelligence Analyst**")
    st.write("London, ON | 2023 – 2024")
    st.write(
        "- Led a Span of Control Optimization project aimed at reducing high turnover rates among clinical leaders by providing HR executives with actionable insights through prescriptive analytics."
        "- Spearheaded the development and maintenance of interactive Power BI dashboards visualizing critical HR metrics like employee turnover, retention, performance, engagement, and satisfaction enhancing decision-making processes."
        "- Integrated diverse data sources (Excel, SQL, SharePoint) using Power BI Desktop and Service; transformed and analyzed data employing DAX and M queries ensuring accurate and actionable insights."
        "- Utilized Python for comprehensive data collection, cleaning, and preparation from various HR data sources addressing challenges of disparate and unstructured data for analytical exploration."
        "- Conducted insightful feature importance analysis to pinpoint critical factors for leader tenure informing targeted interventions to enhance leadership stability and reduce turnover."
    )

    st.write("**Marketing and Sales Manager**")
    st.write("TaskTak, Redmond, WA | 2022 – 2023")
    st.write(
        "- Led the successful expansion into the Canadian market for a SaaS product achieving a remarkable 20% increase in sales in the first year demonstrating effective market penetration and growth strategy execution."
        "- Crafted and executed a comprehensive marketing strategy significantly enhancing brand awareness and customer acquisition across Canada tailored to the unique demands and opportunities of the SaaS industry."
    )

    st.write("**Writer**")
    st.write("Mississauga, ON | 2017 – 2022")
    st.write(
        "- Wrote and published “Instructions to Finding Peace in Pain: An Empirical Narrative” with TellWell Publishing."
        "- Conducted extensive research on topics such as pain management, mindfulness meditation, spirituality, and psychology."
        "- Collected and synthesized patient accounts and journal entries culminating in the publication of a comprehensive medical self-help book."
    )

    st.write("### Education")
    st.write("**M.S. D.S. in Data Science**")
    st.write("Eastern University, Saint Davids, Pennsylvania | 2023 – 12/24")
    st.write("**B.A. in Economics**")
    st.write("University of Waterloo, Waterloo, ON | 2012 – 2016")

    st.write("### Certifications and Licenses")
    st.write("**DP-203 Microsoft Certified: Azure Data Engineer Associate**")
    st.write("Certificate ID: 929933661")

# Projects page
elif page == "Projects":
    st.title("Projects")
    st.write("### General Projects")
    st.write("Links to other completed projects will be provided through my [GitHub profile](https://github.com/your_github_profile).")

# Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title("Intergenerational Income Mobility Predictor")

    if not model or not scaler:
        st.error("Model and/or scaler not loaded. Please check the files.")
    else:
        st.subheader("Enter the following details for prediction:")
        
        # User inputs
        inputs = []
        inputs.append(st.number_input("GDP per Capita"))
        inputs.append(st.number_input("Gini Coefficient"))
        inputs.append(st.number_input("Income Share of the Top 10%"))
        inputs.append(st.number_input("Poverty Headcount Ratio"))
        inputs.append(st.number_input("Income Share Held by Lowest 20%"))
        inputs.append(st.number_input("School Enrollment, Primary (% net)"))
        inputs.append(st.number_input("School Enrollment, Secondary (% net)"))
        inputs.append(st.number_input("Educational Attainment, Primary"))
        inputs.append(st.number_input("Unemployment, Total (% of labor force)"))
        inputs.append(st.number_input("Parental Wealth", value=0.0))  # Quantifiable and contextual feature

        # Prediction
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
