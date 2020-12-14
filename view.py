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
					 "[3] Modifier un tournoi",
					 "\n",
					 "[h] Retourner au menu principale",
					 "\n"
					 ]
		self.on_screen()

	def tournaments_list(self) :
		self.clear()
		self.text = ["			Liste des tournois			",
					"\n\n\n"]
		self.on_screen()

	def new_tournament(self):
		self.clear()
		self.text = ["			Nouveau Tournoi          ",
					"\n\n\n"]
		self.on_screen()

	def add_infos(self,infos):
		self.clear()
		self.text.append("\n")
		for info in infos:
			self.text.append(info)
		self.on_screen()

	def players_list(self, players_list="\n") :
		self.clear()
		self.text = ["				Liste des joueurs		",
					"\n\n\n"]
		self.on_screen()

	def tournaments_list(self, players_list="\n") :
		self.clear()
		self.text = ["				Liste des tournois		",
					"\n\n\n"]
		self.on_screen()

	def play(self):
		self.clear()
		self.text



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
					 "[h] Retourner au menu précédent",
					 "\n"
					 ]
		self.on_screen()

	def on_screen(self):
		print("".join(self.text))

	def update(self):
		pass

	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def reports_main(self):
		self.clear()
		self.text = ["			Reports 			",
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
					 "[6] Liste de tous les tours d'un tournois",
					 "\n",
					 "[7] Liste de tous les matchs d'un tournoi",
					 "\n",
					 ]
		self.on_screen()