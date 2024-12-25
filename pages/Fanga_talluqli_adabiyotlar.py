import streamlit as st

st.title(" Fanni tanlang ! ")
col1,col2,col3,col4 = st.columns((5, 5, 5, 5))
dasturlash = col1.button("Dasturlash" ,type="primary", use_container_width=10)
matimatika = col1.button("Matimatika" ,type="primary", use_container_width=10)
informatika = col2.button("Informatika" ,type="primary", use_container_width=10)
geografiya = col2.button("Geografiya" ,type="primary", use_container_width=10)
tarix = col3.button("Tarix" ,type="primary", use_container_width=10)
falsafa = col3.button("Falsafa" ,type="primary", use_container_width=10)
psixologiya = col4.button("Psixologiya" ,type="primary", use_container_width=10)
metodika = col4.button("Pedagogika" ,type="primary", use_container_width=10)

if dasturlash:
    st.header("Dasturlash faniga oid adabiyotlar")
    st.write("Anvar Narzullayev")
elif matimatika:
    st.header("Matematika faniga oid adabiyotlar")
elif informatika:
    st.header("Informatika faniga oid adabiyotlar")
elif geografiya:
    st.header("Geografiya faniga oid adabiyotlar")
elif tarix:
    st.header("Tarix faniga oid adabiyotlar")
elif falsafa:
    st.header("Falsafa faniga oid adabiyotlar")
elif psixologiya:
    st.header("Psixologiya faniga oid adabiyotlar")
elif metodika:
    st.header("Pedagogika faniga oid adabiyotlar")
    


