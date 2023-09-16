from bibliotheque.lib import *
import streamlit as st

config_site("centered")
# sidebar()

st.title("Questionnaire")

"""
Ce questionnaire en ligne est fourni par antoinemoure.mgc@gmail.com, ci-après dénommée "nous" ou "notre".

Coordonnées :

antoinemoure.mgc@gmail.com

Utilisation des données personnelles :

Les données personnelles que vous fournissez en remplissant ce questionnaire seront utilisées exclusivement aux fins de la prise de rendez-vous ou du rappel, conformément au Règlement Général sur la Protection des Données (RGPD) et à la législation applicable en matière de protection des données.

Vos données personnelles ne seront en aucun cas partagées, vendues ou utilisées à d'autres fins sans votre consentement explicite. Vous avez le droit de retirer votre consentement à tout moment en nous contactant à antoinemoure.mgc@gmail.com. De plus, vous avez le droit d'accéder à vos données personnelles, de les rectifier ou de les supprimer conformément aux dispositions du RGPD. Pour exercer ces droits, veuillez nous contacter à antoinemoure.mgc@gmail.com.

Sécurité des données :

Nous nous engageons à prendre toutes les mesures nécessaires pour protéger vos données personnelles et à les conserver en toute sécurité.

En utilisant ce questionnaire en ligne, vous acceptez les termes de cette politique de confidentialité et de la collecte de vos données personnelles aux fins décrites ci-dessus.

Si vous avez des questions ou des préoccupations concernant notre politique de confidentialité ou l'utilisation de vos données personnelles, veuillez nous contacter à antoinemoure.mgc@gmail.com
"""

if st.button("Questionnaire"):
    switch_page("main")
footer()