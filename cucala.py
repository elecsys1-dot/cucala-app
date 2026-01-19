import streamlit as st

# 1. Configuración básica (DEBE ser la primera línea de Streamlit)
st.set_page_config(page_title="AI Cucala Tecnics", layout="centered")

# 2. Título principal siempre visible
st.title("🛠️ AI Cucala Tecnics")

# 3. Menú de navegación sencillo
opcion = st.radio("Selecciona una función:", 
                 ["Inicio", "🚨 BOTÓN DE PÁNICO", "📋 Presupuestos", "📝 Informes Técnicos"],
                 horizontal=True)

st.divider() # Una línea de separación

# --- LÓGICA DE LAS SECCIONES ---

if opcion == "Inicio":
    st.subheader("Bienvenido al sistema")
    st.write("Selecciona una opción arriba para empezar.")
    st.info("App gestionada por IA Cucala")

elif opcion == "🚨 BOTÓN DE PÁNICO":
    st.header("ASISTENCIA INMEDIATA")
    nombre = st.text_input("Nombre del técnico")
    if st.button("ENVIAR ALERTA URGENTE", type="primary"):
        if nombre:
            st.error(f"¡ALERTA ENVIADA! Técnico {nombre} en apuros.")
            st.camera_input("Captura de pantalla/entorno")
            # Aquí la app pedirá permiso de cámara al usuario
        else:
            st.warning("Introduce tu nombre antes de enviar.")

elif opcion == "📋 Presupuestos":
    st.header("Solicitud de Presupuesto")
    with st.form("presupuesto"):
        cliente = st.text_input("Cliente")
        trabajo = st.text_area("Descripción del trabajo")
        metodo = st.radio("Enviar por:", ["Telegram", "Llamada"])
        
        if st.form_submit_button("Procesar"):
            if metodo == "Llamada":
                st.markdown("[📞 PULSA AQUÍ PARA LLAMAR](tel:+34600000000)")
            else:
                st.success("Enviando datos a Telegram...")

elif opcion == "📝 Informes Técnicos":
    st.header("Nuevo Informe")
    st.write("Registra el trabajo realizado:")
    st.camera_input("Foto del trabajo")
    st.text_area("Observaciones")
    if st.button("Guardar Informe"):
        st.balloons()
        st.success("Informe registrado correctamente.")
