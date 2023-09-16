# Import des bibliothèques
import streamlit as st
from bibliotheque.lib import *
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from bs4 import BeautifulSoup
import base64  # Importer la bibliothèque base64
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

date = datetime.datetime.now().strftime("%d-%m-%Y")


config_site("centered")

st.title("Questionnaire")

# Code principal

# Formulaire

# initialisation du stage
if 'stage' not in st.session_state:
    st.session_state.stage = "début"



















# Première partie du questionnaire si l'état est à "début"
if st.session_state.stage == "début":
    liste_reponse = {}
    st.warning("Attention: Si vous rafraichissez la page, le formulaire est réinitialisé")
    # Introduction
    """
    Bonjour,

    Ce questionnaire est une introduction pour savoir s'il serait pertinent pour vous de découvrir nos solutions de bien être. 
    Avant de commencer, par qui avez vous eu ce questionnaire : 
    """
    # questionnaire
    # Préremplir les champs avec les réponses précédentes si elles existent
    if 'liste_reponse' in st.session_state:
        liste_reponse = st.session_state.liste_reponse

    liste_reponse["recommandation"] = st.text_input("Il m'a été recommandé par :", max_chars=25, placeholder="Nom de la personne", key="recommandation")

    liste_reponse["alimentation_sante"] = st.select_slider(
        "Pensez-vous que les habitudes alimentaires jouent un rôle dans l'état de santé",
        ["Pas du tout", "Plutôt non", "Ça dépend", "Plutôt oui", "Tout à fait"],
        key='alimentation_sante'
    )

    liste_reponse["importance_alimentation"] = st.slider(
        'Sur une échelle de 1 à 10, quelle importance accordez-vous à votre alimentation dans votre vie quotidienne ?',
        0, 10, 5,
        key="importance_alimentation"
    )

    liste_reponse["satisfaction_alimentation"] = st.slider(
        'Sur une échelle de 1 à 10, à quel point votre alimentation actuelle vous satisfait-elle ?',
        0, 10, 5 ,
        key="satisfaction_alimentation"
    )

    choix_regime = ["Omnivore", "Flexitarien", "Végétalien", "Végétarien", "Autre :"]
    liste_reponse["regime_alimentaire"] = st.radio("Êtes-vous", choix_regime, key="regime_alimentaire")

    liste_reponse["regime_autre"] = ""
    if liste_reponse["regime_alimentaire"] == "Autre :":
        liste_reponse["regime_autre"] = st.text_input("Précisez", key="regime_autre")
    
        


    liste_reponse["etat_bien_etre"] = st.select_slider(
        "Pour finir avec les questions générales, globalement, comment estimez vous votre état actuel de bien-être en général :",
        ["Mauvais", "Passable", "Moyen", "Bon", "Excellent"],
        key="etat_bien_etre"
    )

    # envoi des réponses dans un session_state
    st.session_state.liste_reponse = liste_reponse

# création d'un container pour y mettre des éléments
block = st.container()
block.write("")

# bouton pour passer à la deuxième partie si l'état du stage est à "début"
if st.session_state.stage == "début":
    st.button("Suite", on_click=set_stage, args=["deuxième bloc"], key="début_deuxième")

















# Deuxième partie du questionnaire si l'état du stage est à "deuxième bloc"
if st.session_state.stage == "deuxième bloc":
    liste_reponse2 = {}
    

    # Intro
    st.write("Maintenant, parlons de vous :")

    # questionnaire checkbox multiples

    "Si vous deviez changer quelque chose dans votre quotidien, ce serait pour :"
    choix_stress = st.checkbox("Gérez votre stress", key="stress")
    choix_sommeil = st.checkbox("Améliorer votre qualité de sommeil", key="choix_sommeil")
    choix_fatigue = st.checkbox("Diminuer votre fatigue", key="choix_fatigue")
    choix_digestif = st.checkbox("Gagner en confort digestif", key="choix_digestif")
    choix_peau = st.checkbox("Prendre soin de votre peau", key="choix_peau")
    choix_poids = st.checkbox("Gérer votre poids", key="choix_poids")
    choix_forme = st.checkbox("Être plus en forme, avoir plus de tonus", key="choix_forme")
    choix_fumer = st.checkbox("Arrêter de fumer", key="choix_fumer")
    choix_sport = st.checkbox("Améliorer mes performances sportives", key="choix_sport")
    choix_recuperation = st.checkbox("Mieux récupérer après l'effort", key="choix_recuperation")
    choix_vieillir = st.checkbox("Bien vieillir", key="choix_vieillir")
    choix_autre = st.checkbox("Autre :", key="choix_autre")
    autre_changement = None
    if choix_autre:
        autre_changement = st.text_input("Précisez", key="autre_changement")

    liste_reponse2["theme_prefere"] = st.text_input("Parmi les thèmes abordés précédemment, quel est celui sur lequel vous seriez le plus intéressé(e) à en savoir plus ?", key="theme_prefere")

    boolean_liste = ["non","oui"]
    liste_reponse2["accompagnement_perso"] = st.radio("Si vous deviez changer quelque chose dans votre quotidien, pensez-vous qu'un accompagnement personnalisé et gratuit soit un plus ?",boolean_liste , key="accompagnement_perso")
    liste_reponse2["interlocuteur_perso"] = st.radio("Lorsque vous commandez en ligne, préférez-vous avoir un interlocuteur identifié qui puisse vous accompagner au besoin ?", boolean_liste, key="interlocuteur_perso")

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
    if choix_autre:
        liste_checkox2.append(autre_changement)

    liste_reponse2["choix_multiple"] = liste_checkox2

    # envoi de la liste dans un session_state
    st.session_state.liste_reponse2 = liste_reponse2

# bouton pour envoyer à la troisième partie si le stage est à deuxième bloc
if st.session_state.stage == "deuxième bloc":
    st.button("Suite", on_click=set_stage, args=["troisième bloc"], key="deuxième_troisieme")




















# Troisième partie du questionnaire si le stage est à "troisième bloc"
if st.session_state.stage == "troisième bloc":
    # creation de la date si il n'en choisit pas
    liste_reponse3 = {}
    liste_reponse3["date"] = None
        
    # Intro
    "Merci d'avoir répondu ! Et maintenant :"

    # Choix du rendez-vous
    liste_choix_rendezvous = ["Je souhaite prendre rendez-vous pour une présentation personnalisée", "Je souhaite être rappelé à partir du  :"]
    liste_reponse3["rendez_vous"] = st.radio(" ", liste_choix_rendezvous, key="rendez_vous")
    
    if liste_reponse3["rendez_vous"] == "Je souhaite être rappelé à partir du  :":
        liste_reponse3["date"] = st.date_input("", key="date")

    # envoi des données en session_state
    st.session_state.liste_reponse3 = liste_reponse3

# bouton pour envoyer à la quatrième partie si le stage est à troisième bloc
if st.session_state.stage == "troisième bloc":
    st.button("Suite", on_click=set_stage, args=["quatrième bloc"], key="troisième_quatrieme")





















# Troisième partie du questionnaire si le stage est à "troisième bloc"
if st.session_state.stage == "quatrième bloc":
    # Intro
    "Pour que nous puissions vous recontacter, merci de remplir les informations ci-dessous : (tous les champs sont obligatoires)"
    liste_reponse4 = {}
    
    # questionnaire de contacts
    
    liste_reponse4["prenom"] = st.text_input("Prénom", key="prenom", autocomplete="given-name", max_chars=25)
    liste_reponse4["nom"] = st.text_input("Nom", key="nom", autocomplete="family-name", max_chars=25)
    liste_reponse4["adresse"] = st.text_input("Adresse", key="adresse", autocomplete="adress", max_chars=150)
    liste_reponse4["mail"] = st.text_input("Mail", key="mail", autocomplete="email", max_chars=50)
    pattern_mail = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,6}'
    if liste_reponse4["mail"] and not re.match(pattern_mail, liste_reponse4["mail"]):
        st.error("Le mail n'est pas valide")
    liste_reponse4["telephone"] = st.text_input("Téléphone", key="telephone", autocomplete="tel", max_chars=15)
    pattern_tel = r'(0|\+33)[1-9](\s?[0-9]{2}\s?){3}[0-9]{2}'
    if liste_reponse4["telephone"] and not re.match(pattern_tel, liste_reponse4["telephone"]):
        st.error("Le téléphone n'est pas valide")
    liste_reponse4["horaire_appel"] = st.text_input("Jours et horaires d'appels", key="horaire_appel")

    # checkbox choix multiples
    "support d'appel préféré"
    choix_mobile = st.checkbox("Mobile", key="choix_mobile")
    choix_sms = st.checkbox("SMS", key="choix_sms")
    choix_messenger = st.checkbox("Messenger", key="choix_messenger")
    choix_whatshapp = st.checkbox("WhatsApp", key="choix_whatsapp")
    choix_mail = st.checkbox("Mail", key="choix_mail")

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






















# Bouton d'envoi des questions après la quatrième partie
if st.session_state.stage == "quatrième bloc":
    verif_fausse = not liste_reponse4["prenom"] or not liste_reponse4["nom"] or not liste_reponse4["adresse"] or not liste_reponse4["mail"] or not liste_reponse4["telephone"] or not liste_reponse4["horaire_appel"]
    if verif_fausse:
        st.error("Tous les champs sont obligatoires")
    if not verif_fausse and re.match(pattern_mail, liste_reponse4["mail"]) and re.match(pattern_tel, liste_reponse4["telephone"]):
            st.button("Envoi des données", on_click=set_stage, args=["Fin"], key="quatrieme_fin")

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
        file_name=f"réponses_questionnaire_{date}_{st.session_state.liste_reponse4['prenom']}_{st.session_state.liste_reponse4['nom']}.pdf",  # Nom du fichier PDF
        key="download_pdf",
    )

footer()
