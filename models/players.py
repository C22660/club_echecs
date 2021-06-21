import re
import string
from tinydb import TinyDB, Query, where
from pathlib import Path


import json
import os
# import logging

from models.pair import Pair
from models.pair import Pair


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")

# LOGGER = logging.getLogger()

class Player:
    """Gère la création des joueurs et leur ajout dans la base"""

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    users = DB.table("Players")
    db_content = Query()

    team_players = []

    def __init__(self, name, first_name, birth, point='0', ranking=None,sex=None):
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.ranking = ranking
        self.point = point

        # création, lors de l'init, d'une liste des joueurs
        # avec le nombre de point par défaut à 0 pour la première partie
        # self.team_players.append(self)

    def add_player_inputs(self):
        """Verifie si le joueur n'est pas dans la base et sinon, l'ajoute dans la base et la
        liste team player"""
        # vérification que le joueur n'existe pas dans la base joueur (avec where et pas query)
        if not Player.users.get((where('name') == self.name) & (where('first_name') == self.first_name) &
                      (where('birth') == self.birth)):
            # ajout dans la liste team_player
            self.team_players.append([self.name, self.first_name, self.birth, self.sex, self.ranking, self.point])
            # ajout dans la base de données
            Player.users.insert({"name": self.name, "first_name": self.first_name, "birth": self.birth,
                                 "ranking": self.ranking, "points": self.point})
            return True

        else:
            return False

    def serialization_players(self):
        # Pour récupérer l'ID du player dans la base après ajout,
        # on le recherche dans la bse
        current_add = Player.users.get((where('name') == self.name) & (where('first_name') == self.first_name) &
                      (where('birth') == self.birth))
        # adresse à evens les données necessaires à la constitution des paires
        team_serialized = {"points": self.point, "ranking": self.ranking,
                            "player_ID": str(current_add.doc_id)}
        # return type(current_add)
        return team_serialized

    def generate_first_team(self):
        """Adresse la liste des joueurs à Evens pour création des premières paires de joueurs.
        """
        # for i in range(len(self.team_players)):
        #     print(self.team_players[i].index(2,4))
        # # for i in self.team_players:
        # # for i in self.team_players:
        # #     return self.point, self.ranking, self.player_ID
        # return self.team_players


        return Pair.sort_players_ranking(self.team_players)

    def generate_another_teams(self):
        """Adresse la liste des joueurs à Evens pour création des paires suivantes.
        """
        return Pair.sort_players_points(self.team_players)

    def __str__(self):
        return f"le joueur n°{self.player_ID} = {self.name} {self.first_name}, né le {self.birth}, est classé {self.ranking}"

    def modifie_player_ranking(self):
        Player.users.update({"ranking": self.ranking}, (where('name') == self.name) & (where("first_name") == self.first_name)
                            & (where('birth') == self.birth))
        return True


