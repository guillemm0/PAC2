import streamlit as st

st.set_page_config(page_title="Visualització de Dades", layout="wide")

pagines = st.navigation([
    st.Page("pagines/espelmes.py",          title="Gràfic d'Espelmes"),
    st.Page("pagines/barres_apilades.py", title="Barres Apilades"),
    st.Page("pagines/marimekko.py",      title="Marimekko"),
])
pagines.run()
