import json

import jsonpickle

# importer les classes.
from Zoo.Classes.Classe_Enclos import Enclos
from Zoo.Classes.Classe_Veterinaire import Veterinaire


class Animal():
    """
    Classe Animal
    """
    nb_animaux = 0
    ls_animaux = []
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: str = "", p_veterinaire: str = ""):
        """
        Constructeur de la classe Animal
        :param: numero_animal: doit commencer par deux lettres suivies d’un tiret puis de cinq chiffres, exemple : LI-41524.
        :param: surnom: ne comporte aucune validation
        :param: poids: doit être un nombre entier supérieur à 15 lb
        :param: famille: de l’animal à laquelle il appartient : soit mammifères, soit oiseaux, soit reptiles.
        """
        self._numero_animal = p_numero_animal
        self._surnom = p_surnom
        self._poids = p_poids
        self._famille = p_famille
        self._enclos = p_enclos
        self._veterinaire = p_veterinaire
        Animal.nb_animaux += 1
        Animal.ls_animaux.append(self)

    ########################################################

    @property
    def numero_animal(self):
        return self._numero_animal
    @numero_animal.setter
    def numero_animal(self, v_numero_animal):
        if isinstance(v_numero_animal, str) and v_numero_animal[0:1].isalpha() and v_numero_animal[2] == "-" and v_numero_animal[3:7].isnumeric():
            self._numero_animal = v_numero_animal
    @property
    def surnom(self):
        return self._surnom
    @surnom.setter
    def surnom(self, v_surnom):
        self._surnom = v_surnom

    @property
    def poids(self):
        return self._poids
    @poids.setter
    def poids(self, v_poids):
        if isinstance(v_poids, int) and v_poids > 15:
            self._poids = v_poids

    @property
    def famille(self):
        return self._famille
    @famille.setter
    def famille(self, v_famille):
        if isinstance(v_famille, str) and v_famille == "mammiferes" or v_famille == "oiseaux" or v_famille == "reptiles":
            self._famille = v_famille

    ########################################################

    # ajouter les méthodes.

    def ajouterEnclosVeterinaire(self, numero_emp: Veterinaire._numero_emp, enclos: Enclos):
        """
        Permet d'ajouter un enclo a la liste des enclos d'un veterinaire qui s'occupent de l'animal
        """
        if isinstance(numero_emp, Veterinaire._numero_emp):
            Veterinaire._list_enclos.append(enclos)


    # serialiser un instance de la classe Animal
    def serilialiserAnimal(self):
        with open(self._numero_animal + ".json", "w") as f:
            json.dump(jsonpickle.encode(self), f, indent=4)

    # derialiser l'instance de la classe Animal
    @staticmethod
    def desserialiserAnimal(self, nom_fichier):
        with open(nom_fichier, "r") as f:
            animal = f.read()
        objet_animal = jsonpickle.decode(animal)
        return objet_animal


    # Fonction magic de la classe Animal
    def __str__(self):
        return (f"Animal:\n"
                f"Numero de l'animal: {self.numero_animal}\n"
                f"Surnom: {self.surnom}\n"
                f"Poids: {self._poids}\n"
                f"Famille: {self.famille}\n"
                f"Enclo: {self._enclos}\n"
                f"Veterinaire: {self._veterinaire}")