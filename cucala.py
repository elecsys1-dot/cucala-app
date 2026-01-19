import streamlit as st
import requests

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️")

# 2. DISEÑO VISUAL (Estilo Banana simplificado para evitar errores)
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>AI CUCALA TECNICS</h1>", unsafe_allow_index=True)
st.markdown("<p style='text-align: center; background-color: #003366; color: white; padding: 10px; border-radius: 10px;'>Asistencia Técnica Profesional - Reus / Tarragona</p>", unsafe_allow_index=True)

# 3. LOGOTIPO
try:
    st.image("logo.png", width=150)
except:
    st.caption("Cargando Identidad Visual...")

st.write("---")

# 4. BOTÓN DE PÁNICO (Principal)
# Usamos el botón nativo de Streamlit con color resaltado
if st.button("🚨 ENVIAR BOTÓN DE PÁNICO", type="primary", use_container_width=True):
    # Usamos tus credenciales guardadas
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "🔴 **URGENCIA AI CUCALA**\nSe ha solicitado asistencia inmediata."
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.success("¡AVISO ENVIADO A CENTRAL!")
        st.balloons()
    except:
        st.error("Error al conectar con Telegram.")

# 5. BOTONES SECUNDARIOS
st.write("### Servicios Adicional")
col1, col2 = st.columns(2)

with col1:
    if st.button("📋 SOLICITAR INFORME", use_container_width=True):
        st.info("Abriendo gestión de informes...")

with col2:
    if st.button("🔍 RECLAMACIONES", use_container_width=True):
        st.warning("Abriendo gestión de daños ocultos...")

# 6. PIE DE PÁGINA
st.write("---")
st.markdown("<p style='text-align:center; color:gray;'>© 2026 AI Cucala Tecnics</p>", unsafe_allow_index=True)
