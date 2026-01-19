import streamlit as st
import requests

# Configuración de página
st.set_page_config(page_title="AI Cucala Tecnics", layout="centered")

# Título y Logo
st.title("🏗️ AI CUCALA TECNICS")
st.subheader("Asistencia Técnica Reus / Tarragona")

try:
    st.image("logo.png", width=200)
except:
    st.info("Cargando logotipo de la empresa...")

st.divider()

# BOTÓN DE PÁNICO
st.markdown("### 🚨 SISTEMA DE EMERGENCIAS")
if st.button("ENVIAR AVISO INMEDIATO", use_container_width=True):
    # Usamos tus credenciales de los Secrets
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "🔴 **URGENCIA TÉCNICA**\nSe ha activado el botón de pánico en AI Cucala Tecnics.\nRequiere atención inmediata."
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.success("✅ ¡Aviso enviado con éxito! Recibirás respuesta pronto.")
        st.balloons()
    except Exception as e:
        st.error(f"Error al enviar: {e}")

st.divider()
st.caption("© 2026 AI Cucala Tecnics - Gestión de Urgencias")
