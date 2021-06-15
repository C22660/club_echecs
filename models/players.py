"""etapes"""

import json
import os
import logging

from models.evens import Evens

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")

LOGGER = logging.getLogger()

class Player:
    """Docstring"""


    player_id = 0
    serialized_player = {}
    team_players = []

    def __init__(self, name, first_name, birth, sex, ranking, point='0'):
        # l'incrementation ne fonctionne qui si saisie de tous les joueurs en même temps
        type(self).player_id += 1
        self.player_ID = type(self).player_id
        # self.team_players = []
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
        self.team_players.append(["Player-ID "+str(self.player_ID), self.name, self.first_name,
                                  self.birth, self.sex, self.ranking, self.point])

    def generate_first_team(self):
        """Adresse la liste des joueurs à Evens pour création des premières paires de joueurs.
        """
        return Evens.sort_players_ranking(self.team_players)

    def generate_another_teams(self):
        """Adresse la liste des joueurs à Evens pour création des paires suivantes.
        """
        return Evens.sort_players_points(self.team_players)

    def __str__(self):
        # return f"le joueur n°{self.player_ID} = {self.name} {self.first_name}, né le {self.birth}, est classé {self.ranking}"
        return self.team_players

    def generate_even(self):
        """adresse un mix id joueur et rang à la création de pairs"""


    def add_player(self):
        Player.player_id +=1
        serialized_player = {"name": self.name, "first_name": self.first_name, "birth": self.birth,
        "sex": self.sex, "ranking": self.ranking
                             }
        print(serialized_player["ranking"])

        # self.all_players[Player.player_id][serialized_player]

    def modifie_player_ranking(self):
        pass

    def serialized(self):
        pass

    # def save_players(self):
    #     chemin = os.path.join(DATA_DIR, "players.json")
    #     if not os.path.exists(DATA_DIR):
    #         os.makedirs(DATA_DIR)
    #
    #     with open(chemin, "a") as f:
    #         # json.dump(self.players, f, indent=4)
    #         json.dump(self.__dict__, f, indent=4)
    #     # utiliser une class person Encoder(json.JSONEncoder) et json.dump(..., f, cls=personEncoder) ?


        # return True


