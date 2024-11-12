import streamlit as st  #importar todas las herramientas
from gtts import gTTS  # importar todas las notas de voz de google 

def create_audiobook(text , language , output_file): #está función convierte el texto en audio
    tts = gTTS(text = text , lang = language, tld='com') # crea un objeto para generar un audio 
    tts. save( output_file)  #almacena el audio con el nombre que se le asigne 

#Titulo de la aplicación 
st.title("Text2Audio")

#input del texto
text = st.text_area("introduce el texto aqui:")
    
#lista desplegable para el idioma
languages = {
    "español (es)": "es",
    "inglés (en)": "en",
    "francés (fr)": "fr",
    "alemán (de)": "de"
    }
    
language = st.selectbox("selecciona el idioma:", list(languages.keys()))
    
#lista desplegable para el acento 
accents = {
    "com": "estados unidos",
    "co.uk": "reino unido",
    "ca": "canada",
    "com.au": "australia",
    "co.in": "india"
    }
accent = st.selectbox("selecciona el acento", list(accents.keys()))

#boton para generar audiolibro 

if st.button("generar audiolibro"):
    if text:
        output_file = "audiolibro.mp3"
        create_audiobook(text, languages[language], output_file)
        st.audio(output_file, format="audio/mp3")
    else:
        st.error("por favor, introduce un texto.")





