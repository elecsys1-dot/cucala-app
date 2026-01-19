import streamlit as st
import requests
from PIL import Image

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🏗️", layout="centered")

# 2. DISEÑO VISUAL (CSS)
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
    .header-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    <div class="header-box">
        <h1>AI CUCALA TECNICS</h1>
        <p>Gestión de Urgencias e Informes Periciales</p>
    </div>
    """, unsafe_allow_index=True)

# 3. CARGAR EL LOGOTIPO QUE SUBISTE A GITHUB
try:
    imagen_logo = Image.open("logo.png")
    # Esto centra la imagen del logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(imagen_logo, use_container_width=True)
except:
    st.info("Sube el archivo 'logo.png' a tu GitHub para que aparezca aquí el logo.")

# 4. RECUPERAR TUS CLAVES SECRETAS
try:
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
except:
    st.error("Faltan las claves en la sección 'Secrets' de Streamlit.")

# 5. FORMULARIO DE LA APP
st.markdown("---")
nombre = st.text_input("👤 Nombre del Técnico / Cliente:")
averia = st.text_area("📝 Describa la avería o siniestro:")
foto = st.file_uploader("📸 Capturar Foto/Vídeo del daño", type=['png', 'jpg', 'jpeg', 'mp4'])

# 6. LÓGICA DEL BOTÓN DE PÁNICO
if st.button("🚨 ENVIAR EMERGENCIA AHORA"):
    if nombre and averia:
        mensaje = f"🔴 **NUEVA URGENCIA**\n\n**Técnico:** {nombre}\n**Avería:** {averia}"
        url_tg = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url_tg, data=payload)
            if res.status_code == 200:
                st.success("✅ ¡Aviso enviado! Ya estamos en camino.")
                st.balloons()
            else:
                st.error("Error al conectar con Telegram.")
        except:
            st.error("Error en el envío.")
    else:
        st.warning("⚠️ Escribe tu nombre y la avería antes de enviar.")

st.markdown("---")
st.caption("© 2026 AI Cucala Tecnics - Reus / Tarragona")
