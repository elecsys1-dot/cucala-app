import streamlit as st
import requests

# Configuración básica sin complicaciones
st.set_page_config(page_title="AI Cucala Tecnics")

# Título simple (Evita el error de formato)
st.title("AI CUCALA TECNICS")
st.write("Tu asistente inteligente de oficina y hogar")

# Intentar cargar el logo
try:
    st.image("logo.png", width=200)
except:
    st.write("🔧 Logo en carga...")

st.divider()

# BOTÓN DE PÁNICO
if st.button("🚨 ENVIAR AVISO DE EMERGENCIA", use_container_width=True):
    # Usamos tus llaves secretas
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "⚠️ EMERGENCIA TÉCNICA: Se requiere asistencia inmediata."
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje})
        st.success("✅ ¡Aviso enviado!")
    except:
        st.error("❌ Error al conectar.")

st.divider()
st.caption("📍 Tarragona y Reus")
