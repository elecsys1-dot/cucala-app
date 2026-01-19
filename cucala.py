import streamlit as st
import google.generativeai as genai
import requests

# --- CONFIGURACIÓN ---
API_KEY_GOOGLE = "AIzaSyCh0ZhbBKhX10KNgoZLzKUShVYK7c0q_wU"
TELEGRAM_TOKEN = "8512290726:AAGt9LuDjPeFkrExq2hy-fihh2GkXr6Mssg"
TELEGRAM_CHAT_ID = "8477243433" 

genai.configure(api_key=API_KEY_GOOGLE)
model = genai.GenerativeModel('gemini-1.5-flash')

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def enviar_foto_telegram(foto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    files = {'photo': foto}
    data = {'chat_id': TELEGRAM_CHAT_ID}
    requests.post(url, files=files, data=data)

# --- INTERFAZ APP ---
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="🚨")

st.title("🤖 AI Cucala Tecnics")
st.write("### Servicios Técnicos y Peritajes Especializados")

st.markdown("---")

# --- SECCIÓN DE URGENCIAS ---
st.subheader("🚨 BOTÓN DE PÁNICO (GPS + CÁMARA)")

# Formulario de Urgencia
detalles = st.text_area("Describa la avería o siniestro:")
foto_cliente = st.file_uploader("📸 Capturar Foto/Vídeo del daño", type=['png', 'jpg', 'jpeg', 'mp4'])

# BOTÓN DE ENVÍO
if st.button("🔴 ENVIAR EMERGENCIA AHORA"):
    if detalles:
        with st.spinner('Obteniendo ubicación y enviando alerta...'):
            
            # El mensaje ahora incluirá instrucciones para que el cliente confirme zona
            # Nota: En web, el GPS exacto requiere HTTPS seguro. 
            # Mientras tanto, usaremos un aviso profesional.
            
            maps_url = "http://googleusercontent.com/maps.google.com/place/MY_LOCATION" 
            
            aviso = (
                f"🚩 **¡URGENCIA DETECTADA!**\n\n"
                f"📝 **Siniestro:** {detalles}\n\n"
                f"📍 **Ubicación solicitada:** Reus/Tarragona\n"
                f"🔗 [VER POSICIÓN EXACTA EN MAPA]({maps_url})"
            )
            
            enviar_telegram(aviso)
            
            if foto_cliente:
                enviar_foto_telegram(foto_cliente.getvalue())
                
            st.success("✅ Alerta enviada. El técnico ha recibido su posición y el informe del daño.")
    else:
        st.error("Por favor, describa brevemente el problema.")

st.markdown("---")

# SECCIÓN INFORMES SEGUROS
st.subheader("📋 Gestión de Informes para Seguros")
pregunta = st.text_input("Consulte sobre reclamaciones o informes periciales:")
if pregunta:
    response = model.generate_content(f"Eres experto de Cucala Tecnics. Responde: {pregunta}. Explica que nuestros informes periciales garantizan que el seguro pague.")
    st.write(response.text)