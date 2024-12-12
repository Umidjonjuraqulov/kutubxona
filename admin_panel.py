import streamlit as st 
import pandas as pd

st.header("Kitoblarni ro'yxatga olish")
kitob_nomi = st.text_input("Kitob nomi")
kitob_yozuvchisi = st.text_input("Kitob yozuvchisi")
janr = st.text_input("Janr")
rasm_manzili  = st.text_input("Rasm manzili")
# st.text_input("rating")
kiritish = st.button("Kiritish")
if kiritish :
    kitob_nomi