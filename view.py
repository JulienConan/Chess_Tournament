# coding: utf-8
from time import sleep
import os

class Screen:
	def __init__(self):
		pass

	def main_page(self):
		os.system('clear')
		self.text = ["			GESTIONNAIRE DE TOURNOI					",
					"\n\n\n",
					"[1] Gestion des joueurs",
					"\n",
					"[2] Lecture Rapports",
					"\n",
					"[3] Création d'un tournoi",
					"\n",
					"[4] Chargement d'un tournoi",
					"\n"]

		self.on_screen()

	def tournament(self):
		self.text = ["			Nouveau tournoi			"]

	def main_player_page(self):
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
		os.system('clear')