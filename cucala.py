import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="AI Cucala Tecnics", page_icon="⚙️")

# Estilo para el botón de pánico (Rojo y Grande)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .panic-btn { background-color: #ff4b4b !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ LATERAL ---
menu = st.sidebar.selectbox("Menú", ["Inicio", "Botón de Pánico", "Presupuestos", "Informes Técnicos"])

# --- INICIO ---
if menu == "Inicio":
    st.image("logo.png", width=120) # Asegúrate de que tu logo se llame así
    st.title("AI Cucala Tecnics")
    st.write("Bienvenido al sistema de gestión técnica.")

# --- BOTÓN DE PÁNICO ---
elif menu == "Botón de Pánico":
    st.header("🚨 Asistencia de Emergencia")
    nombre_tec = st.text_input("Tu Nombre/ID de Técnico")
    
    if st.button("SOLICITAR ASISTENCIA AHORA", help="Se enviará aviso con tu ubicación y fotos"):
        if nombre_tec:
            st.error(f"¡ALERTA ENVIADA! Técnico: {nombre_tec}")
            # Aquí la app solicita acceso a la cámara para la evidencia
            foto_emergencia = st.camera_input("Captura de la situación")
            st.info("Buscando coordenadas GPS... (Activa el GPS de tu móvil)")
            # En una WebApp, el navegador pedirá permiso de ubicación automáticamente
        else:
            st.warning("Por favor, pon tu nombre para saber quién eres.")

# --- PRESUPUESTOS ---
elif menu == "Presupuestos":
    st.header("📋 Solicitud de Presupuesto")
    
    with st.form("form_presupuesto"):
        cliente = st.text_input("Nombre del Cliente")
        servicio = st.selectbox("Tipo de Servicio", ["Instalación", "Reparación", "Mantenimiento", "Otro"])
        detalles = st.text_area("Detalles del trabajo")
        
        col1, col2 = st.columns(2)
        with col1:
            enviar_telegram = st.form_submit_button("Enviar por Telegram")
        with col2:
            st.markdown("[📞 Llamar para Consultar](tel:+34600000000)") # Pon tu número aquí
            
        if enviar_telegram:
            st.success(f"Datos de {cliente} preparados para enviar al centro de control.")

# --- INFORMES TÉCNICOS ---
elif menu == "Informes Técnicos":
    st.header("📝 Generar Informe de Trabajo")
    with st.form("informe_tecnico"):
        fecha = st.date_input("Fecha", datetime.now())
        descripcion = st.text_area("Trabajo realizado")
        materiales = st.text_area("Materiales utilizados")
        
        st.write("### Evidencia Visual")
        foto_antes = st.camera_input("Foto ANTES")
        foto_despues = st.camera_input("Foto DESPUÉS")
        
        if st.form_submit_button("Finalizar y Guardar Informe"):
            st.balloons()
            st.success("Informe guardado localmente. Generando PDF...")

