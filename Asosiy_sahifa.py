import streamlit as st
import pandas as pd  
#from streamlit_star_rating import st_star_rating

st.title(" Xush kelibsiz ! ")

qidiruv_turi = st.radio("Qidiruv filteri", ["Kitob nomi", "Kitob yozuvchisi", "Janr"], horizontal=True)
col1, col2 = st.columns((8, 2))

qidiruv_matni = col1.text_input("Qaysi kitobni qidiryapsiz") 
qidir = col2.button("Qidir")

if qidir: 
    resurs_link =  "https://docs.google.com/spreadsheets/d/e/2PACX-1vTYMiRw1UOit8ysPyUff6Ob8BvRQXTIZApykHFFiY8EmN9Egy72U0gKsNCWYKUB-hwKwccVw3OPOVt-/pub?gid=0&single=true&output=csv"
    malumotlar = pd.read_csv(resurs_link)

    result = malumotlar[malumotlar[qidiruv_turi].str.contains(qidiruv_matni)] 

    n_result = len(result) 
    if n_result == 0: 
        st.info("Kechirasiz bu haqida ma'lumot mavjud emas", icon='⚠️') 
    
    else: 
        for i in range(n_result): 
            kitob_nomi = result.iloc[i]['Kitob nomi'] 
            yozuvchi = result.iloc[i]['Kitob yozuvchisi'] 
            janr = result.iloc[i]['Janr'] 
            rasm_link = result.iloc[i]['Rasm'] 
            #rating = result.iloc[i]['rating'] 

            col1, col2 = st.columns((3, 7)) 
            col1.image(rasm_link, width=120) 
            col2.subheader(f"Kitob nomi: {kitob_nomi}")
            col2.write(f"Kitob yozuvchisi: {yozuvchi}")
            col2.write(f"Janr: {janr}")
            #stars = st_star_rating("Kitobni baholang ", maxValue=5, defaultValue=rating, key=kitob_nomi) # key="rating"
            st.markdown("***")


else: 
    st.subheader("Mening Kutubxonam 📚")
    st.image("images/kutubxona.JPG")

    st.subheader("Kutubxonamiz imkoniyatlari")
    st.write("* Bizda elektron kitoblardan vaqtinchalik foydalanish imkoniyati")
    st.write("* Bizning kutubxonamizdagi kitoblardan vaqtinchalik foydalanish imkoniyati")
