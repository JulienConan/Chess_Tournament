# coding: utf-8
from time import strftime
from operator import attrgetter


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


class Match:
    """ Create a Match Object """

    def __init__(self, match_id, player1, player2, score_player1=0 , score_player2=0):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        self.statement = "En cours"


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

       



class Round:
    def __init__(self, round_id, players_list, date_start=strftime("%A %d %B %Y %H:%M:%S"), date_end="On course", matchs_validates=0, matchs_list=[] ):

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
    





class Tournament:
    def __init__(self, tournament_infos):
        self.id = tournament_infos['id']
        self.name = tournament_infos['name']
        self.location = tournament_infos['location']
        self.date_start = tournament_infos['date_start']
        self.date_end = tournament_infos['date_end']
        self.time_controler = tournament_infos['time_controler']
        self.description = tournament_infos['description']
        self.total_round = tournament_infos['total_round']
        self.rounds_list = tournament_infos['rounds_list']
        self.players_list = [Player(player) for player in tournament_infos['players_list']]

        self.round = len(self.rounds_list)

    def create_round(self):
        r = Round(self.round + 1, self.players_list)
        if self.round == 0:
            self.rounds_list.append(r.first_round())
        else :
            self.rounds_list.append(r.other_round())
        self.players_list = r.players_list
        self.round += 1


    def serialized(self):
        serialized_tournament = {}
        serialized_tournament['id'] = self.id
        serialized_tournament['name'] = self.name
        serialized_tournament['location'] = self.location
        serialized_tournament['date_start'] = self.date_start
        serialized_tournament['date_end'] = self.date_end
        serialized_tournament['total_round'] = self.total_round
        serialized_tournament['time_controler'] = self.time_controler
        serialized_tournament['description'] = self.description
        serialized_tournament['players_list'] = [player.serialized() for player in self.players_list]
        serialized_tournament['rounds_list'] = [t_round.serialized() for t_round in self.rounds_list]
        return serialized_tournament
