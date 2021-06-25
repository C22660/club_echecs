from tinydb import TinyDB, where
from pathlib import Path


class MatchResults:
    """Centralise les résultats avant de les renvoyer vers la création des paires"""

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    users = DB.table("Players")

    matches = []

    def __init__(self, matche):
        self.matche = matche
        self.player_1_name = None
        self.player_1_first_name = None
        self.player_1_id = None
        self.player_2_name = None
        self.player_2_first_name = None
        self.player_2_id = None
        self.score = 0

    def get_players_by_id(self):
        """ Permet l'affichage de l'indentité du joueur et non seulement son ID"""
        self.player_1_id = self.matche[0][0]
        self.player_2_id = self.matche[0][1]
        data_1 = MatchResults.users.get(doc_id=int(self.player_1_id))
        data_2 = MatchResults.users.get(doc_id=int(self.player_2_id))
        # cls(name=data['name'], first_name=data['first_name'], birth=data['birth'],
        #     ranking=data['ranking'], point=data['points'], id=id)
        self.player_1_name = data_1["name"]
        self.player_1_first_name = data_1["first_name"]
        self.player_2_name = data_2["name"]
        self.player_2_first_name = data_2["first_name"]

        return f"{self.player_1_first_name} {self.player_1_name}, ID {self.player_1_id}  <= & => " \
               f" {self.player_2_first_name} {self.player_2_name}, ID {self.player_2_id}"


    def set_winner(self, winner):
        if winner not in (self.player_1_id, self.player_2_id, 'n', 'N'):
            return False
        if winner == self.player_1_id:
            self.score = (1, 0)
            # self.players[0].add_win()
        elif winner == self.player_2_id:
            self.score = (0, 1)
            # self.players[1].add_win()
        else:
            self.score = (0.5, 0.5)
            # self.players[0].add_tie()
            # self.players[1].add_tie()

        self.matche[1] = self.score
        self.matches.append(self.matche)

if __name__ == '__main__':
    # ---------
    # saisie du score
    liste = [[('1', '7'), None], [('5', '8'), None], [('4', '3'), None], [('6', '2'), None]]
    for i in liste:
        match = MatchResults(i)
        print(match.get_players_by_id())
        saisie = input("Saisissez l'ID gagnant ou N pour matche nul : ")
        print("-"*47)
        match.set_winner(saisie)
    results_matches = MatchResults.matches
    print(results_matches)
    # tournoi.save_scored_matches(results_matches)
    # print(tournoi.rounds)