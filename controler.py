# coding: utf-8

from view import *
from tinydb import TinyDB, Query
from time import strftime
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
			self.reports()
		elif menu == "3":
			self.new_tournament()


	def player_action(self):
		PlayerControler()

	def reports(self):
		Reports()

	def new_tournament(self):
		TournamentControler()

class PlayerControler:
	def __init__(self):
		self.screen = Screen()
		self.screen.player_main_page()
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.create()
		elif menu == "2":
			pass
		elif menu == "3":
			pass
		elif menu == "4":
			MainControler()

	def create(self):
		self.screen.player_main_page()
		self.player_dict = {}
		self.player_dict['surname'] = input("Nom du Joueur : ")
		self.player_dict['name'] = input("Prénom du Joueur : ")
		self.player_dict['birthday'] = input("Age du Joueur : ")
		self.player_dict['sexe'] = input("Sexe du joueur : ")
		self.player_dict['ranking'] = int(-1)
		while self.player_dict['ranking'] < 0:
			try :
				r = int(input("Classement du joueur : "))
				if r < 0 :
					print("le classement doit être supérieur à 0")
				else :
					self.player_dict['ranking'] = r
			except :
				print("le classement doit être un chiffre supérieur ou égal à 0")
				pass

		db.table(ACTORS_TABLE).insert(self.player_dict)


class TournamentControler:
	def __init__(self):
		self.screen = Screen()
		self.screen.tournament_main_page()
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.create()
		elif menu == "2":
			pass
		elif menu == "3":
			MainControler()

	def create(self):
		self.screen.tournament_on_course()
		self.tournament_infos = {}
		self.tournament_infos['name'] = input("Nom du Tournoi")
		self.tournament_infos['location'] = input("Lieu du tournoi")
		self.tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
		self.tournament_infos['date_end'] = "on_course"
		self.tournament_infos['rounds_number'] = ROUNDS_NB
		self.tournament_infos['rounds_list'] = []
		self.tournament_infos['players_list'] = []
		self.tournament_infos['time_controler'] = input("Controleur de temps :")
		self.tournament_infos['description'] = input("Description")