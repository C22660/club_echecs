from tools.timestamp import TimeStamp

"""etape 2 Les rounds correspondent au parties jouées (au tours)"""

# instance créé: ronde = Round()


class Round:
    """Création des parties"""

    round_id = 0
    rounds = []

    def __init__(self, connections):
        # l'incrementation permet de créer un nom du round via l'ID
        type(self).round_id += 1
        self.round_ID = type(self).round_id
        # liste des correspondances ??
        self.connections = connections
        # dates et heures, horodatage automatique
        self.start_date_time = None
        self.end_date_time = None
        self.ranking = None

    def start_round(self):
        self.start_date_time = TimeStamp.time_date_now()

    def end_round(self):
        self.end_date_time = TimeStamp.time_date_now()

    def add_round_inputs(self):
        self.rounds.append(["Round "+str(self.round_ID), self.connections, self.start_date_time,
                            self.end_date_time])

    def visu(self):
        print(self.ranking)


if __name__ == '__main__':
    # ronde = Round()
    # ronde.start_round()
    # ronde.end_round()
    # ronde.add_round_inputs()
    # print(ronde.rounds)
    new_round = Round([['1', '7'], ['5', '8'], ['4', '3'], ['6', '2']])
    new_round.start_round()
    new_round.end_round()
    new_round.add_round_inputs()
    print(Round.rounds)
