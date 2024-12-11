import streamlit as st
st.snow()
# Sahifa sarlavhasi
st.title("Afzalliklar Sahifasi")

# 1-bo'lim: Kirish
with st.container():
    st.header("Nega bizni tanlaysiz?")
    st.write(
        """
        Bizning xizmatlarimiz quyidagi afzalliklarni taqdim etadi:
        - Ishonchlilik va sifat
        - Zamonaviy yondashuv
        - Foydalanuvchilarga qulaylik
        """
    )

# 2-bo'lim: Afzalliklarni ro'yxati
st.subheader("Bizning asosiy afzalliklarimiz:")

# Afzalliklar uchun ustunlar yaratish
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Ishonch")
    st.write("Bizning mijozlarimiz bizga har doim ishonadi.")
    st.image("ishonch.png", width=200)

with col2:
    st.markdown("### Sifat")
    st.write("Biz faqat eng yuqori sifatni taqdim etamiz.")
    st.image("sifat.png", width=200)  # Tasvir

with col3:
    st.markdown("### Innovatsiya")
    st.write("Yangi texnologiyalarni qo‘llash orqali rivojlanamiz.")
    st.image("innovatsiya.png", width=200)  # Tasvir

# 3-bo'lim: Qo'shimcha Afzalliklar
st.divider()
st.write("### Boshqa afzalliklarimiz:")
st.subheader(
    """
    - 24/7 mijozlarni qo‘llab-quvvatlash
    - Tez yetkazib berish xizmati
    - Qulay narx siyosati
    """
)

# Aloqa bo'limi
st.divider()
st.header("Biz bilan bog'laning:")
st.write(
    """
    Agar savollaringiz bo'lsa, biz bilan bog‘lanishingiz mumkin:
    - 📞 Telefon: +998 90 123 45 67
    - 📧 Email: info@example.com
    """
)
