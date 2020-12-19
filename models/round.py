# coding: utf-8
"""Module contenant la classe Round"""

from time import strftime

from player import Player
from match import Match

class Round:
    def __init__(self, round_id, players_list, date_start=strftime("%A %d %B %Y %H:%M:%S"),
    			 date_end="On course", matchs_validates=0, matchs_list=[] ):

        self.round_id = round_id
        self.date_start = date_start
        self.date_end = date_end
        self.players_list = players_list
        self.matchs_list = matchs_list
        self.matchs_validates = matchs_validates

    def __repr__(self):

        return "Round" + str(self.round_id)

    def __str__(self):
        return repr(self)

    def first_round(self):
        self.players_list.sort(key=attrgetter("elo_ranking"), reverse=True)

        for i in range(len(self.players_list)//2):
            self.matchs_list.append(Match(i+1, self.players_list[i], self.players_list[i+4]))
        return self

    def other_round(self):
        self.players_list.sort(key=attrgetter("elo_ranking"), reverse=True)
        self.players_list.sort(key=attrgetter("tournament_score"), reverse=True)
        temp_players_list = []
        
        match_index =1
        while len(self.players_list) > 1 :  
            i = 1
            while self.players_list[0].player_id in self.players_list[i].tournament_opponents and len(self.players_list) > 2 :
                i +=1
            self.matchs_list.append(Match(match_index, self.players_list[0], self.players_list[i]))
            temp_players_list.append(self.players_list[0])
            temp_players_list.append(self.players_list[i])
            del self.players_list[i]
            del self.players_list[0]
            match_index += 1

        self.players_list = temp_players_list
        return self

    def validate_match(self, match, score1, score2):

        self.matchs_list[match - 1].update_score(score1, score2)
        self.matchs_validates += 1
        if self.matchs_validates == len(self.players_list)/2:
            self.date_end = strftime("%A %d %B %Y %H:%M:%S")

    def serialized(self):
        serialized_round = []
        serialized_round.append(self.round_id )
        serialized_round.append(self.date_start) 
        serialized_round.append(self.date_end) 
        serialized_round.append(self.matchs_validates) 
        matchs_list = []
        for match in self.matchs_list:
            matchs_list.append(match.serialized())
        serialized_round.append(matchs_list)
        return serialized_round