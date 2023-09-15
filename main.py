# Import des bibliothèques
import streamlit as st
from bibliotheque.lib import  *
from st_pages import Page, show_pages, add_page_title
import datetime
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from bs4 import BeautifulSoup
import base64  # Importer la bibliothèque base64

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

date = datetime.datetime.now().strftime("%d-%m-%Y")


# Configurations

config_site("centered")
# sidebar()



header_avec_image("Questionnaire", "")

# Code principal




# Formulaire


# initialisation du stage 
if 'stage' not in st.session_state:
    st.session_state.stage = "début"

#  fonction changement de stage
   

# Première partie du questionnaire si l'état est à "début"
if st.session_state.stage == "début":
    liste_reponse = {}
    # Introduction
    """
    Bonjour,

    Ce questionnaire est une introduction pour savoir s'il serait pertinent pour vous de découvrir nos solutions de bien être. 
    Avant de commencer, par qui avez vous eu ce questionnaire : 
    """
    # questionnaire
    liste_reponse["recommandation"] = st.text_input("Il m'a été recommandé par :", max_chars=25, placeholder="Nom de la personne", key="recommandation")
    
    liste_reponse["alimentation_sante"] = st.select_slider(
    "Pensez-vous que les habitudes alimentaires jouent un rôle dans l'état de santé",
    ["Pas du tout", "Plutôt non", "Ca dépends", "Plutôt oui", "Tout à fait"], value="Ca dépends")
    
    liste_reponse["importance_alimentation"] = st.slider('Sur une échelle de 1 à 10, quelle importance accordez-vous à votre alimentation dans votre vie quotidienne ?', 0, 10, 5)
    
    liste_reponse["satisfaction_alimentation"] = st.slider('Sur une échelle de 1 à 10, à quel point votre alimentation actuelle vous satisfait-elle ?', 0, 10, 5)

    liste_reponse["regime_alimentaire"] = st.radio(
    "Êtes-vous",
    ["Aucun", "Végétarien", "Végétalien", "Flexitarien", "Autre"])


    liste_reponse["etat_bien_etre"] = st.select_slider(
    "Pour finir avec les questions générales, globalement, comment estimez vous votre état actuel de bien-être en général :",
    ["Mauvais", "Passable", "Moyen", "Bon", "Excellent"], value="Moyen")

    # envoi des réponses dans un session_state
    st.session_state.liste_reponse = liste_reponse

# création d'un container pour y mettre des éléments
block = st.container()
block.write("")

# bouton pour passer à la deuxième partie si l'état du stage est à "début"
if st.session_state.stage == "début":
    st.button("Suite", on_click=set_stage, args=["deuxième bloc"])


# Deuxième partie du questionnaire si l'état du stage est à "deuxième bloc"
if st.session_state.stage == "deuxième bloc":
    liste_reponse2 = {}
    
    # Intro
    st.write("Maintenant, parlons de vous :")
        
    # questionnaire checkbox multiples
    
    "Si vous deviez changer quelque chose dans votre quotidien, ce serait pour :"
    choix_stress = st.checkbox("Gérez votre stress")
    choix_sommeil = st.checkbox("Améliorer votre qualité de sommeil")
    choix_fatigue = st.checkbox("Diminuer votre fatigue")
    choix_digestif = st.checkbox("Gagner en confort digestif")
    choix_peau = st.checkbox("Prendre soin de votre peau")
    choix_poids = st.checkbox("Gérer votre poids")
    choix_forme = st.checkbox("Être plus en forme, avoir plus de tonus")
    choix_fumer = st.checkbox("Arrêter de fumer")
    choix_sport = st.checkbox("Améliorer mes performances sportives")
    choix_recuperation = st.checkbox("Mieux récupérer après l’effort")
    choix_vieillir = st.checkbox("Bien vieillir")
    choix_autre = st.checkbox("Autre")
    
    liste_reponse2["theme_prefere"] = st.text_input("Parmi les thèmes abordés précédemment, quel est celui sur lequel vous seriez le plus intéressé(e) à en savoir plus ?")
    
    liste_reponse2["accompagnement_perso"] = st.radio("Si vous deviez changer quelque chose dans votre quotidien, pensez-vous qu'un accompagnement personnalisé et gratuit soit un plus ?", ["non","oui"])
    liste_reponse2["interlocuteur_perso"] = st.radio("Lorsque vous commandez en ligne, préférez-vous avoir un interlocuteur identifié qui puisse vous accompagner au besoin ?", ["non","oui"])
    
    
    
    # Création de la liste avec les checkbox choix multiples
    liste_checkox2 = []
    if choix_stress:
        liste_checkox2.append("Gérez votre stress")
    if choix_sommeil:
        liste_checkox2.append("Améliorer votre qualité de sommeil")
    if choix_fatigue:
        liste_checkox2.append("Diminuer votre fatigue")
    if choix_digestif:
        liste_checkox2.append("Gagner en confort digestif")
    if choix_peau:
        liste_checkox2.append("Prendre soin de votre peau")
    if choix_poids:
        liste_checkox2.append("Gérer votre poids")
    if choix_forme:
        liste_checkox2.append("Être plus en forme, avoir plus de tonus")
    if choix_fumer:
        liste_checkox2.append("Arrêter de fumer")
    if choix_sport:
        liste_checkox2.append("Améliorer mes performances sportives")
    if choix_recuperation:
        liste_checkox2.append("Mieux récupérer après l'effort")
    if choix_vieillir:
        liste_checkox2.append("Bien vieillir")
    if choix_autre:
        liste_checkox2.append("Autre")
        
    liste_reponse2["choix_multiple"] = liste_checkox2
    
    # envoi de la liste dans un session_state
    st.session_state.liste_reponse2 = liste_reponse2
    

# bouton pour envoyer à la troisième partie si le stage est à deuxième bloc
if st.session_state.stage == "deuxième bloc":
    st.button("Suite", on_click=set_stage, args=["troisième bloc"])


# Troisième partie du questionnaire si le stage est à "troisième bloc"

if st.session_state.stage == "troisième bloc":
    
    # creation de la date si il n'en choisit pas
    liste_reponse3 = {}
    liste_reponse3["date"] = None
        
    # Intro
    "Merci d'avoir répondu ! Et maintenant :"
    
    # Choix du rendez-vous
    liste_reponse3["rendez_vous"] = st.radio(" ", ["Je souhaite prendre rendez-vous pour une présentation personnalisée", "Je souhaite être rappelé à partir du  :"])
    if liste_reponse3["rendez_vous"] == "Je souhaite être rappelé à partir du  :":
        liste_reponse3["date"] = st.date_input("")

    # envoi des données en session_state
    st.session_state.liste_reponse3 = liste_reponse3

# bouton pour envoyer à la quatrième partie si le stage est à troisième bloc
if st.session_state.stage == "troisième bloc":
    st.button("Suite", on_click=set_stage, args=["quatrième bloc"])


# Troisième partie du questionnaire si le stage est à "troisième bloc"
if st.session_state.stage == "quatrième bloc":
        
    # Intro
    "Pour que nous puissions vous recontacter, merci de remplir les information ci dessous :"
    
    # questionnaire de contacts
    liste_reponse4 = {}
    liste_reponse4["nom"] = st.text_input("Nom")
    liste_reponse4["prenom"] = st.text_input("Prénom")
    liste_reponse4["adresse"] = st.text_input("Adresse")
    liste_reponse4["mail"] = st.text_input("Mail")
    liste_reponse4["telephone"] = st.text_input("Téléphone")
    liste_reponse4["horaire_appel"] = st.text_input("Jours et horaires d'appels")
    
    # checkbox choix multiples
    "support d'appel préféré"
    choix_mobile = st.checkbox("Mobile")
    choix_sms = st.checkbox("SMS")
    choix_messenger = st.checkbox("Messenger")
    choix_whatshapp = st.checkbox("WhatsApp")
    choix_mail = st.checkbox("Mail")
    
    liste_support_prefere = []
    # conversion en une liste
    if choix_mobile:
        liste_support_prefere.append("Mobile")
    if choix_sms:
        liste_support_prefere.append("SMS")
    if choix_messenger:
        liste_support_prefere.append("Messenger")
    if choix_whatshapp:
        liste_support_prefere.append("WhatsApp")
    if choix_mail:
        liste_support_prefere.append("Mail")
    liste_reponse4["support"] = liste_support_prefere
    
    # envoi des données en session_state
    st.session_state.liste_reponse4 = liste_reponse4
    

# Bouton d'envoi des questions après la quatrieme partie
if st.session_state.stage == "quatrième bloc":
    st.button("Envoi des données", on_click=set_stage, args=["Fin"])
    
    
    
    

# Affichage final
if st.session_state.stage == "Fin":


    # Générer le pdf
    pdf_file = generer_pdf()
    envoi_mail()

    # Bouton de téléchargement avec le bon type MIME pour PDF
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
        label="Télécharger le PDF",
        data=pdf_bytes,
        file_name=f"reponses/réponses_questionnaire_{date}_{st.session_state.liste_reponse4['prenom']}_{st.session_state.liste_reponse4['nom']}.pdf",  # Nom du fichier PDF
        key="download_pdf",
    )

    
    

footer()