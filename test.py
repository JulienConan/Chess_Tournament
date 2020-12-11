# coding: utf-8
"""Test"""
from models import*
from tinydb import TinyDB, Query
from constants import *

db = TinyDB('datas_base/db.json')

players_list = []

players_list.append(Player("Dupont", "Jules", "02/15/1986", "Masculin", 89785, 1))
players_list.append(Player("Guilbeau", "Pierre", "25/11/2986", "Masculin", 874, 2))
players_list.append(Player("Rouinsard", "Mo", "26/12/1985", "Féminin", 897, 3))
players_list.append(Player("Dunand", "Alban", "11/02/1990" , "Masculin",654, 4))
players_list.append(Player("Mbapé", "Thierry", "20/59/1698", "Masculin", 213, 5))
players_list.append(Player("CONAN", "Rose", "06/11/1995", "Feminin", 52, 6))
players_list.append(Player("Koba", "Lucie", "12/03/1956", "Féminin", 6546, 7))
players_list.append(Player("Modeus", "Kate", "25/05/1986", "Féminin", 2131, 8))

for i in range(7):
	print("Round" + str(i))
	r = Round(i, players_list)
	if i == 0:
		r.first_round()
	else :
		r.other_round()
		print(r.players_list)

	for j in range(4):
		r.matchs_list[j].update_score(1, 0)
		
	players_list = r.players_list
	for i in range(8):
		print(" Joueur" + str(players_list[i].player_id) + " : " + str(players_list[i].tournament_opponents))
		print(players_list[i].tournament_score)
for i in players_list :
	serialized_players = i.serialized_players()
	index = db.table(ACTORS_TABLE).insert(serialized_players)
	print(index)

P = Query()

print(db.search(P.name == 'Pierre'))
