from views import views
from models.players import Player
from models.tournaments import Tournament
from . import TournamentCreation
from . import ModificationRanking
from . import home
from controllers.RoundsController import RoundsController


# ETAPE 6 Edition des rapport
class ReportController:
    """Gère le rapport final du tournois."""

    id_tournament = len(Tournament.users)

    def __init__(self, id_tournament=id_tournament):
        self.view = views.ReportsElementsView()
        self.id_tournament = id_tournament
        self.player_by_alpha = []

    def __call__(self):
        print("'" * 70)
        print("'              M E N U   D E S   R  A  P  P  O  R  T S         "
              "      '")
        print("'" * 70)
        print("")
        wich_report = input("1: Liste de tous les acteurs \n2: Liste de tous"
                            " les joueurs d'un tournoi"
                            "\n3: Liste de tous les tournois \n4: Liste de"
                            " tous les tours et matches d'un tournoi"
                            "\n5: Retour au menu principal \nIndiquez votre"
                            " choix : ")
        good_choice = (1, 2, 3, 4, 5)
        while wich_report not in str(good_choice):
            self.view.wrong_input()
            self.__call__()

        if wich_report == str(1):
            self.all_actors()
        elif wich_report == str(2):
            self.all_players()
        elif wich_report == str(3):
            self.all_tournaments()
        elif wich_report == str(4):
            self.all_rounds_and_matches()

        actions = (("Créer un tournoi", TournamentCreation.TournamentCreationController()),
                   ("Modifier le rang d'un joueur",
                    ModificationRanking.ModificationRankingController()),
                   ("Gestion des rounds", RoundsController()),
                   ("Rapport d'un tournoi", ReportController())
                   )
        return home.HomeMenuController(actions)

    def all_actors(self):
        # # --- Liste de tous les acteurs ---
        self.view.report_all_actors_title()
        # par alpha
        actor = Player.get_by_id(id=1)
        actors_by_alpha = actor.all_actors_by_alpha()
        self.view.actors_by_alpha_view(actors_by_alpha)
        # par rang
        self.view.report_all_actors_ranking()
        actor = Player.get_by_id(id=1)
        actors_by_rank = actor.all_actors_by_ranking()
        self.view.all_actors_by_ranking_view(actors_by_rank)

        self.__call__()

    def all_players(self):
        self.view.tournements_list_view()
        # print("Parmi ces tournois :")
        result = self.search_all_tournaments()
        choice = input("Quel est l'ID du tournoi souhaité : ")
        while int(choice) not in result:
            print("Cet ID n'est pas dans la liste.")
            choice = input("Quel est l'ID du tournoi souhaité : ")
        tournoi = Tournament.get_by_id(id=int(choice))
        # --- Liste de tous les joueurs d'un tournoi ---
        self.view.players_in_tournament()
        players = tournoi.extract_players()
        print(players)
        for p in players:
            player = Player.get_by_id(id=p)
            result = player.all_players_by_alpha_and_ranking()
            self.player_by_alpha.append(result)

        # par ordre alphabétique
        result_by_alpha = sorted(self.player_by_alpha, key=lambda k: k['name'])
        self.view.players_by_alpha(result_by_alpha)

        # par classement
        result_by_ranking = sorted(self.player_by_alpha, key=lambda
                                   k: k['ranking'], reverse=True
                                   )
        self.view.players_by_ranking(result_by_ranking)

        # par nombre de points gagnés
        result = tournoi.sum_score_of_players()
        for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
            player = Player.get_by_id(id=k)
            self.view.players_by_score_print(player, v)
        self.player_by_alpha.clear()
        self.__call__()

    def search_all_tournaments(self):
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        the_tournaments = tournoi.extract_all_tournaments()
        for t in the_tournaments[0]:
            print(t + "\n")
        return the_tournaments[1]

    def all_tournaments(self):
        # --- Liste de tous les tournois ---
        self.view.tournements_list_view()
        self.search_all_tournaments()

        self.__call__()

    def all_rounds_and_matches(self):
        self.view.tournements_list_view()
        result = self.search_all_tournaments()
        choice = input("Quel est l'ID du tournoi souhaité : ")
        while int(choice) not in result:
            print("Cet ID n'est pas dans la liste.")
            choice = input("Quel est l'ID du tournoi souhaité : ")
        tournoi = Tournament.get_by_id(id=int(choice))
        # --- Liste de tous les matches et round des tournois ---
        self.view.rounds_and_matches_title()
        all_matches = tournoi.extract_all_matches_to_report()
        for component in all_matches:
            self.view.rounds_and_matches_part_1(component)
            for i in component[2]:
                self.view.rounds_and_matches_part_2(i)

        self.__call__()
