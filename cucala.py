import streamlit as st
import requests

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️")

# 2. DISEÑO VISUAL SEGURO (Estilo Banana)
def aplicar_estilo():
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: white; }
        .emergency-btn {
            background: linear-gradient(145deg, #ff4b4b, #8b0000);
            color: white;
            padding: 40px;
            text-align: center;
            border-radius: 25px;
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 20px;
            border: 2px solid white;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_index=True)
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #003366, #d40000); padding: 20px; border-radius: 15px; text-align: center;">
            <h1 style="margin:0; color:white;">AI CUCALA TECNICS</h1>
            <p style="margin:0; color:white; opacity:0.8;">Asistencia Técnica Profesional</p>
        </div>
    """, unsafe_allow_index=True)

aplicar_estilo()

# 3. LOGOTIPO
try:
    st.image("logo.png", width=150)
except:
    st.caption("Cargando Identidad...")

# 4. FUNCIONES DE LA APP
st.write("") # Espaciador

# EL GRAN BOTÓN DE PÁNICO
if st.button("🚨 BOTÓN DE PÁNICO", type="primary", use_container_width=True):
    # Usamos tus credenciales guardadas
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    
    mensaje = "🔴 **URGENCIA AI CUCALA**\nEl botón de pánico ha sido activado."
    
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                      data={"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"})
        st.success("¡AVISO ENVIADO A CENTRAL!")
        st.balloons()
    except:
        st.error("Error al conectar.")

# BOTONES SECUNDARIOS
st.write("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("📋 INFORME", use_container_width=True):
        st.info("Iniciando parte...")
with col2:
    if st.button("🔍 RECLAMACIÓN", use_container_width=True):
        st.warning("Iniciando reclamación...")

st.markdown("<p style='text-align:center; margin-top:30px;'>📍 Reus - Tarragona</p>", unsafe_allow_index=True)
