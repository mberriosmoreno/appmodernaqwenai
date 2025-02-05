import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la página
st.title("📈 Análisis de Datos")

# Cargar datos de ejemplo
@st.cache_data
def cargar_datos():
    return pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = cargar_datos()

# Mostrar datos
st.subheader("Datos del Titanic")
st.dataframe(df.head())

# Gráfico interactivo
st.subheader("Distribución de Edades")
fig = px.histogram(df, x="Age", nbins=30, title="Histograma de Edades")
st.plotly_chart(fig, use_container_width=True)

# Filtrar datos
st.subheader("Filtrar Pasajeros por Clase")
clase = st.selectbox("Selecciona la clase:", [1, 2, 3])
filtered_df = df[df["Pclass"] == clase]
st.dataframe(filtered_df[["Name", "Sex", "Age", "Fare"]])
