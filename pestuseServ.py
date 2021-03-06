# -*- coding: utf-8 -*-

import logging
from collections import OrderedDict
from twisted.internet import defer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util import utiltools
import pestuseParams as pms

import random

from PyQt4 import QtGui

logger = logging.getLogger("le2m.{}".format(__name__))


class Serveur(object):
    def __init__(self, le2mserv):
        self._le2mserv = le2mserv

        # creation of the menu (will be placed in the "part" menu on the
        # server screen)
        actions = OrderedDict()
        actions[u"Configurer"] = self._configure
        actions[u"Afficher les paramètres"] = \
            lambda _: self._le2mserv.gestionnaire_graphique. \
                display_information2(
                utiltools.get_module_info(pms), u"Paramètres")
        actions[u"Démarrer"] = lambda _: self._demarrer()
        actions[u"Afficher les gains"] = \
            lambda _: self._le2mserv.gestionnaire_experience. \
                display_payoffs_onserver("pestuse")
        self._le2mserv.gestionnaire_graphique.add_topartmenu(
            u"Pesticide use", actions)
        # Variable numerotant les partie pestuse qui servira au tirage au sort du gains
        self.indice_part_pestuse = 0
        # On tire au sort qu elle partie pestuse servira au gain et quelle periode
        self.tirage_part_pestuse_gain = random.randint(1, 4)
        self.tirage_periode_pestuse_gain = random.randint(1, pms.NOMBRE_PERIODES)
        self._le2mserv.gestionnaire_graphique.infoserv([None, u"Pestuse : tirage au sort de la période {} pour la partie {}".format(self.tirage_periode_pestuse_gain, self.tirage_part_pestuse_gain)])

    def _configure(self):
        """
        To make changes in the parameters
        :return:
        """
        pass

    @defer.inlineCallbacks
    def _demarrer(self):
        """
        Start the part
        :return:
        """
        type_partie =""
        # Ici on demande quel type de jeu du dictateur sera lancé (Given ou Taken)
        choix, ok = QtGui.QInputDialog.getItem(
            None, "choix", u"Quel type de partie doit ^etre lancé ?",
            ["Benchmark", "Wealth", "Wealth Ext", "Wealth Ins", "Wealth Ext Ins", "Wealth Ins Ext"], current=0,
            editable=False
        )
        if ok:
            if choix == "Benchmark":
                type_partie = "BEN"
            elif choix == "Wealth":
                type_partie = "WEA"
            elif choix == "Wealth Ext":
                type_partie = "WEX"
            elif choix == "Wealth Ins":
                type_partie = "WIN"
            elif choix == "Wealth Ext Ins":
                type_partie = "WEI"
            else:
                type_partie = "WIE"
        """
        Start the part
        :return:
        """
        if type_partie == "BEN":
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Benchmark ?")
        elif type_partie == "WEA":
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Wealth ?")
        elif type_partie == "WEX":
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Wealth Ext ?")
        elif type_partie == "WIN":
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Wealth Ins ?")
        elif type_partie == "WEI":
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Wealth Ext Ins ?")
        else:
            confirmation = self._le2mserv.gestionnaire_graphique. \
                question(u"Démarrer pestuse Wealth Ins Ext ?")
        if not confirmation:
            return

        # init part
        if type_partie == "BEN":
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Benchmark"])
        elif type_partie == "WEA":
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Wealth"])
        elif type_partie == "WEX":
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Wealth Ext"])
        elif type_partie == "WIN":
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Wealth Ins"])
        elif type_partie == "WEI":
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Wealth Ext Ins"])
        else:
            self._le2mserv.gestionnaire_graphique.infoserv([None, u"Démarrage pestuse Wealth Ins Ext"])
                
        yield (self._le2mserv.gestionnaire_experience.init_part(
            "pestuse", "PartiePT",
            "RemotePT", pms))
        self._tous = self._le2mserv.gestionnaire_joueurs.get_players(
            'pestuse')
        logger.info("Tous : {}".format(self._tous))

        # configure part (player and remote)
        yield (self._le2mserv.gestionnaire_experience.run_step(
            u"Configure", self._tous, "configure"))

        # form groups
        if pms.TAILLE_GROUPES > 0:
            try:
                self._le2mserv.gestionnaire_groupes.former_groupes(
                    self._le2mserv.gestionnaire_joueurs.get_players(),
                    pms.TAILLE_GROUPES, forcer_nouveaux=True)
            except ValueError as e:
                self._le2mserv.gestionnaire_graphique.display_error(
                    e.message)
                return

        # Lancement questionnaire de comprehension en fonction du nombre de questions
        yield (self._le2mserv.gestionnaire_experience.run_step(
            u"Questionnaire de compréhension", self._tous, "display_QC", type_partie))

        # ecran d attente de fin de reponses au questionnaire de comprehension
        self._le2mserv.gestionnaire_graphique.display_information(u"Cliquer si il n'y a pas ou plus de question")

        # Start repetitions ----------------------------------------------------
        self.indice_part_pestuse += 1
        for period in xrange(1 if pms.NOMBRE_PERIODES else 0,
                             pms.NOMBRE_PERIODES + 1):

            if self._le2mserv.gestionnaire_experience.stop_repetitions:
                break

            # init period
            self._le2mserv.gestionnaire_graphique.infoserv(
                [None, u"Période {}".format(period)])
            self._le2mserv.gestionnaire_graphique.infoclt(
                [None, u"Période {}".format(period)], fg="white", bg="gray")
            yield (self._le2mserv.gestionnaire_experience.run_func(
                self._tous, "newperiod", period))

            # decision
            yield (self._le2mserv.gestionnaire_experience.run_step(
                u"Décision", self._tous, "display_decision", type_partie))

            # Lancement du de
            yield (self._le2mserv.gestionnaire_experience.run_step(
                u"Tirage du dé", self._tous, "lance_de", type_partie))

            # Affichage resultats
            self.le_payoff = yield (self._le2mserv.gestionnaire_experience.run_step(
                u"Affichage des résultats", self._tous, "affichage_result", type_partie, self.indice_part_pestuse,
                self.tirage_part_pestuse_gain, self.tirage_periode_pestuse_gain))

            # period payoffs
            self._le2mserv.gestionnaire_experience.compute_periodpayoffs(
                "pestuse")

            # summary
            # yield(self._le2mserv.gestionnaire_experience.run_step(
        #                u"Récapitulatif", self._tous, "display_summary"))

        # End of part ----------------------------------------------------------
        if (self.indice_part_pestuse == self.tirage_part_pestuse_gain):
            self._le2mserv.gestionnaire_experience.finalize_part(
                "pestuse", self.tirage_part_pestuse_gain, self.tirage_periode_pestuse_gain)
