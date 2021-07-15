"""Les pairs correspondent au sytème de répartition des joueurs.

Ici, elle est basée sur le système Suisse à mettre dans les tournois
"""


class Pair:

    our_players = []

    def __init__(self, serialization=None):
        self.serialization = serialization
        self.team = []
        self.ranking = None
        self.point = None
        self.player_ID = None
        self.our_evens = []
        self.our_evens_with_name = []

    def add_players_pairs(self):
        # ajout du joueur provenant de la class Player
        self.our_players.append(self.serialization)

    def sort_players_ranking(self):
        """Tri premier tour en fonction du rang."""
        our_evens = []
        our_evens_with_name = []

        # tri selon le rang
        liste_trie = sorted(self.our_players, key=lambda k: k['ranking'],
                            reverse=True)

        # utilisation de zip pour partager la liste en deux et affecter les
        # joueurs dans l'ordre de chaques listes (basée sur la longeur de la
        # liste au lieu d'un index fixe)
        for first_player, second_player in zip(liste_trie,
                                               liste_trie
                                               [len(liste_trie) // 2:]):
            our_evens.append([first_player["player_ID"],
                              second_player["player_ID"]])
            our_evens_with_name.append([(first_player["player_ID"],
                                         first_player["name"],
                                         first_player["first_name"]),
                                        (second_player["player_ID"],
                                         second_player["name"],
                                         second_player["first_name"])
                                        ])

        return our_evens, our_evens_with_name

    def sort_players_points(self):
        """Tri tours suivants en fonction des points et, si égalité, du
        rang."""
        our_evens = []
        our_evens_with_name = []

        s = sorted(self.our_players, key=lambda k: k['ranking'], reverse=True)
        liste_trie = sorted(s, key=lambda k: k['points'], reverse=True)

        # utilisation de zip pour partager la liste en deux et affecter les
        # joueurs dans l'ordre
        # de chaques listes (basée sur la longeur de la liste au lieu
        # d'un index fixe)
        for first_player, second_player in zip(liste_trie,
                                               liste_trie
                                               [len(liste_trie) // 2:]):
            our_evens.append([first_player["player_ID"],
                              second_player["player_ID"]])
            our_evens_with_name.append([(first_player["player_ID"],
                                         first_player["name"],
                                         first_player["first_name"]),
                                        (second_player["player_ID"],
                                         second_player["name"],
                                         second_player["first_name"])
                                        ])

        return our_evens, our_evens_with_name
