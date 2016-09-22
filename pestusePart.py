# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from collections import OrderedDict
from twisted.internet import defer
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, ForeignKey, String

from server.servbase import Base
from server.servparties import Partie
from util.utili18n import le2mtrans
from util.utiltools import get_module_attributes
import pestuseParams as pms
import pestuseTexts as texts


logger = logging.getLogger("le2m")


class PartiePT(Partie):
    __tablename__ = "partie_pestuse"
    __mapper_args__ = {'polymorphic_identity': 'pestuse'}
    partie_id = Column(Integer, ForeignKey('parties.id'), primary_key=True)
    repetitions = relationship('RepetitionsPT')

    def __init__(self, le2mserv, joueur):
        super(PartiePT, self).__init__("pestuse", "PT")
        self._le2mserv = le2mserv
        self.joueur = joueur
        self._texte_recapitulatif = u""
        self._texte_final = u""
        self.PT_gain_ecus = 0
        self.PT_gain_euros = 0
        self._histo_build = OrderedDict()
        self._histo_build[le2mtrans(u"Period")] = "PT_period"
        self._histo_build[le2mtrans(u"DecisionY")] = "PT_decisionY"
        self._histo_build[le2mtrans(u"DecisionZ")] = "PT_decisionZ"
        self._histo_build[le2mtrans(u"NbAteliersY")] = "PT_nbAteliersY"
        self._histo_build[le2mtrans(u"NbAteliersZ")] = "PT_nbAteliersZ"
        self._histo_build[le2mtrans(u"RendementY")] = "PT_rendementY"
        self._histo_build[le2mtrans(u"RendementZ")] = "PT_rendementZ"
        self._histo_build[le2mtrans(u"ProfitY")] = "PT_profitY"
        self._histo_build[le2mtrans(u"ProfitZ")] = "PT_profitZ"
        self._histo_build[le2mtrans(u"Tirage_de")] = "PT_tirage_de"
        self._histo_build[le2mtrans(u"GainY")] = "PT_gainY"
        self._histo_build[le2mtrans(u"GainZ")] = "PT_gainZ"
        self._histo_build[le2mtrans(u"Period\npayoff")] = "PT_periodpayoff"
        self._histo_build[le2mtrans(u"Cumulative\npayoff")] = "PT_cumulativepayoff"
        self._histo_content = [list(self._histo_build.viewkeys())]
#        self.periods = {}
        self._currentperiod = None

    @defer.inlineCallbacks
    def display_QC(self, type_partie):
        """
        Display the comprehension questionnaire screen on the remote
        Get back the decision
        :return:
        """
        if type_partie == "BEN":
            QC = list(pms.QCBEN)
        elif type_partie == "WEX":
            QC = list(pms.QCWEX)
        elif type_partie == "WEA":
            QC = list(pms.QCWEA)
        elif type_partie == "WIN":
            QC = list(pms.QCWIN)
        elif type_partie == "WEI":
            QC = list(pms.QCWEI)
        elif type_partie == "WIE":
            QC = list(pms.QCWIE)
        QC_NbQuest = len(QC)
        reponses_fausse = []
        for i_QC_NbQuest in range(0, QC_NbQuest):        
            logger.debug(u"{} Decision".format(self.joueur))
            debut_QC = datetime.now()
            self.PT_decision_QC = yield(self.remote.callRemote(
                "display_QC", i_QC_NbQuest, type_partie))
            self.PT_decisiontime_QC = (datetime.now() - debut_QC).seconds
            indice_bonne_reponse = QC[i_QC_NbQuest][1].index(QC[i_QC_NbQuest][2][0])
            if self.PT_decision_QC != indice_bonne_reponse:
                reponses_fausse.append(i_QC_NbQuest)
#            self.joueur.info(u"{}".format(self.PT_decision_QC))
            self.joueur.remove_waitmode()
        self.joueur.info(u"Faute(s) {}".format(reponses_fausse))
        
    @property
    def currentperiod(self):
        return self._currentperiod

    @defer.inlineCallbacks
    def configure(self):
        logger.debug(u"{} Configure".format(self.joueur))
        yield (self.remote.callRemote("configure", get_module_attributes(pms)))
        self.joueur.info(u"Ok")

    @defer.inlineCallbacks
    def newperiod(self, period):
        """
        Create a new period and inform the remote
        If this is the first period then empty the historic
        :param periode:
        :return:
        """
        logger.debug(u"{} New Period".format(self.joueur))
        if period == 1:
            del self._histo_content[1:]
        self._currentperiod = RepetitionsPT(period)
        self._le2mserv.gestionnaire_base.ajouter(self.currentperiod)
        self.repetitions.append(self.currentperiod)
        yield (self.remote.callRemote("newperiod", period))
        logger.info(u"{} Ready for period {}".format(self.joueur, period))

    @defer.inlineCallbacks
    def display_decision(self, type_partie):
        """
        Display the decision screen on the remote
        Get back the decision
        :return:
        """
        logger.debug(u"{} Decision".format(self.joueur))
        debut = datetime.now()
        les_decisions = yield(self.remote.callRemote(
            "display_decision",  self._histo_content, type_partie))
        self.currentperiod.PT_decisionY = les_decisions[0]
        self.currentperiod.PT_decisionZ = les_decisions[1]
        self.currentperiod.PT_nbAteliersY = les_decisions[2]
        self.currentperiod.PT_nbAteliersZ = 10 - les_decisions[2]
        self.currentperiod.PT_type_partie = type_partie
        self.currentperiod.PT_decisiontime = (datetime.now() - debut).seconds
        self.joueur.info(u"{} {} {} {}".format(self.currentperiod.PT_nbAteliersY, self.currentperiod.PT_nbAteliersZ, self.currentperiod.PT_decisionY,  self.currentperiod.PT_decisionZ))
        self.joueur.remove_waitmode()

    @defer.inlineCallbacks
    def lance_de(self, type_partie):
        """
        Lancement du de
        :return:
        """
        logger.debug(u"{} tirage du dé".format(self.joueur))
        debut_de = datetime.now()
        self.currentperiod.PT_tirage_de = yield(self.remote.callRemote(
            "tirage_de", type_partie))
        self.currentperiod.PT_decisiontime_de = (datetime.now() - debut_de).seconds
        self.joueur.info(u"{}".format(self.currentperiod.PT_tirage_de))
        self.joueur.remove_waitmode()

    @defer.inlineCallbacks
    def affichage_result(self, type_partie):
        """
        Affichage des resultat de la periode
        :return:
        """
        decision_pour_Y = self.currentperiod.PT_decisionY
        decision_pour_Z = self.currentperiod.PT_decisionZ
        nbAtelierY = self.currentperiod.PT_nbAteliersY
        nbAtelierZ = self.currentperiod.PT_nbAteliersZ
        tirage_du_de = self.currentperiod.PT_tirage_de
        logger.debug(u"{} Affichage des résultats de la période".format(self.joueur))
        debut_ar = datetime.now()
        les_retours = yield(self.remote.callRemote(
            "affichage_result", decision_pour_Y, decision_pour_Z, tirage_du_de, type_partie,  nbAtelierY, nbAtelierZ))
        self.currentperiod.PT_rendementY = les_retours[0]
        self.currentperiod.PT_rendementZ = les_retours[1]
        self.currentperiod.PT_profitY = les_retours[2]
        self.currentperiod.PT_profitZ = les_retours[3]
        self.currentperiod.PT_tirage_de = les_retours[4]
        self.currentperiod.PT_gainY = les_retours[5]
        self.currentperiod.PT_gainZ = les_retours[6]
        # On remplit l historique
        self._histo_content.append(
            [getattr(self.currentperiod, e) for e
             in self._histo_build.viewvalues()])
        self.currentperiod.PT_decisiontime_ar = (datetime.now() - debut_ar).seconds
        self.joueur.info(u"{}".format(self.currentperiod.PT_tirage_ar))
        self.joueur.remove_waitmode()

    def compute_periodpayoff(self):
        """
        Compute the payoff for the period
        :return:
        """
        logger.debug(u"{} Period Payoff".format(self.joueur))
        self.currentperiod.PT_periodpayoff = 0

        # cumulative payoff since the first period
        if self.currentperiod.PT_period < 2:
            self.currentperiod.PT_cumulativepayoff = \
                self.currentperiod.PT_periodpayoff
        else: 
            previousperiod = self.periods[self.currentperiod.PT_period - 1]
            self.currentperiod.PT_cumulativepayoff = \
                previousperiod.PT_cumulativepayoff + \
                self.currentperiod.PT_periodpayoff

        # we store the period in the self.periodes dictionnary
        self.periods[self.currentperiod.PT_period] = self.currentperiod

        logger.debug(u"{} Period Payoff {}".format(
            self.joueur,
            self.currentperiod.PT_periodpayoff))

    @defer.inlineCallbacks
    def display_summary(self, *args):
        """
        Create the summary (txt and historic) and then display it on the
        remote
        :param args:
        :return:
        """
        logger.debug(u"{} Summary".format(self.joueur))
        self._texte_recapitulatif = texts.get_recapitulatif(self.currentperiod)
        self._histo_content.append(
            [getattr(self.currentperiod, e) for e
             in self._histo_build.viewvalues()])
        yield(self.remote.callRemote(
            "display_summary", self._texte_recapitulatif, self._histo_content))
        self.joueur.info("Ok")
        self.joueur.remove_waitmode()
    
    def compute_partpayoff(self):
        """
        Compute the payoff of the part
        :return:
        """
        logger.debug(u"{} Part Payoff".format(self.joueur))
        # gain partie
        self.PT_gain_ecus = self.currentperiod.PT_cumulativepayoff
        self.PT_gain_euros = \
            float(self.PT_gain_ecus) * float(pms.TAUX_CONVERSION)

        # texte final
        self._texte_final = texts.get_texte_final(
            self.PT_gain_ecus,
            self.PT_gain_euros)

        logger.debug(u"{} Final text {}".format(self.joueur, self._texte_final))
        logger.info(u'{} Payoff ecus {} Payoff euros {:.2f}'.format(
            self.joueur, self.PT_gain_ecus, self.PT_gain_euros))


class RepetitionsPT(Base):
    __tablename__ = 'partie_pestuse_repetitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    partie_partie_id = Column(
        Integer,
        ForeignKey("partie_pestuse.partie_id"))

    PT_type_partie = Column(String)
    PT_period = Column(Integer)
    PT_treatment = Column(Integer)
    PT_group = Column(Integer)
    PT_decisionY = Column(Integer)
    PT_decisionZ = Column(Integer)
    PT_nbAteliersY = Column(Integer)
    PT_nbAteliersZ = Column(Integer)
    PT_tirage_de = Column(Integer)
    PT_tirage_ar = Column(Integer)
    PT_rendementY = Column(Float)
    PT_rendementZ = Column(Float)
    PT_profitY = Column(Float)
    PT_profitZ = Column(Float)
    PT_gainY = Column(Float)
    PT_gainZ = Column(Float)
    PT_decision_QC = Column(Integer)
    PT_decisiontime = Column(Integer)
    PT_decisiontime_de = Column(Integer)
    PT_decisiontime_ar = Column(Integer)
    PT_periodpayoff = Column(Float)
    PT_cumulativepayoff = Column(Float)

    def __init__(self, period):
        self.PT_treatment = pms.TREATMENT
        self.PT_period = period
        self.PT_decisiontime = 0
        self.PT_periodpayoff = 0
        self.PT_cumulativepayoff = 0

    def todict(self, joueur):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        temp["joueur"] = joueur
        return temp

