from tools.menus import Menu
from views import views
from controllers.TournamentCreation import TournamentCreationController
from controllers.ModificationRanking import ModificationRankingController
from controllers.ReportController import ReportController
from controllers.RoundsController import RoundsController

# 1 ApplicationController est le chef d'orchestre


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        menu_actions = (("Créer un tournoi", TournamentCreationController()),
                        ("Modifier le rang d'un joueur",
                         ModificationRankingController()),
                        ("Gestion des rounds", RoundsController()),
                        ("Rapport d'un tournoi", ReportController())
                        )
        # au démarrage, on instancie le HomeMenuController
        self.controller = HomeMenuController()
        self.controller.actions_elements = menu_actions
        # tant que sefl.controller n'est pas None (donc while true),
        # l'appli continue de tourner
        while self.controller:
            # si pas __call, self.controller.run()
            self.controller = self.controller()
            # ci-dessus, le self.controller prend l'affectation du return de
            # call, donc change


class HomeMenuController:

    def __init__(self, actions=None):
        self.menu = Menu()
        self.view = views.HomeMenuView(self.menu)
        self.actions_elements = actions

    def __call__(self):
        for sujet in self.actions_elements:
            self.menu.add("auto", sujet[0], sujet[1])

        self.menu.add("q", "Quitter", EndScreenController())

        # 2. Demander à la vue d'afficher le menu et de collecter la réponse
        # de l'utilisateur
        user_choice = self.view.get_user_choice()

        # 3. Retourner le controller associé au choix de l'utilisateur au
        # contrôleur principal
        return user_choice.handler


class EndScreenController:
    def __call__(self):
        print("°" * 70)
        print("°  Au revoir. Merci d'avoir joué avec nous et félicitations à"
              " tous.  °")
        print("°" * 70)


if __name__ == '__main__':
    app = ApplicationController()
    app.start()
