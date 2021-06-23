from tinydb import TinyDB, where
from pathlib import Path

from tools.timestamp import TimeStamp

"""Etape 3 Les tournaments correspondent au tournois
à accès aux rounds et aux pairs"""


# à 1 attibut liste round qui contient une liste d'objets round [round(1), round(2)]




class Tournament:
    """Gère la création du tounroi et son ajout dans la base"""

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    users = DB.table("Tournaments")

    def __init__(self, name, place, date, time_control, description=None, players=None, rounds=None, id=None):
        self.tournament = []
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.time_control = time_control
        self.description = description
        # les elements players et rounds seront ajoutés via la méthode de class (d'où le if/else)
        if players:
            self.players = players
        else:
            self.players = []
        if rounds:
            self.rounds = rounds
        else:
            self.rounds = []
        self.id = id

    def add_tournament_inputs(self):
        """Verifie si le tournoi n'est pas dans la base et sinon, l'ajoute dans la base et la
        liste tournament"""
        # vérification que le tournoi n'existe pas dans la base
        if not Tournament.users.get((where('name') == self.name) & (where('place') == self.place)):
            # ajout dans la liste tournament
            self.tournament.append([self.name, self.place, self.date, self.time_control, self.number_of_rounds,
                                    self.time_control, self.description, self.rounds, self.players])
            # ajout dans la base de données
            Tournament.users.insert({"name": self.name, "place": self.place, "date": self.date,
                                     "Controle de temps": self.time_control, "nombre de rounds": self.number_of_rounds,
                                     "description": self.description, "rounds": self.rounds, "players": self.players})
            return True

        else:
            return False

    @classmethod
    def get_by_id(cls, id):
        """ Pour permettre la mise à jour des rounds d'un tournoi, recherche les éléments dans la base de donnée à
         partir de l'ID du tournoi (recréation de l'objet tournoi)"""
        data = Tournament.users.get(doc_id=id)
        return cls(name=data['name'], place=data['place'], date=data['date'], time_control=data['Controle de temps'],
                   description=data['description'], rounds=data['rounds'], players=data['players'], id=id)

    def add_rounds(self, new_round):
        self.rounds.append(new_round)
        Tournament.users.update({"rounds": self.rounds}, doc_ids=[self.id])
        return True

    def start_current_round(self, round_index=None):
        round_index = len(self.rounds)-1
        self.rounds[round_index][0]["lancement"] = TimeStamp.time_date_now()

    def end_current_round(self):
        round_index = len(self.rounds) - 1
        self.rounds[round_index][0]["fin"] = TimeStamp.time_date_now()

    def add_score(self, round_index, match_index):
        """1 si le premier joueur de la liste est gagnant, 2 si c'est le troisième, 3 si match nul"""
        pass

if __name__ == '__main__':
    liste = [{'Round': 3, 'matches': [['1', '7', None], ['5', '8', None], ['4', '3', None],
        ['6', '2', None]], 'lancement': None, 'fin': None}]
    tournoi = tournament = Tournament.get_by_id(id=1)
    # print(tournoi.rounds.index)
    # tournoi.add_rounds(liste)
    tournoi.start_current_round()

    print(vars(tournament))