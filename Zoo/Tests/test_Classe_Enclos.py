from Zoo.Classes.Classe_Veterinaire import Veterinaire
from Zoo.Classes.Classe_Enclos import Enclos
import pytest

# test fonction estAdapte
@pytest.fixture
def enclos():
    return Enclos("12345ABC", "ENCLO", "petit",
                  "interieur", "A", [Chien, Chat])

@pytest.mark.usefixtures(enclos)("enclos, expected",[
    (enclos, True)
])
def test_estAdapte(enclos, expected):
    assert Enclos.estAdapte(enclos(), taille) == expected

# test 2 fonction estAdapte
@pytest.mark.parametrize("ls_animaux_enclos, taille, expected",[
    (["Chien, Chat"], "petit", True)
    (["Chien, Chat, Oiseau"], "petit", False),
    (["Chien, Chat, Oiseau, Lezard"], "petit", True)
    (["Chen, Chat, Oiseau, Lezard, Poisson"], "moyen", False),
    (["Chien, Chat, Oiseau, Lezard, Poisson"], "grand", True),
    (["Chien, Chat, Oiseau, Lezard, Poisson, Tigre, Lion"], "grand", False)
])
def test_estAdapte(ls_animaux_enclos, taille, expected):
    assert Enclos.estAdapte(ls_animaux_enclos, taille) == expected

# test fonction prendreRetraite
@pytest.mark.parametrize("age, expected",[
    ("0", False),
    ("60", True),
    ("bob", False)
])
def test_prendreRetraite(age, expected):
    assert Veterinaire.PrendreRetraite(age) == expected