import streamlit as st
import pickle 
import numpy as np
import sklearn
import pandas as pd

def load_model():
    with open("logisticRegression.pkl","rb") as file:
        data=pickle.load(file)
        return data

data=load_model();

model_fert=data["model"];
le_Soil=data["le_soil"];
le_Crop=data["le_crop"];


def show_pridict_fertilizer():
    st.title("Welcome to Fertilizer Prediction ")

    st.write("""### We need some information to predict the Fertilizer""")

    soil=("Loamy","Sandy" ,"Clayey" ,"Black"   ,"Red")
    crop=("Sugarcane" ,"Cotton" ,"Millets"  ,"Paddy"   ,"Pulses" ,"Wheat","Tobacco"  ,"Barley","Oil seeds " ,"Ground Nuts "  
     ,"Maize" )

     

    T = st.number_input(
        label="Enter value of Temperature:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    H = st.number_input(
        label="Enter value of Humidity:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    M = st.number_input(
        label="Enter value of Mositure:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    crop=st.selectbox(" Select Crop",crop)
    soil=st.selectbox(" Select Soil",soil)

    N = st.number_input(
        label="Enter value of Nitrogen:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    P = st.number_input(
        label="Enter value of Potassium:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )
    Ph = st.number_input(
        label="Enter value of Phosphorous:",
        value=0.0,          # Default value
        format="%.1f",     # Format the float to 2 decimal places
        step=1.0            # Step size for increments
    )

    ok=st.button("Predict fertilizer")
    if ok:
       
        X=np.array([[T,H,M,soil,crop,N,P,Ph]]);

        X[:,3]=le_Soil.transform(X[:,3])
        X[:,4]=le_Crop.transform(X[:,4])
        X=X.astype(float)

        
        pred=model_fert.predict(X)
        crop_text = ', '.join(pred)
        st.subheader(f"The predicted fertilizer by model is :{crop_text}")
        