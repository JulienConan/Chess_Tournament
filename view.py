# coding: utf-8
from time import sleep
import os

class Screen:
	def __init__(self):
		pass

	def main_page(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.text = ["			GESTIONNAIRE DE TOURNOI					",
					"\n\n\n",
					"[1] Gestion des joueurs",
					"\n",
					"[2] Lecture Rapports",
					"\n",
					"[3] Gestion des tournois",
					"\n"]

		self.on_screen()

	def tournament_main_page(self):
		self.clear()
		self.text = ["			TOURNOI		",
					 "\n\n\n",
					 "[1] Créer un tournoi",
					 "\n",
					 "[2] Charger un tournoi",
					 "\n",
					 "[3] Retourner au menu précédent",
					 "\n"
					 ]
		self.on_screen()

	def tournament_on_course(self):
		self.clear()
		self.text = ["			Nouveau Tournoi          ",
					"\n\n\n"]
		self.on_screen()

	def player_main_page(self):
		self.clear()
		self.text = ["		Gestion des joueurs",
					 "\n\n\n",
					 "[1] Créer un joueur",
					 "\n",
					 "[2] Modifier un joueur",
					 "\n",
					 "[3] Supprimer un joueur",
					 "\n",
					 "[4] Retourner au menu précédent",
					 "\n"
					 ]
		self.on_screen()

	def on_screen(self):
		print("".join(self.text))

	def update(self):
		pass

	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')