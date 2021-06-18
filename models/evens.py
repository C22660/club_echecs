from operator import attrgetter

from models.data import participants
"""Les pairs correspondent au sytème de répartition des joueurs.
    Ici, elle est basée sur le système Suisse
    à mettre dans les tournois
"""

""" prévoir un %2 de la len de liste en allere et si liste impaire, 
ne pas faire l'affectation et demander un joueur de plus"""


class Evens:

    our_players = []

    def __init__(self, serialization):
        self.serialization = serialization
        self.team = []
        self.ranking = None
        self.point = None
        self.player_ID = None

    def add_players_evens(self):
        # ajout du joueur provenant de la class Player
        self.our_players.append(self.serialization)

    def sort_players_ranking(self):
        """Tri premier tour en fonction du rang"""
        # print(self)
        # print(type(self))
        our_evens = []

        if len(self) % 2 != 0:
            # A faire un return sur méthode de gestion des anomalies
            print("Un nombre de joueur pair est nécessaire")
        else:
            liste_trie = sorted(self, key=lambda t: t.ranking, reverse=True)
            half_upper = liste_trie[:len(liste_trie) // 2]
            half_lower = liste_trie[len(liste_trie) // 2:]

            for i in range(len(half_lower)):
                our_evens.append([half_upper[i], half_lower[i]])

        return our_evens

    def sort_players_points(self):
        """Tri tours suivants en fonction des points et, si égalité, du rang"""

        # Solution source docs python, Guide pour le tri, Stabilité des tris et tris complexes
        s = sorted(self, key=attrgetter("ranking"), reverse=True)
        our_evens = sorted(s, key=attrgetter("point"), reverse=True)

        return our_evens

    def make_a_random(self):
        """Tire au sort les couleurs"""
        pass

if __name__ == '__main__':
    pass