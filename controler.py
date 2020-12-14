# coding: utf-8

from view import *
from tinydb import TinyDB, Query
from tinydb.operations import add
from time import strftime
from constants import *
from models import Tournament, Player

players_file = TinyDB('datas_base/players_file.json')
tournaments_file = TinyDB('datas_base/tournaments_file.json')
player_db = Query()
tournament_db = Query()

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
		ReportsControler()

	def new_tournament(self):
		TournamentControler()

class PlayerControler:
	def __init__(self):
		self.screen = Screen()
		self.screen.player_main_page()
		self.count = len(players_file.all())
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.create()
		elif menu == "2":
			pass
		elif menu == "3":
			pass
		elif menu == "h":
			MainControler()
		else : 
			print("Pas la bonne commande")

	def create(self):
		self.screen.player_main_page()
		self.player_dict = {}
		self.player_dict['player_id'] = self.count + 1
		self.player_dict['surname'] = input("Nom du Joueur : ").upper()
		self.player_dict['name'] = input("Prénom du Joueur : ").capitalize()
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
		self.player_dict['birthday'] = input("Date de naissance : ")
		self.player_dict['sexe'] = input("Sexe du joueur : ").capitalize()

		players_file.insert(self.player_dict)
		PlayerControler()


class TournamentControler:
	
	def __init__(self):
		self.screen = Screen()
		self.count = len(tournaments_file.all())
		self.screen.tournament_main_page()
		menu = input(" Rentrer le numéro de l'action à effectuer : ")
		if menu == "1":
			self.create()
		elif menu == "2":
			self.load()
		elif menu == "3":
			self.modify()
		elif menu == "h" or "H":
			MainControler()
		else : 
			print("La saisie ne fait pas partie des choix")
			#TournamentControler()

	def create(self):
		"""Create a new tournmanent"""
		self.count = len(tournaments_file.all())
		print("nb de tournoi : ", self.count)
		tournament = Query()
		self.screen.new_tournament()
		self.tournament_infos = {}
		self.tournament_infos['id'] = str(self.count + 1)
		self.tournament_infos['name'] = input("Nom du Tournoi : ")
		self.tournament_infos['location'] = input("Lieu du tournoi : ")
		self.tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
		self.tournament_infos['date_end'] = "on_course"
		self.tournament_infos['rounds_number'] = ROUNDS_NB
		self.tournament_infos['time_controler'] = input("Controleur de temps (blitz, bullet ou coup rapide) : ")
		self.tournament_infos['description'] = input("Description : ")
		self.tournament_infos['players_list'] = []
		self.tournament_infos['rounds_list'] = []

		while len(self.tournament_infos['players_list']) < 8:
			self.list_of_players('surname')
			print("{} joueurs ajoutés au tournoi".format(len(self.tournament_infos['players_list'])))
			new_player = input("Saisissez l'id du joueur à ajouter : ")
			self.tournament_infos['players_list'].append(Player(players_file.search(player_db.player_id == new_player)[0]))

		self.save(self.tournament_infos)
		print(" Le tournoi est initialisé.\n")

	def load(self):
		self.screen.tournaments_list()
		
		datas = ["ID   ",
				"NOM            ",
				"LIEU         ",
				"DATE DE DEBUT                        ",
				"DATE DE FIN                          ",
				"NOMDRE DE TOUR  ",
				"CONTROLEUR de TEMPS  ",
				"DESCRIPTION                                                                  ",
				"\n"]
		for tournament in tournaments_file.all():
			tournament_infos = [info for info in tournament.values()]
			for i in range(8):
				dif = len(datas[i]) - len(str(tournament_infos[i]))
				if dif < 0:
					datas.append(str(tournament_infos[i])[:(dif - 1)] + " ")
				elif dif > 0:
					datas.append(str(tournament_infos[i]) + dif * " " )
			datas.append("\n")
		self.screen.add_infos(datas)
		tournament_id = input(" veuillez saisir le numéro du tournoi à charger : ")
		self.play(tournament_id)


	def play(self, t_id):
		t = tournaments_file.search(tournament_db.id == t_id)

		print(t[0])
		tournament_on_course = Tournament(t[0])
		print(tournament_on_course)
		print(tournament_on_course.players_list)



	def save(self, tournament_infos):
		"""Save a tournament"""
		tournaments_file.insert(tournament_infos)

	def modify(self):
		self.screen.tournaments_list()
		for tournament in tournaments_file.all():
			print(tournament['id'],
				  tournament['name'], 
				  tournament['location'], 
				  tournament['date_start'])
		tournament = "0"
		while tournament not in range(1, self.count + 1):
			tournament = input("Saisissez le tournoi à modifier : ")
			try :
				tournament = int(tournament)
			except:
				print("Mauvais caractère")
	def list_of_players(self, key):
		self.screen.players_list()
		datas = ["ID  ",
				 "NOM             ",
				 "PRENOM          ",
				 "ELO RANKING     ",
				 "DATE DE NAISSANCE  ",
				 "SEXE             ",
				 "\n"]

		order = False
		if key == 'elo_ranking':
			order = True
		for player in sorted(players_file.all(), key=lambda item : item[key], reverse=order):
			player_infos = [info for info in player.values()]
			for i in range(6):
				dif = len(datas[i]) - len(str(player_infos[i]))
				if dif < 0:
					datas.append(str(player_infos[i])[:(dif - 1)] + " ")
				elif dif > 0:
					datas.append(str(player_infos[i]) + dif * " " )
			datas.append("\n")

		self.screen.add_infos(datas)

		
class ReportsControler:
	"""Controler for reports"""
	def __init__(self):
		self.screen = Screen()
		self.screen.reports_main()
		menu = input("Saisissez le numéro du rapport à afficher : ")
		if menu == "1":
			self.list_of_players('surname')
		elif menu == "2":
			self.list_of_players('elo_ranking')
		elif menu == "3":
			self.t_alpha_players_list()
		elif menu == "4":
			self.t_ranking_players_list()
		elif menu == "5":
			self.tournaments_list()
		elif menu == "6":
			self.rounds_list()
		elif menu == "7":
			self.matchs_list()
		elif menu == "h" or "H":
			MainControler()
		else : 
			print("La saisie ne fait pas partie des choix")
			#TournamentControler()

	def tournaments_list(self):
		self.screen.tournamens_list()
		datas = ["ID   ",
				"NOM            ",
				"LIEU         ",
				"DATE DE DEBUT                        ",
				"DATE DE FIN                          ",
				"NOMDRE DE TOUR  ",
				"CONTROLEUR de TEMPS  ",
				"DESCRIPTION                                                                  ",
				"\n"]
		for tournament in sorted(tournaments_file.all(), key=lambda item : item['id']):
			tournament_infos = [info for info in tournament.values()]
			for i in range(8):
				dif = len(datas[i]) - len(str(tournament_infos[i]))
				if dif < 0:
					datas.append(str(tournament_infos[i])[:(dif - 1)] + " ")
				elif dif > 0:
					datas.append(str(tournament_infos[i]) + dif * " " )
			datas.append("\n")
		self.screen.add_infos(datas)
		menu = ""
		while menu != "h" :
			menu = input("Saisissez 'h' pour revenir au menu principale : ").lower()
		MainControler()

	def list_of_players(self, key):
		self.screen.players_list()
		datas = ["ID  ",
				 "NOM             ",
				 "PRENOM          ",
				 "ELO RANKING     ",
				 "DATE DE NAISSANCE  ",
				 "SEXE             ",
				 "\n"]

		order = False
		if key == 'elo_ranking':
			order = True
		for player in sorted(players_file.all(), key=lambda item : item[key], reverse=order):
			player_infos = [info for info in player.values()]
			for i in range(6):
				dif = len(datas[i]) - len(str(player_infos[i]))
				if dif < 0:
					datas.append(str(player_infos[i])[:(dif - 1)] + " ")
				elif dif > 0:
					datas.append(str(player_infos[i]) + dif * " " )
			datas.append("\n")

		self.screen.add_infos(datas)
		menu = ""
		while menu != "h" :
			menu = input("Saisissez 'h' pour revenir au menu principale : ").lower()
		MainControler()
