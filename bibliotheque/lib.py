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
date = datetime.datetime.now().strftime("%d-%m-%Y")
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from getpass import getpass

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

def set_stage(i):
    """change l'état du stage avec l'entrée

    Args:
        i (string): état dans lequel on met le stage
    """
    st.session_state.stage = i


def generer_pdf():
    """génère un pdf avec les réponses chargées dans les sessions states

    Args:
        0
    Return:
        pdf_file {string} : nom du pdf généré
    """
    
    pdf_file = f"réponses_questionnaire_{date}.pdf"
    document = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    # Créer un style pour le texte
    styles = getSampleStyleSheet()
    style_normal = styles['Normal']
    
    # Créer une liste de contenu
    content = []
    
    # Ajouter du texte au contenu (automatiquement positionné)
    texte = f"<b>Récapitulatif du questionnaire</b>"
    
    texte_contacts = f"""
    {st.session_state.liste_reponse4["prenom"]}  {st.session_state.liste_reponse4["nom"]}<br />
    adresse: {st.session_state.liste_reponse4["adresse"]}<br />
    mail: {st.session_state.liste_reponse4["mail"]}<br />
    téléphone: {st.session_state.liste_reponse4["telephone"]}<br />
    Contact de préférence {st.session_state.liste_reponse4["horaire_appel"]} via {st.session_state.liste_reponse4["support"]}<br />
    <br />
    """
    
    texte_reponses = f"""
    recommandé par {st.session_state.liste_reponse["recommandation"]}<br />
    Les habitudes alimentaires jouent un rôle dans l'état de santé : {st.session_state.liste_reponse["alimentation_sante"]}<br />
    Vous accordez de l'importance à votre alimentation à {st.session_state.liste_reponse["importance_alimentation"]} sur 10<br />
    Votre alimentation actuelle vous satisfait à {st.session_state.liste_reponse["satisfaction_alimentation"]}<br />
    Régime alimentaire: {st.session_state.liste_reponse["regime_alimentaire"]}<br />
    Etat actuel de bien-être en général: {st.session_state.liste_reponse["etat_bien_etre"]}<br />
    <br />
    Vous souhaitez changer dans votre quotidien: <br />
    """
    
    texte_reponse3 = f"""
    Thème qui vous intéresse le plus: {st.session_state.liste_reponse2["theme_prefere"]}<br />
    Si vous deviez changer quelque chose dans votre quotidien, pensez-vous qu'un accompagnement personnalisé et gratuit soit un plus ? : {st.session_state.liste_reponse2["accompagnement_perso"]}<br />
    Lorsque vous commandez en ligne, préférez-vous avoir un interlocuteur identifié qui puisse vous accompagner au besoin ? : {st.session_state.liste_reponse2["interlocuteur_perso"]}<br />
    <br />
    """
    
    texte_rendez_vous_presentation = f"Vous avez choisi un rendez-vous pour une présentation personnalisée.<br />"
    texte_rendez_vous_telephone = f"Vous avez choisi un rendez-vous par téléphone à partir du : {str(st.session_state.liste_reponse3['date'])}. <br />"
    
    # Ajouter du texte au contenu du PDF
    content.append(Paragraph(texte, style_normal))
    content.append(Paragraph(texte_contacts, style_normal))
    content.append(Paragraph(texte_reponses, style_normal))
    for rep in st.session_state.liste_reponse2["choix_multiple"]:
        content.append(Paragraph(f"- {rep}", style_normal))
    content.append(Paragraph(texte_reponse3, style_normal))
    if st.session_state.liste_reponse3["rendez_vous"] == "Je souhaite prendre rendez-vous pour une présentation personnalisée":
        content.append(Paragraph(texte_rendez_vous_presentation, style_normal))
    else:
        content.append(Paragraph(texte_rendez_vous_telephone, style_normal))
        
    # Générer le PDF
    document.build(content)
    
    return pdf_file



def envoi_mail():
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
    message['Subject'] = "Nouvelle Réponse au questionnaire"

    # Corps du message
    corps_message = f"{st.session_state.liste_reponse4['prenom']} {st.session_state.liste_reponse4['nom']} a répondu au questionnaire. Les réponses sont en pièces jointes."

    # Attacher le corps du message au message
    message.attach(MIMEText(corps_message, 'plain'))

    # Pièce jointe
    nom_piece_jointe = f"réponses_questionnaire_{date}.pdf"  # Remplacez par le nom de votre fichier
    chemin_fichier = f"réponses_questionnaire_{date}.pdf"  # Remplacez par le chemin de votre fichier

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

    st.success("Réponses envoyé avec succès.")

# def run_pdf(stage):
#     set_stage(stage)
#     pdf_file = generer_pdf()
#     envoi_mail()
    