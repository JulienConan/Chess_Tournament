"""Module for Reports Class"""
# coding: utf-8
from .function_db import search_db
from .tournament import Tournament


class Reports:
    """Controler for reports"""

    def __init__(self, players_db, tournaments_db):
        self.menu = ["          RAPPORTS             ",
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
                     "\n"]
        self.tournaments_db = tournaments_db
        self.players_db = players_db

    def tournaments_list(self):
        """Display all tournaments"""
        title = ["            LISTE DES TOURNOIS            \n\n\n"]

        entete = ["ID   ",
                  "NOM            ",
                  "LIEU         ",
                  "DATE DE DEBUT                        ",
                  "DATE DE FIN                          ",
                  "NOMDRE DE TOUR  ",
                  "CONTROLEUR de TEMPS  ",
                  "DESCRIPTION                                                                  ",
                  "\n\n"]

        for tournament in sorted(self.tournaments_db.all(),
                                 key=lambda item: item['id']):
            tournament_infos = [info for info in tournament.values()]
            for i in range(8):
                dif = len(entete[i]) - len(str(tournament_infos[i]))
                if dif < 0:
                    entete.append(str(tournament_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    entete.append(str(tournament_infos[i]) + dif * " ")
            entete.append("\n")
        title.extend(entete)
        return title

    def list_of_players(self, key):
        """Display players from database
        Args:
            key (str): key for players sorting
        """
        title = ["          LISTE DES JOUEURS           ",
                 "\n\n\n"]
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
        for player in sorted(self.players_db.all(),
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
        title.extend(datas)
        return title

    def t_players_list(self, tournament_index, key):
        """Return tournament's players list

        Args:
            key (str): key for players sorting
        """
        title = ["          LISTE DES JOUEURS DU TOURNOI        ",
                 "\n\n\n"]
        tournament_players = search_db(tournament_index, self.tournaments_db)['players_list']

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
        for player in sorted(tournament_players, key=lambda item: item[key], reverse=order):
            player_infos = [info for info in player.values()]
            for i in range(6):
                dif = len(datas[i]) - len(str(player_infos[i]))
                if dif < 0:
                    datas.append(str(player_infos[i])[:(dif - 1)] + " ")
                elif dif > 0:
                    datas.append(str(player_infos[i]) + dif * " ")
            datas.append("\n")
        title.extend(datas)
        return title

    def tournament_rounds_list(self, tournament_index):
        """Display round from a tournament"""

        tournament = Tournament(search_db(tournament_index, self.tournaments_db))
        tournament_rounds = search_db(tournament_index, self.tournaments_db)['rounds_list']

        entete_t = ["           LISTES DES TOURS        \n\n\n",
                    tournament.name, "\n",
                    "Début : ", tournament.date_start, "\n",
                    "Fin : ", tournament.date_end, "\n",
                    "Contrôleur de temps : ", tournament.time_controler, "\n",
                    "Description : ", tournament.description, "\n\n"]

        entete_r = ["Round      ",
                    "Date de début                              ",
                    "Date de fin                                ",
                    "Nombre de matchs validés   ",
                    "\n"]

        infos_round = []
        for rounds in tournament_rounds:
            for i in range(4):
                dif = len(entete_r[i]) - len(str(rounds[i]))
                if dif < 0:
                    infos_round.append(str(rounds[i])[:(dif - 1)] + " ")
                else:
                    infos_round.append(str(rounds[i]) + dif * " ")
            infos_round.append("\n")
        entete_t.extend(entete_r)
        entete_t.extend(infos_round)
        return entete_t

    def tournament_matchs_list(self, tournament_index):
        """Display matchs from a tournament"""

        tournament = Tournament(search_db(tournament_index, self.tournaments_db))
        tournament.deserialized()

        entete_t = ["               LISTE DES MATCHS            \n\n\n",
                    tournament.name, "\n",
                    "Début : ", tournament.date_start, "\n",
                    "Fin : ", tournament.date_end, "\n",
                    "Contrôleur de temps : ", tournament.time_controler, "\n",
                    "Description : ", tournament.description, "\n\n"
                    ]
        datas = []
        for rounds in tournament.rounds_list:
            datas.extend([str(rounds), "\n"])
            for match in rounds.matchs_list:
                datas.append(match.result())
                datas.append("\n")
            datas.append("\n\n")

        entete_t.extend(datas)
        return entete_t
