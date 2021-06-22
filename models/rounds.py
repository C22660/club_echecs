from tools.timestamp import TimeStamp

"""etape 2 Les rounds correspondent au parties jouées (au tours)"""

# instance créé: ronde = Round()


class Round:
    """Création des parties"""

    rounds = []

    #rounds: [{'matches': [[0, 1, None]], 'start_datetime': '2021-06-21 12:00:00', 'end_datetime': None}]

    def __init__(self, round_number, pairs=None):
        self.round_number = round_number
        # liste des correspondances ??
        self.pairs = pairs
        # dates et heures, horodatage automatique
        self.start_date_time = None
        self.end_date_time = None
        self.ranking = None
        self.new_round = Round.creation_new_round(self)

    def start_round(self):
        self.start_date_time = TimeStamp.time_date_now()

    def end_round(self):
        self.end_date_time = TimeStamp.time_date_now()

    def creation_new_round(self):
        self.rounds.append({"Round": self.round_number, "matches": [], "lancement": self.start_date_time,
                            "fin": self.end_date_time})

    def add_pairs(self):
        """On ajoute au couple d'ID représentant le match, un élément qui sera la référence du gagnant
        ou matche nul"""
        matches = []
        for i in self.pairs:
            # print(i[0], i[1])
            matches.append([i[0], i[1], None])
        self.rounds[0]["matches"] = matches
        print(matches)


            #Round.rounds[0]["matches"] = (i(0), i(1), None)

    def visu(self):
        print(self.ranking)


if __name__ == '__main__':
    # ronde = Round()
    # ronde.start_round()
    # ronde.end_round()
    # ronde.add_round_inputs()
    # print(ronde.rounds)
    matches = [['1', '7'], ['5', '8'], ['4', '3'], ['6', '2']]
    new_round = Round(1, matches)
    print(new_round.rounds)
    new_round.add_pairs()
    print(new_round.rounds)
    # for i in matches:
    #     new_round = Round(i)
    #     print(new_round.rounds)
        # new_round.start_round()
        # new_round.add_round_inputs()
        # print(Round.rounds)
