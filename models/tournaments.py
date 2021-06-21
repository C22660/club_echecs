from tinydb import TinyDB, Query, where
from pathlib import Path

"""Etape 3 Les tournaments correspondent au tournois
à accès aux rounds et aux pairs"""


# à 1 attibut liste round qui contient une liste d'objets round [round(1), round(2)]




class Tournament:
    """Gère la création du tounroi et son ajout dans la base"""

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    users = DB.table("Tournaments")

    def __init__(self, name, place, date, time_control, description=None):
        self.tournament = []
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.rounds = []
        self.time_control = time_control
        self.description = description

    def add_tournament_inputs(self):
        """Verifie si le tournoi n'est pas dans la base et sinon, l'ajoute dans la base et la
        liste tournament"""
        # vérification que le tournoi n'existe pas dans la base
        if not Tournament.users.get((where('name') == self.name) & (where('place') == self.place)):
            # ajout dans la liste tournament
            self.tournament.append([self.name, self.place, self.date, self.time_control, self.number_of_rounds,
                                    self.description])
            # ajout dans la base de données
            Tournament.users.insert({"name": self.name, "place": self.place, "date": self.date,
                                     "Controle de temps": self.time_control, "nombre de round": self.number_of_rounds,
                                     "description": self.description})
            return True

        else:
            return False
        # self.tournament.append([self.name, self.place, self.date])
