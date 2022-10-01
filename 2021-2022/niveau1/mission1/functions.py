from typing import List, NoReturn


# Fonction permettant l'affichage des règles
def affichage_regles() -> NoReturn:
    print('\n==============================================================')
    print('=== Rappel des règles  :')
    print('== - La pierre écrase les ciseaux et gagne.')
    print('== - La feuille enveloppe la pierre et gagne.')
    print('== - Les ciseaux découpent la feuille et gagnent.')
    print('== ')
    print('=== Le premier joueur qui gagne 3 manches gagne la partie')
    print('==============================================================\n')


# Fonction permettant l'affichage des choix des joueurs
def affichage_choix(nom_j1: str, choix_j1: str, nom_j2: str, choix_j2: str) -> NoReturn:
    print('\n==============================================================')
    print(f'== - Choix {nom_j1} : {choix_j1}')
    print(f'== - Choix {nom_j2} : {choix_j2}')
    print('==============================================================\n')


# Fonction permettant l'affichage des scores
def affichage_score(nom_j1: str, nom_j2: str, score: List[int]) -> NoReturn:
    print('\n==============================================================')
    print(f'== - Score {nom_j1} : {score[0]}')
    print(f'== - Score {nom_j2} : {score[1]}')
    print('==============================================================\n')


# Fonction permettant l'affichage du gagnant
def affichage_gagnant(nom_j1: str, nom_j2: str, score: List[int]) -> NoReturn:
    if score[0] == 3:
        print(f'Bravo {nom_j1} vous gagnez la partie')
    else:
        print(f'Bravo {nom_j2} vous gagnez la partie')


# Fonction permettant de récupérer le choix du joueur
def saisie_joueur(nom_joueur: str) -> int:
    while True:
        saisie = input('> ' + nom_joueur + ' \n(1) - Pierre \n(2) - Feuille \n(3) - Ciseaux\nFaites votre choix : ')
        if saisie not in ["1", "2", "3"]:
            print('Proposition incorrecte, veuillez respecter le format souhaité')
        else:
            return int(saisie)
