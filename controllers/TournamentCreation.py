from views import views
from models.pairs import Pair
from models.tournaments import Tournament
from tools.inputs_check import check_names, check_date
from controllers.PlayersCreation import PlayersCreationController


# ETAPE 1 Création d'un nouveau tournoi
class TournamentCreationController:
    """Contrôleur responsable de gérer le menu de  création d'un nouveau
    tournoi (nom, lieu, date(s), type de contrôle de temps (pour info), et
    commentaire éventuel).
    Eléments sauvegardés dans la base tournoi. Passe ensuite la main au
    contrôleur des joueurs.
    """

    def __init__(self):
        self.view = views.TournamentCreationView()

    def __call__(self):
        # 1 générer les inputs
        self.view.get_tournament_elements()
        name = self.view.get_tournament_name()
        while not check_names(name):
            self.view.check_name_view()
            name = self.view.get_tournament_name()
        place = self.view.get_tournament_place()
        while not check_names(place):
            self.view.check_place_view()
            place = self.view.get_tournament_place()
        start_date = self.view.get_tournament_start_date()
        while not check_date(start_date):
            self.view.check_start_date_view()
            start_date = self.view.get_tournament_start_date()
        end_date = self.view.get_tournament_end_date()
        while not check_date(end_date):
            self.view.check_end_date_view()
            end_date = self.view.get_tournament_end_date()
        time_control = self.view.get_tournament_time()
        description = self.view.get_trournament_description()

        new_tournament = Tournament(name, place, start_date, end_date,
                                    time_control, description)
        enregistrement = new_tournament.add_tournament_inputs()
        if enregistrement:
            numero = new_tournament.id
            self.view.info_tournament_recorded(numero)
        else:
            self.view.info_trounament_present()

        # Avant de passer la main à la création des joueurs, je m'assure
            # que l'arribut de class Pair est vide car contient les éléments
            # précédents en cas de plusieurs tournois sur un même programme
        check_pairs = Pair()
        check_pairs.our_players.clear()

        return PlayersCreationController()
