import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la página
st.title("🌍 Visualización Interactiva")

# Cargar datos de ejemplo
@st.cache_data
def cargar_datos():
    return pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = cargar_datos()

# Gráfico de dispersión
st.subheader("Gráfico de Dispersión: Tarifa vs Edad")
fig = px.scatter(
    df,
    x="Age",
    y="Fare",
    color="Pclass",
    title="Relación entre Edad y Tarifa",
    hover_data=["Name", "Sex"]
)
st.plotly_chart(fig, use_container_width=True)

# Mapa interactivo
st.subheader("Mapa de Origen de Pasajeros")
df_map = df.dropna(subset=["Embarked"])
df_map["Latitude"] = df_map["Embarked"].map({"S": 50.8973, "C": 49.1865, "Q": 51.4818})
df_map["Longitude"] = df_map["Embarked"].map({"S": -1.4044, "C": 1.3194, "Q": -8.2958})

fig_map = px.scatter_geo(
    df_map,
    lat="Latitude",
    lon="Longitude",
    color="Embarked",
    title="Origen de los Pasajeros",
    hover_name="Embarked"
)
st.plotly_chart(fig_map, use_container_width=True)
