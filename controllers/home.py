from tools.menus import Menu
from views import views
from models.players import Player
from models.pair import Pair
# from views.views import HomeMenuView
# from views.views import get_tournament_elements
from models.tournaments import Tournament
from models.rounds import Round
from tools.inputs_check import check_names, check_birth_date, check_tournament_date

"""les inputs ici"""

# 1 AppliationController est le chef d'orchestre
class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self, actions=None):
        actions = (("Créer un tournoi", NewTournamentController()), ("Saisir la liste des joueurs",
                                                                     PlayersCreationController()),
                   ("Modifier le rang d'un joueur", ModificationRankingController()),
                    ("Démarrer le tournoi", NewRoundController())
                    )
        # au démarrage, on instancie le HomeMenuController
        self.controller = HomeMenuController()
        self.controller.actions_elements = actions
        # tant que sefl.controller n'est pas None (donc while true), l'appli continue de tourner
        while self.controller:
            # si pas __call, self.controller.run()
            self.controller = self.controller()
            # ci-dessus, le self.controller prend l'affectation du return de call, donc change


# 2 on définit ensuite les parcours utilisateur (for class chef d'orchestre pour respecter le principe de
# responsabilité unique)

# Menu d'acceuil, implémente la logique du menu d'accueil
# class HomeMenuController:
#     def __init__(self):
#         # on instancie un menu qui vient des models et donc ajouter un modèle de menu via utils.menu()
#         # on crée donc un menu et avec le add du call, on lui passe des instructions
#         self.menu = Menu()
#         # et on envoi le menu à la vue
#         self.view = views.HomeMenuView(self.menu)
#
#     # au lieu de call, on pourrait faire def run(self):
#     # la méthode spéciale call permet d'exécuter directement le controller self.controller()
#     #  au lieu de self.controller.run() puisque self.controller = HomeMenuController()
#     def __call__(self):
#         # 1. Construire un menu (video 32'')
#         # dans ce menu on ajoute certaines entrées et récupérer l'entrée de l'utilisateur
#         # self.menu.add(key, option, controller associé à cette option)
#         # la clé pourrait être directement un chiffre, ou une auto numérotation, ou q pour qitter
#         # en placant () après le controller, cela veut dire qu'on l'instancie directement
#         self.menu.add("auto", "Créer un tournoi", NewTournamentController())
#         self.menu.add("auto", "Saisir / modifier la liste des joueurs", PlayersCreationController())
#         self.menu.add("auto", "Démarrer le tournoi", NewRoundController())
#         self.menu.add("q", "Quitter", EndScreenController())
#
#         # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur (video 50')
#         user_choice = self.view.get_user_choice()
#
#         # 3. Retourner le controller associé au choix de l'utilisateur au contrôleur principal
#         return user_choice.handler

# class OtherMenuController:
class HomeMenuController:
    actions_elements = []

    def __init__(self):
        self.menu = Menu()
        self.view = views.HomeMenuView(self.menu)
        self.actions = []

    def add_actions(self, elements):
        self.actions.append[elements]

    def __call__(self):
        for sujet in self.actions_elements:
            self.menu.add("auto", sujet[0], sujet[1])

        self.menu.add("q", "Quitter", EndScreenController())

        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur (video 50')
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controller associé au choix de l'utilisateur au contrôleur principal
        return user_choice.handler

# menu de connection
class ConnectionMenuController:
    def __call__(self):
        print("dans le controleur de connection")
        return HomeMenuController()
        # ici, sans le return, il y aurait un None d'adresser ce qui amenerait à quitter le process

# menu d'inscription
class SignupMenuController:
    pass

# Création d'un nouveau tournoi
class NewTournamentController:
    """Contrôleur responsable de gérer le menu de  création
     d'un nouveau tournoi.
     """
    def __init__(self):
        self.view = views.TournamentCreationView()

    def __call__(self):
        # 1 générer les inputs
        tournament = self.view.get_tournament_elements()
        name = self.view.get_tournament_name()
        while not check_names(name):
            print("!"*37)
            print("! Merci de saisir un nom pour ce tournoi !")
            print("!" * 37)
            name = self.view.get_tournament_name()
        place = self.view.get_tournament_place()
        while not check_names(place):
            print("!"*37)
            print("! Merci de saisir un nom de lieu pour ce tournoi !")
            print("!" * 37)
            name = self.view.get_tournament_place()
        date = self.view.get_tournament_date()
        while not check_tournament_date(date):
            print("!"*37)
            print("! Merci de saisir un nom de lieu pour ce tournoi !")
            print("!" * 37)
            name = self.view.get_tournament_place()
        time_control = self.view.get_tournament_time()
        description = self.view.get_trournament_description()

        new_tournament = Tournament(name, place, date, time_control, description)
        enregistrement = new_tournament.add_tournament_inputs()
        if enregistrement:
            print("Tournoi enregistré")
        else:
            print("Tournoi déjà présent dans la base")

        return PlayersCreationController()

# Saisie des joueurs
class PlayersCreationController:
    """Contrôleur responsable de gérer le menu de  création et de gestion
     des joueurs.
     """
    def __init__(self):
        self.view = views.PlayersElementsView()

    def __call__(self):
        # 1 générer les inputs
        number_of_players = self.view.size_team()
        counter = 1
        while counter < int(number_of_players)+1:
            addition = PlayersCreationController.player_addition(self, counter)
            # 2 instancier un joueur
            new_player = Player(*addition)
            add_data_base = new_player.add_player_inputs()
            if not add_data_base:
                print("!" * 36)
                print("! Joueur déjà présent dans la base !")
                print("!" * 36)
                print("")
                counter -= 1
            else:
                players_serialized = new_player.serialization_players()
                print(players_serialized)
                print(f"player serialisé = {type(players_serialized)}")

                # ajout des joueurs sérialisés dans la class Evens
                preparation_even = Pair(players_serialized)
                preparation_even.add_players_pairs()
            # print(f"liste reçue = {type(preparation_even.our_players)}")
            counter += 1


        # new_player.generate_first_team()

        # 3 retour au menu général
        return FirstRoundController()

    def player_addition(self, counter):
        """permet de répéter la collecte de l'ensemble des éléments d'un joueur
        avec, en argument, le numéro du joueur en cours de sa saisie pour que le gestionnaire
        sache où il en est (n'est pas l'ID joueur) via counter issu de la class Player"""

        self.view = views.PlayersElementsView(counter)
        self.view.get_player_elements()
        name = self.view.get_player_name()
        while not check_names(name):
            print("!" * 37)
            print("! Merci de saisir un nom de famille !")
            print("!" * 37)
            name = self.view.get_player_name()
        first_name = self.view.get_player_first_name()
        while not check_names(first_name):
            print("!" * 29)
            print("! Merci de saisir un prénom !")
            print("!" * 29)
            first_name = self.view.get_player_first_name()
        birth = self.view.get_player_birth()
        sex = self.view.get_player_sex()
        ranking = self.view.get_player_ranking()
        print(type(ranking))
        while not ranking.isdigit():
            print("!" * 37)
            print("! Le classement doit être un nombre !")
            print("!" * 37)
            ranking = self.view.get_player_ranking()
        # print(elements)
        return name, first_name, birth, ranking, sex

class ModificationRankingController:
    """Permet de modifier le rang d'un joueur"""
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
            print("Modification de rang enregistrée")
        else:
            print("Joueur non trouvé")


        return HomeMenuController()


class FirstRoundController:
    def __call__(self):

        """Reprise de  l'ajout des joueurs dans l'attibut de la classe Pair depuis PlayerCreationControler
         pour créer les pairs du premier match"""
        # actions = (("Afficher la liste des matches", xx()), ("Saisir / modifier la liste des joueurs",
        #                                                              PlayersCreationController()),
        #            ("Démarrer le tournoi", NewRoundController()))
        # # return ???
        first_couples = Pair.sort_players_ranking()
        new_round = Round(first_couples)
        new_round.start_round()


# reprendre une partie encours
class OngoingGameController:
    pass

# consulter le palmarès
class RankingController:
    pass

#
class EndScreenController:
    def __call__(self):
        print("dans le controleur de fin: bye bye")



if __name__ == '__main__':
    actions = (("Créer un tournoi", NewTournamentController()), ("Saisir / modifier la liste des joueurs",
                                                                 PlayersCreationController()), ("Démarrer le tournoi", NewRoundController()))
    app = ApplicationController()
    app.start()
    # app.start(actions)
    # one_menu = HomeMenuController()
    # one_menu.__call__()
    # one_menu.actions_elements = actions
    # for indice, sujet in enumerate(one_menu.actions_elements):
    #     print(indice, sujet[1])