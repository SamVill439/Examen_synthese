# importer le fichier du ui converti en py.
from PyQt5.QtCore import pyqtSlot

# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# Importer le message_box pour les erreurs.
from PyQt5.QtWidgets import QMessageBox

# Importer le module sys nécessaire à l'exécution.
import sys

# Importer les fichiers d'interface graphique .py
import UI_PY.DialogEnclos as DialogEnclos

# Importer les classe.
from Zoo.Classes.Classe_Enclos import Enclos

# le numero de lenclos doit: être composé d’un nombre entier sur 5 caractères suivi de trois lettres. Exemple : 12345ABC
# le nom de lenclose doit: être composé d’un maximum de 25 lettres
# la taille de lenclos doit: avoir l’une des trois valeurs : petit, moyen ou grand
# le type de lenclos doit: être soit interieur ou exterieur
# la localisation de lenclos doit: être A, B ou C.

class DialogEnclos(QtWidgets.QDialog, DialogEnclos.Ui_Dialog):
    """
    Classe du gestion d'evenement de l'interface DialogEnclos
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe DialogEnclos
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(DialogEnclos, self).__init__(parent)
        self.setupUi(self)

        #gerer les evenements


def main():
    '''
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = DialogEnclos()  # Nom de ma classe
    form.show()
    app.exec()

if __name__ == "__main__":
    main()
