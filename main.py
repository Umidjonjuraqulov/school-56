import streamlit as st

st.snow()

def page2():
    st.title("Second page")

pg = st.navigation([
    #st.image("images/school_56.png")
    st.Page("page1.py", title="Home page", icon="🏠"),
    st.Page("page2.py", title="Afzalliklar", icon="🎖"),
    st.Page("page3.py", title="Rahbariyat", icon="👨🏻‍💼"),
    st.Page("page4.py", title="Iqtidorli o'quvchilar", icon="🧠"),
    st.Page("page5.py", title="Kasbiy ta'lim", icon="🎓"),
    st.Page("page6.py", title="Statistika", icon="📈"),
    st.Page("page7.py", title="Manzil", icon=""),
    st.Page("page8.py", title="Ijtimoiy tarmoqlari", icon="📥"),
    st.Page("page9.py", title="web-sayt yaratish xizmati", icon="👨🏻‍💻"),
])
pg.run()