import streamlit as st
import requests
from PIL import Image

# Configuración de la App
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🤖", layout="centered")

# Estilo Negro y Neón (Como la imagen que te gusta)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* Botón de Pánico Gigante */
    .stButton>button {
        width: 100%;
        height: 250px;
        border-radius: 30px;
        background: linear-gradient(145deg, #ff4b4b, #8b0000);
        color: white;
        font-size: 40px;
        font-weight: bold;
        border: 4px solid #ffffff33;
        box-shadow: 0px 15px 30px rgba(255, 75, 75, 0.4);
    }
    
    /* Botones Secundarios */
    .sec-btn>div>button {
        height: 80px;
        font-size: 16px;
        background-color: #1f2937;
    }
    </style>
    <h2 style='text-align: center; color: #00d4ff;'>AI Cucala Tecnics</h2>
    <p style='text-align: center; opacity: 0.8;'>Tu asistente inteligente de oficina y hogar</p>
    """, unsafe_allow_index=True)

# Cargar el logo que acabas de subir
try:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("logo.png", use_container_width=True)
except:
    st.write("Cargando logo...")

st.markdown("<br>", unsafe_allow_index=True)

# EL GRAN BOTÓN DE PÁNICO
if st.button("🚨 BOTÓN DE PÁNICO"):
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    texto = "⚠️ **¡ALERTA DE EMERGENCIA TÉCNICA!** ⚠️\nSe requiere asistencia inmediata en Tarragona/Reus."
    
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                      data={"chat_id": chat_id, "text": texto, "parse_mode": "Markdown"})
        st.error("¡EMERGENCIA ENVIADA! La central ha sido notificada.")
        st.balloons()
    except:
        st.error("Error al conectar con la central.")

# Botones de servicios
col_a, col_b = st.columns(2)
with col_a:
    st.button("📋 SOLICITAR INFORME", key="inf")
with col_b:
    st.button("🔍 RECLAMACIONES", key="rec")

st.markdown("<p style='text-align:center; margin-top:50px;'>📍 Tarragona, Reus y alrededores</p>", unsafe_allow_index=True)
