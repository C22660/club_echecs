import time

from views import views
from models.players import Player
from models.pairs import Pair
from models.tournaments import Tournament
from models.rounds import Round
from tools.inputs_check import check_names, check_date
from . import TournamentCreation
from controllers.ModificationRanking import ModificationRankingController
from . import home
from controllers.ReportController import ReportController
from controllers.RoundsController import RoundsController


# ETAPE 2 Saisie des joueurs
class PlayersCreationController:
    """Contrôleur responsable de gérer le menu de  création des joueurs du
    tournoi et formation des premières paires de joueur.
    Eléments joueurs sauvegardés dans la base joueurs. Eléments des
    paires (et round) sauvegardés dans la base tournoi. Passe ensuite la
    main au contrôleur des rounds.
    """

    def __init__(self):
        self.view = views.PlayersElementsView()

    def __call__(self):
        # 1 générer les inputs concernant les joueurs
        number_of_players = self.view.size_team()
        while not number_of_players.isdigit()\
                or not int(number_of_players) % 2 == 0 or not \
                int(number_of_players) != 0:
            self.view.pair_mandatory()
            number_of_players = self.view.size_team()
        counter = 1
        while counter < int(number_of_players) + 1:
            addition = PlayersCreationController.player_addition(self, counter)
            # 2 instancier un joueur
            new_player = Player(*addition)
            add_data_base = new_player.add_player_inputs()
            if not add_data_base:
                self.view.info_player_present()

            players_serialized = new_player.serialization_players()

            # 3 ajout du joueur sérialisé dans la class Pair
            preparation_even = Pair(players_serialized)
            preparation_even.add_players_pairs()

            # 4 ajout du joueur dans la class Tournament
            id_current_tournament = len(Tournament.users)
            tournoi = Tournament.get_by_id(id=id_current_tournament)
            tournoi.add_players(new_player.id)
            counter += 1
        # 5 Une fois les paires effectuées, affichage à l'écran
        our_pairs = preparation_even.sort_players_ranking()
        self.view.first_players_pair()
        for couple in our_pairs[1]:
            self.view.couple_in_our_pairs(couple[0], couple[1])
        print("*" * 70)
        # 6 passage de ces paires à la class Round
        new_round = Round(1, our_pairs[0])

        # 7 on récupère les rondes sous la bonne mise en forme, et on l'adresse
        # à Tournament la class Tournament est "réveillée" par la @classmethode
        # et récupère les infos contenues dans sa base
        rondes = new_round.add_pairs()
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        tournoi.add_rounds(rondes)

        # return MatchesController()
        time.sleep(3)
        actions = (("Créer un tournoi", TournamentCreation.TournamentCreationController()),
                   ("Modifier le rang d'un joueur",
                    ModificationRankingController()),
                   ("Gestion des rounds", RoundsController()),
                   ("Rapport d'un tournoi", ReportController())
                   )
        return home.HomeMenuController(actions)

    def player_addition(self, counter):
        """permet de répéter la collecte de l'ensemble des éléments d'un joueur
        avec, en argument, le numéro du joueur en cours de sa saisie pour que
        le gestionnaire sache où il en est (n'est pas l'ID joueur) via counter
        issu de la class Player."""

        self.view = views.PlayersElementsView(counter)
        self.view.get_player_elements()
        name = self.view.get_player_name()
        while not check_names(name):
            self.view.check_player_name()
            name = self.view.get_player_name()
        first_name = self.view.get_player_first_name()
        while not check_names(first_name):
            self.view.check_player_first_name()
            first_name = self.view.get_player_first_name()
        birth = self.view.get_player_birth()
        while not check_date(birth):
            self.view.check_player_birth()
            birth = self.view.get_player_birth()
        sex = self.view.get_player_sex()
        ranking = self.view.get_player_ranking()
        while not ranking.isdigit():
            self.view.check_player_ranking()
            ranking = self.view.get_player_ranking()
        return name, first_name, birth, ranking, sex
