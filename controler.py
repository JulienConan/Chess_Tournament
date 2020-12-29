# coding: utf-8

from view import *
from tinydb import TinyDB, Query
from time import strftime
import time
from models.constants import ROUNDS_NB, TOURNAMENT_PLAYERS_NB
from models.tournament import Tournament


players_db = TinyDB('models/datas_base/players_file.json')
tournaments_db = TinyDB('models/datas_base/tournament_file.json')
p_query = Query()
t_query = Query()


def input_menu_vérifcation(index, message):
    """Fonction vérifiant si la saisie d'un menu est valide"""
    saisie = input(message)
    try:
        saisie = int(saisie)
        if saisie in range(1, (index + 1)):
            return saisie
        else:
            print("La saisie daoit être comprise entre 1 et {}".format(index))
            return input_menu_vérifcation(index, message)
    except ValueError:
        saisie = saisie.lower()
        if saisie == 'h':
            MainControler()
        else:
            print("La saisie doit être un chiffre compris entre 1 et {}"
                .format(index))
            return input_menu_vérifcation(index, message)


class MainControler:
    def __init__(self):
        self.screen = Screen()
        self.screen.main_page()
        self.menu_index = 3
        menu = input_menu_vérifcation(self.menu_index, " Saisissez le numéro du menu désiré : ")

        if menu == 1:
            self.player_action()
        elif menu == 2:
            self.reports()
        elif menu == 3:
            self.new_tournament()       

    def player_action(self):
        player_a = PlayerControler()
        player_a.main()

    def reports(self):
        report = ReportsControler()
        report.main()

    def new_tournament(self):
        TournamentControler()


class PlayerControler:
    def __init__(self):
        self.screen = Screen()
        
    def main(self):
        self.screen.player_main_page()
        self.count = len(players_db.all())
        menu = input_menu_vérifcation(3, "Saisissez le numéro de l'action désirée :")
        if menu == 1:
            self.create()
        elif menu == 2:
            self.modify()
        elif menu == 3:
            pass

    def create(self):
        self.screen.player_main_page()
        self.player_dict = {}
        self.player_dict['player_id'] = self.count + 1
        self.player_dict['surname'] = input("Nom du Joueur: ").upper()
        self.player_dict['name'] = input("Prénom du Joueur : ").capitalize()
        self.player_dict['ranking'] = int(-1)
        while self.player_dict['ranking'] < 0:
            try:
                r = int(input("Classement du joueur: "))
                if r < 0:
                    print("le classement doit être supérieur à 0")
                else:
                    self.player_dict['ranking'] = r
            except:
                print("le classement doit être un chiffre supérieur ou égal à 0")
                pass
        self.player_dict['birthday'] = input("Date de naissance : ")
        self.player_dict['sexe'] = input("Sexe du joueur : ").capitalize()

        players_db.insert(self.player_dict)
        PlayerControler()

    def modify(self):
        report = ReportsControler()
        report.list_of_players('surname')
        id_player = input_menu_vérifcation(players_db.__len__(), "Saisissez le numéro du joueur à modifier :")
                
        print("Choix de la modification :\n",
                    "           [1] Nom \n",
                    "           [2] Prénom \n",
                    "           [3] Classement \n",
                    "           [4] Date de naissance \n",
                    "           [5] Sexe \n")
        modify = input_menu_vérifcation(5, " Saisissez le numéro de la donnée à modifier :")
        info_modify = input("Saisissez la modification :")
        if modify == 1 :
            key = 'surname'   
        if modify == 2 :
            key = 'name'
        if modify == 3 :
            key = 'elo_ranking'
            info_modify = int(info_modify)
        if modify == 4 :
            key = 'birthday'
        if modify == 5 :
            key = 'sexe'

        players_db.update({key : info_modify}, p_query.player_id == str(modify)) 


class TournamentControler:
    
    def __init__(self):
        self.screen = Screen()
        self.count = len(tournaments_db.all())
        self.screen.tournament_main_page()
        menu = input_menu_vérifcation(3, " Saisissez le menu désiré : ")

        if menu == 1:
            self.create()
        elif menu == 2:
            self.load()
        elif menu == 3:
            self.modify()

    def create(self):
        """Create a new tournmanent"""
        self.count = len(tournaments_db.all())
        print("nb de tournoi : ", self.count)
        tournament = Query()
        self.screen.new_tournament()
        self.tournament_infos = {}
        self.tournament_infos['id'] = str(self.count + 1)
        self.tournament_infos['name'] = input("Nom du Tournoi : ")
        self.tournament_infos['location'] = input("Lieu du tournoi : ")
        self.tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
        self.tournament_infos['date_end'] = "on_course"
        self.tournament_infos['total_round'] = ROUNDS_NB
        print("Choix du controleur de temps :\n",
                    "           [1] Blitz \n",
                    "           [2] Bullet \n",
                    "           [3] Coup Rapide \n")
        controler_saisie = input_menu_vérifcation(3, "Veuillez saisir le numéro correspondant à votre choix : ")
        
        if controler_saisie == 1:
            self.tournament_infos['time_controler'] = "Blitz"
        elif controler_saisie == 2:
            self.tournament_infos['time_controler'] = "Bullet"
        elif controler_saisie == 3:
            self.tournament_infos['time_controler'] = "Coup rapide"

        self.tournament_infos['description'] = input("Description : ")
        self.tournament_infos['players_list'] = []
        self.tournament_infos['rounds_list'] = []

        players_on_course = []
        while len(self.tournament_infos['players_list']) < 8:
            self.list_of_players()
            print("{} joueurs ajoutés au tournoi".format(len(self.tournament_infos['players_list'])))
            id_player = input_menu_vérifcation(players_db.__len__(), "Entrez le numéro du joueur à ajouter au tournoi : ")
            while id_player in players_on_course:
                print("Le joueur {} est déjà inscrit dans ce tournoi".format(id_player))
                id_player = input_menu_vérifcation(players_db.__len__(), "Entrez le numéro du joueur à ajouter au tournoi : ")
            players_on_course.append(id_player)
            self.tournament_infos['players_list'].append(players_db.search(p_query.player_id == str(id_player))[0])

        tournament = Tournament(self.tournament_infos)
        tournament.save(tournaments_db)
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

        tournament_id = input(
            " veuillez saisir le numéro du tournoi à charger : ")
        tournament = Tournament(
            tournaments_db.search(t_query.id == tournament_id)[0])
        tournament.deserialized()
        tournament.save(tournaments_db)
        self.play(tournament)
    
    def play(self, tournament):
        tournament_infos_list = [tournament.name, "\n",
                                 "Lieu : ",
                                 tournament.location, "\n",
                                 "Début du tournoi : ",
                                 tournament.date_start, "\n"]

        if tournament.round != 0:
            while tournament.rounds_list[-1].date_end == 'On course':
                self.screen.play()
                self.screen.add_infos(tournament_infos_list)
                round_infos = [str(tournament.rounds_list[-1]), "\n"]
                for match in tournament.rounds_list[-1].matchs_list:
                    round_infos.append(str(match))
                    round_infos.append("\n")
                self.screen.add_infos(round_infos)
                match_index = input_menu_vérifcation(int(TOURNAMENT_PLAYERS_NB/2), "Pour quel match voulez vous rentrer les résultats : ")
                if tournament.rounds_list[-1].matchs_list[match_index-1].statement == "Validé":
                    print("Match déjà joué.")
                    time.sleep(1)
                else:
                    score_p1 = int(input("Rentrez le score du joueur 1 : "))
                    score_p2 = int(input("Rentrez le score du joueur 2 : "))
                    tournament.rounds_list[-1].validate_match(
                        match_index, score_p1, score_p2)
                tournament.save(tournaments_db)


        while tournament.round < 4:
            tournament.create_round()
            tournament.save(tournaments_db)

            while tournament.rounds_list[-1].date_end == 'On course':
                self.screen.play()
                self.screen.add_infos(tournament_infos_list)
                round_infos = [str(tournament.rounds_list[-1]), "\n"]
                for match in tournament.rounds_list[-1].matchs_list:
                    round_infos.append(str(match))
                    round_infos.append("\n")
                self.screen.add_infos(round_infos)
                match_index = input_menu_vérifcation(int(TOURNAMENT_PLAYERS_NB/2), "Pour quel match voulez vous rentrer les résultats : ")
                if tournament.rounds_list[-1].matchs_list[match_index-1].statement == "Validé":
                    print("Match déjà joué.")
                    time.sleep(1)       
                else:
                    score_p1 = int(input("Rentrez le score du joueur 1 : "))
                    score_p2 = int(input("Rentrez le score du joueur 2 : "))
                    tournament.rounds_list[-1].validate_match(
                        match_index, score_p1, score_p2)
                tournament.save(tournaments_db)
            
        tournament.date_end = strftime("%A %d %B %Y %H:%M:%S")       
        tournament.save(tournaments_db)

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

    def list_of_players(self):
        report = ReportsControler()
        report.list_of_players('surname')
        
class ReportsControler:
    """Controler for reports"""
    def __init__(self):
        self.screen = Screen()

    def main(self):
        self.screen.reports_main()
        self.menu_index = 7
        menu = input_menu_vérifcation(self.menu_index)
        if menu == 1:
            self.list_of_players('surname')
        elif menu == 2:
            self.list_of_players('elo_ranking')
        elif menu == 3:
            self.t_players_list('surname')
        elif menu == 4:
            self.t_players_list('elo_ranking')
        elif menu == 5:
            self.tournaments_list()      
        elif menu == 6:
            self.tournament_rounds_list()
        elif menu == 7:
            self.tournament_matchs_list()
        self.go_back()

    def go_back(self):
        menu = ""
        while menu != "h":
            menu = input(
            "Saisissez 'h' pour revenir au menu principale : ").lower()
        MainControler()

    def tournaments_list(self):
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
        for tournament in sorted(tournaments_db.all(),
                                 key=lambda item: item['id']):
            tournament_infos = [info for info in tournament.values()]
            for i in range(8):
                dif = len(datas[i]) - len(str(tournament_infos[i]))
                if dif < 0:
                    datas.append(str(tournament_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(tournament_infos[i]) + dif * " ")
            datas.append("\n")
        self.screen.add_infos(datas)

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
        for player in sorted(players_db.all(),
                             key=lambda item: item[key],
                             reverse=order):
            player_infos = [info for info in player.values()]
            for i in range(6):
                dif = len(datas[i]) - len(str(player_infos[i]))
                if dif < 0:
                    datas.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(player_infos[i]) + dif * " ")
            datas.append("\n")

        self.screen.add_infos(datas)
        
    def t_players_list(self, key):
        order = False
        if key == 'elo_ranking':
            order = True
        self.tournaments_list()
        tournament_index = str(input_menu_vérifcation(30))
        tournaments_players = tournaments_db.search(t_query.id == tournament_index)[0]['players_list']
        self.screen.players_list()
        datas = ["ID  ",
                 "NOM             ",
                 "PRENOM          ",
                 "ELO RANKING     ",
                 "DATE DE NAISSANCE  ",
                 "SEXE             ",
                 "\n"]
        for player in sorted(tournaments_players, key=lambda item: item[key], reverse = order):
            player_infos = [info for info in player.values()]
            for i in range(6):
                dif = len(datas[i]) - len(str(player_infos[i]))
                if dif < 0:
                    datas.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(player_infos[i]) + dif * " ")
            datas.append("\n")

        self.screen.add_infos(datas)

    def tournament_rounds_list(self):
        self.tournaments_list()
        tournament_index = str(input_menu_vérifcation(30))
        tournaments_rounds = tournaments_db.search(t_query.id == tournament_index)[0]['rounds_list']
        self.screen.rounds_list()
        datas = ["Round  ",
                 "Date de début             ",
                 "Date de fin         ",
                 "Nombre de matchs validés   ",
                 "\n"]
        for rounds in tournaments_rounds:
            for i in range(4):
                dif = len(datas[i]) - len(str(rounds[i]))
                if dif < 0:
                    datas.append(str(rounds[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(rounds[i]) + dif * " ")
            datas.append("\n")
        self.screen.add_infos(datas)

    def tournament_matchs_list(self):
        self.tournaments_list()
        tournament_index = str(input_menu_vérifcation(30))
        tournament = Tournament(
            tournaments_db.search(t_query.id == tournament_index)[0])
        tournament.deserialized()

        self.screen.matchs_list()
        tournament_infos = [tournament.name, "\n"]
        self.screen.add_infos(tournament_infos)
        for rounds in tournament.rounds_list:
            print(rounds,"\n")
            for match in rounds.matchs_list:
                print(match)
            print("\n")
