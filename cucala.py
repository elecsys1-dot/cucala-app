import streamlit as st
import requests

# 1. IDENTIDAD DE LA APP
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️")

# 2. CABECERA (Usando funciones nativas seguras)
st.title("🏗️ AI CUCALA TECNICS")
st.info("Asistencia Técnica Profesional - Reus / Tarragona")

# Intentar mostrar tu logo
try:
    st.image("logo.png", width=150)
except:
    st.caption("Identidad visual: AI Cucala Tecnics")

st.divider()

# 3. BOTÓN DE PÁNICO (Rojo y Grande)
st.error("### 🚨 SISTEMA DE EMERGENCIAS")
if st.button("ENVIAR ALERTA DE PÁNICO", type="primary", use_container_width=True):
    # Usamos tus credenciales exactas
    token = "8512290726:AAGt9LuDjPeFkrExq2hy-fihh2GkXr6Mssg"
    chat_id = "8477243433"
    
    mensaje = "🔴 **URGENCIA AI CUCALA**\nSe ha solicitado asistencia inmediata desde la App."
    
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.success("✅ ¡AVISO ENVIADO A CENTRAL!")
        st.balloons()
    except:
        st.error("Error de conexión. Revisa tu cobertura.")

st.write("") 

# 4. BOTONES DE SERVICIOS (Informes y Reclamaciones)
st.subheader("🛠️ Gestión de Servicios")
col1, col2 = st.columns(2)

with col1:
    if st.button("📋 SOLICITAR INFORME", use_container_width=True):
        st.write("Abriendo panel de informes técnicos...")

with col2:
    if st.button("🔍 RECLAMACIONES", use_container_width=True):
        st.write("Abriendo gestión de daños ocultos...")

# 5. PIE DE PÁGINA
st.divider()
st.caption("© 2026 AI Cucala Tecnics - Reus / Tarragona")
