import streamlit as st
import google.generativeai as genai
import requests

# Configuración de la página con estilo moderno
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️", layout="centered")

# Estilo CSS para que parezca una App de Android elegante
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stTextInput>div>div>input { border-radius: 15px; }
    .header-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    <div class="header-box">
        <h1>AI CUCALA TECNICS</h1>
        <p>Gestión de Urgencias e Informes Periciales</p>
    </div>
    """, unsafe_allow_index=True)

# Recuperar secretos
api_key = st.secrets["API_KEY_GOOGLE"]
token = st.secrets["TELEGRAM_TOKEN"]
chat_id = st.secrets["TELEGRAM_CHAT_ID"]

# Formulario principal
nombre = st.text_input("👤 Nombre del Técnico / Cliente:")
averia = st.text_area("📝 Descripción de la avería o siniestro:")
foto = st.file_uploader("📸 Capturar Foto del daño", type=['png', 'jpg', 'jpeg'])

if st.button("🚨 ENVIAR EMERGENCIA AHORA"):
    if nombre and averia:
        mensaje = f"🔴 **NUEVA URGENCIA**\n\n**Técnico:** {nombre}\n**Avería:** {averia}"
        url_tg = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}
        
        response = requests.post(url_tg, data=payload)
        if response.status_code == 200:
            st.success("✅ Aviso enviado correctamente a la central.")
            st.balloons()
        else:
            st.error("❌ Error al enviar. Revisa la configuración.")
    else:
        st.warning("⚠️ Por favor, rellena el nombre y la descripción.")

st.markdown("---")
st.caption("© 2026 AI Cucala Tecnics - Reus / Tarragona")
