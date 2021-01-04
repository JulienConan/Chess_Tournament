"""Module for controler
# coding: utf-8

Attributes:
    p_query (TYPE): Query for players database
    players_db (TYPE): Database for players
    t_query (TYPE): Query for tournaments database
    tournaments_db (TYPE): Database for tournaments
"""

from time import strftime
import time
from sys import exit
from tinydb import TinyDB, Query
from view import Screen
from models.constants import ROUNDS_NB, TOURNAMENT_PLAYERS_NB
from models.tournament import Tournament


players_db = TinyDB('models/datas_base/players_file.json')
tournaments_db = TinyDB('models/datas_base/tournament_file.json')
p_query = Query()
t_query = Query()


def input_menu_verification(index, message):
    """Verification for user keystroke

    Args:
        index (int): Number of possibilities
        message (str): message for the display
    """
    saisie = input(
        message + " (h pour revenir au menu principale ou q pour quitter le programme) : ")
    try:
        saisie = int(saisie)
        if saisie in range(1, (index + 1)):
            return saisie
        else:
            print("La saisie doit être comprise entre 1 et {}.".format(index))
            return input_menu_verification(
                index, message)
    except ValueError:
        saisie = saisie.lower()
        if saisie == 'h':
            MainControler()
        elif saisie == 'q':
            exit()
        else:
            print("La saisie doit être un chiffre compris entre 1 et {}."
                  .format(index))
            return input_menu_verification(index, message)


class MainControler:
    """Main controler

    Attributes:
        screen (object): Display for main menu
    """

    def __init__(self):
        self.screen = Screen()
        self.screen.main_page()
        menu = input_menu_verification(3, "Saisissez le numéro du menu désiré")

        if menu == 1:
            self.player_action()
        elif menu == 2:
            self.reports()
        elif menu == 3:
            self.new_tournament()

    def player_action(self):
        """Go to player actions menu"""
        player_a = PlayerControler()
        player_a.main()

    def reports(self):
        """Go to reports menu"""
        report = ReportsControler()
        report.main()

    def new_tournament(self):
        """Create a new tournament"""
        TournamentControler()


class PlayerControler:

    """Player controler

    Attributes:
        count (int): Number of players in database
        player_dict (dict): Dictionnary contains player info
        screen (object): Description
    """

    def __init__(self):
        self.screen = Screen()

    def main(self):
        """Main menu for player action"""
        self.screen.player_main_page()
        self.count = len(players_db.all())
        menu = input_menu_verification(
            3, "Saisissez le numéro de l'action désirée")
        if menu == 1:
            self.create()
        elif menu == 2:
            self.modify()
        elif menu == 3:
            self.delete()

    def create(self):
        """Create a player"""
        self.screen.player_main_page()
        self.player_dict = {}
        self.player_dict['player_id'] = self.count + 1
        self.player_dict['surname'] = input("Nom du Joueur: ").upper()
        self.player_dict['name'] = input("Prénom du Joueur : ").capitalize()
        self.player_dict['elo_ranking'] = int(-1)
        while self.player_dict['ranking'] < 0:
            try:
                r = int(input("Classement du joueur: "))
                if r < 0:
                    print("le classement doit être supérieur à 0")
                else:
                    self.player_dict['ranking'] = r
            except ValueError:
                print("le classement doit être un chiffre supérieur ou égal à 0")
        self.player_dict['birthday'] = input("Date de naissance : ")
        self.player_dict['sexe'] = input("Sexe du joueur : ").capitalize()

        players_db.insert(self.player_dict)
        self.main()

    def modify(self):
        """Modify a player info"""
        report = ReportsControler()
        report.list_of_players('player_id')
        id_player = input_menu_verification(
            players_db.__len__(), "Saisissez le numéro du joueur à modifier")

        print("Choix de la modification :\n",
              "           [1] Nom \n",
              "           [2] Prénom \n",
              "           [3] Classement \n",
              "           [4] Date de naissance \n",
              "           [5] Sexe \n")
        modify = input_menu_verification(
            5, "Saisissez le numéro de la donnée à modifier")
        info_modify = input("Saisissez la modification : ")
        if modify == 1:
            key = 'surname'
            info_modify = info_modify.upper()
        if modify == 2:
            key = 'name'
            info_modify = info_modify.capitalize()
        if modify == 3:
            key = 'elo_ranking'
            try:
                info_modify = int(info_modify)
            except ValueError:
                info_modify = input_menu_verification(100000000,
                                                      "Le classement doit être chiffre positif")
        if modify == 4:
            key = 'birthday'
        if modify == 5:
            info_modify = info_modify.capitalize()
            key = 'sexe'

        players_db.update({key: info_modify}, p_query.player_id == id_player)
        self.modify()

    def delete(self):
        """Delete a player"""
        report = ReportsControler()
        report.list_of_players('player_id')
        id_player = input_menu_verification(
            players_db.__len__(), "Saisissez le numéro du joueur à effacer")
        players_db.remove(p_query.player_id == id_player)
        self.delete()


class TournamentControler:
    """Tournament controler

    Attributes:
        count (int): Number of tournament in database
        screen (object): display for tournament controler
        tournament_infos (dict): Dictionnary contains infos for a tournament
    """

    def __init__(self):
        self.screen = Screen()
        self.count = len(tournaments_db.all())
        self.screen.tournament_main_page()
        menu = input_menu_verification(3, "Saisissez le menu désiré")

        if menu == 1:
            self.create()
        elif menu == 2:
            self.load()
        elif menu == 3:
            self.modify()

    def create(self):
        """Create a new tournmanent"""
        print("nb de tournoi : ", self.count)
        tournament = Query()
        self.screen.new_tournament()
        self.tournament_infos = {}
        self.tournament_infos['id'] = self.count + 1
        self.tournament_infos['name'] = input("Nom du Tournoi : ")
        self.tournament_infos['location'] = input("Lieu du tournoi : ")
        self.tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
        self.tournament_infos['date_end'] = "on_course"
        self.tournament_infos['total_round'] = ROUNDS_NB
        print("Choix du controleur de temps :\n",
              "           [1] Blitz \n",
              "           [2] Bullet \n",
              "           [3] Coup Rapide \n")
        controler_saisie = input_menu_verification(
            3, "Veuillez saisir le numéro correspondant à votre choix")

        if controler_saisie == 1:
            self.tournament_infos['time_controler'] = "Blitz"
        elif controler_saisie == 2:
            self.tournament_infos['time_controler'] = "Bullet"
        elif controler_saisie == 3:
            self.tournament_infos['time_controler'] = "Coup rapide"

        self.tournament_infos['description'] = input("Description : ")
        self.tournament_infos['players_list'] = []
        self.tournament_infos['rounds_list'] = []

        self.tournament = Tournament(self.tournament_infos)
        players_on_course = []
        while len(self.tournament_infos['players_list']) < 8:
            report = ReportsControler()
            report.list_of_players('player_id')
            print("{} joueurs ajoutés au tournoi".format(
                len(self.tournament_infos['players_list'])))
            id_player = input_menu_verification(
                players_db.__len__(), "Entrez le numéro du joueur à ajouter au tournoi")
            while id_player in players_on_course:
                print("Le joueur {} est déjà inscrit dans ce tournoi".format(id_player))
                id_player = input_menu_verification(
                    players_db.__len__(), "Entrez le numéro du joueur à ajouter au tournoi")
            players_on_course.append(id_player)
            try:
                self.tournament_infos['players_list'].append(
                players_db.search(p_query.player_id == id_player)[0])
            except IndexError:
                print("Le joueur {} n'existe pas.".format(id_player))
                time.sleep(1)
        self.tournament = Tournament(self.tournament_infos)

        self.play()

    def load(self):
        """Load a tournament"""
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
                    datas.append(str(tournament_infos[i]) + dif * " ")
            datas.append("\n")
        self.screen.add_infos(datas)

        tournament_id = input_menu_verification(tournaments_db.__len__(),
                                                "Saisissez le numéro du tournoi à charger")
        self.tournament = Tournament(
            tournaments_db.search(t_query.id == tournament_id)[0])
        self.tournament.deserialized()
        self.play()

    def play(self):
        """Play a tournament

        Args:
            tournament (object): Tournament object
        """
        tournament_infos_list = [self.tournament.name, "\n",
                                 "Lieu : ",
                                 self.tournament.location, "\n",
                                 "Début du tournoi : ",
                                 self.tournament.date_start, "\n"]

        while self.tournament.round < 4:
            if self.tournament.rounds_list == [] or self.tournament.rounds_list[-1].date_end != 'On course':
                self.tournament.create_round()
                self.tournament.save(tournaments_db)
            while self.tournament.rounds_list[-1].date_end == 'On course':
                self.screen.play()
                self.screen.add_infos(tournament_infos_list)
                round_infos = [str(self.tournament.rounds_list[-1]), "\n\n"]
                for match in self.tournament.rounds_list[-1].matchs_list:
                    round_infos.append(str(match))
                    round_infos.append("\n")
                self.screen.add_infos(round_infos)
                self.actions()
                self.tournament.save(tournaments_db)

        if self.tournament.date_end == 'on_course':
            self.tournament.date_end = strftime("%A %d %B %Y %H:%M:%S")
            self.tournament.save(tournaments_db)

        self.tournament.players_list = sorted(
            self.tournament.players_list, key=lambda player: player.elo_ranking)
        self.tournament.players_list = sorted(
            self.tournament.players_list, key=lambda player: player.tournament_score, reverse=True)
        self.result()
        input_menu_verification(1, "")

    def actions(self):
        self.screen.add_infos(["Actions possibles :\n",
                               "            [1] Saisir le score d'un match\n",
                               "            [2] Modifiez le classement d'un joueur\n"])
        choice = input_menu_verification(
            2, "Saisissez le numéro de l'action souhaitée")
        if choice == 1:
            self.update_score()
        elif choice == 2:
            self.modify_ranking_players()

    def update_score(self):
        match_index = input_menu_verification(int(TOURNAMENT_PLAYERS_NB / 2),
                                              "Pour quel match voulez vous rentrer les résultats")
        if self.tournament.rounds_list[-1].matchs_list[match_index - 1].statement == "Validé":
            print("Match déjà joué.")
            time.sleep(1)
            self.update_score()
        player_1 = str(self.tournament.rounds_list[-1].matchs_list[match_index - 1].player1)
        player_2 = str(self.tournament.rounds_list[-1].matchs_list[match_index - 1].player2)
        self.screen.add_infos(["Choix du score pour les joueurs :\n",
                               "    [1] ", player_1, " remporte le match\n",
                               "    [2] Match nul\n",
                               "    [3] ", player_2," remporte le match\n"])
        choix_score = input_menu_verification(
            3, "Choisir le score du joueur 1")
        if choix_score == 1:
            score_p1 = 1
            score_p2 = 0
        elif choix_score == 2:
            score_p1 = 0.5
            score_p2 = 0.5
        elif choix_score == 3:
            score_p1 = 0
            score_p2 = 1
        self.tournament.rounds_list[-1].validate_match(
            match_index, score_p1, score_p2)

    def modify_ranking_players(self):

        self.list_of_players()
        id_player = input_menu_verification(len(self.tournament.players_list),
                                            "Saisissez l'id du joueur à modifier")
        new_ranking = input_menu_verification(1000000000,
                                              "Saisissez le nouveau classement du joueur")
        for player in self.tournament.players_list:
            if player.player_id == id_player:
                player.modify_ranking(new_ranking)
                players_db.update(
                    {'elo_ranking': new_ranking}, p_query.player_id == id_player)

    def result(self):
        """Display result for a tournament"""
        tournament_result = ["Classement  ",
                             "NOM          ",
                             "PRENOM       ",
                             "SCORE        ",
                             "\n\n"]
        t_rank = 1
        for player in self.tournament.players_list:
            player_infos = []
            player_infos.append(str(t_rank))
            player_infos.append(player.surname)
            player_infos.append(player.name)
            player_infos.append(str(player.tournament_score))
            for i in range(4):
                dif = len(tournament_result[i]) - len(player_infos[i])
                if dif < 0:
                    tournament_result.append(
                        str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    tournament_result.append(str(player_infos[i]) + dif * " ")
            tournament_result.append("\n")
            t_rank += 1

        self.screen.tournament_result(tournament_result)

    def modify(self):
        """Modify info for a tournament"""
        self.screen.tournaments_list()
        report = ReportsControler()
        report.tournaments_list()
        tournament_id = 0
        while tournament_id not in range(1, self.count + 1):
            tournament_id = input_menu_verification(
                tournaments_db.__len__(), "Saisissez le numéro du tournoi à modifier")
        print("Choix de la modification :\n",
              "           [1] Nom \n",
              "           [2] Lieu \n",
              "           [3] Description \n")
        modify = input_menu_verification(
            3, "Saisissez le numéro de la donnée à modifier")
        info_modify = input("Saisissez la modification : ")
        if modify == 1:
            key = 'name'
        if modify == 2:
            key = 'location'
        if modify == 3:
            key = 'description'

        tournaments_db.update({key: info_modify}, t_query.id == tournament_id)
        self.modify()

    def list_of_players(self):
        """Display players list for tournament on course"""
        tournaments_players = tournaments_db.search(
            t_query.id == self.tournament.id)[0]['players_list']
        self.screen.players_list()
        datas = ["ID  ",
                 "NOM             ",
                 "PRENOM          ",
                 "ELO RANKING     ",
                 "DATE DE NAISSANCE  ",
                 "SEXE             ",
                 "\n\n"]
        for player in sorted(tournaments_players, key=lambda item: item['elo_ranking'], reverse=True):
            player_infos = [info for info in player.values()]
            for i in range(6):
                dif = len(datas[i]) - len(str(player_infos[i]))
                if dif < 0:
                    datas.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(player_infos[i]) + dif * " ")
            datas.append("\n")

        self.screen.add_infos(datas)


class ReportsControler:
    """Controler for reports

    Attributes:
        screen (Screen): Reports Display
    """

    def __init__(self):
        self.screen = Screen()

    def main(self):
        """Main menu for reports"""
        self.screen.reports_main()
        menu = input_menu_verification(
            7, "Saisissez le numéro du rapport souhaité")
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
        input_menu_verification(1, "")

    def go_back(self):
        """go back to main menu"""
        menu = ""
        while menu != "h":
            menu = input(
                "Saisissez 'h' pour revenir au menu principale : ").lower()
        MainControler()

    def tournaments_list(self):
        """Display all tournaments"""
        self.screen.tournaments_list()
        datas = ["ID   ",
                 "NOM            ",
                 "LIEU         ",
                 "DATE DE DEBUT                        ",
                 "DATE DE FIN                          ",
                 "NOMDRE DE TOUR  ",
                 "CONTROLEUR de TEMPS  ",
                 "DESCRIPTION                                                                  ",
                 "\n\n"]
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
        """Display players from database
        Args:
            key (str): key for players sorting
        """
        self.screen.players_list()
        datas = ["ID  ",
                 "NOM             ",
                 "PRENOM          ",
                 "ELO RANKING     ",
                 "DATE DE NAISSANCE  ",
                 "SEXE             ",
                 "\n\n"]

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
        """Display players from a tournament

        Args:
            key (str): key for players sorting
        """
        order = False
        if key == 'elo_ranking':
            order = True
        self.tournaments_list()
        tournament_index = input_menu_verification(
            tournaments_db.__len__(), "Saisissez le numéro du tournoi")
        
        tournaments_players = tournaments_db.search(
            t_query.id == tournament_index)[0]['players_list']
        self.screen.players_list()
        datas = ["ID  ",
                 "NOM             ",
                 "PRENOM          ",
                 "ELO RANKING     ",
                 "DATE DE NAISSANCE  ",
                 "SEXE             ",
                 "\n\n"]
        for player in sorted(tournaments_players, key=lambda item: item[key], reverse=order):
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
        """Display round from a tournament"""
        self.tournaments_list()
        tournament_index = input_menu_verification(
            tournaments_db.__len__(), "Saisissez le numéro du tournoi")
        tournaments_rounds = tournaments_db.search(
            t_query.id == tournament_index)[0]['rounds_list']
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
        """Display matchs from a tournament"""
        self.tournaments_list()
        tournament_index = input_menu_verification(
            tournaments_db.__len__(), "Saisissez le numéro du tournoi")
        tournament = Tournament(
            tournaments_db.search(t_query.id == tournament_index)[0])
        tournament.deserialized()

        self.screen.matchs_list()
        tournament_infos = [tournament.name, "\n"]
        self.screen.add_infos(tournament_infos)
        for rounds in tournament.rounds_list:
            print(rounds, "\n")
            for match in rounds.matchs_list:
                print(match)
            print("\n")
