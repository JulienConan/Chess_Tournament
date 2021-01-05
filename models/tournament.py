"""Module for Tournament Class
"""
# coding: utf-8
from tinydb import Query
from .player import Player
from .round import Round


class Tournament:

    """Create Tournament object

    Attributes:
        date_end (str): Date when tournament finished
        date_start (str): Date when tournament start
        description (str): Tournament's description
        id (int): Tournament's id
        location (str): Location of the tournament
        name (str): Tournament's name
        players_list (list): List of tournament's players
        round (TYPE): Count of created round
        rounds_list (list): List of tournament's rounds
        time_controler (str): Tournament's time controler
        total_round (int): Tournament's round number
    """

    def __init__(self, tournament_infos):
        """Tournament object initialisation

        Args:
            tournament_infos (dict): Dictionnary contains tournament informations
        """
        self.id = tournament_infos['id']
        self.name = tournament_infos['name']
        self.location = tournament_infos['location']
        self.date_start = tournament_infos['date_start']
        self.date_end = tournament_infos['date_end']
        self.time_controler = tournament_infos['time_controler']
        self.description = tournament_infos['description']
        self.total_round = tournament_infos['total_round']
        self.rounds_list = tournament_infos['rounds_list']
        self.players_list = [Player(player)
                             for player in tournament_infos['players_list']]

        self.round = len(self.rounds_list)

    def create_round(self):
        """Creation of a round
        """
        r = Round(self.round + 1, self.players_list, matchs_list=[])
        if self.round == 0:
            self.rounds_list.append(r.first_round())
        else:
            self.rounds_list.append(r.other_round())
        self.players_list = r.players_list
        self.round += 1

    def save(self, tournament_db):
        """Save the tournament in database

        Args:
            tournament_db (TYPE): tournament's tinydb database
        """
        t_db = tournament_db
        tournament = Query()
        serialized_tournament = {}
        serialized_tournament['id'] = self.id
        serialized_tournament['name'] = self.name
        serialized_tournament['location'] = self.location
        serialized_tournament['date_start'] = self.date_start
        serialized_tournament['date_end'] = self.date_end
        serialized_tournament['total_round'] = self.total_round
        serialized_tournament['time_controler'] = self.time_controler
        serialized_tournament['description'] = self.description
        serialized_tournament['players_list'] = [
            player.serialized() for player in self.players_list]
        serialized_tournament['rounds_list'] = [
            t_round.serialized() for t_round in self.rounds_list]

        if t_db.search(tournament.id == self.id) == []:
            t_db.insert(serialized_tournament)
        else:
            t_db.remove(tournament.id == self.id)
            t_db.insert(serialized_tournament)

    def deserialized(self):
        """Deserialized Tounrament"""
        deserialized_round = []
        for rounds in self.rounds_list:
            r = Round(rounds[0], self.players_list, rounds[1],
                      rounds[2], rounds[3], rounds[4])
            r.deserialized()
            deserialized_round.append(r)
        self.rounds_list = deserialized_round
