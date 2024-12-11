import streamlit as st 
st.snow()

st.title("Kasbiy Ta'lim")

# Kirish bo‘limi
st.header("Kasbiy Ta'lim haqida umumiy ma'lumot")
st.write(
    """
    Kasbiy ta'lim insonning muayyan kasbga oid bilim va ko‘nikmalarni egallashiga yordam beradi.  
    Bu ta'lim turi nafaqat o‘quvchilarga, balki ishchilar va boshqalarga o‘z kasbiy malakalarini oshirish uchun keng imkoniyatlar yaratadi.
    """
)

# Kasbiy ta'lim afzalliklari
st.subheader("Kasbiy ta'limning afzalliklari:")
st.subheader(
    """
    - Zamonaviy bozor talablariga mos ko‘nikmalarni rivojlantiradi.
    - Tez ishga joylashish imkoniyatini beradi.
    - Amaliy mashg‘ulotlar orqali ko‘nikmalar mustahkamlanadi.
    - Kelgusida biznes boshlash uchun zarur bilimlarni taqdim etadi.
    """
)

# Yo‘nalishlar
st.divider()
st.header("Kasbiy Ta'lim Yo'nalishlari")
directions = [
    {"name": "Axborot texnologiyalari", "description": "Dasturlash, tarmoq boshqaruvi va IT yechimlar."},
    {"name": "Mexanik muhandislik", "description": "Texnik jihozlarni loyihalash va ularga xizmat ko‘rsatish."},
    {"name": "Oshpazlik san'ati", "description": "Milliy va xalqaro oshxona mutaxassisliklari."},
    {"name": "Tikuvchilik", "description": "Modalar dizayni va kiyim-kechak ishlab chiqarish."},
    {"name": "Iqtisodiyot va boshqaruv", "description": "Hisob-kitob, marketing va biznes boshqaruvi."},
]

for direction in directions:
    st.markdown(f"### {direction['name']}")
    st.write(f"{direction['description']}")
    st.divider()

# Kasbiy kurslar haqida ma'lumot
st.header("Kasbiy Kurslar va Mashg‘ulotlar")
courses = [
    {"course": "Python dasturlash", "duration": "3 oy", "fee": "500,000 so‘m"},
    {"course": "Grafik dizayn", "duration": "4 oy", "fee": "600,000 so‘m"},
    {"course": "Muhandislik asoslari", "duration": "6 oy", "fee": "800,000 so‘m"},
]

st.table(courses)

# Savol-javob bo‘limi
st.divider()
st.header("Savollaringiz bormi?")
st.write("Quyidagi ma’lumotlar orqali biz bilan bog‘lanishingiz mumkin:")
st.write(
    """
    📍 Manzil: Toshkent shahar, Chilonzor tumani, 5-maktab ko‘chasi, 22-uy  
    📞 Telefon: +998 91 123 45 67  
    📧 Email: kasbiy.talim@example.com  
    """
)