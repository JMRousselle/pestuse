# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pestuseDecision.ui'
#
# Created: Fri Sep  9 10:38:32 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1032, 768)
        Dialog.setMinimumSize(QtCore.QSize(1032, 768))
        Dialog.setMaximumSize(QtCore.QSize(1032, 768))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_periode = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_periode.setFont(font)
        self.label_periode.setObjectName(_fromUtf8("label_periode"))
        self.horizontalLayout.addWidget(self.label_periode)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_historique = QtGui.QPushButton(Dialog)
        self.pushButton_historique.setObjectName(_fromUtf8("pushButton_historique"))
        self.horizontalLayout.addWidget(self.pushButton_historique)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_nbAteliersY = QtGui.QLabel(Dialog)
        self.label_nbAteliersY.setObjectName(_fromUtf8("label_nbAteliersY"))
        self.horizontalLayout_6.addWidget(self.label_nbAteliersY)
        self.spinBox_nbAteliersY = QtGui.QSpinBox(Dialog)
        self.spinBox_nbAteliersY.setObjectName(_fromUtf8("spinBox_nbAteliersY"))
        self.horizontalLayout_6.addWidget(self.spinBox_nbAteliersY)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.tableWidget_ateliersYZ = QtGui.QTableWidget(Dialog)
        self.tableWidget_ateliersYZ.setMinimumSize(QtCore.QSize(132, 330))
        self.tableWidget_ateliersYZ.setMaximumSize(QtCore.QSize(132, 330))
        self.tableWidget_ateliersYZ.setObjectName(_fromUtf8("tableWidget_ateliersYZ"))
        self.tableWidget_ateliersYZ.setColumnCount(1)
        self.tableWidget_ateliersYZ.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_ateliersYZ.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget_ateliersYZ.setItem(9, 0, item)
        self.horizontalLayout_4.addWidget(self.tableWidget_ateliersYZ)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.label_10 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_6.addWidget(self.label_10)
        self.label_rendement_Y = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rendement_Y.setFont(font)
        self.label_rendement_Y.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_rendement_Y.setText(_fromUtf8(""))
        self.label_rendement_Y.setObjectName(_fromUtf8("label_rendement_Y"))
        self.verticalLayout_6.addWidget(self.label_rendement_Y)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem12)
        self.label_11 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_profit_Y = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_profit_Y.setFont(font)
        self.label_profit_Y.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_profit_Y.setText(_fromUtf8(""))
        self.label_profit_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_profit_Y.setObjectName(_fromUtf8("label_profit_Y"))
        self.verticalLayout_7.addWidget(self.label_profit_Y)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem13)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_8.addWidget(self.label_13)
        self.label_rendement_Z_max = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rendement_Z_max.setFont(font)
        self.label_rendement_Z_max.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_rendement_Z_max.setText(_fromUtf8(""))
        self.label_rendement_Z_max.setObjectName(_fromUtf8("label_rendement_Z_max"))
        self.verticalLayout_8.addWidget(self.label_rendement_Z_max)
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_rendement_Z_moy = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rendement_Z_moy.setFont(font)
        self.label_rendement_Z_moy.setStyleSheet(_fromUtf8("color: rgb(0, 128, 0);"))
        self.label_rendement_Z_moy.setText(_fromUtf8(""))
        self.label_rendement_Z_moy.setObjectName(_fromUtf8("label_rendement_Z_moy"))
        self.verticalLayout_8.addWidget(self.label_rendement_Z_moy)
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_8.addWidget(self.label_16)
        self.label_rendement_Z_min = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rendement_Z_min.setFont(font)
        self.label_rendement_Z_min.setStyleSheet(_fromUtf8("color: rgb(192, 0, 0);"))
        self.label_rendement_Z_min.setText(_fromUtf8(""))
        self.label_rendement_Z_min.setObjectName(_fromUtf8("label_rendement_Z_min"))
        self.verticalLayout_8.addWidget(self.label_rendement_Z_min)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem15)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 1, 3, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem16)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_9.addWidget(self.label_4)
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_9.addWidget(self.label_14)
        self.label_profit_Z_max = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_profit_Z_max.setFont(font)
        self.label_profit_Z_max.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.label_profit_Z_max.setText(_fromUtf8(""))
        self.label_profit_Z_max.setObjectName(_fromUtf8("label_profit_Z_max"))
        self.verticalLayout_9.addWidget(self.label_profit_Z_max)
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_9.addWidget(self.label_17)
        self.label_profit_Z_moy = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_profit_Z_moy.setFont(font)
        self.label_profit_Z_moy.setStyleSheet(_fromUtf8("color: rgb(0, 128, 0);"))
        self.label_profit_Z_moy.setText(_fromUtf8(""))
        self.label_profit_Z_moy.setObjectName(_fromUtf8("label_profit_Z_moy"))
        self.verticalLayout_9.addWidget(self.label_profit_Z_moy)
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_9.addWidget(self.label_18)
        self.label_profit_Z_min = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_profit_Z_min.setFont(font)
        self.label_profit_Z_min.setStyleSheet(_fromUtf8("color: rgb(192, 0, 0);"))
        self.label_profit_Z_min.setText(_fromUtf8(""))
        self.label_profit_Z_min.setObjectName(_fromUtf8("label_profit_Z_min"))
        self.verticalLayout_9.addWidget(self.label_profit_Z_min)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem17)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 2, 3, 1, 1)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_10.addWidget(self.label_2)
        self.horizontalScrollBar_produitY = QtGui.QScrollBar(Dialog)
        self.horizontalScrollBar_produitY.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalScrollBar_produitY.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalScrollBar_produitY.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_produitY.setObjectName(_fromUtf8("horizontalScrollBar_produitY"))
        self.verticalLayout_10.addWidget(self.horizontalScrollBar_produitY)
        self.label_val_cursY = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_val_cursY.setFont(font)
        self.label_val_cursY.setText(_fromUtf8(""))
        self.label_val_cursY.setAlignment(QtCore.Qt.AlignCenter)
        self.label_val_cursY.setObjectName(_fromUtf8("label_val_cursY"))
        self.verticalLayout_10.addWidget(self.label_val_cursY)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 3, 1, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_11.addWidget(self.label_3)
        self.horizontalScrollBar_produitZ = QtGui.QScrollBar(Dialog)
        self.horizontalScrollBar_produitZ.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalScrollBar_produitZ.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalScrollBar_produitZ.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_produitZ.setObjectName(_fromUtf8("horizontalScrollBar_produitZ"))
        self.verticalLayout_11.addWidget(self.horizontalScrollBar_produitZ)
        self.label_val_cursZ = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_val_cursZ.setFont(font)
        self.label_val_cursZ.setText(_fromUtf8(""))
        self.label_val_cursZ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_val_cursZ.setObjectName(_fromUtf8("label_val_cursZ"))
        self.verticalLayout_11.addWidget(self.label_val_cursZ)
        self.gridLayout_2.addLayout(self.verticalLayout_11, 3, 4, 1, 1)
        self.verticalLayout_graph_profit_Y = QtGui.QVBoxLayout()
        self.verticalLayout_graph_profit_Y.setObjectName(_fromUtf8("verticalLayout_graph_profit_Y"))
        self.gridLayout_2.addLayout(self.verticalLayout_graph_profit_Y, 2, 1, 1, 1)
        self.verticalLayout_graph_rendement_Y = QtGui.QVBoxLayout()
        self.verticalLayout_graph_rendement_Y.setObjectName(_fromUtf8("verticalLayout_graph_rendement_Y"))
        self.gridLayout_2.addLayout(self.verticalLayout_graph_rendement_Y, 1, 1, 1, 1)
        self.verticalLayout_graph_rendement_Z = QtGui.QVBoxLayout()
        self.verticalLayout_graph_rendement_Z.setObjectName(_fromUtf8("verticalLayout_graph_rendement_Z"))
        self.gridLayout_2.addLayout(self.verticalLayout_graph_rendement_Z, 1, 4, 1, 1)
        self.verticalLayout_graph_profit_Z = QtGui.QVBoxLayout()
        self.verticalLayout_graph_profit_Z.setObjectName(_fromUtf8("verticalLayout_graph_profit_Z"))
        self.gridLayout_2.addLayout(self.verticalLayout_graph_profit_Z, 2, 4, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.line_3 = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 2, 2, 1, 1)
        self.line_4 = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 1, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem19)
        self.line_2 = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.tableWidget_histo_produitY = QtGui.QTableWidget(Dialog)
        self.tableWidget_histo_produitY.setMinimumSize(QtCore.QSize(500, 220))
        self.tableWidget_histo_produitY.setMaximumSize(QtCore.QSize(500, 220))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_histo_produitY.setFont(font)
        self.tableWidget_histo_produitY.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_histo_produitY.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_histo_produitY.setObjectName(_fromUtf8("tableWidget_histo_produitY"))
        self.tableWidget_histo_produitY.setColumnCount(5)
        self.tableWidget_histo_produitY.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_histo_produitY.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitY.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tableWidget_histo_produitY)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_10.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.tableWidget_histo_produitZ = QtGui.QTableWidget(Dialog)
        self.tableWidget_histo_produitZ.setMinimumSize(QtCore.QSize(500, 220))
        self.tableWidget_histo_produitZ.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget_histo_produitZ.setFont(font)
        self.tableWidget_histo_produitZ.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_histo_produitZ.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_histo_produitZ.setObjectName(_fromUtf8("tableWidget_histo_produitZ"))
        self.tableWidget_histo_produitZ.setColumnCount(6)
        self.tableWidget_histo_produitZ.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_histo_produitZ.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.tableWidget_histo_produitZ)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem25 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem25)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.horizontalScrollBar_produitY, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_val_cursY.setNum)
        QtCore.QObject.connect(self.horizontalScrollBar_produitZ, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_val_cursZ.setNum)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_periode.setText(_translate("Dialog", "Période 0", None))
        self.pushButton_historique.setText(_translate("Dialog", "Historique", None))
        self.label_nbAteliersY.setText(_translate("Dialog", "Combien d\'ateliers voulez-vous affecter \n"
"à la fabrication du produit Y ?", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9", None))
        item = self.tableWidget_ateliersYZ.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10", None))
        item = self.tableWidget_ateliersYZ.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Produit", None))
        __sortingEnabled = self.tableWidget_ateliersYZ.isSortingEnabled()
        self.tableWidget_ateliersYZ.setSortingEnabled(False)
        self.tableWidget_ateliersYZ.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("Dialog", "Rendement", None))
        self.label_11.setText(_translate("Dialog", "Profit", None))
        self.label.setText(_translate("Dialog", "Rendement", None))
        self.label_13.setText(_translate("Dialog", "Maximum", None))
        self.label_15.setText(_translate("Dialog", "Moyen", None))
        self.label_16.setText(_translate("Dialog", "Minimum", None))
        self.label_4.setText(_translate("Dialog", "Profit", None))
        self.label_14.setText(_translate("Dialog", "Maximum", None))
        self.label_17.setText(_translate("Dialog", "Moyen", None))
        self.label_18.setText(_translate("Dialog", "Minimum", None))
        self.label_2.setText(_translate("Dialog", "Quantité d\'intrans X", None))
        self.label_3.setText(_translate("Dialog", "Quantité d\'intrans X", None))
        self.label_5.setText(_translate("Dialog", "PRODUIT Y", None))
        self.label_6.setText(_translate("Dialog", "PRODUIT Z", None))
        self.label_7.setText(_translate("Dialog", "HISTORIQUE", None))
        self.label_9.setText(_translate("Dialog", "PRODUIT Y", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9", None))
        item = self.tableWidget_histo_produitY.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10", None))
        item = self.tableWidget_histo_produitY.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "x", None))
        item = self.tableWidget_histo_produitY.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "nb ateliers", None))
        item = self.tableWidget_histo_produitY.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "rendement", None))
        item = self.tableWidget_histo_produitY.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "profit", None))
        item = self.tableWidget_histo_produitY.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "gain", None))
        self.label_8.setText(_translate("Dialog", "PRODUIT Z", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9", None))
        item = self.tableWidget_histo_produitZ.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "x", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "nb ateliers", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "dé", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "rendement", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "profit", None))
        item = self.tableWidget_histo_produitZ.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "gain", None))

