# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
# importer les classes
from Zoo.Classes.Classe_Animal import Animal
from Zoo.Classes.Classe_Enclos import Enclos

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
        self.ajouter_comboBox_enclos_animal()
    def ajouter_comboBox_enclos_animal(self):
        """
        Gestion des enclos dans le comboBox_enclos_animal
        """
        for enclos in Enclos.ls_enclos:
            self.enclos_comboBox.addItem(enclos)

    def on_pushButton_ajouter_clicked(self):
        """

        """
        animal1 = Animal()
        numero_animal = self.lineEdit_numero_animal.texte()
        surnom = self.lineEdit_surnom_animal.texte()
        poids = self.lineEdit_poids_animal.texte()
        famille = self.comboBox_famille_animal.currentText()
        enclos = self.comboBox_enclos_animal.currentText()
