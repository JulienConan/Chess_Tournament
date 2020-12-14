from tinydb import TinyDB, Query


tours = TinyDB('tournaments_file.json')
players = TinyDB('players_file.json')
tournament = Query()

for player in sorted(players.all(), key=lambda item : item['elo_ranking']):
	print(str([value for value in player.values()]))