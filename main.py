# Import des bibliothèques
import streamlit as st
from bibliotheque.lib import  *
from st_pages import Page, show_pages, add_page_title
import datetime


# Configurations

config_site("centered")
# sidebar()



header_avec_image("Questionnaire", "")

# Code principal










# Formulaire

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button(block, liste_reponse1):
    st.session_state.clicked = True
    block.write(f"Bienvenue")
    block.write(liste_reponse1)


if not st.session_state.clicked:
    """
    Bonjour,

    Ce questionnaire est une introduction pour savoir s'il serait pertinent pour vous de découvrir nos solutions de bien être. 
    Avant de commencer, par qui avez vous eu ce questionnaire : 
    """
    recommandation = st.text_input("Il m'a été recommandé par :", max_chars=25, placeholder="Nom de la personne", key="recommandation")
    
    alimentation_sante = st.radio(
    "Pensez-vous que les habitudes alimentaires jouent un rôle dans l'état de santé",
    ["Pas du tout", "Ca dépends", "Tout à fait", "Plutôt non", "Plutôt oui"])
    
    importance_alimentation = st.slider('Sur une échelle de 1 à 10, quelle importance accordez-vous à votre alimentation dans votre vie quotidienne ?', 0, 10, 5)
    satisfaction_alimentation = st.slider('Sur une échelle de 1 à 10, à quel point votre alimentation actuelle vous satisfait-elle ?', 0, 10, 5)

    regime_alimentaire = st.radio(
    "Êtes-vous",
    ["Aucun", "Végétarien", "Végétalien", "Flexitarien", "Autre"])


    etat_bien_etre = st.select_slider(
    "Pour finir avec les questions générales, globalement, comment estimez vous votre état actuel de bien-être en général :",
    ["Mauvais", "Passable", "Moyen", "Bon", "Excellent"], value="Moyen")

    liste_reponse1 = [recommandation, alimentation_sante, importance_alimentation, satisfaction_alimentation, regime_alimentaire, etat_bien_etre]

block = st.container()
block.write("")

if not st.session_state.clicked:
    submitted = st.button("Envoyer", on_click=click_button, args=[block, liste_reponse1])













# # Bonton envoi mail
# import smtplib
# from email.mime.text import MIMEText


# if st.button('envoi email'):
# # Création de l'email
#     import smtplib
#     from email.mime.multipart import MIMEMultipart
#     from email.mime.text import MIMEText
#     from email.mime.application import MIMEApplication
#     from getpass import getpass

#     # Informations sur l'expéditeur
#     expediteur = "melo.surseine@gmail.com"
#     # Ouvrir le fichier texte contenant le mot de passe
#     with open("token.txt", "r") as fichier:
#         mot_de_passe = fichier.read().strip()



#     # Informations sur le destinataire
#     destinataire = "melo.surseine@gmail.com"

#     # Créer un objet MIMEMultipart
#     message = MIMEMultipart()

#     # Configurer les détails du message
#     message['From'] = expediteur
#     message['To'] = destinataire
#     message['Subject'] = "Sujet de l'e-mail"

#     # Corps du message
#     corps_message = "Ceci est le corps de l'e-mail."

#     # Attacher le corps du message au message
#     message.attach(MIMEText(corps_message, 'plain'))

#     # Pièce jointe
#     nom_piece_jointe = "CV-Melody-Duplaix.pdf"  # Remplacez par le nom de votre fichier
#     chemin_fichier = "assets/CV-Melody-Duplaix.pdf"  # Remplacez par le chemin de votre fichier

#     with open(chemin_fichier, "rb") as fichier:
#         piece_jointe = MIMEApplication(fichier.read(), _subtype="txt")
#         piece_jointe.add_header('content-disposition', 'attachment', filename=nom_piece_jointe)
#         message.attach(piece_jointe)


#     # Établir une connexion avec le serveur SMTP de Gmail
#     serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
#     serveur_smtp.starttls()

#     # Connexion au compte Gmail
#     serveur_smtp.login(expediteur, mot_de_passe)

#     # Envoyer l'e-mail
#     texte_complet = message.as_string()
#     serveur_smtp.sendmail(expediteur, destinataire, texte_complet)

#     # Fermer la connexion SMTP
#     serveur_smtp.quit()

#     print("E-mail envoyé avec succès.")










# # bouton pdf
# import streamlit as st
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import base64  # Importer la bibliothèque base64

# # Fonction pour générer le PDF
# def generer_pdf():
#     # Créer un objet de document PDF
#     pdf_file = "assets/exemple.pdf"
#     document = SimpleDocTemplate(pdf_file, pagesize=letter)

#     # Créer un style pour le texte
#     styles = getSampleStyleSheet()
#     style_normal = styles['Normal']

#     # Créer une liste de contenu
#     content = []

#     # Ajouter du texte au contenu (automatiquement positionné)
#     texte = """
#     Ceci est un exemple de document PDF généré avec Streamlit.
#     Le positionnement du texte est géré automatiquement.
#     """

#     content.append(Paragraph(texte, style_normal))

#     # Générer le PDF
#     document.build(content)

#     return pdf_file

# # Interface utilisateur Streamlit
# st.title("Générateur de PDF")

# # Bouton pour générer le PDF
# if st.button("Générer le PDF"):
#     pdf_file = generer_pdf()
#     st.success("Le PDF a été généré avec succès!")

#     # Bouton de téléchargement avec le bon type MIME pour PDF
#     with open(pdf_file, "rb") as f:
#         pdf_bytes = f.read()
#     st.download_button(
#         label="Télécharger le PDF",
#         data=pdf_bytes,
#         file_name="assets/exemple.pdf",  # Nom du fichier PDF
#         key="download_pdf",
#     )


        



























footer()