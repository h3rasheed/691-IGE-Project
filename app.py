import streamlit as st
import numpy as np
import joblib

# Load the model with error handling
try:
    model = joblib.load('best_IGE_model.pkl')
except FileNotFoundError:
    st.error("The model file 'best_IGE_model.pkl' was not found.")
except joblib.externals.loky.process_executor.TerminatedWorkerError:
    st.error("The model file might be corrupted or incompatible.")
except AttributeError as e:
    if "Can't get attribute '__pyx_unpickle_CyHalfSquaredError'" in str(e):
        st.error("The model file is incompatible with the current version of scikit-learn. Please re-save the model with the current version.")
    else:
        st.error(f"An unexpected error occurred: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# Education page content
st.write('### Education')
st.write('**M.S. D.S. in Data Science**')
st.write('Eastern University, Saint Davids, Pennsylvania | 2023 – 12/24')

st.write('**Post-Graduate Diploma in Artificial Intelligence for Business**')
st.write('The University of Texas, Austin, Texas | 2021')

st.write('**B.A. in Economics**')
st.write('University of Waterloo, Waterloo, ON | 2012 – 2016')

st.write('### Computer & Other Skills')
st.write('''
- Proficient with Microsoft Word, Excel, Power Point
- Familiar with Git, SAP, and SharePoint
- Languages: Python/R-Proficient 
- Visualizations: PowerBI/Tableau
- Databases: PostgreSQL/T-SQL
- ML/AI: Scikit-Learn/TensorFlow
- Cloud Computing: Azure/AWS
- Operating Systems: Windows/Linux
- Big Data: PySpark
- Human Resources Info Systems
- Healthcare Data Governance
- Environmental Awareness
- Business Acumen
- Data Ethics
''')

st.write('### Certifications and Licenses')
st.write('**DP-203 Microsoft Certified: Azure Data Engineer Associate**')
st.write('Certificate ID: 929933661')

# Projects page
page = st.sidebar.selectbox("Select Page", ["Education", "Projects", "Intergenerational Income Mobility Predictor"])

if page == "Projects":
    st.title('Projects')
    st.write('### General Projects')
    st.write('Links to other completed projects will be provided through my [GitHub profile](https://github.com/h3rasheed).')

# Intergenerational Income Mobility Predictor page
elif page == "Intergenerational Income Mobility Predictor":
    st.title('Intergenerational Income Mobility Predictor')
    st.write('Enter the socio-economic factors to predict intergenerational income mobility.')

    # Input fields for the features
    educational_attainment_primary = st.number_input('Educational attainment, at least completed primary (% of relevant age group)')
    gdp_per_capita = st.number_input('GDP per Capita')
    gini_coefficient = st.number_input('Gini Coefficient')
    income_share_lowest_20 = st.number_input('Income Share Held by Lowest 20%')
    income_share_top_10 = st.number_input('Income Share of the Top 10%')
    poverty_headcount_ratio = st.number_input('Poverty Headcount Ratio')
    school_enrollment_primary = st.number_input('School Enrollment, Primary (% net)')
    school_enrollment_secondary = st.number_input('School Enrollment, Secondary (% net)')
    unemployment_total = st.number_input('Unemployment, Total (% of total labor force)')
    gdp_per_capita_lag = st.number_input('GDP per Capita (Lagged)')

    # Predict button
    if st.button('Predict'):
        input_data = np.array([[educational_attainment_primary, gdp_per_capita, gini_coefficient, income_share_lowest_20, income_share_top_10, poverty_headcount_ratio, school_enrollment_primary, school_enrollment_secondary, unemployment_total, gdp_per_capita_lag]])
        input_data = scaler.transform(input_data)
        prediction = model.predict(input_data)
        st.write(f'Predicted Intergenerational Income Mobility (IGE): {prediction[0]}')

    # Explanation of IGE value
    st.write("""
    ### How to Interpret the IGE Value
    The Intergenerational Income Elasticity (IGE) value is a measure of the degree to which income status is transmitted from one generation to the next. 
    - **High IGE value**: Indicates low intergenerational mobility, meaning that children’s incomes are highly dependent on their parents’ incomes.
    - **Low IGE value**: Indicates high intergenerational mobility, meaning that children’s incomes are less dependent on their parents’ incomes.
    The value ranges from 0 to 1, where 0 represents perfect mobility (no relationship between parents’ and children’s incomes) and 1 represents perfect immobility (children’s incomes are completely determined by their parents’ incomes).
    """)
