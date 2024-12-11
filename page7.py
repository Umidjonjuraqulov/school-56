import streamlit as st 
import pandas as pd 
import folium
from streamlit_folium import st_folium


st.snow()



# Sahifa sarlavhasi
st.title("Manzil")

# Kirish bo‘limi
st.header("Bizning Manzilimiz")
st.write(
    """
    Bizning maktabimizga tashrif buyurmoqchimisiz?  
    Quyida aniq manzilimiz, xaritadagi joylashuvimiz va biz bilan bog‘lanish uchun zarur ma’lumotlarni topishingiz mumkin.
    """
)

# Maktab manzili
st.subheader("Bizning aloqa ma'lumotlarimiz:")
st.write(
    """
    📍 **Manzil**: Toshkent shahar, Chilonzor tumani, 5-maktab ko‘chasi, 22-uy  
    📞 **Telefon**: +998 91 123 45 67  
    📧 **Email**: info@maktab.uz  
    🕒 **Ish vaqti**: Dushanba - Juma, soat 08:00 - 17:00  
    """
)

# Xarita
st.subheader("Xaritada joylashuvimiz:")

# Folium xaritasi
latitude, longitude = 41.2995, 69.2401  # Toshkent shahrining taxminiy koordinatalari
mymap = folium.Map(location=[latitude, longitude], zoom_start=12)
folium.Marker(
    location=[latitude, longitude],
    popup="Bizning maktab",
    tooltip="Maktab joylashuvi",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Xarita Streamlitda aks ettiriladi
st_folium(mymap, width=700, height=500)

# Aloqa uchun qo‘shimcha savollar
st.divider()
st.header("Savollaringiz bormi?")
st.write("Bizga murojaat qiling yoki tashrif buyuring!")
st.write(
    """
    🌐 Veb-sayt: [www.maktab.uz](https://www.maktab.uz)  
    📱 Telegram: [@maktab_contact](https://t.me/maktab_contact)  
    """
)
