import streamlit as st
import requests
from PIL import Image

# 1. CONFIGURACIÓN BÁSICA
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🤖", layout="centered")

# 2. DISEÑO VISUAL CORREGIDO
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>AI CUCALA TECNICS</h1>", unsafe_allow_index=True)
st.markdown("<p style='text-align: center;'>Tu asistente inteligente de oficina y hogar</p>", unsafe_allow_index=True)

# 3. CARGAR EL LOGO
try:
    # Usamos el archivo que ya tienes en GitHub
    st.image("logo.png", width=200)
except:
    st.write("Cargando logo...")

# 4. BOTÓN DE PÁNICO GIGANTE
st.write("---")
if st.button("🚨 BOTÓN DE PÁNICO", use_container_width=True):
    # Recuperamos tus secretos guardados
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "⚠️ **¡ALERTA DE EMERGENCIA TÉCNICA!** ⚠️\nSe requiere asistencia inmediata."
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.error("¡EMERGENCIA ENVIADA! La central ha sido notificada.")
        st.balloons()
    except:
        st.error("Error al enviar el aviso.")

# 5. OTROS SERVICIOS
st.write("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 SOLICITAR INFORME", use_container_width=True):
        st.info("Función de informes seleccionada.")
with col2:
    if st.button("🔍 RECLAMACIONES", use_container_width=True):
        st.warning("Área de reclamaciones técnica.")

st.markdown("<br><p style='text-align:center; color:gray;'>📍 Tarragona, Reus y alrededores</p>", unsafe_allow_index=True)
