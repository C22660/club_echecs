from pathlib import Path

from tinydb import TinyDB, where


class Player:
    """Gère la création des joueurs et leur ajout dans la base."""

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    users = DB.table("Players")

    def __init__(self, name=None, first_name=None, birth=None, ranking=None,
                 sex=None, point=0, id=None):
        self.name = name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.ranking = int(ranking)
        self.point = point
        self.id = id

    def add_player_inputs(self):
        """1 Verifie si le joueur n'est pas dans la base et sinon ajout et si
        oui, mise à 0 des points."""
        # vérification que le joueur n'existe pas dans la base joueur
        if not self.player_exists():
            Player.users.insert({"name": self.name,
                                 "first_name": self.first_name,
                                 "birth": self.birth, "sex": self.sex,
                                 "ranking": self.ranking,
                                 "points": self.point})
            return True

        else:
            Player.users.update({"ranking": self.ranking},
                                (where('name') == self.name) &
                                (where("first_name") == self.first_name) &
                                (where('birth') == self.birth)
                                )
            Player.users.update({"points": self.point},
                                (where('name') == self.name) &
                                (where("first_name") == self.first_name) &
                                (where('birth') == self.birth)
                                )

            return False

    def serialization_players(self):
        """A partir de la base de données, collecte les éléments nécessaires à
        la création des paires."""
        current_add = Player.users.get((where('name') == self.name) &
                                       (where('first_name') == self.first_name)
                                       &
                                       (where('birth') == self.birth)
                                       )
        # adresse à evens les données necessaires à la constitution des paires
        self.id = current_add.doc_id
        team_serialized = {"points": self.point, "ranking": self.ranking,
                           "player_ID": self.id, "name": self.name,
                           "first_name": self.first_name
                           }

        return team_serialized

    @classmethod
    def get_by_id(cls, id):
        """Pour permettre la mise à jour des points d'un joueur avant envoi
        pour création des nouvelles paires, recherche les éléments dans la base
        de donnée à partir de l'ID et les retourne à la class Player
        (recréation des joueurs)"""
        data = Player.users.get(doc_id=id)
        return cls(name=data['name'], first_name=data['first_name'],
                   birth=data['birth'],
                   ranking=data['ranking'], point=data['points'], id=id)

    @property
    def player_found(self):
        # retourne l'élément (comme si self.player_found) ou None si
        # l'utilisateur n'existe pas
        return Player.users.get((where('name') == self.name) &
                                (where('first_name') == self.first_name) &
                                (where('birth') == self.birth))

    def __str__(self):
        return f"le joueur ID {self.id} = {self.name} {self.first_name}," \
               f" né le {self.birth}, classé {self.ranking}"

    def player_exists(self):
        # Converti le retour de player_found en bouléen pour avoir True si
        # données, ou False si pas de données
        return bool(self.player_found)

    def modifie_player_ranking(self):
        if self.player_exists():
            Player.users.update({"ranking": self.ranking},
                                (where('name') == self.name) &
                                (where("first_name") == self.first_name) &
                                (where('birth') == self.birth))
            return True

    def modifie_player_point(self, point):
        self.point = point
        if self.player_exists():
            Player.users.update({"points": self.point},
                                (where('name') == self.name) &
                                (where("first_name") == self.first_name) &
                                (where('birth') == self.birth)
                                )
            return True

    def all_actors_by_alpha(self):
        actors = Player.users.search(where('name') != "")
        actors_by_alpha = sorted(actors, key=lambda k: k['name'])

        return actors_by_alpha

    def all_actors_by_ranking(self):
        actors = Player.users.search(where('ranking') != "")
        actors_by_rank = sorted(actors, key=lambda k: k['ranking'],
                                reverse=True)

        return actors_by_rank

    def all_players_by_alpha_and_ranking(self):
        one_player = {"ID": self.id, "name": self.name,
                      "first_name": self.first_name, "ranking": self.ranking}
        return one_player
