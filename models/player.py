# coding: utf-8
"""Module contenant la classe Player"""

class Player:
    """ Create a Player Object"""
    def __init__(self, player_infos):
        self.player_id = player_infos['player_id']
        self.surname = player_infos['surname']
        self.name = player_infos['name']
        self.elo_ranking = int(player_infos['elo_ranking'])
        self.birthday = player_infos['birthday']
        self.sexe = player_infos['sexe']
        if 'tournament_opponents' not in player_infos:
            self.tournament_opponents = []
        else :
            self.tournament_opponents = player_infos['tournament_opponents']
        if 'tournament_score' not in player_infos:
            self.tournament_score = 0
        else :
            self.tournament_score = player_infos['tournament_score']



    def __repr__(self):
        return self.surname

    def __str__(self):
        return repr(self)

    def serialized(self):
        player_infos = {}
        player_infos['player_id'] = self.player_id
        player_infos['surname'] = self.surname
        player_infos['name'] = self.name
        player_infos['elo_ranking'] = self.elo_ranking
        player_infos['birthday'] = self.birthday
        player_infos['sexe'] = self.sexe
        player_infos['tournament_opponentes'] = self.tournament_opponents
        player_infos['tournament_score'] = self.tournament_score
        return player_infos
