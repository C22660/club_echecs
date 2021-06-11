"""Etape 3 Les tournaments correspondent au tournois
à accès aux rounds et aux pairs"""


# à 1 attibut liste round qui contient une liste d'objets round [round(1), round(2)]




class Tournament:

    def __init__(self, name, place, date):
        self.tournament = []
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.rounds = []

    def add_tournament_inputs(self):
        self.tournament.append([self.name, self.place, self.date])
