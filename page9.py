import streamlit as st 
st.snow()

st.title("Sayt Yaratuvchisi Haqida")

# Kirish bo‘limi
st.header("Sayt Yaratuvchisi")
st.write(
    """
    Ushbu veb-saytni yaratgan shaxs haqida qisqacha ma'lumot.  
    Quyida dasturchining professional tajribasi, yutuqlari va bog‘lanish ma'lumotlari keltirilgan.
    """
)

# Dasturchi haqida ma'lumot
st.subheader("Dasturchi: Ismi va Ma'lumotlari")
st.write(
    """
    💻 **Ismi:** Umidjon Juraqulov  
    🎓 **Ta'lim:** O'zbekiston Finlandiya pedagogika instituti  
    📜 **Mutaxassisligi:** Matematika va informatika yo'nalishi  
    🏆 **Tajribasi:** 1+ yillik tajribaga ega dasturchi  
    🌟 **Yutuqlari:**  
      - 3+ muvaffaqiyatli veb-loyihalar  
      - Turli xalqaro dasturiy tanlovlarda ishtirokchi  
      - O‘quvchilar uchun bepul kodlash kurslari tashkilotchisi  
    """
)

# Portfolio uchun qisqa havola
st.subheader("Portfolio:")
st.write("🔗 [Portfolio Havolasi](https://umidjon.streamlit.app/)")

# Bog‘lanish ma’lumotlari
st.subheader("Bog‘lanish:")
st.write(
    """
    📞 **Telefon:** +998 93 331 33 48  
    📧 **Email:** juraqulovumdijon0210@gmail.com  
    🌐 **LinkedIn:** akkount mavjud emas  
    🐦 **GitHub:** [GitHub Havolasi](https://github.com/Umidjonjuraqulov)  
    """
)

# Qiziqarli faktlar bo‘limi
st.subheader("Qiziqarli Faktlar:")
st.write(
    """
    - Kodlashdan tashqari, men kitob o‘qishni va shaxmat o‘ynashni yaxshi ko‘radi.  
    - Uning ilhom manbasi - o‘z tajribalarini o‘rgatish va jamiyat rivojlanishiga hissa qo‘shish.
    """
)

# Rasmlar uchun bo'lim (agar mavjud bo'lsa)
st.subheader("Rasm:")
st.image(
    "umid_image.png", 
    caption="Umidjon Juraqulov",
    width=300
)

# Taklif yoki fikr bildirish uchun bo‘lim
st.divider()
st.header("Fikr va Takliflar")
st.write(
    """
    Ushbu veb-sayt yoki boshqa xizmatlar bo‘yicha fikr-mulohaza bildirishingiz mumkin.  
    Quyidagi aloqa vositalari orqali murojaat qiling:
    """
)
st.text_area("O‘z fikringizni yozing:", placeholder="Fikringizni yozing...")
st.button("Yuborish")
