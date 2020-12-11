# coding: utf-8

from view import *
from tinydb import TinyDB, Query
from constants import *

db = TinyDB('datas_base/db.json')

class MainControler:
	def __init__(self):
		self.screen = Screen()
		self.screen.main_page()
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.player_action()
		elif menu == "2":
			self.menu()
		elif menu == "3":
			self.menu()
		elif menu == "4":
			self.menu()

	def player_action(self):
		PlayerControler()

	def reports(self):
		pass

	def create_tournament(self):
		pass

	def load_tournaments(self): 
		pass


class PlayerControler:
	def __init__(self):
		self.screen = Screen()
		self.screen.main_player_page()
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.create()
		elif menu == 2:
			pass
		elif menu == 3:
			pass
		elif menu == 4:
			MainControler()

	def create(self):
		self.screen.main_player_page()
		self.player_dict = {}
		self.player_dict['surname'] = input("Nom du Joueur : ")
		self.player_dict['name'] = input("Prénom du Joueur : ")
		self.player_dict['birthday'] = input("Age du Joueur : ")
		self.player_dict['sexe'] = input("Sexe du joueur : ")
		self.player_dict['ranking'] = int(-1)
		while self.player_dict['ranking'] < 0:
			try :
				r = int(input("Classement du joueur : "))
				self.player_dict['ranking'] = r
			except :
				print("le classement doit être un chiffre supérieur ou égal à 0")
				pass


		db.table(ACTORS_TABLE).insert(self.player_dict)



			




if __name__ == "__main__":
	m = MainControler()