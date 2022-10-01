from typing import List, NoReturn
import functions as shifumi


# Variables globales
options = ['Pierre', 'Feuille', 'Ciseaux']
score = [0, 0]


# ================== Partie à recoder ==================
# Fonction determinant le gagnant de la manche
"""
❗❗❗              Information Importante :              ❗❗❗
saisie_jx : 1 pour Pierre, 2 pour Feuille, 3 pour Ciseaux
Utiliser plusieurs fois les conditions ci-dessous
"""
def test_gagnant(nom_j1: str, saisie_j1: int, nom_j2: str, saisie_j2: int, game_score: List[int]):
    # Si égalité
    if False:
        print('Égalité ! Personne ne gagne de point.')
    # Si le joueur 1 gagne
    if False:
        print(f'{nom_j1} gagne la manche !')
        game_score[0] += 1
    # Si le joueur 2 gagne
    if False:
        print(f'{nom_j2} gagne la manche !')
        game_score[1] += 1
    return game_score
# ================= Fin partie à coder =================


# Fonction déterminant le déroulement d'une partie
def game() -> NoReturn:
    global score
    shifumi.affichage_regles()
    while score[0] != 3 and score[1] != 3:
        saisie_j1 = shifumi.saisie_joueur('Joueur 1')
        saisie_j2 = shifumi.saisie_joueur('Joueur 2')
        shifumi.affichage_choix('Joueur 1', options[saisie_j1 - 1], 'Joueur 2', options[saisie_j2 - 1])
        score = test_gagnant('Joueur 1', saisie_j1, 'Joueur 2', saisie_j2, score)
        shifumi.affichage_score('Joueur 1', 'Joueur 2', score)
    shifumi.affichage_gagnant('Joueur 1', 'Joueur 2', score)


# Fonction déterminant le déroulement du programme
def main() -> int:
    global score
    while True:
        saisie = input('Voulez vous lancer une partie de Pierre / Feuille / Ciseaux ? (O)ui / (N)on : ').upper()
        if saisie in ['O', 'N', 'OUI', 'NON']:
            if saisie in ['O', 'OUI']:
                score = [0, 0]
                game()
            else:
                return 0
        else:
            print('Saisie incorrect !')


if __name__ == '__main__':
    main()
