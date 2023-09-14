# Import des bibliothèques
import streamlit as st
import pandas as pd
from bibliotheque.lib import  *
from st_pages import Page, show_pages, add_page_title


# Configurations

config_site("centered")
# sidebar()



header_avec_image("Questionnaire", "Questionnaire")

# Code principal

# Formulaire
with st.form("Formulaire d'ajout", clear_on_submit=True):
    
    prenom = st.text_area("Prénom", max_chars=25, placeholder="Pas de prénom", height=1, key="prenom")
    
    nom = st.text_area("Nom", max_chars=25, placeholder="Pas de nom", height=1, key="nom")
    
    mail = st.text_area("Mail", max_chars=50, placeholder="Pas de mail", height=1, key="mail")
    if mail and( not "@" in mail or " " in mail):
        st.write(":red[Le mail n'est pas valide !]")
        
    today = datetime.datetime.now()
    date_de_naissance = st.date_input(
        "Date de naissance", max_value=datetime.date((today.year-18), 1, 1), min_value= datetime.date((today.year-100), 1, 1),
        format="DD/MM/YYYY", value= datetime.date((today.year-30), 1, 1), key="date_naissance"
    )

    genre = st.selectbox("Genre", ("F","M"), help="Homme : H Femme : F", key="genre")
    date_arrive = st.date_input(
        "Date d'entrée dans l'entreprise", min_value= datetime.date((today.year-60), 1, 1),
        format="DD/MM/YYYY", key="date_arrive"
    )
    
    
    submitted = st.form_submit_button("Envoyer")
    if submitted and prenom and nom and mail:
        pass






footer()