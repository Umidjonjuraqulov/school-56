import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


st.snow()

# Sahifa sarlavhasi
st.title("Statistika Sahifasi")

# Kirish qismi
st.header("Statistik Ma'lumotlar")
st.write(
    """
    Bu sahifada maktab faoliyati va natijalari bilan bog'liq statistik ma'lumotlar taqdim etiladi.  
    Quyida siz jadvallar, grafiklar va ko'rsatkichlar bilan tanishishingiz mumkin.
    """
)

# Asosiy statistik ma'lumotlar
st.subheader("Umumiy Ko'rsatkichlar:")
st.metric("O‘quvchilar soni", 350)
st.metric("O‘qituvchilar soni", 50)
st.metric("Fan olimpiadalari sovrindorlari", 25)

# Jadvallar
st.divider()
st.subheader("O‘quvchilar soni sinflar bo‘yicha:")

data = {
    "Sinf": ["1-sinf", "2-sinf", "3-sinf", "4-sinf", "5-sinf"],
    "O‘quvchilar soni": [45, 50, 40, 55, 55],
}
df = pd.DataFrame(data)
st.table(df)

# Grafik
st.divider()
st.subheader("Sinflar bo‘yicha o‘quvchilar soni")

fig, ax = plt.subplots()
ax.bar(df["Sinf"], df["O‘quvchilar soni"], color="skyblue")
ax.set_xlabel("Sinflar")
ax.set_ylabel("O‘quvchilar soni")
ax.set_title("O‘quvchilar soni sinflar bo‘yicha")
st.pyplot(fig)

# Yillik o‘zgarishlar
st.divider()
st.subheader("O‘quvchilar sonidagi o‘sish (yillar bo‘yicha):")

growth_data = {
    "Yil": ["2020", "2021", "2022", "2023", "2024"],
    "O‘quvchilar soni": [300, 320, 340, 360, 350],
}
growth_df = pd.DataFrame(growth_data)
st.line_chart(growth_df.set_index("Yil"))

# Statistika bo‘yicha savollar
st.divider()
st.header("Savollaringiz bormi?")
st.write("Biz bilan bog‘laning:")
st.write(
    """
    📍 Manzil: Toshkent shahar, Chilonzor tumani, 5-maktab ko‘chasi, 22-uy  
    📞 Telefon: +998 91 123 45 67  
    📧 Email: statistika@example.com  
    """
)
