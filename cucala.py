import streamlit as st
import requests
import pandas as pd

# 1. CONFIGURACIÓN DE APARIENCIA TIPO APP MÓVIL
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️", layout="centered")

st.markdown("""
    <style>
    /* Fondo oscuro profesional */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Cabecera con degradado */
    .header-container {
        background: linear-gradient(135deg, #003366 0%, #d40000 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #ffffff33;
    }
    
    /* BOTÓN DE PÁNICO GIGANTE */
    .stButton>button[kind="primary"] {
        width: 100%;
        height: 180px;
        border-radius: 25px;
        background: linear-gradient(145deg, #ff4b4b, #8b0000);
        color: white;
        font-size: 30px !important;
        font-weight: bold;
        border: 4px solid #ffffff44;
        box-shadow: 0px 10px 20px rgba(212, 0, 0, 0.5);
    }

    /* BOTONES SECUNDARIOS */
    .stButton>button[kind="secondary"] {
        width: 100%;
        height: 80px;
        border-radius: 15px;
        background-color: #1f2937;
        color: #00d4ff;
        font-weight: bold;
        border: 1px solid #374151;
    }
    </style>
    
    <div class="header-container">
        <h1 style='margin:0; font-size: 24px;'>AI CUCALA TECNICS</h1>
        <p style='margin:0; opacity:0.8;'>Asistencia Inteligente de Oficina y Hogar</p>
    </div>
    """, unsafe_allow_index=True)

# 2. LOGOTIPO
try:
    st.image("logo.png", width=140)
except:
    st.caption("Cargando Identidad Visual...")

# 3. GEOLOCALIZACIÓN (Sencilla y funcional)
st.markdown("### 📍 Ubicación del Servicio")
# Usamos un checkbox para que el usuario autorice el GPS en el móvil
if st.checkbox("Activar GPS y Cámara"):
    st.info("Obteniendo coordenadas de Tarragona/Reus...")
    # Nota: La geolocalización real en Streamlit Web requiere componentes que ya tienes en requirements.
    # Por ahora, preparamos el campo para el envío.

# 4. CUERPO DE LA APP (Botones de Banana)
st.markdown("<br>", unsafe_allow_index=True)

# EL GRAN BOTÓN DE PÁNICO
if st.button("🚨 BOTÓN DE PÁNICO", type="primary"):
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "🔴 **¡ALERTA DE EMERGENCIA TÉCNICA!**\n\n"
    mensaje += "Se requiere asistencia inmediata.\n"
    mensaje += "📍 *Ubicación:* Enviada desde el dispositivo móvil."
    
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                      data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.success("¡EMERGENCIA ENVIADA! Estamos avisando a la central.")
        st.balloons()
    except:
        st.error("Error de conexión con la central.")

st.markdown("<br>", unsafe_allow_index=True)

# BOTONES SECUNDARIOS
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 SOLICITAR INFORME", type="secondary"):
        st.write("Abriendo gestor de informes...")
with col2:
    if st.button("🔍 RECLAMACIONES", type="secondary"):
        st.write("Abriendo área de daños ocultos...")

# 5. PIE DE PÁGINA
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>📍 Tarragona · Reus · Cambrils</p>", unsafe_allow_index=True)
