import streamlit as st
import requests
from PIL import Image

# Configuración de estilo Android Moderno
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background: #0e1117; }
    
    /* Contenedor del Título */
    .header-style {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        border-radius: 15px;
        margin-bottom: 25px;
    }

    /* Botón de Pánico Estilo App */
    .stButton>button {
        width: 100%;
        height: 150px;
        border-radius: 25px;
        background-color: #ff4b4b;
        color: white;
        font-size: 28px;
        font-weight: bold;
        border: 5px solid #ffffff33;
        box-shadow: 0px 10px 20px rgba(255, 75, 75, 0.4);
        text-transform: uppercase;
    }
    
    /* Estilo para los otros botones */
    .secondary-btn {
        display: flex;
        gap: 10px;
        margin-top: 20px;
    }
    </style>
    
    <div class="header-style">
        <h1 style='color: white; margin:0;'>AI CUCALA TECNICS</h1>
        <p style='color: #e0e0e0;'>Tu asistente inteligente de oficina y hogar</p>
    </div>
    """, unsafe_allow_index=True)

# Cargar Logo
try:
    logo = Image.open("logo.png")
    st.image(logo, width=150)
except:
    st.write("🔧 *Cargando Logo...*")

# BOTÓN DE PÁNICO (Principal)
if st.button("🚨 BOTÓN DE PÁNICO 🚨"):
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    texto = "⚠️ **¡ALERTA DE EMERGENCIA TÉCNICA!** ⚠️\nUn cliente necesita asistencia inmediata."
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": texto, "parse_mode": "Markdown"})
    st.error("¡EMERGENCIA ENVIADA! Estamos avisando a la central.")
    st.balloons()

# Secciones secundarias
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 SOLICITAR INFORME"):
        st.info("Función de informes activada.")
with col2:
    if st.button("🔍 RECLAMACIONES"):
        st.warning("Área de reclamaciones técnica.")

st.markdown("---")
st.write("📍 **Cobertura:** Tarragona, Reus y alrededores")
