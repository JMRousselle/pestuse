# -*- coding: utf-8 -*-
"""
Ce module contient les boites de dialogue du programme.
"""

import logging
import random

from PyQt4 import QtGui, QtCore

from client.cltgui.cltguidialogs import GuiHistorique
from util.utili18n import le2mtrans
from client import clttexts as textes_main
import pestuseParams as pms
import pestuseTexts as texts
from pestuseGuiSrc import pestuseDecision
from pestuseGuiSrc import questcomp
from pestuseGuiSrc import affichageResultats

# Pour le tirage du de (de util.servguidialogs.py)
from util.dice import dice

# Import da matplotlib pour les graphiques
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 
import numpy as plab 

logger = logging.getLogger("le2m")

class GuiDecision_QC(QtGui.QDialog):
    def __init__(self, defered, automatique, parent, num_question, type_partie):
        super(GuiDecision_QC, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
        self.num_question = num_question
#        self._historique = GuiHistorique(self, historique)

        # gui
        self.ui = questcomp.Ui_Dialog()
        self.ui.setupUi(self)
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
        
        # Decision
        # On affiche la question ici
        self.ui.textEdit_ennonce.setText(self.QC[num_question][0])        

        # la zone des propositions
        espace_gauche = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, 
        QtGui.QSizePolicy.Minimum)
        self.ui.hl_propositions.addItem(espace_gauche)
        
        self._cases_decisions = [] 
        
        # boutons radio
        for p in range(0, len(self.QC[num_question][1])):
            boutonRadio = QtGui.QRadioButton(self)
            boutonRadio.setText(self.QC[num_question][1][p])
            self._cases_decisions.append(boutonRadio)
            self.ui.hl_propositions.addWidget(boutonRadio)
        # checkbox
#        for p in self._question.propositions:
#            checkbox = QtGui.QCheckBox(self)
#            checkbox.setText(p)
#            self._cases_decisions.append(checkbox)
#            self.ui.hl_propositions.addWidget(checkbox)

        espace_droite = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, 
        QtGui.QSizePolicy.Minimum)
        self.ui.hl_propositions.addItem(espace_droite)

        # automatic
        if self._automatique:
            # On tire au hasard une option pour la question
            le_choix_auto = random.randint(1, len(self.QC[num_question][1]))
            for b in self._cases_decisions:
                b.setChecked(True)             
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(self._accept)
            self._timer_automatique.start(7000)

        # Bouton de validation
        self.ui.pushButton_valider.clicked.connect(self._accept)
        
    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
#        if not self._automatique:
#            confirmation = QtGui.QMessageBox.question(
#                self, texts.DECISION_confirmation.titre,
#                texts.DECISION_confirmation.message,
#                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes
#            )
#            if confirmation != QtGui.QMessageBox.Yes: 
#                return
#        self._defered.callback(decision)
#        self.accept()
        
        faute = 0
        textes_items_selectionnes = []
        self.bonnes_reponses = self.QC[self.num_question][2]
        self.explication = self.QC[self.num_question][3]
        for b in self._cases_decisions:
            if b.isChecked(): 
                textes_items_selectionnes.append(b.text())
        
        if not textes_items_selectionnes:
            QtGui.QMessageBox.warning(self, u'Absence de réponse', 
            u'Vous n\'avez pas répondu à la question')
            return
        else:
            for br in self.bonnes_reponses:
                if br not in textes_items_selectionnes: 
                    faute = 1
        if len(self.bonnes_reponses) > 1: 
            texte = u'Les bonnes réponses étaient: \n- {}\n'.\
            format('\n- '.join(map(str, self.bonnes_reponses)))
        else: 
            texte = u'La bonne réponse était: {}\n'.\
            format(self.bonnes_reponses[0])

        texte += self.explication
        
        if not self._automatique:
            QtGui.QMessageBox.information(self, 'Explication', texte)
        
        self._defered.callback(faute)
        self.accept()

class GuiDecision(QtGui.QDialog):
    def __init__(self, defered, automatique, parent, periode, historique, type_partie):
        super(GuiDecision, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
#        self._historique = GuiHistorique(self, historique)
        self_historique = historique
        self.type_partie = type_partie

        # gui
        self.ui = pestuseDecision.Ui_Dialog()
        self.ui.setupUi(self)

        # period and history
        if periode:
            self.ui.label_periode.setText(textes_main.PERIODE_label(periode))
            self.ui.pushButton_historique.setText(
                le2mtrans(u"History"))
#            self.ui.pushButton_historique.clicked.connect(
#                self._historique.show)
        else:
            self.ui.label_periode.setVisible(False)
            self.ui.pushButton_historique.setVisible(False)

        # On cache le bouton historique
        self.ui.pushButton_historique.setVisible(False)
        
        #On retaille la hauteur des ligne des tableaux historiques
        for x in range(10):
            self.ui.tableWidget_histo_produitY.setRowHeight(x, 19)
            self.ui.tableWidget_histo_produitZ.setRowHeight(x, 19)
        #On peut retailler la largeur des colonnes des tableaux historique
        self.ui.tableWidget_histo_produitY.setColumnWidth(0, 40)
        self.ui.tableWidget_histo_produitZ.setColumnWidth(0, 40)
        self.ui.tableWidget_histo_produitZ.setColumnWidth(2, 25)
        
        #On trace les graphes initiaux
        self.ini_graph_rendement_Y(0)
        self.ini_graph_profit_Y(0)
        self.ini_graph_rendement_Z(0)
        self.ini_graph_profit_Z(0)

        # Explanation
#        self.ui.textEdit_explication.setText(texts.DECISION_explication)
#        self.ui.textEdit_explication.setReadOnly(True)
#        self.ui.textEdit_explication.setFixedSize(400, 80)

        if type_partie == "BEN" or type_partie == "WEA" or type_partie == "WIN":
            # Au niveau Benchmark pas besoin de demander combien d ateliers Y
            self.ui.label_nbAteliersY.setVisible(False)
            self.ui.spinBox_nbAteliersY.setVisible(False)
            # Il y a 5 ateliers pour Y et 5 pour Z
            nbAteliersY = 5
            self.nbAteliersY = nbAteliersY
            # On tire au hasard si on affiche les ateliers Y en premier ou pas
            afficheAtelierYPremier = random.randint(0, 1)
            if afficheAtelierYPremier == 0:
                for iy in range(0, nbAteliersY):
                    textY = QtGui.QTableWidgetItem('%s' %(str("Y")))
                    self.ui.tableWidget_ateliersYZ.setItem(iy,  0,  textY)                
                    self.ui.tableWidget_ateliersYZ.item(iy, 0).setBackgroundColor(QtGui.QColor(154, 255, 154))
                    self.ui.tableWidget_ateliersYZ.item(iy, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                for iz in range(nbAteliersY, 10):
                    textZ = QtGui.QTableWidgetItem('%s' %(str("Z")))
                    self.ui.tableWidget_ateliersYZ.setItem(iz,  0,  textZ)                
                    self.ui.tableWidget_ateliersYZ.item(iz, 0).setBackgroundColor(QtGui.QColor(139, 255, 255))
                    self.ui.tableWidget_ateliersYZ.item(iz, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            else:
                for iz in range(0, 10 - nbAteliersY):
                    textZ = QtGui.QTableWidgetItem('%s' %(str("Z")))
                    self.ui.tableWidget_ateliersYZ.setItem(iz,  0,  textZ)                
                    self.ui.tableWidget_ateliersYZ.item(iz, 0).setBackgroundColor(QtGui.QColor(139, 255, 255))
                    self.ui.tableWidget_ateliersYZ.item(iz, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                for iy in range(10 - nbAteliersY, 10):
                    textY = QtGui.QTableWidgetItem('%s' %(str("Y")))
                    self.ui.tableWidget_ateliersYZ.setItem(iy,  0,  textY)                    
                    self.ui.tableWidget_ateliersYZ.item(iy, 0).setBackgroundColor(QtGui.QColor(154, 255, 154))
                    self.ui.tableWidget_ateliersYZ.item(iy, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        else:
            # Au niveau extensive on demande combien d ateliers Y
            self.ui.label_nbAteliersY.setVisible(True)
            self.ui.spinBox_nbAteliersY.setVisible(True)
            # On gere l affichage des ateliers Y et Z en fonction du choix du sujet
            # On positionne un SIGNAL en cas de changement de valeur du nombre d atelier Y
            self.connect(self.ui.spinBox_nbAteliersY, QtCore.SIGNAL('valueChanged(int)'), self._colore_atelier)
            # Au premier affichage on positionne le nombre des ateliers a 5 chacun
            for iy in range(0, 5):
                textY = QtGui.QTableWidgetItem('%s' %(str("Y")))
                self.ui.tableWidget_ateliersYZ.setItem(iy,  0,  textY)                
                self.ui.tableWidget_ateliersYZ.item(iy, 0).setBackgroundColor(QtGui.QColor(154, 255, 154))
            for iz in range(5, 10):
                textZ = QtGui.QTableWidgetItem('%s' %(str("Z")))
                self.ui.tableWidget_ateliersYZ.setItem(iz,  0,  textZ)                
                self.ui.tableWidget_ateliersYZ.item(iz, 0).setBackgroundColor(QtGui.QColor(139, 255, 255))
            self.ui.spinBox_nbAteliersY.setValue(5)
                
        # On remplit le tableau historique
        if periode > 1:
            for iper in range(1, periode):
                # Qte de X pour produit Y
                tab_histo_decisionY = QtGui.QTableWidgetItem('%s' %(str(historique[iper][1])))
                self.ui.tableWidget_histo_produitY.setItem(iper - 1,  0,  tab_histo_decisionY)
                # Qte de X pour produit Z
                tab_histo_decisionZ = QtGui.QTableWidgetItem('%s' %(str(historique[iper][2])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  0,  tab_histo_decisionZ)
                # Nb ateliers Y
                tab_histo_nbAteliersY = QtGui.QTableWidgetItem('%s' %(str(historique[iper][3])))
                self.ui.tableWidget_histo_produitY.setItem(iper - 1,  1,  tab_histo_nbAteliersY)
                # Nb ateliers Z
                tab_histo_nbAteliersZ = QtGui.QTableWidgetItem('%s' %(str(historique[iper][4])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  1,  tab_histo_nbAteliersZ)
                # Rendement Y
                tab_histo_rendementY = QtGui.QTableWidgetItem('%s' %(str(historique[iper][5])))
                self.ui.tableWidget_histo_produitY.setItem(iper - 1,  2,  tab_histo_rendementY)
                # Tirage du de pour Z
                tab_histo_tirage_de = QtGui.QTableWidgetItem('%s' %(str(historique[iper][9])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  2,  tab_histo_tirage_de)                  
                # Rendement Z
                tab_histo_rendementZ = QtGui.QTableWidgetItem('%s' %(str(historique[iper][6])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  3,  tab_histo_rendementZ)
                # Profit Y
                tab_histo_profitY = QtGui.QTableWidgetItem('%s' %(str(historique[iper][7])))
                self.ui.tableWidget_histo_produitY.setItem(iper - 1,  3,  tab_histo_profitY)
                # Profit Z
                tab_histo_profitZ = QtGui.QTableWidgetItem('%s' %(str(historique[iper][8])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  4,  tab_histo_profitZ)
                # Gain Y
                tab_histo_gainY = QtGui.QTableWidgetItem('%s' %(str(historique[iper][10])))
                self.ui.tableWidget_histo_produitY.setItem(iper - 1,  4,  tab_histo_gainY)
                # Gain Z
                tab_histo_gainZ = QtGui.QTableWidgetItem('%s' %(str(historique[iper][11])))
                self.ui.tableWidget_histo_produitZ.setItem(iper - 1,  5,  tab_histo_gainZ)                

        # On positionne les connecteurs/signaux
        self.connect(self.ui.horizontalScrollBar_produitY, QtCore.SIGNAL("valueChanged(int)"), self.calcul_rendement_Y)
        self.connect(self.ui.horizontalScrollBar_produitZ, QtCore.SIGNAL("valueChanged(int)"), self.calcul_rendement_Z)
        
        # Decision
        # On rend desabled le tableau des ateliers YZ pour eviter la saisie a l interieur de ses case
        self.ui.tableWidget_ateliersYZ.setEnabled(False)
        # On calibre les curseurs de choix de X pour les produit Y et Z
        self.ui.horizontalScrollBar_produitY.setMinimum(pms.MIN_X_POUR_Y)
        self.ui.horizontalScrollBar_produitY.setMaximum(pms.MAX_X_POUR_Y)
        self.ui.horizontalScrollBar_produitZ.setMinimum(pms.MIN_X_POUR_Z)
        self.ui.horizontalScrollBar_produitZ.setMaximum(pms.MAX_X_POUR_Z)        

        # bouton box
        self.ui.buttonBox.accepted.connect(self._accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setVisible(
            False)

        # title and size
        self.setWindowTitle(texts.DECISION_titre)
#        self.setFixedSize(1032, 768)

        # automatic
        if self._automatique:
            # On tire au sort le nombre d atelier Y
            nbAteliersY = random.randint(1, 10)
            self.nbAteliersY = nbAteliersY
            self.ui.spinBox_nbAteliersY.setValue(nbAteliersY)
            # On tire au hasard une valeur de X pour chacun des produits Y et Z
            self.ui.horizontalScrollBar_produitY.setValue(random.randrange(pms.MIN_X_POUR_Y, pms.MAX_X_POUR_Y))
            self.ui.horizontalScrollBar_produitZ.setValue(random.randrange(pms.MIN_X_POUR_Z, pms.MAX_X_POUR_Z))
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(self._accept)
            self._timer_automatique.start(7000)
                
    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        decision = []
        decision.append(self.ui.horizontalScrollBar_produitY.value())
        decision.append(self.ui.horizontalScrollBar_produitZ.value())
        if self.type_partie == "BEN" or self.type_partie == "WEA" or self.type_partie == "WIN":
            nbAteliersY = 5
        else:
            nbAteliersY = self.ui.spinBox_nbAteliersY.value()
        decision.append(nbAteliersY) 
        if not self._automatique:
            confirmation = QtGui.QMessageBox.question(
                self, texts.DECISION_confirmation.titre,
                texts.DECISION_confirmation.message,
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes
            )
            if confirmation != QtGui.QMessageBox.Yes: 
                return
        self._defered.callback(decision)
        self.accept()
        
    def calcul_profit_Y(self, le_rendement_Y,  le_nbX_pour_Y):
        #ICI on calcul le profit du produit Y et on l affiche dans la variable label_profit_Y
        profitY = 10 * le_rendement_Y - le_nbX_pour_Y
        self.ui.label_profit_Y.setNum(round(profitY, 2))
        # On retrace le graphique avec le nouveau point
        self.maj_graph_profit_Y(le_nbX_pour_Y)
        return

    def ini_graph_rendement_Y(self, x_du_point):    # NOUVELLE APPROCHE TEST
        
        width = 4
        height = 3
        dpi = 70        
        
        # On trace la courbe de la fonction rendement de Y
        self.fig_rdt_Y = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes_rdt_Y = self.fig_rdt_Y.add_subplot(111)
        self.canvasRY = FigureCanvas(self.fig_rdt_Y)        
 
        self.ui.verticalLayout_graph_rendement_Y.addWidget(self.canvasRY)  # the matplotlib canvas        

        self.x = plab.linspace(pms.MIN_X_POUR_Y, pms.MAX_X_POUR_Y, 50)
        self.y = 20.0 * self.x ** .3
        self.line, = self.axes_rdt_Y.plot(self.x, self.y)
        
        # Ajout d'un point sur la ligne
        y_du_point = 20.0 * x_du_point ** .3
        self.point = self.axes_rdt_Y.scatter([x_du_point, ], [y_du_point, ], 50, color='black')
        
        self.canvasRY.draw()
        
    def maj_graph_rendement_Y(self, x_du_point):    # NOUVELLE APPROCHE TEST
        
        self.axes_rdt_Y.cla()
        self.axes_rdt_Y = self.fig_rdt_Y.add_subplot(111)

        self.x = plab.linspace(pms.MIN_X_POUR_Y, pms.MAX_X_POUR_Y, 50)
        self.y = 20.0 * self.x ** .3
        self.line, = self.axes_rdt_Y.plot(self.x, self.y)
        
        # Ajout d'un point sur la ligne
        y_du_point = 20.0 * x_du_point ** .3
        self.point = self.axes_rdt_Y.scatter([x_du_point, ], [y_du_point, ], 50, color='black')
        
        self.canvasRY.draw()        

    def ini_graph_profit_Y(self, x_du_point):
        # On trace la courbe de la fonction rendement de Y
        width = 4
        height = 3
        dpi = 70
        self.fig_pro_Y = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes_pro_Y = self.fig_pro_Y.add_subplot(111)
        self.canvasPY = FigureCanvas(self.fig_pro_Y)
        
        self.ui.verticalLayout_graph_profit_Y.addWidget(self.canvasPY)  # the matplotlib canvas
 
        self.x = plab.linspace(pms.MIN_X_POUR_Y, pms.MAX_X_POUR_Y, 50)
        rend_Y = 20.0 * self.x ** .3
        self.y = 10 * rend_Y - self.x
        self.line, = self.axes_pro_Y.plot(self.x, self.y)
        # On fixe les axes
        xmin = pms.MIN_X_POUR_Y
        xmax = pms.MAX_X_POUR_Y
        ymin = min(self.y)
        ymax = max(self.y) * 1.1
        plt.xlim(xmin,  xmax)
        plt.ylim(ymin,  ymax)

        # Ajout d'un point sur la ligne
        rend_y_du_point = 20.0 * x_du_point ** .3
        y_du_point = 10 * rend_y_du_point - x_du_point
        self.point = self.axes_pro_Y.scatter([x_du_point, ], [y_du_point, ], 30, color='black')        

        self.canvasPY.draw()
  
    def maj_graph_profit_Y(self, x_du_point):
        self.axes_pro_Y.cla()
        self.axes_pro_Y = self.fig_pro_Y.add_subplot(111)
 
        self.x = plab.linspace(pms.MIN_X_POUR_Y, pms.MAX_X_POUR_Y, 50)
        rend_Y = 20.0 * self.x ** .3
        self.y = 10 * rend_Y - self.x
        self.line, = self.axes_pro_Y.plot(self.x, self.y)
        # On fixe les axes
        xmin = pms.MIN_X_POUR_Y
        xmax = pms.MAX_X_POUR_Y
        ymin = min(self.y)
        ymax = max(self.y) * 1.1
        plt.xlim(xmin,  xmax)
        plt.ylim(ymin,  ymax)
        
        # Commande hold qui devrait permettre de garder les memes axes (marche pas)
        plt.hold(True)        

        # Ajout d'un point sur la ligne
        rend_y_du_point = 20.0 * x_du_point ** .3
        y_du_point = 10 * rend_y_du_point - x_du_point

        self.point = self.axes_pro_Y.scatter([x_du_point, ], [y_du_point, ], 50, color='black')

        self.canvasPY.draw()    

    def calcul_rendement_Y(self, nbX_pour_Y):
        #ICI on calcul le rendement du produit Y et on l affiche dans la variable label_rendement_Y
        rendementY = 20.0 * nbX_pour_Y ** .3
        self.ui.label_rendement_Y.setNum(round(rendementY, 2))
#        self.graph_rendement_Y(rendementY, nbX_pour_Y)
        self.calcul_profit_Y(rendementY,  nbX_pour_Y)
        # On retrace le graphique avec le nouveau point
        self.maj_graph_rendement_Y(nbX_pour_Y)
        return
        
    def calcul_profit_Z(self, le_rendement_Z_max,  le_rendement_Z_moy,  le_rendement_Z_min,  le_nbX_pour_Z):
        #ICI on calcul le profit du produit Z et on l affiche dans les variables adequates
        profitZ_max = 10 * le_rendement_Z_max - le_nbX_pour_Z
        profitZ_moy = 10 * le_rendement_Z_moy - le_nbX_pour_Z
        profitZ_min = 10 * le_rendement_Z_min - le_nbX_pour_Z
        self.ui.label_profit_Z_max.setNum(round(profitZ_max, 2))
        self.ui.label_profit_Z_moy.setNum(round(profitZ_moy, 2))
        self.ui.label_profit_Z_min.setNum(round(profitZ_min, 2))
        # On retrace le graphique avec le nouveau point
        self.maj_graph_profit_Z(le_nbX_pour_Z)        
        return

    def ini_graph_rendement_Z(self, x_du_point):    # NOUVELLE APPROCHE TEST
        
        width = 4
        height = 3
        dpi = 70        
        
        # On trace la courbe de la fonction rendement de Y
        self.fig_rdt_Z = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes_rdt_Z = self.fig_rdt_Z.add_subplot(111)
        self.canvasRZ = FigureCanvas(self.fig_rdt_Z)        
 
        self.ui.verticalLayout_graph_rendement_Z.addWidget(self.canvasRZ)  # the matplotlib canvas        

        self.x = plab.linspace(pms.MIN_X_POUR_Z, pms.MAX_X_POUR_Z, 600)
        self.y_max = (20.0 * self.x ** .3)  + (1 * 100 * self.x ** pms.BETA)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_max)
        self.y_moy = (20.0 * self.x ** .3)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_moy)
        self.y_min = (20.0 * self.x ** .3)  - (1 * 100 * self.x ** pms.BETA)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_min)

        # Ajout d'un point sur la ligne
        if x_du_point != 0:
            y_du_point_max = (20.0 * x_du_point ** .3)  + (1 * 100 * x_du_point ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_max, ], 50, color='black')
            y_du_point_moy = 20.0 * x_du_point ** .3
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_moy, ], 50, color='black')
            y_du_point_min = (20.0 * x_du_point ** .3)  - (1 * 100 * x_du_point ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_min, ], 50, color='black')
        else:
            y_du_point_max = (20.0 * 0.1 ** .3)  + (1 * 100 * 0.1 ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_max, ], 50, color='black')
            y_du_point_moy = 20.0 * 0.1 ** .3
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_moy, ], 50, color='black')
            y_du_point_min = (20.0 * 0.1 ** .3)  - (1 * 100 * 0.1 ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_min, ], 50, color='black')
            
        self.canvasRZ.draw()
        
    def maj_graph_rendement_Z(self, x_du_point):    # NOUVELLE APPROCHE TEST
        
        self.axes_rdt_Z.cla()
        self.axes_rdt_Z = self.fig_rdt_Z.add_subplot(111)

        self.x = plab.linspace(pms.MIN_X_POUR_Z, pms.MAX_X_POUR_Z, 600)
        self.y_max = (20.0 * self.x ** .3)  + (1 * 100 * self.x ** pms.BETA)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_max)
        self.y_moy = (20.0 * self.x ** .3)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_moy)
        self.y_min = (20.0 * self.x ** .3)  - (1 * 100 * self.x ** pms.BETA)
        self.line, = self.axes_rdt_Z.plot(self.x, self.y_min)
        
        # Ajout d'un point sur la ligne
        if x_du_point != 0:
            y_du_point_max = (20.0 * x_du_point ** .3)  + (1 * 100 * x_du_point ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_max, ], 50, color='black')
            y_du_point_moy = 20.0 * x_du_point ** .3
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_moy, ], 50, color='black')
            y_du_point_min = (20.0 * x_du_point ** .3)  - (1 * 100 * x_du_point ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([x_du_point, ], [y_du_point_min, ], 50, color='black')
        else:
            y_du_point_max = (20.0 * 0.1 ** .3)  + (1 * 100 * 0.1 ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_max, ], 50, color='black')
            y_du_point_moy = 20.0 * 0.1 ** .3
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_moy, ], 50, color='black')
            y_du_point_min = (20.0 * 0.1 ** .3)  - (1 * 100 * 0.1 ** pms.BETA)
            self.point = self.axes_rdt_Z.scatter([0.1, ], [y_du_point_min, ], 50, color='black')

        self.canvasRZ.draw()        

    def ini_graph_profit_Z(self, x_du_point):
        # On trace la courbe de la fonction rendement de Y
        width = 4
        height = 3
        dpi = 70
        self.fig_pro_Z = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes_pro_Z = self.fig_pro_Z.add_subplot(111)
        self.canvasPZ = FigureCanvas(self.fig_pro_Z)
        
        self.ui.verticalLayout_graph_profit_Z.addWidget(self.canvasPZ)  # the matplotlib canvas
 
        self.x = plab.linspace(pms.MIN_X_POUR_Z, pms.MAX_X_POUR_Z, 600)
        rend_Z_max = (20.0 * self.x ** .3) + (1 * 100 * self.x ** pms.BETA)
        self.z_max = 10 * rend_Z_max - self.x +100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_max)
        rend_Z_moy = (20.0 * self.x ** .3)
        self.z_moy = 10 * rend_Z_moy - self.x + 100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_moy)
        rend_Z_min = (20.0 * self.x ** .3) - (1 * 100 * self.x ** pms.BETA)
        self.z_min = 10 * rend_Z_min - self.x +100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_min)
        
        if x_du_point != 0:
            rend_z_du_point_max = (20.0 * x_du_point ** .3) + (1 * 100 * x_du_point ** pms.BETA)
            z_du_point_max = 10 * rend_z_du_point_max - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_max, ], 50, color='black')
            rend_z_du_point_moy = (20.0 * x_du_point ** .3)
            z_du_point_moy = 10 * rend_z_du_point_moy - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_moy, ], 50, color='black')
            rend_z_du_point_min = (20.0 * x_du_point ** .3) - (1 * 100 * x_du_point ** pms.BETA)
            z_du_point_min = 10 * rend_z_du_point_min - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_min, ], 50, color='black')
        else:
            rend_z_du_point_max = (20.0 * 0.1 ** .3) + (1 * 100 * 0.1 ** pms.BETA)
            z_du_point_max = 10 * rend_z_du_point_max - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_max, ], 50, color='black')
            rend_z_du_point_moy = (20.0 * 0.1 ** .3)
            z_du_point_moy = 10 * rend_z_du_point_moy - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_moy, ], 50, color='black')
            rend_z_du_point_min = (20.0 * 0.1 ** .3) - (1 * 100 * 0.1 ** pms.BETA)
            z_du_point_min = 10 * rend_z_du_point_min - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_min, ], 50, color='black')

        self.canvasPZ.draw()
  
    def maj_graph_profit_Z(self, x_du_point):
        self.axes_pro_Z.cla()
        self.axes_pro_Z = self.fig_pro_Z.add_subplot(111)
 
        self.x = plab.linspace(pms.MIN_X_POUR_Z, pms.MAX_X_POUR_Z, 600)
        rend_Z_max = (20.0 * self.x ** .3) + (1 * 100 * self.x ** pms.BETA)
        self.z_max = 10 * rend_Z_max - self.x +100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_max)
        rend_Z_moy = (20.0 * self.x ** .3)
        self.z_moy = 10 * rend_Z_moy - self.x + 100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_moy)
        rend_Z_min = (20.0 * self.x ** .3) - (1 * 100 * self.x ** pms.BETA)
        self.z_min = 10 * rend_Z_min - self.x +100
        self.line, = self.axes_pro_Z.plot(self.x, self.z_min)
        
        # Ajout d'un point sur la ligne
        if x_du_point != 0:
            rend_z_du_point_max = (20.0 * x_du_point ** .3) + (1 * 100 * x_du_point ** pms.BETA)
            z_du_point_max = 10 * rend_z_du_point_max - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_max, ], 50, color='black')
            rend_z_du_point_moy = (20.0 * x_du_point ** .3)
            z_du_point_moy = 10 * rend_z_du_point_moy - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_moy, ], 50, color='black')
            rend_z_du_point_min = (20.0 * x_du_point ** .3) - (1 * 100 * x_du_point ** pms.BETA)
            z_du_point_min = 10 * rend_z_du_point_min - x_du_point + 100
            self.point = self.axes_pro_Z.scatter([x_du_point, ], [z_du_point_min, ], 50, color='black')
        else:
            rend_z_du_point_max = (20.0 * 0.1 ** .3) + (1 * 100 * 0.1 ** pms.BETA)
            z_du_point_max = 10 * rend_z_du_point_max - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_max, ], 50, color='black')
            rend_z_du_point_moy = (20.0 * 0.1 ** .3)
            z_du_point_moy = 10 * rend_z_du_point_moy - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_moy, ], 50, color='black')
            rend_z_du_point_min = (20.0 * 0.1 ** .3) - (1 * 100 * 0.1 ** pms.BETA)
            z_du_point_min = 10 * rend_z_du_point_min - 0.1 + 100
            self.point = self.axes_pro_Z.scatter([0.1, ], [z_du_point_min, ], 50, color='black')

        self.canvasPZ.draw()    

    def calcul_rendement_Z(self, nbX_pour_Z):
        #ICI on calcul le rendement du produit Y et on l affiche dans les variables adequates
        if nbX_pour_Z != 0:
            rendementZ_max = (20.0 * nbX_pour_Z ** .3) + (1 * 100 * nbX_pour_Z ** pms.BETA)
            rendementZ_moy = (20.0 * nbX_pour_Z ** .3)
            rendementZ_min = (20.0 * nbX_pour_Z ** .3) - (1 * 100 * nbX_pour_Z ** pms.BETA)
        else:
            rendementZ_max = (20.0 * 0.1 ** .3) + (1 * 100 * 0.1 ** pms.BETA)
            rendementZ_moy = (20.0 * 0.1 ** .3)
            rendementZ_min = (20.0 * 0.1 ** .3) - (1 * 100 * 0.1 ** pms.BETA)
        self.ui.label_rendement_Z_max.setNum(round(rendementZ_max, 2))
        self.ui.label_rendement_Z_moy.setNum(round(rendementZ_moy, 2))
        self.ui.label_rendement_Z_min.setNum(round(rendementZ_min, 2))
        self.calcul_profit_Z(rendementZ_max, rendementZ_moy, rendementZ_min,  nbX_pour_Z)
        # On retrace le graphique avec le nouveau point
        self.maj_graph_rendement_Z(nbX_pour_Z)        
        return

    def _colore_atelier(self):
        nbAteliersY = self.ui.spinBox_nbAteliersY.value()
        for iy in range(0, nbAteliersY):
            textY = QtGui.QTableWidgetItem('%s' %(str("Y")))
            self.ui.tableWidget_ateliersYZ.setItem(iy,  0,  textY)                
            self.ui.tableWidget_ateliersYZ.item(iy, 0).setBackgroundColor(QtGui.QColor(154, 255, 154))
        for iz in range(nbAteliersY, 10):
            textZ = QtGui.QTableWidgetItem('%s' %(str("Z")))
            self.ui.tableWidget_ateliersYZ.setItem(iz,  0,  textZ)                
            self.ui.tableWidget_ateliersYZ.item(iz, 0).setBackgroundColor(QtGui.QColor(139, 255, 255))
        if nbAteliersY == 0:
            self.ui.horizontalScrollBar_produitY.setEnabled(False)
        else:
            self.ui.horizontalScrollBar_produitY.setEnabled(True)
        if nbAteliersY == 10:
            self.ui.horizontalScrollBar_produitZ.setEnabled(False)
        else:
            self.ui.horizontalScrollBar_produitZ.setEnabled(True) 

class GuiTirage_de(QtGui.QDialog):
    def __init__(self, defered, automatique, parent, periode, historique, type_partie):
        super(GuiTirage_de, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
        self._historique = GuiHistorique(self, historique)

        layout = QtGui.QVBoxLayout(self)
        self._widdice = dice.WDice(parent=self, automatique = self._automatique)
        layout.addWidget(self._widdice)

        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self._accept)
        layout.addWidget(buttons)

        self.setWindowTitle(le2mtrans(u"Lancé de dé"))
        self.adjustSize()
        self.setFixedSize(self.size())
        
        # automatic
        if self._automatique:
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(self._accept)
            self._timer_automatique.start(7000)        

    def _accept(self):
        #ICI RECUPERER LA VALEUR DU DE
        le_tirage_de = self.get_dicevalue()
        if self._widdice.ui.pushButton_start.isEnabled():
            QtGui.QMessageBox.warning(
                self, le2mtrans(u"Warning"),
                le2mtrans(u"Vous devez lancer puis arrêter le dé avant de valider"))
            return
        self._defered.callback(le_tirage_de)
        self.accept()

    def get_dicevalue(self):
        return self._widdice.get_dicevalue()

class GuiAffichage_result(QtGui.QDialog):
    def __init__(self, defered, automatique, parent, periode, historique, decision_pour_Y, decision_pour_Z, tirage_du_de, type_partie, nbAteliersY, nbAteliersZ):
        super(GuiAffichage_result, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
        self._historique = GuiHistorique(self, historique)
        self.tirage_du_de = tirage_du_de
        
        # gui
        self.ui = affichageResultats.Ui_Dialog()
        self.ui.setupUi(self)

        # period and history
        if periode:
            self.ui.label_periode.setText(textes_main.PERIODE_label(periode))
            self.ui.pushButton_historique.setText(
                le2mtrans(u"History"))
            self.ui.pushButton_historique.clicked.connect(
                self._historique.show)
        else:
            self.ui.label_periode.setVisible(False)
            self.ui.pushButton_historique.setVisible(False)

        # On cache le bouton historique
        self.ui.pushButton_historique.setVisible(False)
        
        #On retaille la hauteur des ligne des tableaux historiques
        for x in range(10):
            self.ui.tableWidget_histo_produitY.setRowHeight(x, 19)
            self.ui.tableWidget_histo_produitZ.setRowHeight(x, 19)
        #On peut retailler la largeur des colonnes des tableaux historique
        self.ui.tableWidget_histo_produitY.setColumnWidth(0, 40)
        self.ui.tableWidget_histo_produitZ.setColumnWidth(0, 40)
        self.ui.tableWidget_histo_produitZ.setColumnWidth(2, 25)
        
        # bouton box
        self.ui.buttonBox.accepted.connect(self._accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setVisible(
            False)

        # title and size
        self.setWindowTitle(texts.DECISION_titre)
#        self.setFixedSize(1032, 768)

        # On rempli les lignes Y et Z du tableau resultat
        tab_decision_pour_Y = QtGui.QTableWidgetItem('%s' %(str(decision_pour_Y)))
        tab_decision_pour_Z = QtGui.QTableWidgetItem('%s' %(str(decision_pour_Z)))
        tab_tirage_du_de = QtGui.QTableWidgetItem('%s' %(str(self.tirage_du_de)))
        self.ui.tableWidget_histo_produitY.setItem(0,  0,  tab_decision_pour_Y)
        self.ui.tableWidget_histo_produitZ.setItem(0,  0,  tab_decision_pour_Z)
        self.ui.tableWidget_histo_produitZ.setItem(0,  2,  tab_tirage_du_de)
        # Suite du remplissage tableau pour le benchmark
        tab_nbateliersY = QtGui.QTableWidgetItem('%s' %(str(nbAteliersY)))
        self.ui.tableWidget_histo_produitY.setItem(0,  1,  tab_nbateliersY)
        tab_nbateliersZ = QtGui.QTableWidgetItem('%s' %(str(nbAteliersZ)))
        self.ui.tableWidget_histo_produitZ.setItem(0,  1,  tab_nbateliersZ)

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
            complement_rendementZ = float(epsylon * 100 * decision_pour_Z** pms.BETA)
        elif type_partie == "WIN" or type_partie == "WEI" or type_partie == "WIE":
            if tirage_du_de == 1:
                epsylon = -1.
            elif tirage_du_de == 6:
                epsylon = 1
            else:
                epsylon = 0
            if epsylon == -1.:
                complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) -4 + 12)
            else:
                complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) -4)

        self.le_rendementY = round(20.0 * float(decision_pour_Y) ** .3, 2)
        tab_le_rendementY = QtGui.QTableWidgetItem('%s' %(str(self.le_rendementY)))
        self.ui.tableWidget_histo_produitY.setItem(0,  2,  tab_le_rendementY)
        self.le_profitY = round((pms.PRIX_PRODUIT_Y * self.le_rendementY) - (decision_pour_Y * pms.PRIX_PRODUIT_X) + bonus + montant_fixe, 2)
        tab_le_profitY = QtGui.QTableWidgetItem('%s' %(str(self.le_profitY)))
        self.ui.tableWidget_histo_produitY.setItem(0,  3,  tab_le_profitY)
        self.le_gainY = self.le_profitY * float(nbAteliersY)
        tab_le_gainY = QtGui.QTableWidgetItem('%s' %(str(self.le_gainY)))
        self.ui.tableWidget_histo_produitY.setItem(0,  4,  tab_le_gainY)
        
        self.le_rendementZ = round((20.0 * float(decision_pour_Z) ** .3 + complement_rendementZ), 2)
        tab_le_rendementZ = QtGui.QTableWidgetItem('%s' %(str(self.le_rendementZ)))
        self.ui.tableWidget_histo_produitZ.setItem(0,  3,  tab_le_rendementZ)
        self.le_profitZ = round((pms.PRIX_PRODUIT_Z * self.le_rendementZ) - (decision_pour_Z * pms.PRIX_PRODUIT_X) + bonus + montant_fixe, 2)
        tab_le_profitZ = QtGui.QTableWidgetItem('%s' %(str(self.le_profitZ)))
        self.ui.tableWidget_histo_produitZ.setItem(0,  4,  tab_le_profitZ)
        self.le_gainZ = self.le_profitZ * float(nbAteliersZ)
        tab_le_gainZ = QtGui.QTableWidgetItem('%s' %(str(self.le_gainZ)))
        self.ui.tableWidget_histo_produitZ.setItem(0,  5,  tab_le_gainZ)        
        
        # automatic
        if self._automatique:
            # On rempli les lignes Y et Z du tableau resultat
            tab_decision_pour_Y = QtGui.QTableWidgetItem('%s' %(str(decision_pour_Y)))
            tab_decision_pour_Z = QtGui.QTableWidgetItem('%s' %(str(decision_pour_Z)))
            tab_tirage_du_de = QtGui.QTableWidgetItem('%s' %(str(self.tirage_du_de)))
            self.ui.tableWidget_histo_produitY.setItem(0,  0,  tab_decision_pour_Y)
            self.ui.tableWidget_histo_produitZ.setItem(0,  0,  tab_decision_pour_Z)
            self.ui.tableWidget_histo_produitZ.setItem(0,  2,  tab_tirage_du_de)
            # Suite du remplissage tableau pour le benchmark
            tab_nbateliersY = QtGui.QTableWidgetItem('%s' %(str(nbAteliersY)))
            self.ui.tableWidget_histo_produitY.setItem(0,  1,  tab_nbateliersY)
            tab_nbateliersZ = QtGui.QTableWidgetItem('%s' %(str(nbAteliersZ)))
            self.ui.tableWidget_histo_produitZ.setItem(0,  1,  tab_nbateliersZ)
            
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
                complement_rendementZ = float(epsylon * 100 * decision_pour_Z** pms.BETA)
            elif type_partie == "WIN" or type_partie == "WEI" or type_partie == "WIE":
                if tirage_du_de == 1:
                    epsylon = -1.
                elif tirage_du_de == 6:
                    epsylon = 1
                else:
                    epsylon = 0
                if epsylon == -1.:
                    complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) -4 + 12)
                else:
                    complement_rendementZ = float(epsylon * 100 * (decision_pour_Z** pms.BETA) -4)            
            
            self.le_rendementY = round(20.0 * float(decision_pour_Y) ** .3, 2)
            tab_le_rendementY = QtGui.QTableWidgetItem('%s' %(str(self.le_rendementY)))
            self.ui.tableWidget_histo_produitY.setItem(0,  2,  tab_le_rendementY)
            self.le_profitY = round(10 * self.le_rendementY - decision_pour_Y, 2)
            tab_le_profitY = QtGui.QTableWidgetItem('%s' %(str(self.le_profitY)))
            self.ui.tableWidget_histo_produitY.setItem(0,  3,  tab_le_profitY)
            self.le_gainY = self.le_profitY * float(nbAteliersY)
            tab_le_gainY = QtGui.QTableWidgetItem('%s' %(str(self.le_gainY)))
            self.ui.tableWidget_histo_produitY.setItem(0,  4,  tab_le_gainY)
            
            self.le_rendementZ = round((20.0 * float(decision_pour_Z) ** .3), 2)
            tab_le_rendementZ = QtGui.QTableWidgetItem('%s' %(str(self.le_rendementZ)))
            self.ui.tableWidget_histo_produitZ.setItem(0,  3,  tab_le_rendementZ)
            self.le_profitZ = round(10 * self.le_rendementZ - decision_pour_Z, 2)
            tab_le_profitZ = QtGui.QTableWidgetItem('%s' %(str(self.le_profitZ)))
            self.ui.tableWidget_histo_produitZ.setItem(0,  4,  tab_le_profitZ)
            self.le_gainZ = self.le_profitZ * float(nbAteliersZ)
            tab_le_gainZ = QtGui.QTableWidgetItem('%s' %(str(self.le_gainZ)))
            self.ui.tableWidget_histo_produitZ.setItem(0,  5,  tab_le_gainZ)            
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(self._accept)
            self._timer_automatique.start(7000)
                
    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        retour = []
        retour.append(self.le_rendementY)
        retour.append(self.le_rendementZ)
        retour.append(self.le_profitY)
        retour.append(self.le_profitZ)
        retour.append(self.tirage_du_de)
        retour.append(self.le_gainY)
        retour.append(self.le_gainZ)
        if not self._automatique:
            confirmation = QtGui.QMessageBox.question(
                self, texts.DECISION_confirmation.titre,
                texts.DECISION_confirmation.message,
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes
            )
            if confirmation != QtGui.QMessageBox.Yes: 
                return
        self._defered.callback(retour)
        self.accept()
        
