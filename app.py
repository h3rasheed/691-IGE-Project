import joblib
import streamlit as st
import numpy as np

# Load the model with error handling
try:
    model = joblib.load('best_IGE_model.pkl')
except FileNotFoundError:
    st.error("The model file 'best_IGE_model.pkl' was not found.")
except joblib.externals.loky.process_executor.TerminatedWorkerError:
    st.error("The model file might be corrupted or incompatible.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# Ensure the rest of your app.py script follows after the model loading section
