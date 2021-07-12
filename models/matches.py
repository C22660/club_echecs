from pathlib import Path

from tinydb import TinyDB


class MatchResults:
    """Centralise les résultats avant de les renvoyer vers la création des
    paires."""

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
        self.matches_scored = []

    def get_players_by_id(self):
        """Permet l'affichage de l'indentité du joueur et non seulement son
        ID."""
        self.player_1_id = self.matche[0][0]
        self.player_2_id = self.matche[0][1]
        # A partir des Id des joueurs, collecte les infos dans la base joueurs
        data_1 = MatchResults.users.get(doc_id=int(self.player_1_id))
        data_2 = MatchResults.users.get(doc_id=int(self.player_2_id))
        self.player_1_name = data_1["name"]
        self.player_1_first_name = data_1["first_name"]
        self.player_2_name = data_2["name"]
        self.player_2_first_name = data_2["first_name"]
        # retroune un print lisible du résutat à saisir
        return f"{self.player_1_first_name} {self.player_1_name}," \
               f" ID {self.player_1_id}  <= & => " \
               f" {self.player_2_first_name} {self.player_2_name}," \
               f" ID {self.player_2_id}"

    def check_input_winner(self):
        saisie_id = input("Saisissez l'ID gagnant ou N pour matche nul : ")
        print("-" * 70)
        good_inputs = (str(self.player_1_id), str(self.player_2_id), 'n', 'N')
        if saisie_id not in good_inputs:
            print(f"Attention, la saisie doit être un des ID"
                  f" ({self.player_1_id} ou {self.player_2_id})"
                  f" ou N (pour nul)")
            self.check_input_winner()
        else:
            self.set_winner(saisie_id)

    def set_winner(self, winner):
        if winner == str(self.player_1_id):
            self.score = (1, 0)
        elif winner == str(self.player_2_id):
            self.score = (0, 1)
        else:
            self.score = (0.5, 0.5)

        self.matche[1] = self.score
        self.matches.append(self.matche)
