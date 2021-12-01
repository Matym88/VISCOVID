
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")

st.title("visualizacion de los datos COVID-19 chile")

st.markdown("### bienvenido al visualizador")

df = pd.read_csv(
    "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")

st.dataframe(df.head(10))
# agregaremos dos columnas
col1, col2 = st.columns(2)


with col1:

    region = st.radio("Region", df.Region.unique())
    st.markdown("Su seleccion es: " + region)
with col2:
    categoria = st.radio("Categoria", df.Categoria.unique())
    st.markdown("Su seleccion es: "+categoria)

columnas = list(df.columns)
# st.markdown(columnas)

# filtrando los datos que necesito
ilocs = df.iloc[:, 2:-1]
super_filtro = df[(df.Region == region) & (df.Categoria == categoria)]
st.dataframe(super_filtro)

# definiendo la figura del grafico
fig, ax = plt.subplots()
to_plot = super_filtro.iloc[:, 2:-1]
# grafico
ax.plot(to_plot.T)
# adornando el grafico
ax.set_title(region)
ax.set_ylabel('casos')
ax.set_xlabel('fechas')

xs = np.arange(0, super_filtro.shape[1]-2, 30)
plt.xticks(xs, rotation=90)

# grafico de la figura
st.pyplot(fig)
