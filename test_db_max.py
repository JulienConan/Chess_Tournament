from controler import PlayerControler
from tinydb import TinyDB, Query
from tinydb.operations import add

players_db = TinyDB('models/datas_base/players_file.json')
p_query = Query()

i = 0
for player in players_db:
	print(player)
	if player['player_id'] > i:
		i = player['player_id']

print(i) 

