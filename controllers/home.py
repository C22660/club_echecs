from tools.menus import Menu
from views import views
from models.players import Player
# from views.views import HomeMenuView
# from views.views import get_tournament_elements
from models.tournaments import Tournament
from tools.inputs_check import check_names, check_birth_date, check_tournament_date

"""les inputs ici"""

# 1 AppliationController est le chef d'orchestre
class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        # au démarrage, on instancie le HomeMenuController
        # actions = ({"Créer un tournoi" : "NewTournamentController()"}, {"Saisir / modifier la liste des joueurs":
        #             "PlayersController()"}, {"Démarrer le tournoi": "NewRoundController()"}
        #             )
        self.controller = HomeMenuController()
        # tant que sefl.controller n'est pas None (donc while true), l'appli continue de tourner
        while self.controller:
            # si pas __call, self.controller.run()
            self.controller = self.controller()
            # ci-dessus, le self.controller prend l'affectation du return de call, donc change


# 2 on définit ensuite les parcours utilisateur (for class chef d'orchestre pour respecter le principe de
# responsabilité unique)

# Menu d'acceuil, implémente la logique du menu d'accueil
class HomeMenuController:
    def __init__(self):
        # on instancie un menu qui vient des models et donc ajouter un modèle de menu via utils.menu()
        # on crée donc un menu et avec le add du call, on lui passe des instructions
        self.menu = Menu()
        # et on envoi le menu à la vue
        self.view = views.HomeMenuView(self.menu)

    # au lieu de call, on pourrait faire def run(self):
    # la méthode spéciale call permet d'exécuter directement le controller self.controller()
    #  au lieu de self.controller.run() puisque self.controller = HomeMenuController()
    def __call__(self):
        # 1. Construire un menu (video 32'')
        # dans ce menu on ajoute certaines entrées et récupérer l'entrée de l'utilisateur
        # self.menu.add(key, option, controller associé à cette option)
        # la clé pourrait être directement un chiffre, ou une auto numérotation, ou q pour qitter
        # en placant () après le controller, cela veut dire qu'on l'instancie directement
        self.menu.add("auto", "Créer un tournoi", NewTournamentController())
        self.menu.add("auto", "Saisir / modifier la liste des joueurs", PlayersController())
        self.menu.add("auto", "Démarrer le tournoi", NewRoundController())
        self.menu.add("q", "Quitter", EndScreenController())

        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur (video 50')
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controller associé au choix de l'utilisateur au contrôleur principal
        return user_choice.handler

class PlayerMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = views.HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto", "Créer un tournoi", NewTournamentController())
        self.menu.add("auto", "Saisir / modifier la liste des joueurs", PlayersController())
        self.menu.add("auto", "Démarrer le tournoi", NewRoundController())
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
        # elements = self.view.get_tournament_elements()
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
        # print(elements)
        # 2 instancier un tournoi
        new_tournament = Tournament(name, place, date)
        new_tournament.add_tournament_inputs()
        # print(new_tournament.tournament)
        # 3 retour au menu général
        return PlayersController()

# Saisie des joueurs
class PlayersController:
    """Contrôleur responsable de gérer le menu de  création et de gestion
     des joueurs.
     """
    def __init__(self):
        self.view = views.PlayersElementsView()

    def __call__(self):
        # 1 générer les inputs
        number_of_players = self.view.size_team()
        counter = 0
        while counter < int(number_of_players):
            elements = self.view.get_player_elements()
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
            # 2 instancier un joueur
            new_player = Player(name, first_name, birth, sex, ranking)
            new_player.add_player_inputs()
            counter += 1

        print(new_player.team_players)
        # 3 retour au menu général
        return NewRoundController()

# Saisie des joueurs
class NewRoundController:
    def __call__(self):
        print("Lancement des matches")
        # return ???

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
    app = ApplicationController()
    app.start()