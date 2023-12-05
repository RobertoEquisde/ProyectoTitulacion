import pandas as pd
import unicodedata

# Función para normalizar el texto
def normalizar_texto(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join([char for char in texto if unicodedata.category(char) not in ['Mn']])
    return texto

# Ruta del archivo CSV
file_path = 'dataset.csv'

# Leer el archivo CSV con la codificación Latin-1
df = pd.read_csv(file_path, encoding='latin1')

# Limpieza de datos y normalización
df = df.drop_duplicates()
df = df.fillna('')

# Aplicar la normalización a las columnas 'pregunta' y 'respuesta'
df['pregunta'] = df['pregunta'].apply(normalizar_texto).str.lower()
df['respuesta'] = df['respuesta'].apply(normalizar_texto).str.lower()

# Guardar el archivo CSV con la codificación Latin-1
df.to_csv('dataset.csv', index=False, encoding='latin1')
