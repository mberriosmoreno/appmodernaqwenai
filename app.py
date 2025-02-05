import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi App Moderna",
    page_icon="📊",  # Emoji como ícono
    layout="wide",   # Usa todo el ancho de la pantalla
    initial_sidebar_state="expanded"
)

# Personalización global del estilo
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6;
        }
        h1 {
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Personalización del sidebar
st.sidebar.image("assets/logo.png", use_container_width =True)
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

# Pie de página
st.markdown("---")
st.markdown("© 2023 Mi App Moderna. Todos los derechos reservados.")
