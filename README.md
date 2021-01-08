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

## Téléchargement

### Depuis ce dépot, télécharger l'archive : 

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/GitHub_Download.png)

Décompresser l'archive __Chess_Tournament-master.zip__.  

### Depuis la Source  

- Python 3.6 minimumu requis  

Dans un invite de commande, saisir :   

`git clone https://github.com/JulienConan/Chess_Tournament.git`

## Installation des dépendances requises

Se placer dans le dossier principale de l'application et saisir :

`pip install -r requirements.txt`  

## Utilisation  

Pour lancer l'application, ouvrir un invite de commande dans le dossier principale de l'application  et saisir :  

### Sur windows     
`python main.py`  
### Sur Linux   
`python3 main.py`  
### Sur MacOs   
`python[ma_version] main.py`  __[ma_version]__ correspondant à la version de python installée sur l'ordinateur de l'utilisateur.  

![](https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/main_menu.png)

Pour chaque action (aller dans un menu ou effectuer une action), l'utilisateur doit saisir le chiffre correspondant et valider la saisie avec la touche __Entrée__. A chaque saisie l'utilisateur pourra quitter le programme ou revenir au menu principale.  

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

# Génération fichier flake8-html

Afin de vérifier que les directives de la PEP8 ont bien été suivi, vous pouvez générer un un fichier flake8_html en saisissant dans un invite de commande ouvert dans le dossier principale de l'application :  
`flake8 --format=html --htmldir=flake-rapport`
Cela créera un dossier flake8_rapport dans lequel se trouve le fichier __index.html__ que l'on peut ouvrir afin de vérifier le peluchage du code.


