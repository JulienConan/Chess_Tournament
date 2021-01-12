"""Module for Screen Class"""
# coding: utf-8

import os


class Screen:
    """ Class used for display informations on screen"""
    def __init__(self):
        pass

    def on_screen(self):
        """Print on screen self.text"""
        print("".join(self.text))

    def add_infos(self, infos):
        """Add text on self.text"""
        self.clear()
        self.text.append("\n")
        for info in infos:
            self.text.append(info)
        self.on_screen()

    def info_users(self, info):
        """Add info for bad user keystroke"""
        self.text = [data for data in info]
        self.on_screen()

    def clear(self):
        """Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_page(self):
        """Display main page"""
        self.clear()
        self.text = ["            CHESS TOURNAMENTS MANAGER             ",
                     "\n\n\n",
                     "[1] Gestion des joueurs",
                     "\n",
                     "[2] Lecture Rapports",
                     "\n",
                     "[3] Gestion des tournois",
                     "\n"]

        self.on_screen()

    def player_main_page(self):
        """Player actions main page"""
        self.clear()
        self.text = ["      GESTION DES JOUEURS",
                     "\n\n\n",
                     "[1] Créer un joueur",
                     "\n",
                     "[2] Modifier un joueur",
                     "\n",
                     "[3] Supprimer un joueur",
                     "\n"]
        self.on_screen()

    def reports_main(self):
        """Reports main page"""
        self.clear()
        self.text = ["          RAPPORTS             ",
                     "\n\n\n",
                     "[1] Liste des joueurs par ordre alphabétique",
                     "\n",
                     "[2] Liste des joueurs par classement",
                     "\n",
                     "[3] Liste des joueurs d'un tournoi par ordre alphabétique",
                     "\n",
                     "[4] Liste des joueurs d'un tournoi par classement",
                     "\n",
                     "[5] Liste de tous les tournois",
                     "\n",
                     "[6] Liste de tous les tours d'un tournoi",
                     "\n",
                     "[7] Liste de tous les matchs d'un tournoi",
                     "\n",
                     ]
        self.on_screen()

    def tournament_main_page(self):
        """Tournament main page"""
        self.clear()
        self.text = ["         GESTION DES TOURNOIS     ",
                     "\n\n\n",
                     "[1] Créer un tournoi",
                     "\n",
                     "[2] Charger un tournoi",
                     "\n",
                     "[3] Modifier un tournoi",
                     "\n"]
        self.on_screen()

    def tournaments_list(self):
        """Tournaments list page header"""
        self.clear()
        self.text = ["          LISTE DES TOURNOIS          ",
                     "\n\n\n"]
        self.on_screen()

    def new_tournament(self):
        """New tournament page header"""
        self.clear()
        self.text = ["          NOUVEAU TOURNOI         ",
                     "\n\n\n"]
        self.on_screen()

    def players_list(self, players_list="\n"):
        """Players list page header"""
        self.clear()
        self.text = ["              LISTE DES JOUEURS      ",
                     "\n\n\n"]
        self.on_screen()

    def tournament_result(self, infos):
        """Tournament result page header"""
        self.clear()
        self.text = ["          RESULTAT DU TOURNOI         ",
                     "\n\n\n"]
        self.add_infos(infos)

    def play(self):
        """Tournament on course page header"""
        self.clear()
        self.text = ["          TOURNOI EN COURS            ",
                     "\n\n\n"]
        self.on_screen()

    def matchs_list(self):
        """Matchs list page header"""
        self.clear()
        self.text = ["          LISTE DES MATCHS            ",
                     "\n\n\n"]
        self.on_screen()

    def rounds_list(self):
        """Rounds list page header"""
        self.clear()
        self.text = ["          LISTE DES ROUNDS            ",
                     "\n\n\n"]
        self.on_screen()
