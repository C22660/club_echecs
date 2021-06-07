# Application de gestion d'un tournoi d'échecs

Ce programme à pour objet de permettre à un club d'échecs de gérer ses tournois :
- Saisie manuelle des caractéristiques du tournoi. 
  nom, lieu, date, nombre de tours (par défaut à 4), le mode de cotrôle de temps (en simple information),
  des remarques générales
- Saisie manuelle des informations relatives aux joueurs.
  Nom, Prénom, Date de naissance, sexe, classement, nombre de points (à partir du 2ème match)
- A la fin du tournoi, saisie manuelle des classements des joueurs.
- Le gestionnaire peut modifier le classement d'un joueur à tout moment.

Gestion automatique des paires de joueurs :
- Selon le classement des joueurs au premier tour.
- Selon nombre de points sur les tours suivants (ou classement si égalité)

Génération d'un rapport final


## Information
Dans ce programme, la génération des paires s'inspire de l'esprit du système suisse
mais ne prétend pas en être la parfaite application.
L'équilibre des couleurs des jeux n'est pas géré par le programme mais via tirage au sort
par le gestionnaire du tournoi.

## Techologies
Python 3.9
Package ajouté : TinyDB

## Auteur
Cédric M
