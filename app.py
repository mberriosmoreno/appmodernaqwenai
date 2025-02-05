import streamlit as st

# Configuración de la página (primera instrucción)
st.set_page_config(
    page_title="Mi App Moderna",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Personalización del estilo
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6; /* Fondo claro */
        }
        h1 {
            color: #4CAF50; /* Títulos en verde */
        }
    </style>
""", unsafe_allow_html=True)

# Contenido principal
st.title("📊 Mi Aplicación Moderna y Elegante")
st.markdown("""
    Esta es una aplicación de ejemplo creada con **Streamlit**.  
    Aquí puedes realizar análisis de datos, visualizar gráficos interactivos y más.
""")

# Pie de página
st.markdown("---")
st.markdown("© 2023 Mi App Moderna. Todos los derechos reservados.")
