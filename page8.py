import streamlit as st 
st.snow()

st.title("Ijtimoiy Tarmoqlar")

# Kirish
st.header("Bizning Ijtimoiy Tarmoqlardagi Rasmiy Sahifalarimiz")
st.write(
    """
    Tashkilotimizni ijtimoiy tarmoqlarda kuzatib boring!  
    Quyidagi platformalar orqali bizning yangiliklarimiz, tadbirlarimiz va o‘quvchilarimizning yutuqlari haqida xabardor bo‘ling.
    """
)

# Ijtimoiy tarmoqlar
social_media = {
    "Telegram": "https://t.me/maktab_official",
    "Instagram": "https://instagram.com/maktab_official",
    "Facebook": "https://facebook.com/maktab.official",
    "YouTube": "https://youtube.com/@maktab_official",
    "LinkedIn": "https://linkedin.com/company/maktab-official",
}

# Platformalarni ro‘yxatda ko‘rsatish
st.subheader("Ijtimoiy tarmoqlar havolalari:")
for platform, link in social_media.items():
    st.markdown(f"📌 [{platform}]({link})")

# Har bir platforma uchun ikonka va havola
st.subheader("Tarmoqlarga tezkor ulanish:")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg", width=50)
    st.markdown("[Telegram](https://t.me/maktab_official)")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png", width=50)
    st.markdown("[Instagram](https://instagram.com/maktab_official)")

with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg", width=50)
    st.markdown("[Facebook](https://facebook.com/maktab.official)")

# Ikkinchi qatordagi ijtimoiy tarmoqlar
col4, col5 = st.columns(2)
with col4:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png", width=50)
    st.markdown("[YouTube](https://youtube.com/@maktab_official)")

with col5:
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png", width=50)
    st.markdown("[LinkedIn](https://linkedin.com/company/maktab-official)")

# Foydalanuvchilarni taklif qilish
st.divider()
st.header("Bizga Qo'shiling!")
st.write(
    """
    Bizni kuzatishda davom eting va yangiliklarimizdan birinchi bo‘lib xabardor bo‘ling!  
    Agar savollaringiz bo‘lsa, quyidagi aloqa vositalarimiz orqali bog‘lanishingiz mumkin:
    """
)
st.write(
    """
    📞 Telefon: +998 90 123 45 67  
    📧 Email: social@maktab.uz  
    🌐 Veb-sayt: [www.maktab.uz](https://www.maktab.uz)
    """
)
