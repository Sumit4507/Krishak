import streamlit as st
from predict_crop import show_pridict_page
from pridict_fertilizer import show_pridict_fertilizer

bar=("Crop for soil","fertilizer for soil")
page=st.sidebar.selectbox("Features",bar)

if page=="Crop for soil":
    show_pridict_page()
else:
    show_pridict_fertilizer()