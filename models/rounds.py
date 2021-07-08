from tools.timestamp import TimeStamp

"""etape 2 Les rounds correspondent au parties jouées (au tours)"""


class Round:
    """Création d'un round à parti des pairs de joueurs (matches)

        rendu visuel de round = [{'Round': 1, 'matches': [[('1', '7'), None], [('5', '8'), None], [('4', '3'), None],
        [('6', '2'), None]], 'lancement': None, 'fin': None}]"""

    def __init__(self, round_number, pairs=None):
        self.round = []
        self.round_number = round_number
        # liste des correspondances ??
        self.pairs = pairs
        # dates et heures, horodatage automatique
        self.start_date_time = None
        self.end_date_time = None
        self.new_round = Round.creation_new_round(self)

    def start_round(self):
        self.start_date_time = TimeStamp.time_date_now()

    def end_round(self):
        self.end_date_time = TimeStamp.time_date_now()

    def creation_new_round(self):
        """ 1 Mise en forme de self.round"""
        self.round.append({"Round": self.round_number, "matches": [], "lancement": self.start_date_time,
                           "fin": self.end_date_time})

    def add_pairs(self):
        """ 2 On ajoute 1 tuple avec les couples d'ID représentant les matches, un élément qui sera un tuple
            du résultat du matche. Exemple [('1', '7'), None]"""
        matches = []
        for i in self.pairs:
            matches.append([(i[0], i[1]), (0, 0)])
        self.round[0]["matches"] = matches
        return self.round

    def __str__(self):
        return f"Le round sera : {self.round}."


if __name__ == '__main__':
    les_matches = [['1', '7'], ['5', '8'], ['4', '3'], ['6', '2']]
    new_round = Round(1, les_matches)
    ronde = new_round.add_pairs()
    print(ronde)
    # print(new_round)
