import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


data = pd.read_csv('dataset.csv', encoding='latin1')
data.fillna('', inplace=True)  # Reemplaza los valores NaN con cadenas vacías
preguntas = data["pregunta"].tolist()
respuestas = data["respuesta"].tolist()

vectorizer = TfidfVectorizer()
preguntas_vectorizadas = vectorizer.fit_transform(preguntas)
respuestas_vectorizadas = vectorizer.transform(respuestas)

modelo = NearestNeighbors(n_neighbors=1)
modelo.fit(preguntas_vectorizadas)

def obtener_respuesta(pregunta):
    pregunta_vectorizada = vectorizer.transform([pregunta])
    indice_mas_cercano = modelo.kneighbors(pregunta_vectorizada)[1][0][0]
    return respuestas[indice_mas_cercano]

st.title("Chatbot")

pregunta = st.text_input("Pregunta:")
if st.button("Enviar"):
    respuesta = obtener_respuesta(pregunta)
    if respuesta:
        st.markdown(f'**Respuesta:**\n\n{respuesta}')
    else:
        st.markdown('Lo siento, esta pregunta aún no soy capaz de responderla, ¿podrias reformular tu pregunta?')

for _ in range(10):  # Añadir espacios en blanco
    st.write('')

st.markdown('---')

st.markdown('<p style="text-align: center;">UPIICSA - IPN</p>', unsafe_allow_html=True)
st.write('2020600143 BARROSO MOLINA KATHERINE.')
st.write('2019602149 GONZÁLEZ PEÑA MARCOS')
st.write('2014170481 HERNANDEZ ARTEAGA DANTE OLAF')
st.write('2020600591 HERNÁNDEZ HERRERA NATALIA PAOLA')
st.write('2020600986 RUVALCABA BUENROSTRO ROBERTO CARLO')