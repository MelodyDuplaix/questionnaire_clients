# Import des bibliothèques
import streamlit as st
from bibliotheque.lib import  *
import datetime
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Comic Sans MS', 'assets/ComicSans.ttf'))
date = datetime.datetime.now().strftime("%d-%m-%Y")
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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
        layout=f_layout,
        menu_items={
            "Get Help": "mailto:antoinemoure.mgc@gmail.com",
            "About" : "https://beautysane.com/?idm=144394"
        }
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
        <a href='Pages/mentions_legales.py' target='_self' class='link'>Mentions légales</a> 
        <a href='Pages/rgpd.py' target='_self' class='link'>RGPD</a> 
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
    # Nom du fichier PDF
    pdf_file = f"reponses/réponses_questionnaire_{date}_{st.session_state.liste_reponse4['prenom']}_{st.session_state.liste_reponse4['nom']}.pdf"
    
    # Création du document PDF
    document = SimpleDocTemplate(pdf_file, pagesize=letter)
    
    # Styles personnalisés
    styles = getSampleStyleSheet()
    style_titre = ParagraphStyle(
        "StyleTitre",
        parent=styles["Heading1"],
        fontSize=16,
        textColor=colors.blue,
        alignment=1,
        spaceBefore=12,
        spaceAfter=12,
        fontName='Comic Sans MS'
    )
    style_sous_titre = ParagraphStyle(
        "StyleSousTitre",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.blue,
        alignment=0,
        spaceBefore=12,
        spaceAfter=12,
        fontName='Comic Sans MS'
    )
    style_normal = ParagraphStyle(
        "StyleNormal",
        parent=styles["Normal"],
        fontSize=12,
        textColor=colors.black,
        alignment=0,
        spaceBefore=6,
        spaceAfter=6,
        leftIndent=30,
    )
    
    # Contenu du PDF
    content = []
    
    # Titre principal
    titre = Paragraph("Recapitulatif du questionnaire", style_titre)
    content.append(titre)
    content.append(Paragraph(f"{st.session_state.liste_reponse4['prenom']} {st.session_state.liste_reponse4['nom']}", style_titre))
    
    # Informations de contact
    content.append(Spacer(1, 12))  # Espace vertical
    content.append(Paragraph("Informations de contact :", style_sous_titre))
    content.append(Paragraph(f"Adresse : {st.session_state.liste_reponse4['adresse']}", style_normal))
    content.append(Paragraph(f"Mail : {st.session_state.liste_reponse4['mail']}", style_normal))
    content.append(Paragraph(f"Téléphone : {st.session_state.liste_reponse4['telephone']}", style_normal))
    content.append(Paragraph(f"Contact de préférence : {st.session_state.liste_reponse4['horaire_appel']} via {' ou '.join(st.session_state.liste_reponse4['support'])}", style_normal))
    
    # Réponses au questionnaire
    content.append(Spacer(1, 12))  # Espace vertical
    content.append(Paragraph("Reponses au questionnaire :", style_sous_titre))
    content.append(Paragraph(f"Recommandé par : {st.session_state.liste_reponse['recommandation']}", style_normal))
    content.append(Paragraph(f"Les habitudes alimentaires jouent un rôle dans l'état de santé : {st.session_state.liste_reponse['alimentation_sante']}", style_normal))
    content.append(Paragraph(f"Importance accordée à l'alimentation : {st.session_state.liste_reponse['importance_alimentation']}/10", style_normal))
    content.append(Paragraph(f"Satisfaction actuelle de l'alimentation : {st.session_state.liste_reponse['satisfaction_alimentation']}/10", style_normal))
    content.append(Paragraph(f"Régime alimentaire : {st.session_state.liste_reponse['regime_alimentaire']} {st.session_state.liste_reponse['regime_autre']}", style_normal))
    content.append(Paragraph(f"État actuel de bien-être en général : {st.session_state.liste_reponse['etat_bien_etre']}", style_normal))
    content.append(Paragraph("Changements souhaités dans le quotidien :", style_normal))
    for rep in st.session_state.liste_reponse2["choix_multiple"]:
        content.append(Paragraph(f" • {rep}", style_normal))
    content.append(Paragraph(f"Thème qui m'intéresse le plus : {st.session_state.liste_reponse2['theme_prefere']}", style_normal))
    
    # Accompagnement personnalisé et interlocuteur identifié
    content.append(Spacer(1, 12))  # Espace vertical
    content.append(Paragraph("Choix d'accompagnemant :", style_sous_titre))
    content.append(Paragraph(f"Accompagnement personnalisé et gratuit : {st.session_state.liste_reponse2['accompagnement_perso']}", style_normal))
    content.append(Paragraph(f"Interlocuteur identifié pour les commandes en ligne : {st.session_state.liste_reponse2['interlocuteur_perso']}", style_normal))
    
    # Rendez-vous
    content.append(Spacer(1, 12))  # Espace vertical
    content.append(Paragraph("Rendez-vous :", style_sous_titre))
    if st.session_state.liste_reponse3["rendez_vous"] == "Je souhaite prendre rendez-vous pour une présentation personnalisée":
        content.append(Paragraph("Vous avez choisi un rendez-vous pour une présentation personnalisée.", style_normal))
    else:
        content.append(Paragraph(f"Vous avez choisi un rendez-vous par téléphone à partir du : {st.session_state.liste_reponse3['date']}.", style_normal))
    
    # Génération du PDF
    document.build(content)
    
    return pdf_file



def envoi_mail():
    # Informations sur l'expéditeur
    expediteur = "melo.surseine@gmail.com"
    # Ouvrir le fichier texte contenant le mot de passe
    try:
        mot_de_passe = st.secrets["token_mail"]
    except:
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
    nom_piece_jointe = f"reponses/réponses_questionnaire_{date}_{st.session_state.liste_reponse4['prenom']}_{st.session_state.liste_reponse4['nom']}.pdf"  # Remplacez par le nom de votre fichier
    chemin_fichier = f"reponses/réponses_questionnaire_{date}_{st.session_state.liste_reponse4['prenom']}_{st.session_state.liste_reponse4['nom']}.pdf"  # Remplacez par le chemin de votre fichier

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


def switch_page(page_name: str):
    """change de page

    Args:
        page_name (str): nom de la ou l'on veut emmener

    Raises:
        RerunException: page non trouvée
        ValueError: noms des pages dispo

    Returns:
        _type_: _description_
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("main.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")