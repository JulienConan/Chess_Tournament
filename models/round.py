"""Module for Round Class"""
# coding: utf-8

from time import strftime
from operator import attrgetter
from .match import Match


class Round:
    """Create a round object

    Attributes:
        date_start (str): date when started round
        date_end (str): date when finished round
        matchs_list (list): Round's matchs list
        matchs_validates (int): Number of validated matchs
        players_list (list): Round's players list
        round_id (int): Round index
    """

    def __init__(self, round_id, players_list, date_start=strftime("%A %d %B %Y %H:%M:%S"),
                 date_end="On course", matchs_validates=0, matchs_list=[]):
        """Round object initialisation"""
        self.round_id = round_id
        self.players_list = players_list
        self.date_start = date_start
        self.date_end = date_end
        self.matchs_list = matchs_list
        self.matchs_validates = matchs_validates

    def __repr__(self):
        return "Round" + str(self.round_id)

    def __str__(self):
        return repr(self)

    def first_round(self):
        """create and stock matchs for the first round"""
        self.players_list.sort(key=attrgetter("elo_ranking"), reverse=True)

        for i in range(len(self.players_list) // 2):
            self.matchs_list.append(
                Match(i + 1, self.players_list[i], self.players_list[i + 4]))
        return self

    def other_round(self):
        """create and stock matchs for the other round"""
        self.players_list.sort(key=attrgetter("elo_ranking"), reverse=True)
        self.players_list.sort(key=attrgetter(
            "tournament_score"), reverse=True)
        temp_players_list = []

        match_index = 1
        while len(self.players_list) > 1:
            i = 1
            if self.players_list[0].player_id in self.players_list[i].tournament_opponents:
                inside = True
            else:
                inside = False
            while inside and len(self.players_list) > 2:
                i += 1
                if i == len(self.players_list):
                    i = 1
                    inside = False

            self.matchs_list.append(
                Match(match_index, self.players_list[0], self.players_list[i]))
            temp_players_list.append(self.players_list[0])
            temp_players_list.append(self.players_list[i])
            del self.players_list[i]
            del self.players_list[0]
            match_index += 1

        self.players_list = temp_players_list
        return self

    def validate_match(self, match, score1, score2):
        """Validate match and update validates matchs count

        Args:
            match (int): match index for a round
            score1 (TYPE): score for the first player of the match
            score2 (TYPE): score for the second player of the match
        """
        self.matchs_list[match - 1].update_score(score1, score2)
        self.matchs_validates += 1
        if self.matchs_validates == len(self.players_list) / 2:
            self.date_end = strftime("%A %d %B %Y %H:%M:%S")

    def serialized(self):
        """Serialized round informations for tournament export

        Returns:
            list: List contains round informations
        """
        serialized_round = []
        serialized_round.append(self.round_id)
        serialized_round.append(self.date_start)
        serialized_round.append(self.date_end)
        serialized_round.append(self.matchs_validates)
        matchs_list = []
        for match in self.matchs_list:
            matchs_list.append(match.serialized())
        serialized_round.append(matchs_list)
        return serialized_round

    def deserialized(self):
        """Deserialized round informations for tournament import"""
        deserialized_match = []
        for match in self.matchs_list:
            for player in self.players_list:
                if player.player_id == match[2][0]:
                    player1 = player
                if player.player_id == match[3][0]:
                    player2 = player
            m = Match(match[0], player1, player2,
                      match[2][1], match[3][1], match[1])
            deserialized_match.append(m)
        self.matchs_list = deserialized_match
