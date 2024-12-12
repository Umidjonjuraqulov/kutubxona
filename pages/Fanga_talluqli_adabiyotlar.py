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
metodika = col4.button("Metodika" ,type="primary", use_container_width=10)

if dasturlash:
    st.header("Dasturlash faniga oid adabiyotlar")
    st.write("Anvar Narzullayev")
elif matimatika:
    pass
elif informatika:
    pass
elif geografiya:
    pass
elif tarix:
    pass
elif falsafa:
    pass
elif psixologiya:
    pass
elif metodika:
    pass


