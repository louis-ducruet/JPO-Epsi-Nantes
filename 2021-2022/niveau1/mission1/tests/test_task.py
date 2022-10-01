import unittest

from shifumi import test_gagnant

testValues = [
    {"j1": 1, "j2": 1, "sc": [0, 0], "msg": "Vérifie l'égalité de la pierre"},
    {"j1": 2, "j2": 2, "sc": [0, 0], "msg": "Vérifie l'égalité de la feuille"},
    {"j1": 3, "j2": 3, "sc": [0, 0], "msg": "Vérifie l'égalité des ciseaux"},
    {"j1": 1, "j2": 2, "sc": [0, 1], "msg": "Victoire de la feuille sur la pierre"},
    {"j1": 1, "j2": 3, "sc": [1, 0], "msg": "Victoire de la pierre sur les ciseaux"},
    {"j1": 2, "j2": 1, "sc": [1, 0], "msg": "Victoire de la feuille sur la pierre"},
    {"j1": 2, "j2": 3, "sc": [0, 1], "msg": "Victoire des ciseaux sur la feuille"},
    {"j1": 3, "j2": 1, "sc": [0, 1], "msg": "Victoire de la pierre sur les ciseaux"},
    {"j1": 3, "j2": 2, "sc": [1, 0], "msg": "Victoire des ciseaux sur la feuille"}
]

class TestCase(unittest.TestCase):
    def test_add(self):
        for tv in testValues:
            self.assertEqual(test_gagnant("", tv["j1"], "", tv["j2"], [0, 0]), tv["sc"], msg=tv["msg"])
