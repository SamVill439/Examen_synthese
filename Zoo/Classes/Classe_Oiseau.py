from Classe_Animal import Animal

class Oiseau():
    """
    Classe Oiseau
    sous classe de la classe Animal
    """
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", p_veterinaire: str = "", p_longueur_bec: float = 0.00):
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
        self._longueur_bec = p_longueur_bec

    ########################################################

    @property
    def longueur_bec(self):
        return self._longueur_bec
    @longueur_bec.setter
    def longueur_bec(self, v_longueur_bec):
        if isinstance(v_longueur_bec, float) and v_longueur_bec > 0.00:
            self._longueur_bec = v_longueur_bec