import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi App Moderna",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Personalización del sidebar
st.sidebar.image("assets/logo.png", use_container_width=True)
st.sidebar.title("Menú")
st.sidebar.markdown("""
    Bienvenido a mi aplicación moderna y elegante.  
    Navega por las opciones del menú para explorar diferentes funcionalidades.
""")

# Contenido principal
st.title("📊 Mi Aplicación Moderna y Elegante")
st.markdown("""
    Esta es una aplicación de ejemplo creada con **Streamlit**.  
    Aquí puedes realizar análisis de datos, visualizar gráficos interactivos y más.
""")
