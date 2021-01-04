# coding: utf-8
from controler import PlayerControler
from tinydb import TinyDB, Query
from tinydb.operations import add

players_db = TinyDB('models/datas_base/players_file.json')

p = [{'player_id' : 1, 'surname' : 'DUPONT', 'name' : 'Tom', 'elo_ranking' : 230 , 'birthday' : '20/15/1996' , 'sexe' : 'masculin' },
	  {'player_id' : 2, 'surname' : 'CONAN', 'name' : 'Julien', 'elo_ranking' : 112, 'birthday' : '30/01/1980' , 'sexe' : 'masculin' },
	  {'player_id' : 3, 'surname' : 'ROUINSARD', 'name' : 'Mo', 'elo_ranking' : 210, 'birthday' : '01/02/1932' , 'sexe' : 'feminin' },
	  {'player_id' : 4, 'surname' : 'THEVENET', 'name' : 'Maria', 'elo_ranking' : 650 , 'birthday' : '06/12/1930' , 'sexe' : 'feminin' },
	  {'player_id' : 5, 'surname' : 'GUILBEAU', 'name' : 'Pierre', 'elo_ranking' : 5646, 'birthday' : '25/05/2000' , 'sexe' : 'masculin' },
	  {'player_id' : 6, 'surname' : 'GRATTON', 'name' : 'Louis', 'elo_ranking' : 598, 'birthday' : '23/13/2020' , 'sexe' : 'feminin' },
	  {'player_id' : 7, 'surname' : 'LEDUC', 'name' : 'Camille', 'elo_ranking' : 2063, 'birthday' : '24/06/1970' , 'sexe' : 'masculin' },
	  {'player_id' : 8, 'surname' : 'TAPIN', 'name' : 'Laurianne', 'elo_ranking' : 1023, 'birthday' : '10/04/1965' , 'sexe' : 'feminin' },
	  {'player_id' : 9, 'surname' : 'ROUSSEAU', 'name' : 'Emilie', 'elo_ranking' : 6875, 'birthday' : '16/07/1950' , 'sexe' : 'masculin' },
	  {'player_id' : 10, 'surname' : 'RABBIOSI', 'name' : 'Gael', 'elo_ranking' : 10, 'birthday' : '18/06/2003' , 'sexe' : 'feminin' },
	  {'player_id' : 11, 'surname' : 'MAMMONE', 'name' : 'Leo', 'elo_ranking' : 0, 'birthday' : '23/01/1940' , 'sexe' : 'masculin' },
	  {'player_id' : 12, 'surname' : 'ROUX', 'name' : 'Niko', 'elo_ranking' : 564654, 'birthday' : '26/08/1950' , 'sexe' : 'feminin' },
	  {'player_id' : 13, 'surname' : 'BISMUTH', 'name' : 'Paul', 'elo_ranking' :300 , 'birthday' : '27/10/200' , 'sexe' : 'feminin' }]


for player in p :
	players_db.insert(player)