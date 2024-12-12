import streamlit as st



st.title(" Tilni tanlang ! ")
col1,col2 = st.columns((5, 5))
col1.button("Ingliz tili" ,type="primary", use_container_width=10)
col1.button("Rus tili" ,type="primary", use_container_width=10)
col1.button("Yapon tili" ,type="primary", use_container_width=10)
col2.button("Nemis tili" ,type="primary", use_container_width=10)
col2.button("Fransuz tili" ,type="primary", use_container_width=10)
col2.button("Kores tili" ,type="primary", use_container_width=10)