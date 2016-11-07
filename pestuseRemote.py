# -*- coding: utf-8 -*-

import logging
import random

from twisted.internet import defer
from twisted.spread import pb

from client.cltgui.cltguidialogs import GuiRecapitulatif
import pestuseParams as pms
from pestuseGui import GuiDecision
from pestuseGui import GuiDecision_QC
from pestuseGui import GuiTirage_de
from pestuseGui import GuiAffichage_result

logger = logging.getLogger("le2m")


class RemotePT(pb.Referenceable):
    """
    Class remote, remote_ methods can be called by the server
    """
    def __init__(self, le2mclt):
        self._le2mclt = le2mclt
        self._currentperiod = 0
        self._histo = []

    def remote_configure(self, params):
        """
        Appelé au démarrage de la partie, permet de configure le remote
        par exemple: traitement, séquence ...
        :param args:
        :return:
        """
        logger.info(u"{} configure".format(self._le2mclt.uid))
        for k, v in params.iteritems():
            setattr(pms, k, v)

    def remote_newperiod(self, periode):
        """
        Appelé au début de chaque période.
        L'historique est "vidé" s'il s'agit de la première période de la partie
        Si c'est un jeu one-shot appeler cette méthode en mettant 0
        :param periode: le numéro de la période courante
        :return:
        """
        logger.info(u"{} Period {}".format(self._le2mclt.uid, periode))
        self._currentperiod = periode
        if self._currentperiod == 1:
            del self._histo[:]

    def remote_display_QC(self, i_QC_NbQuest, type_partie):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} Questionnaire compréhension".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            if type_partie == "BEN":
                self.QC = list(pms.QCBEN)
            elif type_partie == "WEX":
                self.QC = list(pms.QCWEX)
            elif type_partie == "WEA":
                self.QC = list(pms.QCWEA)
            elif type_partie == "WIN":
                self.QC = list(pms.QCWIN)
            elif type_partie == "WEI":
                self.QC = list(pms.QCWEI)
            elif type_partie == "WIE":
                self.QC = list(pms.QCWIE)            
            decision_QC = \
                random.randint(
                    1,
                    len(self.QC[i_QC_NbQuest][1])
                    )
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, decision_QC))
            return decision_QC
        else: 
            defered = defer.Deferred()
            ecran_decision_QC = GuiDecision_QC(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen, i_QC_NbQuest, type_partie)
            ecran_decision_QC.show()
            return defered    

    def remote_display_decision(self, histo_content, type_partie):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} Decision".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            decision = []
            decisionY = \
                random.randrange(
                    pms.MIN_X_POUR_Y,
                    pms.MAX_X_POUR_Y)
            decisionZ = \
                random.randrange(
                    pms.MIN_X_POUR_Z,
                    pms.MAX_X_POUR_Z)
            if type_partie == "BEN" or type_partie == "WEA" or type_partie == "WIN":
                decision_nb_at = 5
            else:
                decision_nb_at =  random.randint(1, 10)
            decision.append(decisionY)
            decision.append(decisionZ)
            decision.append(decision_nb_at)
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, decision))
            return decision
        else: 
            defered = defer.Deferred()
            ecran_decision = GuiDecision(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen, self._currentperiod, histo_content, type_partie)
            ecran_decision.show()
            return defered

    def remote_tirage_de(self, type_partie):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} Tirage du dé".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            tirage_de = \
                random.randint(1, 6)
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, tirage_de))
            return tirage_de
        else: 
            defered = defer.Deferred()
            ecran_tirage_de = GuiTirage_de(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen, self._currentperiod, self._histo, type_partie)
            
            ecran_tirage_de.show()
            return defered 
            
    def remote_affichage_result(self, decision_pour_Y, decision_pour_Z, tirage_du_de, type_partie, nbAteliersY, nbAteliersZ):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} affichage des résultats de la période".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            
            if type_partie == "BEN":
                bonus = pms.BONUS
                montant_fixe = 0
            else:
                bonus = pms.BONUS
                montant_fixe = pms.MONTANT_FIXE
                
            if type_partie == "BEN":
                complement_rendementZ = 0
            elif type_partie == "WEA" or type_partie == "WEX":
                if tirage_du_de == 1:
                    epsylon = -1.
                elif tirage_du_de == 6:
                    epsylon = 1
                else:
                    epsylon = 0
                if decision_pour_Z == 0:
                    complement_rendementZ = 0
                else:
                    complement_rendementZ = float(epsylon * 100 * decision_pour_Z** pms.BETA)
            elif type_partie == "WIN" or type_partie == "WEI" or type_partie == "WIE":
                if tirage_du_de == 1:
                    epsylon = -1.
                elif tirage_du_de == 6:
                    epsylon = 1
                else:
                    epsylon = 0
                if epsylon == -1.:
                    if decision_pour_Z == 0:
                        complement_rendementZ = 0
                    else:
                        complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) - pms.ASSUR + pms.INDEMNITE)
                else:
                    if decision_pour_Z == 0:
                        complement_rendementZ = 0
                    else:
                        complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) - pms.ASSUR)            
            
            self.tirage_du_de = tirage_du_de
            if decision_pour_Y == 0:
                self.le_rendementY = 0
                self.le_profitY = 0
                self.le_gainY = 0
            else:
                self.le_rendementY = round(20.0 * float(decision_pour_Y) ** .3, 2)
                self.le_profitY = bonus + round(10 * self.le_rendementY - decision_pour_Y, 2) + montant_fixe
                self.le_gainY = self.le_profitY * float(nbAteliersY)
            if decision_pour_Z == 0:
                self.le_rendementZ = 0
                self.le_profitZ = 0
                self.le_gainZ = 0
            else:                
                self.le_rendementZ = round((20.0 * float(decision_pour_Z) ** .3 + complement_rendementZ), 2)
                self.le_profitZ = bonus + round(10 * self.le_rendementZ - decision_pour_Z, 2) + montant_fixe
                self.le_gainZ = self.le_profitZ * float(nbAteliersZ)
            
            retour = []
            retour.append(self.le_rendementY)
            retour.append(self.le_rendementZ)
            retour.append(self.le_profitY)
            retour.append(self.le_profitZ)
            retour.append(self.tirage_du_de)
            retour.append(self.le_gainY)
            retour.append(self.le_gainZ)                      
            
            return retour
        else: 
            defered = defer.Deferred()
            ecran_affichage_result = GuiAffichage_result(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen, self._currentperiod, self._histo, decision_pour_Y, decision_pour_Z, tirage_du_de, type_partie, nbAteliersY, nbAteliersZ)
            ecran_affichage_result.show()
            return defered             

    def remote_display_summary(self, texte_recap, historique):
        """
        Display the summary screen
        :param texte_recap:
        :param historique:
        :return: deferred
        """
        logger.info(u"{} Summary".format(self._le2mclt.uid))
        self._histo = historique
        if self._le2mclt.simulation:
            return 1
        else:
            defered = defer.Deferred()
            ecran_recap = GuiRecapitulatif(
                defered, self._le2mclt.automatique, self._le2mclt.screen,
                self._currentperiod, self._histo, texte_recap)
            ecran_recap.show()
            return defered
