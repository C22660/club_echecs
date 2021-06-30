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

    number_of_rounds = 4

    def __init__(self, name, place, date, time_control, description=None, players=None, rounds=None, id=None,
                 number_of_rounds=number_of_rounds):
        self.tournament = []
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
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
        new_tournament = Tournament.users.get((where('name') == self.name) & (where('place') == self.place))
        if not new_tournament:
            # ajout dans la liste tournament
            self.tournament.append([self.name, self.place, self.date, self.time_control, self.number_of_rounds,
                                    self.time_control, self.description, self.rounds, self.players])
            # ajout dans la base de données
            Tournament.users.insert({"name": self.name, "place": self.place, "date": self.date,
                                     "Controle de temps": self.time_control, "nombre de rounds": self.number_of_rounds,
                                     "description": self.description, "rounds": self.rounds, "players": self.players})

            search_id = Tournament.users.get((where('name') == self.name) & (where('place') == self.place))
            self.id = search_id.doc_id

            return True

        else:
            return False

    @classmethod
    def get_by_id(cls, id):
        """ Pour permettre la mise à jour des rounds d'un tournoi, recherche des éléments dans la base de données à
         partir de l'ID du tournoi (recréation de l'objet tournoi)"""
        data = Tournament.users.get(doc_id=id)
        return cls(name=data['name'], place=data['place'], date=data['date'], time_control=data['Controle de temps'],
                   description=data['description'], rounds=data['rounds'], players=data['players'], id=id)

    def add_players(self, player):
        self.players.append(player)
        Tournament.users.update({"players": self.players}, doc_ids=[self.id])
        return True

    def extract_players(self):
        return self.players

    def add_rounds(self, new_round):
        self.rounds.append(new_round)
        Tournament.users.update({"rounds": self.rounds}, doc_ids=[self.id])
        return True

    def start_current_round(self):
        current_round_index = len(self.rounds) - 1
        self.rounds[current_round_index][0]["lancement"] = TimeStamp.time_date_now()

    def end_current_round(self):
        current_round_index = len(self.rounds) - 1
        self.rounds[current_round_index][0]["fin"] = TimeStamp.time_date_now()

    def extract_match_to_add_scores(self):
        current_round_index = len(self.rounds) - 1
        matches = self.rounds[current_round_index][0]["matches"]
        round_number = self.rounds[current_round_index][0]["Round"]
        return matches, round_number

    def save_scored_matches(self, scored_matches):
        current_round_index = len(self.rounds) - 1
        self.rounds[current_round_index][0]["matches"] = scored_matches
        Tournament.users.update({"rounds": self.rounds}, doc_ids=[self.id])

    def number_of_rounds_decrement(self):
        rounds_remaining = self.number_of_rounds - len(self.rounds)

        return rounds_remaining

    def sum_score_of_players(self):
        current_round_index = len(self.rounds) - 1
        all_matches = []
        sum_scores = {}
        # on prépare la dictionnaire sum_score à accueillir un couple clé "ID" une valeur cumul de score
        # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for id in self.players:
            sum_scores[id] = 0

        # on récupère chaque round de match
        for each_round in self.rounds:
            total_matches = each_round[0]["matches"]
        # puis, on va chercher chaque match pour ne faire qu'une liste de tous les  couples ID Scores [[1, 7], [1, 0]]..
            for element in total_matches:
                all_matches.append(element)
        # on parcours cette liste complète, index 0
        for couple in all_matches:
            id_first_player = couple[0][0]
            score_first_player = couple[1][0]
            for key, value in sum_scores.items():
                if key == id_first_player:
                    sum_scores[key] = value+score_first_player
        # même chose pour le deuxième joueur, index 1
        for couple in all_matches:
            id_second_player = couple[0][1]
            score_second_player = couple[1][1]
            for key, value in sum_scores.items():
                if key == id_second_player:
                    sum_scores[key] = value+score_second_player

        return sum_scores

    def extract_all_tournaments(self):
        tournaments = Tournament.users.search(where('name') != "")
        for tournament in tournaments:
            id_tournament = tournament.doc_id

            return f"Le tournoi ID n°{id_tournament}, {tournament['name']}, à eu lieu à {tournament['place']} " \
                   f"en date du {tournament['date']}."

    def extract_all_matches_to_report(self):
        recap_matches_by_tournaments = []
        tournaments = Tournament.users.search(where('name') != "")

        for element in tournaments:
            id_tournament = element.doc_id
            recap_rounds = element["rounds"]
            for recap_round in recap_rounds:
                for rounds_per_tournament in recap_round:
                    recap_matches_by_tournaments.append([id_tournament, rounds_per_tournament['Round'],
                                                         rounds_per_tournament['matches']])

        return recap_matches_by_tournaments


if __name__ == '__main__':
    pass

    # # 1 liste = [{'Round': 3, 'matches': [[('1', '7'), None], [('5', '8'), None], [('4', '3'), None],
    #     [('6', '2'), None]], 'lancement': None, 'fin': None}]
    # id_current_tournament = len(Tournament.users)
    # tournoi = Tournament.get_by_id(id=id_current_tournament)
    # # print(tournoi.rounds.index)
    # tournoi.add_rounds(liste)
    # tournoi.start_current_round()
    # # print(vars(tournoi))
    # matches = tournoi.extract_match_to_add_scores()
    # # ---------
    # # # 2 saisie du score
    # # liste = [[('1', '7'), None], [('5', '8'), None], [('4', '3'), None], [('6', '2'), None]]
    # # for i in matches:
    # #     match = MatchResults(i)
    # #     print(match.get_players_by_id())
    # #     saisie = input("Saisissez l'ID gagnant ou N pour matche nul : ")
    # #     print("-"*47)
    # #     match.set_winner(saisie)
    # # results_matches = MatchResults.matches
    # # results_matches = [[('1', '7'), (1, 0)], [('5', '8'), (0, 1)], [('4', '3'), (0.5, 0.5)], [('6', '2'), (1, 0)]]
    # results_matches = [[('1', '7'), (1, 0)], [('5', '8'), (0, 1)], [('4', '3'), (0.5, 0.5)], [('6', '2'), (1, 0)]]
    # tournoi.save_scored_matches(results_matches)
    # print(tournoi.rounds)
    # # # # -------
    # id_current_tournament = len(Tournament.users)
    # tournoi = Tournament.get_by_id(id=id_current_tournament)
    # matches = tournoi.extract_match_to_add_scores()
    # print(matches)
    # for element in matches:
    #     id_first_player = element[0][0]
    #     score_first_player = element[1][0]
    #     print("joueur", id_first_player, "score", score_first_player)
    # print("second")
    # for element in matches:
    #     id_second_player = element[0][1]
    #     score_second_player = element[1][1]
    #     print("joueur", id_second_player, "score", score_second_player)
    # -----
    # id_current_tournament = len(Tournament.users)
    # tournoi = Tournament.get_by_id(id=id_current_tournament)
    # result = tournoi.sum_score_of_players()
    # for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
    #     # print(k, v)
    #     print(f"Le joueur {k} totalise {v} point(s).")
