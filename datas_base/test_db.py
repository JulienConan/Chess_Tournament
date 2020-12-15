from tinydb import TinyDB, Query


tours = TinyDB('tournaments_file.json')
players = TinyDB('players_file.json')
tournament = Query()

print(tours.search(tournament.id == 1))
