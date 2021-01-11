# CTG

## Gestionnaire de tournois d'échecs

 CTG est une application python dédiée à la gestion de tournois selon le système de tournois __suisse__. Ses fonctionnalités se découpent en trois grandes parties :

* Gestion de joueurs :
	* Créer un joueur
	* Modifier un joueur
	* Supprimer un joueur

* Gestion de rapports :  
	* Liste des joueurs par ordre alphabétique
	* Liste des joueurs par classement
	* Liste des joueurs d'un tournoi par ordre alphabétique
	* Liste des joueurs d'un tournoi par classement
	* Liste de tous les tournois
	* Liste de tous les tours d'un tournois
	* Liste de tous les matchs d'un tournoi

* Gestion de tournoi : 
	* Créer un tournoi
	* Charger un tournoi
	* Modifier un tournoi

# Installation
- Python 3.6 minimumu requis  
- Librairie python Virtualenv : saisir dans un invite de commande : `pip install virtualenv`  

## Téléchargement

### Depuis ce dépot, télécharger l'archive : 

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/GitHub_Download.png)

Décompresser l'archive __Chess_Tournament-master.zip__.  

### Depuis la Source  

Dans un invite de commande, saisir :   

`git clone https://github.com/JulienConan/Chess_Tournament.git`

## Création d'un environnement virtuel

Dans un invite de commande situé dans le dossier principal de l'application, saisir :  

### Windows  
`python -m venv env`  
### Linux
`python3 -m venv env`  
### MacOs  
`virtualenv env`  

## Activation de l'environnement virtuel  

Dans un invite de commande situé dans le dossier principal de l'application, saisir :
### Windows  
`env\Scripts\activate.bat`
### Linux & MacOs
`source env/bin/activate`

## Installation des dépendances requises

Se placer dans le dossier principale de l'application et saisir :

`pip install -r requirements.txt`  

## Désactivation environnement virtuel  

Lorsque qu'un environnement virtuel est activé dans un invite de commande, pour le désactiver saisir :  
`desactivate`  

# Utilisation de l'application  

Activer l'environnement virtuel situé dans le dossier principal de l'application, puis saisir dans l'invite de commande :  

### Windows    
`python main.py`  
### Linux   
`python3 main.py`  
### MacOs   
`python[ma_version] main.py`  __[ma_version]__ correspondant à la version de python installée sur l'ordinateur de l'utilisateur.  

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/main_menu.png)

Pour chaque action (aller dans un menu ou effectuer une action), l'utilisateur doit saisir le chiffre correspondant et valider la saisie avec la touche __Entrée__. A chaque saisie l'utilisateur pourra quitter le programme ou revenir au menu principal.  

### Gestion de joueurs

Ce menu permet de :  

* Créer un nouveau joueur et de le sauvegarder dans la base de données  
* Modifier un joueur présent dans la base de données  
* Supprimer un joueur présent dans la base de données

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/players_manager.png)

### Gestion des tournois  

Ce menu permet de :  

* Créer un nouveau tournoi  
* Charger un tournoi  
* Modifier les information d'un tournoi  

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/tournaments_manager.png)

| Nouveau tournoi | Ajout des joueurs | Saisie score match | Résultats |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/new_tournament.PNG">|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/add_player.PNG">|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/match_tournament.PNG">|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/results.PNG">|

#### Création d'un tournoi  

L'utilisateur devra tout d'abord saisir les informations concernant le Tournoi :  
* Son nom
* Le lieu où se déroule tournoi  
* Le type de contrôleur de temps  
* Sa description  

A la suite de cela, l'utilisateur est invité à ajouter les joueurs qui participent au tournoi. Quand cela est fait le tournoi est automatiquement sauvegardé dans la base de données des tournois et le sera à chaque saisie de l'utilisateur.  

L'application génère ensuite automatiquement les matchs du premier tour du tournoi.  
L'utilisateur est invité à saisir les résultats de chaque match du tour et quand 
celui-ci est terminé, l'application génére le tour suivant.

A la fin du dernier tour, l'application affiche les résultats du tournoi.

__A tout moment l'utilisateur peut modifier le classement d'un joueur en choisissant d'effectuer l'action *2*.__  

#### Chargement d'un tournoi  

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/tournaments_list.PNG)

L'utilisateur est invité à saisir l'__ID__ du tournoi qu'il souhaite charger. 
Si celui-si n'est pas terminé, le tournoi se poursuit, sinon les résultats du tournois sont affichés.  

#### Modification d'un tournoi  

L'utilisateur est invité à saisir l'__ID__ du tournoi qu'il souhaite modifier.  
A la suite de cela, il est peut modifier les informations de ce tournoi.

### Rapports  

L'utilisateur est invité à saisir le chiffre correspondant au rapport qu'il souhaite afficher.
Pour les rapports concernant les tournois, il sera invité à la suite, à saisir l'__ID__ correspondant au tournoi souhaité.

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/reports.png)  
# Modification des paramètres des tournois  

Au besoin plusieurs paramètres peuvent être changer :  
* Le nombre de joueurs par tournoi  
* Le nombre de tour par tournoi  
* Le chemin d'accès aux base de données (si vous souhaiter créer différentes bases de données)  

Pour cela déplacez vous dans le dossier __models__ situé dans le dossier principale de l'application, et ouvrez avec un éditeur de texte le fichier __constants.py__. Vous pourrez alors modifié ces paramètres en les remplacant.  

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/const.PNG)  

# Génération fichier flake8-html

Afin de vérifier que les directives de la PEP8 ont bien été suivi, vous pouvez générer un fichier __flake8_html__. Activez l'environnement virtuel précédemment crééet saisissez :  
`flake8 --format=html --htmldir=flake8-rapport`
Cela créera un dossier __flake8_rapport__ dans lequel se trouve le fichier __index.html__ que l'on peut ouvrir afin de vérifier le peluchage du code.


