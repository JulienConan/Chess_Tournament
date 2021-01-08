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

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/players_menu.jpeg"> |<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/reports.jpeg">|<img width="1604" alt="screen shot 2017-08-07 at 12 18 15 pm" src="https://raw.githubusercontent.com/JulienConan/Chess_Tournament/master/screenshots/tournaments_menu.jpeg)">|
Pour chaque action (aller dans un menu ou effectuer une action), l'utilisateur doit saisir le chiffre correspondant et valider la saisie avec la touche __Entrée__. De plus à chaque saisie l'utilisateur pourra quitter le programme ou revenir au menu principale.  



