import streamlit as st
from bibliotheque.lib import  *
from st_pages import Page, show_pages, add_page_title, Section
from datetime import datetime
from PIL import Image


# Définition des fonctions


def sidebar():
    """
    Nom : sidebar
    Paramètres : 0
    Traitement : configures les pages de la sidebar
    Retour : un affichage
    """
    show_pages(
        [
            Page("main.py", "Home", "🏠")
        ]
    )
    st.sidebar.title("Menu")


def header_avec_image(f_titre, f_contexte):
    """
    Nom : header_avec_image
    Paramètres : 2, 1-chaine de caractère, 2-chaine de caractère
    Traitement : crée un header avec une image, un titre, et un contexte
    Retour : un affichage
    """
    colonne_logo, colonne_titre = st.columns([1,5])
    with colonne_logo:
        logo = Image.open("images/photoprofillinkedIn.excalidraw.png")
        logo_reduit = logo.resize([70,50])
        st.image(logo_reduit)
    with colonne_titre:
        st.title(f_titre)
    st.write(f_contexte)
    st.write()


def header(f_titre, f_contexte):
    """
    Nom : header
    Paramètres : 2, 1-chaine de caractère, 2-chaine de caractère
    Traitement : crée un header avec un titre, et un contexte
    Retour : un affichage
    """
    colonne_logo, colonne_titre = st.columns([1,5])
    with colonne_logo:
        st.write("")
    with colonne_titre:
        st.title(f_titre)
    st.write(f_contexte)
    st.write()


def formatage_de_la_page(f_fichier_css):
    """
    Nom : formatage_de_la_page
    Paramètres : 1 chaine de caractère
    Traitement : prend un fichier css et applique le style
    Retour : un affichage
    """
    with open(f_fichier_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def config_site(f_layout):
    """
    Nom : config_site
    Paramètres : 1 chaine de caractère
    Traitement : configure les options de la page, avec le layout choisi ("wide" ou "centered")
    Retour : un affichage
    """
    st.set_page_config(
        page_title="Questionnaire",
        page_icon="📄",
        layout=f_layout
    )
    formatage_de_la_page("style.css")


def footer():
    """
    Nom : footer
    Paramètres : 0
    Traitement : crée un footer avec les deux liens vers RGPD et mentions légales
    Retour : un affichage
    """
    texte = """
    <div class=footer>
        <a href='Mentions Légales' target='_self' class='link'>Mentions légales</a> 
        <a href='RGPD' target= '_self' class='link'>RGPD</a> 
    </div>
    """
    st.markdown(texte, unsafe_allow_html=True)
