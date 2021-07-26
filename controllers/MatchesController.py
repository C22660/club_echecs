import time

from views import views
from models.tournaments import Tournament
from models.matches import MatchResults
from . import TournamentCreation
from . import ModificationRanking
from . import home
from . import RoundsController
from . import ReportController


# ETAPE 5 Gestion des matches
class MatchesController:
    """Contrôle le lancement et l'arrêt des macthes, gère l'ajout des résultats
    et leur sauvegarde dans la base du tournoi en cours (round
    correspondant)"""

    def __init__(self):
        self.view = views.MatchesElementsView()

    def __call__(self):
        # la class Tournament est "réveillée" par la @classmethode et récupère
        # les infos contenues dans sa base
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        # on démarre les matches et donc on ajoute l'heure et la date de
        # démarrage
        while True:
            print("")
            lancement = input("Quand vous souhaitez lancer les matches, "
                              "saisissez G (comme Go) : ")
            if lancement not in ("g", "G"):
                self.view.wrong_input()
            else:
                tournoi.start_current_round()
                break
        self.view.game_launched()
        # 10 on arrête le jeux quand les matches sont terminés
        while True:
            stop = input("Quans vous souhaitez arrêter les matches, saisissez"
                         " S (comme Stop) : ")
            if stop in ("s", "S"):
                tournoi.end_current_round()
                break
            else:
                self.view.wrong_input()
        self.view.game_finished()
        # on récupère dans le round de la base tournoi, la partie relative
        # au matches
        matches = tournoi.extract_match_to_add_scores()
        # Le gestionnaire va saisir les scores
        self.view.results_input_announcement()
        # Remise à vide de l'attribut matches=[] de class MartchResult
        MatchResults.matches = []
        for i in matches[0]:
            match = MatchResults(i)
            print(match.get_players_by_id())
            match.check_input_winner()
        results_matches = MatchResults.matches
        tournoi.save_scored_matches(results_matches)
        self.view.input_results_finished()
        time.sleep(2)
        actions = (("Créer un tournoi", TournamentCreation.TournamentCreationController()),
                   ("Modifier le rang d'un joueur",
                    ModificationRanking.ModificationRankingController()),
                   ("Gestion des rounds", RoundsController.RoundsController()),
                   ("Rapport d'un tournoi", ReportController.ReportController())
                   )
        return home.HomeMenuController(actions)
