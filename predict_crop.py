import streamlit as st
import pickle 
import numpy as np
import sklearn

def load_model():
    with open("decisionClassifier.pkl","rb") as file:
        model=pickle.load(file)
        return model

model=load_model();

def show_pridict_page():
    st.title("Crop Prediction website")

    st.write("""### We need some information to predict the crop""")

    N = st.number_input(
        label="Enter value of Nitrogen:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    P = st.number_input(
        label="Enter value of Phosporus:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    K = st.number_input(
        label="Enter value of Calsium:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    T = st.number_input(
        label="Enter value of Temperture:",
        value=0.0,          # Default value
        format="%.2f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    H = st.number_input(
        label="Enter value of Humidity:",
        value=0.0,          # Default value
        format="%.2f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    PH = st.number_input(
        label="Enter value of PH:",
        value=0.0,          # Default value
        format="%.2f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    Rain_fall = st.number_input(
        label="Enter value of RainFall:",
        value=0.0,          # Default value
        format="%.2f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )

    ok=st.button("Predict Crop")
    if ok:
        
        pred=model.predict([[N,P,K,T,H,PH,Rain_fall]])
        crop_text1 = ', '.join(pred)
        st.subheader(f"The predicted crop by model is {crop_text1}")