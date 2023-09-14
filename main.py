# Import des bibliothèques
import streamlit as st
from bibliotheque.lib import  *
from st_pages import Page, show_pages, add_page_title
import datetime


# Configurations

config_site("centered")
# sidebar()



header_avec_image("Questionnaire", "Questionnaire")

# Code principal










# Formulaire

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button(prenom, nom, block):
    st.session_state.clicked = True
    block.write(f"Bienvenue {prenom} {nom}")

prenom =""
nom=""

if not st.session_state.clicked:
    prenom = st.text_area("Prénom", max_chars=25, placeholder="Pas de prénom", height=1, key="prenom")
    st.write("hello world")
    nom = st.text_area("Nom", max_chars=25, placeholder="Pas de nom", height=1, key="nom")

    mail = st.text_area("Mail", max_chars=50, placeholder="Pas de mail", height=1, key="mail")
    # if mail and( not "@" in mail or " " in mail):
    #     st.write(":red[Le mail n'est pas valide !]")
        
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

block = st.container()
block.write("")

if not st.session_state.clicked:
    submitted = st.button("Envoyer", on_click=click_button, args=[prenom, nom, block])










# Bonton envoi mail
import smtplib
from email.mime.text import MIMEText


if st.button('envoi email'):
# Création de l'email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from getpass import getpass

    # Informations sur l'expéditeur
    expediteur = "melo.surseine@gmail.com"
    # Ouvrir le fichier texte contenant le mot de passe
    with open("token.txt", "r") as fichier:
        mot_de_passe = fichier.read().strip()



    # Informations sur le destinataire
    destinataire = "melo.surseine@gmail.com"

    # Créer un objet MIMEMultipart
    message = MIMEMultipart()

    # Configurer les détails du message
    message['From'] = expediteur
    message['To'] = destinataire
    message['Subject'] = "Sujet de l'e-mail"

    # Corps du message
    corps_message = "Ceci est le corps de l'e-mail."

    # Attacher le corps du message au message
    message.attach(MIMEText(corps_message, 'plain'))

    # Pièce jointe
    nom_piece_jointe = "CV-Melody-Duplaix.pdf"  # Remplacez par le nom de votre fichier
    chemin_fichier = "assets/CV-Melody-Duplaix.pdf"  # Remplacez par le chemin de votre fichier

    with open(chemin_fichier, "rb") as fichier:
        piece_jointe = MIMEApplication(fichier.read(), _subtype="txt")
        piece_jointe.add_header('content-disposition', 'attachment', filename=nom_piece_jointe)
        message.attach(piece_jointe)


    # Établir une connexion avec le serveur SMTP de Gmail
    serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    serveur_smtp.starttls()

    # Connexion au compte Gmail
    serveur_smtp.login(expediteur, mot_de_passe)

    # Envoyer l'e-mail
    texte_complet = message.as_string()
    serveur_smtp.sendmail(expediteur, destinataire, texte_complet)

    # Fermer la connexion SMTP
    serveur_smtp.quit()

    print("E-mail envoyé avec succès.")






footer()