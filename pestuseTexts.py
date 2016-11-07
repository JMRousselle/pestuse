# -*- coding: utf-8 -*-
"""
Ce module contient les textes des écrans
"""
__author__ = "Dimitri DUBOIS"


from collections import namedtuple
from util.utiltools import get_pluriel
import pestuseParams as pms

# pour i18n:
# 1)  décommenter les lignes ci-après,
# 2) entourer les expressions à traduire par _PT()
# 3) dans le projet créer les dossiers locale/fr_FR/LC_MESSAGES
# en remplaçant fr_FR par la langue souhaitée
# 4) créer le fichier pestuse.po: dans invite de commande, taper:
# xgettext fichierTextes.py -p locale/fr_FR/LC_MESSAGES -d pestuse
# 5) avec poedit, éditer le fichier pestuse.po qui a été créé

# import os
# import configuration.configparam as params
# import gettext
# localedir = os.path.join(params.getp("PARTSDIR"), "pestuse", "locale")
# _PT = gettext.translation(
#   "pestuse", localedir, languages=[params.getp("LANG")]).ugettext


TITLE_MSG = namedtuple("TITLE_MSG", "titre message")


# ECRAN DECISION ===============================================================
DECISION_titre = u"Decision"
DECISION_explication = u"Explanation text"
DECISION_labelY = u"Le produit Y"
DECISION_labelZ = u"Le produit Z"
DECISION_erreur = TITLE_MSG(
    u"Warning",
    u"Warning message")
DECISION_confirmation = TITLE_MSG(
    u"Confirmation",
    u"Confirmez-vous vos choix ?")
HISTO_confirmation = TITLE_MSG(
    u"Continuer",
    u"Voulez-vous continuer ?")

# ECRAN RECAPITULATIF ==========================================================
def get_recapitulatif(currentperiod):
    txt = u"Summary text"
    return txt


# TEXTE FINAL PARTIE ===========================================================
def get_texte_final(gain_ecus, gain_euros, tirage_part_pestuse_gain, tirage_periode_pestuse_gain):
    txt = u"C'est la partie {tir_part_pestuse_gain} et la période {tir_periode_pestuse_gain} qui ont été tirées au sort. Vous avez gagné {gain_en_ecu}, soit {gain_en_euro}.".format(
        tir_part_pestuse_gain = tirage_part_pestuse_gain, 
        tir_periode_pestuse_gain = tirage_periode_pestuse_gain, 
        gain_en_ecu=get_pluriel(gain_ecus, u"ecu"),
        gain_en_euro=get_pluriel(gain_euros, u"euro")
    )
    return txt
