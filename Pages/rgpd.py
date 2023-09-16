from bibliotheque.lib import *
import streamlit as st

config_site("centered")
# sidebar()

st.title("RGPD")

"""
En remplissant ce questionnaire en ligne et en fournissant vos coordonnées pour un rendez-vous ou un rappel, vous consentez à la collecte et au traitement de vos données personnelles conformément au Règlement Général sur la Protection des Données (RGPD) et à la législation applicable en matière de protection des données. Vos données personnelles seront utilisées exclusivement aux fins de la prise de rendez-vous ou du rappel, et elles ne seront en aucun cas partagées, vendues ou utilisées à d'autres fins sans votre consentement explicite.

Vous avez le droit de retirer votre consentement à tout moment en nous contactant à antoinemoure.mgc@gmail.com. De plus, vous avez le droit d'accéder à vos données personnelles, de les rectifier ou de les supprimer conformément aux dispositions du RGPD. Pour exercer ces droits, veuillez nous contacter à antoinemoure.mgc@gmail.com.
"""

if st.button("Questionnaire"):
    switch_page("main")
footer()