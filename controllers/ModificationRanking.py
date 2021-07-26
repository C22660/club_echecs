import time

from views import views
from models.players import Player
from . import TournamentCreation
from . import home
from controllers.ReportController import ReportController
from . import PlayersCreation
from controllers.RoundsController import RoundsController


# OUTIL SI BESOIN Modification du rang d'un joueur
class ModificationRankingController:
    """Permet de modifier le rang d'un joueur."""

    def __init__(self):
        self.view = views.PlayersElementsView()

    def __call__(self):
        self.view.get_new_ranking()
        name = self.view.get_player_name()
        first_name = self.view.get_player_first_name()
        birth = self.view.get_player_birth()
        ranking = self.view.get_player_ranking()
        player_modified = Player(name, first_name, birth, ranking)
        check_modification = player_modified.modifie_player_ranking()
        if check_modification:
            self.view.ranking_modified()
        else:
            self.view.player_not_found()

        time.sleep(2)
        actions = (("Créer un tournoi", TournamentCreation.TournamentCreationController()),
                   ("Saisir la liste des joueurs", PlayersCreation.PlayersCreationController()),
                   ("Modifier le rang d'un joueur", ModificationRankingController()),
                   ("Gestion des rounds", RoundsController()),
                   ("Rapport du tournoi", ReportController())
                   )

        return home.HomeMenuController(actions)
