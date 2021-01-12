"""Module for controler
# coding: utf-8

Attributes:
    p_query (TYPE): Query for players database
    players_db (TYPE): Database for players
    t_query (TYPE): Query for tournaments database
    tournaments_db (TYPE): Database for tournaments
"""

from time import strftime, sleep
import sys

from constants import (
                       ROUNDS_NB,
                       TOURNAMENT_PLAYERS_NB,
                       P_DATABASE,
                       T_DATABASE
                       )

from models.tournament import Tournament
from models.reports import Reports
from models.function_db import (
                                access_db,
                                query,
                                max_id,
                                add_item_db,
                                search_db,
                                update_item_in_db,
                                remove_in_db
                                )

from view import Screen


players_db = access_db(P_DATABASE)
tournaments_db = access_db(T_DATABASE)
p_query = query()
t_query = query()


def input_menu_verification(index, message):
    """Verification for user keystroke

    Args:
        index (int): Number of possibilities
        message (str): message for the display
    """
    screen = Screen()
    saisie = input(
        message + " (h pour revenir au menu principale ou q pour quitter le programme) : ")
    try:
        saisie = int(saisie)
        if saisie in range(1, (index + 1)):
            return saisie
        else:
            screen.warning(
                "La saisie doit être comprise entre 1 et {}.".format(index))
            sleep(1)
            return input_menu_verification(
                index, message)
    except ValueError:
        saisie = saisie.lower()
        if saisie == 'h':
            MainControler()
        elif saisie == 'q':
            sys.exit()
        else:
            screen.warning(
                "La saisie doit être un chiffre compris entre 1 et {}.".format(index))
            sleep(1)
            return input_menu_verification(index, message)


class MainControler:
    """Main controler

    Attributes:
        screen (object): Display for main menu
    """

    def __init__(self):
        self.screen = Screen()
        self.screen.clear()
        self.screen.info_users(["            CHESS TOURNAMENTS MANAGER             ",
                                "\n\n\n",
                                "[1] Gestion des joueurs",
                                "\n",
                                "[2] Lecture Rapports",
                                "\n",
                                "[3] Gestion des tournois",
                                "\n"])
        self.screen.on_screen()
        menu = input_menu_verification(3, "Saisissez le numéro du menu désiré")

        if menu == 1:
            self.player_action()
        elif menu == 2:
            self.reports()
        elif menu == 3:
            self.tournament_actions()

    def player_action(self):
        """Go to player actions menu"""
        player_a = PlayerControler()
        player_a.main()

    def reports(self):
        """Go to reports menu"""
        report = ReportsControler()
        report.main()

    def tournament_actions(self):
        """Create a new tournament"""
        TournamentControler()


class PlayerControler:

    """Player controler

    Attributes:
        player_dict (dict): Dictionnary contains player info
        screen (object): Description
    """

    def __init__(self):
        self.screen = Screen()

    def main(self):
        """Main menu for player action"""
        self.screen.info_users(
            ["      GESTION DES JOUEURS",
             "\n\n\n",
             "[1] Créer un joueur",
             "\n",
             "[2] Modifier un joueur",
             "\n",
             "[3] Supprimer un joueur",
             "\n"]
        )
        self.screen.clear()
        self.screen.on_screen()
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
        self.screen.info_users(
            ["              AJOUT D'UN JOUEUR           \n\n\n"])
        self.screen.clear()
        self.screen.on_screen()
        player_dict = {}
        player_dict['id'] = max_id(players_db) + 1
        player_dict['surname'] = input("Nom du Joueur: ").upper()
        player_dict['name'] = input("Prénom du Joueur : ").capitalize()
        player_dict['elo_ranking'] = int(-1)
        while player_dict['elo_ranking'] < 0:
            try:
                ranking = int(input("Classement du joueur: "))
                if ranking < 0:
                    self.screen.warning(
                        "le classement doit être supérieur à 0")
                else:
                    player_dict['elo_ranking'] = ranking
            except ValueError:
                self.screen.warning(
                    "le classement doit être un chiffre supérieur ou égal à 0")
        player_dict['birthday'] = input("Date de naissance : ")
        player_dict['sexe'] = input("Sexe du joueur : ").capitalize()

        add_item_db(player_dict, players_db)
        self.main()

    def modify(self):
        """Modify a player info"""
        self.screen.info_users(
            ["              MODIFICATION D'UN JOUEUR           \n\n\n"])
        self.screen.clear()
        self.screen.on_screen()
        report = Reports(players_db, tournaments_db)
        self.screen.info_users(report.list_of_players('id'))
        self.screen.clear()
        self.screen.on_screen()
        id_player = input_menu_verification(
            max_id(players_db), "Saisissez le numéro du joueur à modifier")
        try:
            players_db.search(p_query.player_id == id_player)[0]
        except IndexError:
            self.screen.warning(
                "Le joueur {} n'existe pas.".format(id_player))
            sleep(1)
            self.modify()

        self.screen.add_infos(["Choix de la modification :\n",
                               "           [1] Nom \n",
                               "           [2] Prénom \n",
                               "           [3] Classement \n",
                               "           [4] Date de naissance \n",
                               "           [5] Sexe \n"])
        self.screen.clear()
        self.screen.on_screen()
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
                info_modify = input_menu_verification(
                    100000000, "Le classement doit être chiffre positif")
        if modify == 4:
            key = 'birthday'
        if modify == 5:
            info_modify = info_modify.capitalize()
            key = 'sexe'

        update_item_in_db(players_db, key, info_modify, id_player)
        self.screen.warning("Modification appliquée")
        sleep(1)
        self.modify()

    def delete(self):
        """Delete a player"""
        self.screen.info_users(
            ["              SUPPRESSION D'UN JOUEUR           \n\n\n"])
        self.screen.clear()
        self.screen.on_screen()
        report = Reports(players_db, tournaments_db)
        self.screen.info_users(report.list_of_players('id'))
        self.screen.clear()
        self.screen.on_screen()

        id_player = input_menu_verification(
            players_db.__len__(), "Saisissez le numéro du joueur à effacer")
        remove_in_db(players_db, id_player)
        self.delete()


class TournamentControler:
    """Tournament controler

    Attributes:
        screen (object): display for tournament controler
        tournament_infos (dict): Dictionnary contains infos for a tournament
        tournament (object): tournament on course
    """

    def __init__(self):
        self.screen = Screen()
        self.screen.info_users(
            ["         GESTION DES TOURNOIS     ",
             "\n\n\n",
             "[1] Créer un tournoi",
             "\n",
             "[2] Charger un tournoi",
             "\n",
             "[3] Modifier un tournoi",
             "\n"]
        )
        self.screen.clear()
        self.screen.on_screen()

        menu = input_menu_verification(3, "Saisissez le menu désiré")

        if menu == 1:
            self.create()
        elif menu == 2:
            self.load()
        elif menu == 3:
            self.modify()

    def create(self):
        """Create a new tournmanent"""
        self.screen.info_users(
            ["               CREATION DE TOURNOI             \n\n\n"])
        self.screen.clear()
        self.screen.on_screen()
        tournament_infos = {}
        tournament_infos['id'] = max_id(tournaments_db) + 1
        tournament_infos['name'] = input("Nom du Tournoi : ")
        tournament_infos['location'] = input("Lieu du tournoi : ")
        tournament_infos['date_start'] = strftime("%A %d %B %Y %H:%M:%S")
        tournament_infos['date_end'] = "on_course"
        tournament_infos['total_round'] = ROUNDS_NB
        self.screen.info_users(["Choix du controleur de temps :\n",
                                "           [1] Blitz \n",
                                "           [2] Bullet \n",
                                "           [3] Coup Rapide \n"])
        self.screen.on_screen()

        controler_saisie = input_menu_verification(
            3, "Veuillez saisir le numéro correspondant à votre choix")

        if controler_saisie == 1:
            tournament_infos['time_controler'] = "Blitz"
        elif controler_saisie == 2:
            tournament_infos['time_controler'] = "Bullet"
        elif controler_saisie == 3:
            tournament_infos['time_controler'] = "Coup rapide"

        tournament_infos['description'] = input("Description : ")
        tournament_infos['players_list'] = []
        tournament_infos['rounds_list'] = []

        self.tournament = Tournament(tournament_infos)
        self.tournament.save(tournaments_db)
        self.players_on_load = []
        while len(self.tournament.players_list) < TOURNAMENT_PLAYERS_NB:
            self.add_player_on_tournament()
            self.tournament.save(tournaments_db)
        self.play()

    def add_player_on_tournament(self):
        """Add a player in a tournament"""
        self.screen.clear()
        report = Reports(players_db, tournaments_db)
        self.screen.info_users(report.list_of_players('id'))
        self.screen.add_infos(["{} joueurs ajoutés au tournoi".format(
            len(self.tournament.players_list))])
        self.screen.on_screen()
        id_player = input_menu_verification(
            max_id(players_db), "Entrez le numéro du joueur à ajouter au tournoi")
        while id_player in self.players_on_load:
            self.screen.warning(
                "Le joueur {} est déjà inscrit dans ce tournoi".format(id_player))
            id_player = input_menu_verification(
                max_id(players_db), "Entrez le numéro du joueur à ajouter au tournoi")
        valid_player = search_db(id_player, players_db)
        if valid_player is not False:
            self.tournament.add_player(valid_player)
            self.players_on_load.append(id_player)
        else:
            self.screen.warning("Le joueur {} n'existe pas.".format(id_player))
            sleep(1)

    def load(self):
        """Load a tournament"""
        report = Reports(players_db, tournaments_db)
        self.screen.clear()
        self.screen.info_users(report.tournaments_list())
        self.screen.on_screen()
        tournament_id = input_menu_verification(max_id(tournaments_db),
                                                "Saisissez le numéro du tournoi à charger")

        valid_tournament = search_db(tournament_id, tournaments_db)

        if valid_tournament is False:
            self.screen.warning(
                "Le tournoi {} n'existe pas.".format(tournament_id))
            sleep(1)
            self.load()
        else:
            tournament_on_load = Tournament(valid_tournament)
            tournament_on_load.deserialized()
            self.tournament = tournament_on_load
        self.players_on_load = []
        for player in self.tournament.players_list:
            self.players_on_load.append(player.player_id)

        while len(self.tournament.players_list) < TOURNAMENT_PLAYERS_NB:
            self.add_player_on_tournament()

        self.play()

    def play(self):
        """Play a tournament

        Args:
            tournament (object): Tournament object
        """
        self.screen.clear()
        tournament_infos_list = [self.tournament.name, "\n",
                                 "Lieu : ",
                                 self.tournament.location, "\n",
                                 "Début du tournoi : ",
                                 self.tournament.date_start, "\n"]

        while self.tournament.round < ROUNDS_NB:
            if self.tournament.rounds_list == [] or self.tournament.rounds_list[-1].date_end != 'On course':
                self.tournament.create_round()
                self.tournament.save(tournaments_db)
            while self.tournament.rounds_list[-1].date_end == 'On course':
                self.screen.info_users(
                    ["               TOURNOI EN COURS            \n\n\n"])
                self.screen.add_infos(tournament_infos_list)
                round_infos = [str(self.tournament.rounds_list[-1]), "\n\n"]
                for match in self.tournament.rounds_list[-1].matchs_list:
                    round_infos.append(str(match))
                    round_infos.append("\n")
                self.screen.add_infos(round_infos)
                self.screen.on_screen()
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
        """choice of actions in tournament"""
        self.screen.info_users(["Actions possibles :\n",
                                "            [1] Saisir le score d'un match\n",
                                "            [2] Modifiez le classement d'un joueur\n"])
        self.screen.on_screen()
        choice = input_menu_verification(
            2, "Saisissez le numéro de l'action souhaitée")
        if choice == 1:
            self.update_score()
        elif choice == 2:
            self.modify_player_rank()

    def update_score(self):
        """Updating a match score"""
        match_index = input_menu_verification(int(TOURNAMENT_PLAYERS_NB / 2),
                                              "Pour quel match voulez vous rentrer les résultats")
        if self.tournament.rounds_list[-1].matchs_list[match_index - 1].statement == "Validé":
            self.screen.info_users(["Match déjà joué."])
            sleep(1)
            self.update_score()
        player_1 = str(
            self.tournament.rounds_list[-1].matchs_list[match_index - 1].player1)
        player_2 = str(
            self.tournament.rounds_list[-1].matchs_list[match_index - 1].player2)
        self.screen.info_users(["Choix du score pour les joueurs :\n",
                                "    [1] ", player_1, " remporte le match\n",
                                "    [2] Match nul\n",
                                "    [3] ", player_2, " remporte le match\n"])
        self.screen.on_screen()
        choix_score = input_menu_verification(
            3, "")
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
        self.screen.clear()

    def modify_player_rank(self):
        """Modify a player's rank"""
        self.screen.clear()
        self.screen.info_users(self.list_of_players())
        self.screen.on_screen()
        id_player = input_menu_verification(self.max_player_id_tournament(),
                                            "Saisissez l'id du joueur dont vous souhaitez modifier le rang")
        id_players_list = []
        for player in self.tournament.players_list:
            id_players_list.append(player.player_id)

        if id_player not in id_players_list:
            self.screen.warning(
                "Le joueur {} n'est pas présent dans le tournoi.".format(id_player))
            sleep(1)
            self.modify_player_rank()
        new_ranking = input_menu_verification(1000000000,
                                              "Saisissez le nouveau classement du joueur")
        for player in self.tournament.players_list:
            if player.player_id == id_player:
                player.modify_ranking(new_ranking)
                update_item_in_db(players_db, 'elo_ranking',
                                  new_ranking, id_player)
        self.screen.clear()

    def max_player_id_tournament(self):
        """Define maximum player id"""
        i = 0
        for player in self.tournament.players_list:
            if player.player_id > i:
                i = player.player_id
        return i

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

        self.screen.info_users(tournament_result)
        self.screen.on_screen()

    def modify(self):
        """Modify info for a tournament"""
        report = Reports(players_db, tournaments_db)
        self.screen.clear()
        self.screen.info_users(report.tournaments_list())
        self.screen.on_screen()

        tournament_id = input_menu_verification(max_id(
            tournaments_db), "Saisissez le numéro du tournoi à modifier")

        self.screen.info_users(
            ["Choix de la modification :\n",
             "           [1] Nom \n",
             "           [2] Lieu \n",
             "           [3] Description \n"]
        )
        self.screen.on_screen()
        modify = input_menu_verification(
            3, "Saisissez le numéro de la donnée à modifier")
        info_modify = input("Saisissez la modification : ")
        if modify == 1:
            key = 'name'
        if modify == 2:
            key = 'location'
        if modify == 3:
            key = 'description'
        update_item_in_db(tournaments_db, key, info_modify, tournament_id)
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
        for player in sorted(
                tournaments_players, key=lambda item: item['elo_ranking'], reverse=True):
            player_infos = [info for info in player.values()]
            for i in range(6):
                dif = len(datas[i]) - len(str(player_infos[i]))
                if dif < 0:
                    datas.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(player_infos[i]) + dif * " ")
            datas.append("\n")

        return datas


class ReportsControler:
    """Go to reports menu"""

    def __init__(self):
        self.report = Reports(players_db, tournaments_db)
        self.screen = Screen()

    def main(self):
        self.screen.clear()
        self.screen.add_infos(self.report.menu)
        self.screen.on_screen()
        menu = input_menu_verification(
            7, "Saisissez le numéro du rapport souhaité")
        self.screen.clear()

        if menu == 1:
            self.players_list('surname')
        elif menu == 2:
            self.players_list('elo_ranking')
        elif menu == 3:
            self.players_list_tournament('surname')
        elif menu == 4:
            self.players_list_tournament('elo_ranking')
        elif menu == 5:
            self.tournaments_list()
        elif menu == 6:
            self.tournament_rounds_list()
        elif menu == 7:
            self.tournament_matchs_list()

        self.screen.on_screen()
        menu = input_menu_verification(
            1, "Saisir [1] pour revenir au menu des rapports")
        report = ReportsControler()
        report.main()

    def players_list(self, key):
        self.screen.info_users(self.report.list_of_players(key))

    def tournaments_list(self):
        self.screen.info_users(self.report.tournaments_list())

    def choice_tournament(self):
        self.tournaments_list()
        self.screen.on_screen()
        tournament_index = input_menu_verification(
            max_id(tournaments_db), "Saisissez le numéro du tournoi")
        self.screen.clear()
        return tournament_index

    def players_list_tournament(self, key):
        tournament_index = self.choice_tournament()
        self.screen.info_users(
            self.report.t_players_list(tournament_index, key))

    def tournament_rounds_list(self):
        tournament_index = self.choice_tournament()
        self.screen.info_users(
            self.report.tournament_rounds_list(tournament_index))

    def tournament_matchs_list(self):
        tournament_index = self.choice_tournament()
        self.screen.info_users(
            self.report.tournament_matchs_list(tournament_index))
