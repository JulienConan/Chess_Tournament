# coding: utf-8
""" Module contenant la classe Tournament"""

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
