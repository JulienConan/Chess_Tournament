# coding: utf-8

from view import *
from tinydb import TinyDB, Query
from tinydb.operations import add
from time import strftime
from models import constants
from models.tournament import Tournament

players_db = TinyDB('datas_base/players_file.json')
tournaments_db = TinyDB('datas_base/tournaments_file.json')
player_db = Query()
tournament_db = Query()

class MainControler:
    def __init__(self):
        self.screen = Screen()
        self.screen.main_page()
        menu = input("Rentrer le numéro de l'action à effectuer : ")
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
        self.count = len(players_db.all())
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

        players_db.insert(self.player_dict)
        PlayerControler()


class TournamentControler:
    
    def __init__(self):
        self.screen = Screen()
        self.count = len(tournaments_db.all())
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
        self.count = len(tournaments_db.all())
        print("nb de tournoi : ", self.count)
        tournament = Query()
        self.screen.new_tournament()
        self.tournament_infos = {}
        self.tournament_infos['id'] = (self.count + 1)
        self.tournament_infos['name'] = input("Nom du Tournoi : ")
        self.tournament_infos['location'] = input("Lieu du tournoi : ")
        self.tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
        self.tournament_infos['date_end'] = "on_course"
        self.tournament_infos['total_round'] = ROUNDS_NB
        self.tournament_infos['time_controler'] = input("Controleur de temps (blitz, bullet ou coup rapide) : ")
        self.tournament_infos['description'] = input("Description : ")
        self.tournament_infos['players_list'] = []
        self.tournament_infos['rounds_list'] = []

        while len(self.tournament_infos['players_list']) < 8:
            self.list_of_players('surname')
            print("{} joueurs ajoutés au tournoi".format(len(self.tournament_infos['players_list'])))
            id_player = input("Saisissez l'id du joueur à ajouter : ")
            self.tournament_infos['players_list'].append(players_db.search(player_db.player_id == id_player)[0])

        tournament = Tournament(self.tournament_infos)
        self.save(tournament)
        self.play(tournament)

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
        for tournament in tournaments_db.all():
            tournament_infos = [info for info in tournament.values()]
            for i in range(8):
                dif = len(datas[i]) - len(str(tournament_infos[i]))
                if dif < 0:
                    datas.append(str(tournament_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(tournament_infos[i]) + dif * " " )
            datas.append("\n")
        self.screen.add_infos(datas)
        tournament_id = int(input(" veuillez saisir le numéro du tournoi à charger : "))
        tournaments_load = tournaments_db.search(tournament_db.id == tournament_id)[0]

        tournament_load = Tournament(tournaments_db.search(tournament_db.id == tournament_id)[0])
        self.play(tournament_load)

    def deserialized(self, tournament):
        deserialized_players = [Player(player) for player in tournament['players_list']]
        deserialized_rounds = []
        for rounds in tournament['rounds_list']:
            rounds.insert(1, deserialized_players)
            deserialized_match = []
            for match in rounds[5]:
                for player in deserialized_players:
                    if player.player_id == match[2][0]:
                        player1 = player 
                    elif player.player_id == match[3][0]:
                        player2 = player
                deserialized_match.append(Match(match[0], player1, player2, match[2][1], match[3][1]))





    def play(self, tournament):
        
        tournament_infos_list = [tournament.name, "\n",
                                 "Lieu : ", tournament.location, "\n",
                                 "Début du tournoi : ", tournament.date_start, "\n"]

        while tournament.round < 4:
            tournament.create_round()
            while tournament.rounds_list[-1].date_end == 'On course':
                self.screen.play()
                self.screen.add_infos(tournament_infos_list)
                round_infos = [str(tournament.rounds_list), "\n"]
                for match in tournament.rounds_list[-1].matchs_list:
                    round_infos.append(str(match))
                    round_infos.append("\n")
                self.screen.add_infos(round_infos)
                print(tournament.rounds_list)
                match_index = int(input("Pour quel match voulez vous rentrer les résultats : "))
                if match_index > TOURNAMENT_PLAYERS_NB/2 :
                    print("Le numéro du match doit être compris entre 1 et 4 ")
                elif tournament.rounds_list[-1].matchs_list[match_index -1].statement == "Validé":
                    print("Match déjà joué.")
                else:
                    score_p1 = int(input("Rentrez le score du joueur 1 : "))
                    score_p2 = int(input("Rentrez le score du joueur 2 : "))
                    tournament.rounds_list[-1].validate_match(match_index, score_p1, score_p2)
                self.save(tournament)
            
        tournament.date_end = strftime("%A %d %B %Y %H:%M:%S")       
        self.save(tournament)

        tournament.players_list = sorted(tournament.players_list, key= lambda player : player.elo_ranking)
        tournament.players_list = sorted(tournament.players_list, key = lambda player : player.tournament_score, reverse = True)
        self.result(tournament)   

    def result(self, tournament):
        tournament_result = ["Classement  ",
                            "NOM          ",
                            "PRENOM       ",
                            "SCORE        ",
                            "\n\n"]
        t_rank = 1 
        for player in tournament.players_list:
            player_infos = []
            player_infos.append(str(t_rank))
            player_infos.append(player.surname)
            player_infos.append(player.name)
            player_infos.append(str(player.tournament_score))
            for i in range(4):
                dif = len(tournament_result[i]) - len(player_infos[i])
                if dif < 0:
                    tournament_result.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    tournament_result.append(str(player_infos[i]) + dif * " " )
            tournament_result.append("\n")
            t_rank += 1

        self.screen.tournament_result(tournament_result)





    def save(self, tournament):
        tournament_serialized = tournament.serialized()
        if tournaments_db.search(tournament_db.id == []):
            tournaments_db.insert(tournament_serialized)
        else :
            tournaments_db.remove(tournament_db.id == tournament_serialized['id'])
            tournaments_db.insert(tournament_serialized)
        


    def modify(self):
        self.screen.tournaments_list()
        for tournament in tournaments_db.all():
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
        for player in sorted(players_db.all(), key=lambda item : item[key], reverse=order):
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
        for tournament in sorted(tournaments_db.all(), key=lambda item : item['id']):
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
        for player in sorted(players_db.all(), key=lambda item : item[key], reverse=order):
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
