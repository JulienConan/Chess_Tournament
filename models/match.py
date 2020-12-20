# coding: utf-8
"""Module contenant la classe Match"""

class Match:
    """ Create a Match Object """

    def __init__(self, match_id, player1, player2, score_player1=0 , score_player2=0, statement="En cours"):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        self.statement = statement


    def __repr__(self):
        return ("Match " + str(self.match_id) + " : " 
                + str(self.player1) + ", " + str(self.score_player1) 
                + " vs " 
                + str(self.player2) + ", " + str(self.score_player2) 
                + " => Etat : " + str(self.statement))

    def __str__(self):
        return repr(self)
        

    def update_score(self, score1, score2):
        self.score_player1 = score1
        self.score_player2 = score2
        self.player1.tournament_score += score1
        self.player2.tournament_score += score2
        self.player1.tournament_opponents.append(self.player2.player_id)
        self.player2.tournament_opponents.append(self.player1.player_id)
        self.statement = "Validé"

    def serialized(self):
        serialized_match = []
        serialized_match.append(self.match_id)
        serialized_match.append(self.statement)
        serialized_match.append((self.player1.player_id, self.score_player1))
        serialized_match.append((self.player2.player_id, self.score_player2))
        return serialized_match
