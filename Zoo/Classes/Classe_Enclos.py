class Enclos():
    """
    Classe Enclos
    """
    ls_enclos = []
    nb_enclos = 0
    def __init__(self, p_numero_enclos: str = "", p_nom_enclos: str = "", p_taille: str = "",
                 p_type: str = "", p_localisation: str = "", p_ls_animaux_enclos: list = None):
        """
        Constructeur de la classe Enclos
        """
        self._numero_enclos = p_numero_enclos
        self._nom_enclos = p_nom_enclos
        self._taille = p_taille
        self._type = p_type
        self._localisation = p_localisation
        if p_ls_animaux_enclos == None:
            self._ls_animaux_enclos = []
        else:
            self._ls_animaux_enclos = p_ls_animaux_enclos
        Enclos.nb_enclos += 1
        Enclos.ls_enclos.append(self)

    ########################################################
    @property
    def numero_enclos(self):
        return self._numero_enclos
    @numero_enclos.setter
    def numero_enclos(self, v_numero_enclos):
        if isinstance(v_numero_enclos, str) and v_numero_enclos[0:4].isalpha() and v_numero_enclos[5:7].isnumeric() and len(v_numero_enclos) == 8:
            self._numero_enclos = v_numero_enclos

    @property
    def nom_enclos(self):
        return self._nom_enclos
    @nom_enclos.setter
    def nom_enclos(self, v_nom_enclos):
        if isinstance(v_nom_enclos, str) and v_nom_enclos.isalpha() and len(v_nom_enclos) <= 25:
            self._nom_enclos = v_nom_enclos

    @property
    def taille(self):
        return self._taille
    @taille.setter
    def taille(self, v_taille):
        if isinstance(v_taille, str) and v_taille == "petit" or v_taille == "moyen" or v_taille == "grand":
            self._taille = v_taille

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, v_type):
        if isinstance(v_type, str) and v_type == "interieur" or v_type == "exterieur":
            self._type = v_type

    @property
    def localisation(self):
        return self._localisation
    @localisation.setter
    def localisation(self, v_localisation):
        if isinstance(v_localisation, str) and v_localisation == "A" or v_localisation == "B" or v_localisation == "C":
            self._localisation = v_localisation

    @property
    def ls_animaux_enclos(self):
        return self._ls_animaux_enclos
    @ls_animaux_enclos.setter
    def ls_animaux_enclos(self, v_ls_animaux_enclos):
        if isinstance(v_ls_animaux_enclos, Animal):
            self._ls_animaux_enclos = v_ls_animaux_enclos

    ########################################################

    # ajouter les methodes.

    def estAdapte(self):
        """
        permet de verifier si le nombre limit d'animaux dans l'enclos est ataint.
        """
        enclos_adapte = False
        if len(self._ls_animaux_enclos) <=2 and self._taille == "petit" or self._taille == "moyen" or self._taille == "grand":
            enclos_adapte = True
        elif len(self._ls_animaux_enclos) <=4 and self._taille == "moyen" or self._taille == "grand":
            enclos_adapte = True
        elif len(self._ls_animaux_enclos) <=6 and self._taille == "grand":
            enclos_adapte = True
        else:
            enclos_adapte = False

        return enclos_adapte