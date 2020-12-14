# coding: utf-8
from time import strftime
from operator import attrgetter


class Player:
    """ Create a Player Object"""
    def __init__(self, player_infos):
        self.player_id = player_infos['player_id']
        self.surname = player_infos['surname']
        self.name = player_infos['name']
        self.elo_ranking = player_infos['ranking']
        self.birthday = player_infos['birthday']
        self.sexe = player_infos['sexe']
        self.tournament_opponents = []
        self.tournament_score = 0

    def __repr__(self):
        return self.surname

    def __str__(self):
        return repr(self)

    def serialized_players(self):
        player_dict = {}
        player_dict['player_id'] = self.player_id
        player_dict['surname'] = self.surname
        player_dict['name'] = self.name
        player_dict['elo_ranking'] = self.elo_ranking
        player_dict['birthday'] = self.birthday
        player_dict['sexe'] = self.sexe
        return player_dict


class Match:
    """ Create a Match Object """

    def __init__(self, match_id, player1, player2):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0
        self.on_course = True
        self.player1.tournament_opponents.append(self.player2.player_id)
        self.player2.tournament_opponents.append(self.player1.player_id)


    def __repr__(self):
        return "Match " + str(self.match_id) + "([" + str(self.player1) + ", " + str(self.score_player1) + "], [" + str(self.player2) + ", " + str(self.score_player2) + "])"

    def __str__(self):
        return repr(self)
        

    def update_score(self, score1, score2):
        self.score_player1 = score1
        self.score_player2 = score2
        self.player1.tournament_score += score1
        self.player2.tournament_score += score2
        self.on_course = False


class Round:
    def __init__(self, round_id, players_list, on_course=True):

        self.name = "Round" + str(round_id)
        self.round_id = round_id
        self.on_course = True
        self.date_start = strftime("%A %d %B %Y %H:%M:%S")
        self.date_end = "On course"
        self.players_list = players_list
        self.matchs_list = []

    def __repr__(self):
        return self.name + " => " + "Date de début : " + self.date_start +  " , Date de fin : " + self.date_end

    def __str__(self):
        return repr(self)

    def first_round(self):
        self.players_list.sort(key=attrgetter("elo_ranking"), reverse=True)

        for i in range(len(self.players_list)//2):
            self.matchs_list.append(Match(i+1, self.players_list[i], self.players_list[i+4]))

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
            print(self.matchs_list)
            temp_players_list.append(self.players_list[0])
            temp_players_list.append(self.players_list[i])
            del self.players_list[i]
            del self.players_list[0]
            match_index += 1

        self.players_list = temp_players_list

    def end(self):
        self.date_end = strftime("%A %d %B %Y %H:%M:%S")
        self.on_course = False

class Tournament:
    def __init__(self, dictio):
        self.name = dictio['name']
        self.location = dictio['location']
        self.date_start = dictio['date_start']
        self.date_end = dictio['date_end']
        self.time_controller = dictio['time_controler']
        self.description = dictio['description']
        self.total_round = dictio['rounds_number']
        self.players_list = dictio['players_list']
        self.rounds_list = dictio['rounds_list']
        self.round = 1

    def create_round(self):
        r = Round(self.round, self.players_list)
        if self.round == 1:
            self.rounds_list.append(r.first_round())
        else :
            self.rounds_list.append(r.other_round())
        self.players_list = r.players_list
        self.round += 1


    def serialized_tournament(self):
        pass