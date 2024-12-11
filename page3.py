import streamlit as st 
st.snow()

st.header("MAKTABIMIZ RAHBARIYATI")
st.title("Maktab Rahbariyati")

# Kirish qismi
st.header("Bizning Maktab Rahbariyatimiz")
st.write(
    """
    Bizning maktab rahbariyati bilimli, tajribali va maktabni yanada rivojlantirishga bag‘ishlangan insonlardan iborat.
    Quyida rahbariyat a’zolari haqida ma’lumot berilgan.
    """
)

# Rahbariyat bo‘limlari uchun ustunlar
st.subheader("Rahbariyat A'zolari:")
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/150", width=150)  # Direktor rasmi
    st.markdown("### Ism Familiya")
    st.write("Lavozim: Maktab direktori")
    st.write("Telefon: +998 90 123 45 67")
    st.write("Email: direktor@example.com")

with col2:
    st.image("https://via.placeholder.com/150", width=150)  # O‘rinbosar rasmi
    st.markdown("### Ism Familiya")
    st.write("Lavozim: O‘quv ishlari bo‘yicha direktor o‘rinbosari")
    st.write("Telefon: +998 90 987 65 43")
    st.write("Email: orinbosar@example.com")

# Yana boshqa rahbariyat a'zolari
st.divider()
st.subheader("Boshqa Rahbariyat A'zolari:")

rahbariyat = [
    {"name": "Ism Familiya", "lavozim": "Ma’naviy-ma’rifiy ishlar bo‘yicha direktor o‘rinbosari"},
    {"name": "Ism Familiya", "lavozim": "Yoshlar yetakchisi"},
    {"name": "Ism Familiya", "lavozim": "Xo‘jalik ishlari boshqaruvchisi"},
]

for r in rahbariyat:
    st.write(f"**{r['name']}** — {r['lavozim']}")