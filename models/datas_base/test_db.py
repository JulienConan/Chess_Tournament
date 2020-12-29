from tinydb import TinyDB, Query


tours = TinyDB('tournament_file.json')
players = TinyDB('players_file.json')
tournament = Query()

print(players.__len__())
