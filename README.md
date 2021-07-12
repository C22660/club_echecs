# Application de gestion d'un tournoi d'échecs

Ce programme à pour objet de permettre à un club d'échecs de gérer ses tournois :
- Saisie manuelle des caractéristiques du tournoi.   
  nom, lieu, date(s), nombre de tours (par défaut à 4, modifiable dans models\Tournaments), le mode de contrôle de temps (en simple information),
  des remarques générales facultatives.
- Saisie manuelle des informations relatives aux joueurs.  
  Nom, Prénom, Date de naissance, sexe, classement, nombre de points (à partir du 2ème match)
- A la fin du tournoi, saisie manuelle des classements des joueurs.
- Le gestionnaire peut modifier le classement d'un joueur à tout moment.

Gestion automatique des paires de joueurs :
- Selon le classement des joueurs au premier tour.
- Selon nombre de points sur les tours suivants (ou classement si égalité)

Génération d'un rapport final


## Informations
Dans ce programme, la génération des paires s'inspire de l'esprit du système suisse
mais ne prétend pas en être la parfaite application.  
L'équilibre des couleurs des jeux n'est pas géré par le programme mais via tirage au sort
par le gestionnaire du tournoi.

**Configurations et exécution du programme**
Le promramme sera executé directement depuis python -m club_echecs

Etape 1 : Création d'un tournoi (participants compris), ce qui va générer les
premières paires de joueurs

Etape 2 : Vous lancez, stoppez les rounds et saisissez les résultats depuis le
menu Gestion des rounds

**Génération d'un nouveau rapport flake8**
A partir du terminal, taper la commande suivante :
flake8 --format=html --htmldir=flake-report

## Techologies
Python 3.9  
Package ajouté : TinyDB

## Auteur
Cédric M
