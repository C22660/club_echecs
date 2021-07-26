import time

from views import views
from models.players import Player
from models.pairs import Pair
from models.tournaments import Tournament
from models.rounds import Round
from . import TournamentCreation
from . import ModificationRanking
from controllers.MatchesController import MatchesController
from . import home
from . import ReportController


# ETAPE 3 Gestion des rounds
class RoundsController:
    """une fois les premiers matches réalisés, collecte la synthèse des matches
    depuis la base tournoi et met à jour les scores dans la class joueurs pour
    générer de nouvelles paires, puis un nouveau round.
    Par défaut, l'id du tournoi est le tournoi en cours, soit le dernier
    des tournois enregistrés
    """

    def __init__(self):
        self.tournaments = None
        self.view = views.RoundsElementsView()

    def __call__(self):
        # On initialise la class Tournament pour récupérer l'ensemble des ID
        # des tournois enregistrés
        tournoi = Tournament.get_by_id(id=1)
        self.tournaments = tournoi.search_id_tournaments()

        # On isole l'Id du tournoi en cours pour instancier un tounoi en cours
        id_current_tournament = self.tournaments[-1]
        current_tournament = Tournament.get_by_id(id=id_current_tournament)
        result = current_tournament.extract_match_to_add_scores()
        # On récupère le compteur des rounds
        rounds_remaining = current_tournament.number_of_rounds_decrement()
        if rounds_remaining == 0:
            self.view.no_round_remaining()
            time.sleep(3)
            actions = (("Créer un tournoi", TournamentCreation.TournamentCreationController()),
                       ("Modifier le rang d'un joueur",
                        ModificationRanking.ModificationRankingController()),
                       ("Gestion des rounds", RoundsController()),
                       ("Rapport d'un tournoi", ReportController.ReportController())
                       )
            return home.HomeMenuController(actions)

        elif tournoi.number_of_rounds == rounds_remaining:
            # Alors, les premières paires n'ont pas été encore jouées
            number = tournoi.number_of_rounds
            self.view.all_rounds_remaining(number)
            return MatchesController
        else:
            # Sinon, réalisation de nouvelles paires de joueurs
            self.view.how_many_rounds(rounds_remaining)
            # result comprend une liste des matches et le numéro du round
            matches = result[0]
            round_number = result[1]
            # Remise à 0 de l'attribut de class our_players
            Pair.our_players = []
            for element in matches:
                id_first_player = element[0][0]
                score_first_player = element[1][0]
                player = Player.get_by_id(id=id_first_player)
                player.modifie_player_point(score_first_player)
                player_serialized = player.serialization_players()
                # ajout du joueur sérialisé dans la class Pair
                preparation_even = Pair(player_serialized)
                preparation_even.add_players_pairs()
            for element in matches:
                id_second_player = element[0][1]
                score_second_player = element[1][1]
                player = Player.get_by_id(id=id_second_player)
                player.modifie_player_point(score_second_player)
                player_serialized = player.serialization_players()
                # ajout du joueur sérialisé dans la class Pair
                preparation_even = Pair(player_serialized)
                preparation_even.add_players_pairs()

            # Une fois les paires effectuées (avec les points puis rangs si
            # nécessaire, affichage à l'écran
            our_pairs = preparation_even.sort_players_points()
            self.view.print_pairs(our_pairs[1])

            # passage de ces paires à la class Round
            new_round = Round(round_number + 1, our_pairs[0])

            # on récupère les rondes sous la bonne mise en forme, et on
            # l'adresse à Tournament
            # la class Tournament est "réveillée" par la @classmethode et
            # récupère les infos contenues dans sa base
            rondes = new_round.add_pairs()
            id_current_tournament = len(Tournament.users)
            tournoi = Tournament.get_by_id(id=id_current_tournament)
            tournoi.add_rounds(rondes)

            return MatchesController()
