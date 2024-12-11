import streamlit as st 
st.snow()

st.title("Iqtidorli O‘quvchilar")

# Kirish qismi
st.header("Bizning Iqtidorli O‘quvchilarimiz")
st.write(
    """
    Maktabimizda ta’lim olayotgan o‘quvchilar orasida ko‘plab iqtidorli yoshlar bor.  
    Ular nafaqat fan olimpiadalarida, balki sport, san’at va boshqa sohalarda ham o‘zlarining ajoyib natijalari bilan bizni faxrlantirib kelmoqda.
    Quyida ularning muvaffaqiyatlari bilan tanishishingiz mumkin.
    """
)

# Iqtidorli o‘quvchilar haqida ma’lumotlar
st.subheader("Iqtidorli o‘quvchilar ro‘yxati:")

students = [
    {"name": "Jasur Bekmurodov", "achievement": "Matematika fan olimpiadasi g‘olibi", "image": "https://via.placeholder.com/150"},
    {"name": "Madina Xolmatova", "achievement": "Kimyo fanidan xalqaro tanlov g‘olibi", "image": "https://via.placeholder.com/150"},
    {"name": "Alisher Qobilov", "achievement": "Yengil atletika chempioni", "image": "https://via.placeholder.com/150"},
    {"name": "Shaxzoda Karimova", "achievement": "Rassomlik san’ati ko‘rgazmasi ishtirokchisi", "image": "https://via.placeholder.com/150"},
]

# Har bir o‘quvchini alohida ko‘rsatish
for student in students:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(student["image"], width=120)
    with col2:
        st.markdown(f"### {student['name']}")
        st.write(student["achievement"])
    st.divider()

# Qisqa statistika
st.subheader("Maktab Iqtidorli O‘quvchilar Statistikasidan:")
stats = {
    "Fan olimpiadalari g‘oliblari": 25,
    "Sport musobaqalari g‘oliblari": 15,
    "San’at tanlovlari ishtirokchilari": 10,
    "Xalqaro tanlov ishtirokchilari": 5,
}

for category, count in stats.items():
    st.write(f"- **{category}**: {count} o‘quvchi")

# Aloqa qismi
st.divider()
st.header("Qo‘shimcha ma’lumotlar uchun bog‘laning:")
st.write(
    """
    📞 Telefon: +998 90 123 45 67  
    📧 Email: info@maktab.uz  
    """
)