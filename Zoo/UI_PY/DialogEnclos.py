# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogEnclos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(921, 734)
        self.pushButtonAjouterEnclos = QtWidgets.QPushButton(Dialog)
        self.pushButtonAjouterEnclos.setGeometry(QtCore.QRect(30, 530, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonAjouterEnclos.setFont(font)
        self.pushButtonAjouterEnclos.setObjectName("pushButtonAjouterEnclos")
        self.pushButtonModifierEnclos = QtWidgets.QPushButton(Dialog)
        self.pushButtonModifierEnclos.setGeometry(QtCore.QRect(250, 530, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonModifierEnclos.setFont(font)
        self.pushButtonModifierEnclos.setObjectName("pushButtonModifierEnclos")
        self.pushButtonSupprimerEnclos = QtWidgets.QPushButton(Dialog)
        self.pushButtonSupprimerEnclos.setGeometry(QtCore.QRect(30, 630, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonSupprimerEnclos.setFont(font)
        self.pushButtonSupprimerEnclos.setObjectName("pushButtonSupprimerEnclos")
        self.lineEditNumeroEnclos = QtWidgets.QLineEdit(Dialog)
        self.lineEditNumeroEnclos.setGeometry(QtCore.QRect(30, 40, 191, 41))
        self.lineEditNumeroEnclos.setObjectName("lineEditNumeroEnclos")
        self.lineEditNomEnclos = QtWidgets.QLineEdit(Dialog)
        self.lineEditNomEnclos.setGeometry(QtCore.QRect(30, 130, 191, 41))
        self.lineEditNomEnclos.setObjectName("lineEditNomEnclos")
        self.lineEditType = QtWidgets.QLineEdit(Dialog)
        self.lineEditType.setGeometry(QtCore.QRect(30, 330, 191, 41))
        self.lineEditType.setObjectName("lineEditType")
        self.lineEditLocalisation = QtWidgets.QLineEdit(Dialog)
        self.lineEditLocalisation.setGeometry(QtCore.QRect(30, 440, 191, 41))
        self.lineEditLocalisation.setObjectName("lineEditLocalisation")
        self.lineEditTaille = QtWidgets.QLineEdit(Dialog)
        self.lineEditTaille.setGeometry(QtCore.QRect(30, 230, 191, 41))
        self.lineEditTaille.setObjectName("lineEditTaille")
        self.labelNumeroEnclos = QtWidgets.QLabel(Dialog)
        self.labelNumeroEnclos.setGeometry(QtCore.QRect(30, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNumeroEnclos.setFont(font)
        self.labelNumeroEnclos.setObjectName("labelNumeroEnclos")
        self.labelTaille = QtWidgets.QLabel(Dialog)
        self.labelTaille.setGeometry(QtCore.QRect(30, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelTaille.setFont(font)
        self.labelTaille.setObjectName("labelTaille")
        self.labelNomEnclos = QtWidgets.QLabel(Dialog)
        self.labelNomEnclos.setGeometry(QtCore.QRect(30, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNomEnclos.setFont(font)
        self.labelNomEnclos.setObjectName("labelNomEnclos")
        self.labelType = QtWidgets.QLabel(Dialog)
        self.labelType.setGeometry(QtCore.QRect(30, 300, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelType.setFont(font)
        self.labelType.setObjectName("labelType")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowserEnclos = QtWidgets.QTextBrowser(Dialog)
        self.textBrowserEnclos.setGeometry(QtCore.QRect(540, 270, 311, 281))
        self.textBrowserEnclos.setObjectName("textBrowserEnclos")
        self.labelErreurNumeroEnclos = QtWidgets.QLabel(Dialog)
        self.labelErreurNumeroEnclos.setGeometry(QtCore.QRect(30, 80, 591, 21))
        self.labelErreurNumeroEnclos.setText("")
        self.labelErreurNumeroEnclos.setObjectName("labelErreurNumeroEnclos")
        self.labelErreurNomEnclos = QtWidgets.QLabel(Dialog)
        self.labelErreurNomEnclos.setGeometry(QtCore.QRect(30, 170, 321, 21))
        self.labelErreurNomEnclos.setText("")
        self.labelErreurNomEnclos.setObjectName("labelErreurNomEnclos")
        self.labelErreurTaille = QtWidgets.QLabel(Dialog)
        self.labelErreurTaille.setGeometry(QtCore.QRect(30, 270, 381, 21))
        self.labelErreurTaille.setText("")
        self.labelErreurTaille.setObjectName("labelErreurTaille")
        self.labelErreurType = QtWidgets.QLabel(Dialog)
        self.labelErreurType.setGeometry(QtCore.QRect(30, 380, 381, 21))
        self.labelErreurType.setText("")
        self.labelErreurType.setObjectName("labelErreurType")
        self.labelErreurLocalisation = QtWidgets.QLabel(Dialog)
        self.labelErreurLocalisation.setGeometry(QtCore.QRect(30, 490, 221, 21))
        self.labelErreurLocalisation.setText("")
        self.labelErreurLocalisation.setObjectName("labelErreurLocalisation")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DialogEnclos"))
        self.pushButtonAjouterEnclos.setText(_translate("Dialog", "Ajouter"))
        self.pushButtonModifierEnclos.setText(_translate("Dialog", "Modifier"))
        self.pushButtonSupprimerEnclos.setText(_translate("Dialog", "Supprimer"))
        self.labelNumeroEnclos.setText(_translate("Dialog", "Numero de l\'enclos"))
        self.labelTaille.setText(_translate("Dialog", "Taille"))
        self.labelNomEnclos.setText(_translate("Dialog", "Nom de l\'enclos"))
        self.labelType.setText(_translate("Dialog", "Type"))
        self.label_6.setText(_translate("Dialog", "Localisation"))
