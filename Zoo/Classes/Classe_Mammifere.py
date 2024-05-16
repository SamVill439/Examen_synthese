from Classe_Animal import Animal

class Mammifere():
    """
    Classe Mammifere
    sous classe de la classe Animal
    """
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "", p_enclos: str = "", p_veterinaire: str = "", p_couleur_poil: str = ""):
        """
        Constructeur de la classe Mammifere
        :param: numero_animal: doit commencer par deux lettres suivies d’un tiret puis de cinq chiffres, exemple : LI-41524.
        :param: surnom: ne comporte aucune validation
        :param: poids: doit être un nombre entier supérieur à 15 lb
        :param: famille: de l’animal à laquelle il appartient : soit mammifères, soit oiseaux, soit reptiles.
        """
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, p_veterinaire)
        self._numero_animal = p_numero_animal
        self._surnom = p_surnom
        self._poids = p_poids
        self._famille = p_famille
        self._enclos = p_enclos
        self._veterinaire = p_veterinaire
        self._couleur_poil = p_couleur_poil

    ########################################################

    @property
    def couleur_poil(self):
        return self._couleur_poil
    @couleur_poil.setter
    def couleur_poil(self, v_couleur_poil):
        if (isinstance(v_couleur_poil, str) and v_couleur_poil == "noire" or v_couleur_poil == "blanche" or v_couleur_poil == "brune" or v_couleur_poil == "grise" or v_couleur_poil == "beige"
                or v_couleur_poil == "multi couleurs"):
            self._couleur_poil = v_couleur_poil

    ########################################################

    def __str__(self):
        return (f"Animal:\n"
                f"Numero de l'animal: {self.numero_animal}\n"
                f"Surnom: {self.surnom}\n"
                f"Poids: {self._poids}\n"
                f"Famille: {self.famille}\n"
                f"Enclo: {self._enclos}\n"
                f"Veterinaire: {self._veterinaire}\n"
                f"Couleur Poil: {self._couleur_poil}")
