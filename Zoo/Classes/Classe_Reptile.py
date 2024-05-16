from Classe_Animal import Animal


class Reptile():
    """
    Classe Reptile
    sous classe de la classe Animal
    """

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", p_veterinaire: str = "", p_venimeux: bool = False):
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
        self._venimeux = p_venimeux

    ########################################################

    @property
    def venimeux(self):
        return self._venimeux
    @venimeux.setter
    def venimeux(self, v_venimeux):
        if isinstance(v_venimeux, bool) and v_venimeux == True or v_venimeux == False:
            self._venimeux = v_venimeux