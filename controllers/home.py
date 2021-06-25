from tools.menus import Menu
from views import views
from models.players import Player
from models.pairs import Pair
# from views.views import HomeMenuView
# from views.views import get_tournament_elements
from models.tournaments import Tournament
from models.rounds import Round
from models.matches import MatchResults
from tools.inputs_check import check_names, check_birth_date, check_tournament_date

"""les inputs ici"""

# 1 AppliationController est le chef d'orchestre


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        actions = (("Créer un tournoi", TournamentCreationController()), ("Saisir la liste des joueurs",
                   PlayersCreationController()),
                   ("Modifier le rang d'un joueur", ModificationRankingController()),
                   ("Démarrer le tournoi", RoundController())
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

    # def add_actions(self, elements):
    #     self.actions.append[elements]

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
class TournamentCreationController:
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
            numero = new_tournament.id
            print('"'*45)
            print(f"----INFO----> Tournoi enregistré sous l'ID {numero}.")
            print('"' * 45)
        else:
            print('"' * 45)
            print("----INFO----> Tournoi déjà présent dans la base.")
            print('"' * 45)

        return PlayersCreationController()

# Saisie des joueurs
class PlayersCreationController:
    """Contrôleur responsable de gérer le menu de  création et de gestion
     des joueurs.
     """
    def __init__(self):
        self.view = views.PlayersElementsView()

    def __call__(self):
        # 1 générer les inputs concernant les joueurs
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

                # 3 ajout du joueur sérialisé dans la class Pair
                preparation_even = Pair(players_serialized)
                preparation_even.add_players_pairs()

                # 4 ajout du joueur dans la class Tournament
                id_current_tournament = len(Tournament.users)
                tournoi = Tournament.get_by_id(id=id_current_tournament)
                tournoi.add_players(new_player.id)
            # print(f"liste reçue = {type(preparation_even.our_players)}")
            counter += 1

        # 5 Une fois les paires effectuées, affichage à l'écran
        our_pairs = preparation_even.sort_players_ranking()
        print("*"*30)
        print(" Les paires de joueurs sont : ")
        # passer par la view car résultat :(12, 'MOUIL', 'Jule') <---&---> (11, 'POLIU', 'Lucienne')
        for couple in our_pairs[1]:
            print(couple)
            print(f'{couple[0]} <---&---> {couple[1]}')

        # 6 passage de ces paires à la class Round
        les_matches = [['1', '7'], ['5', '8'], ['4', '3'], ['6', '2']]
        new_round = Round(1, our_pairs[0])

        # 7 on récupère les rondes sous la bonne mise en forme, et on l'adresse à Tournament
        # la class Tournament est "réveillée" par la @classmethode et récupère les infos contenues dans sa base
        rondes = new_round.add_pairs()
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        tournoi.add_rounds(rondes)
        # 8 on démarre les matches et donc on ajoute l'heure et la date de démarrage
        lancement = input("Quans vous souhaitez lancer les matches, saisissez G (comme Go) : ")
        if lancement in ("g", "G"):
            tournoi.start_current_round()
        else:
            print("Erreur de commande")
            return lancement
        print("")
        print("------> JEU EN COURS")
        print("")
        # 10 on arrête le jeux quand les matches sont terminés
        stop = input("Quans vous souhaitez arrêter les matches, saisissez S (comme Stop) : ")
        if stop in ("s", "S"):
            tournoi.end_current_round()
        else:
            print("Erreur de commande")
            return stop
        print("")
        print("------> JEU TERMINÉ")
        print("")
        # 10 on récupre dans le round de la base tournoi, la partie relative au matches
        matches = tournoi.extract_match_to_add_scores()
        # 11 Le gestionnaire va saisir les scores
        print('"'*50)
        print("Vous allez procéder à la saisie des résultats")
        for i in matches:
            match = MatchResults(i)
            print(match.get_players_by_id())
            saisie = input("Saisissez l'ID gagnant ou N pour matche nul : ")
            print("-" * 47)
            if match.set_winner(saisie):
                pass
            else:
                return saisie
        results_matches = MatchResults.matches
        tournoi.save_scored_matches(results_matches)
        print(tournoi.rounds)

        # 3 retour au menu général
        return RoundController()

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
        while not ranking.isdigit():
            print("!" * 37)
            print("! Le classement doit être un nombre !")
            print("!" * 37)
            ranking = self.view.get_player_ranking()
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


class RoundController:
    def __call__(self):
        print("coté round controler")
        """Reprise de  l'ajout des joueurs dans l'attibut de la classe Pair depuis PlayerCreationControler
         pour créer les pairs du premier match"""
        # actions = (("Afficher la liste des matches", xx()), ("Saisir / modifier la liste des joueurs",
        #                                                              PlayersCreationController()),
        #            ("Démarrer le tournoi", NewRoundController()))
        # # return ???
        # couples = Pair.our_players
        # print(couples)
        # new_round = Round(1, couples)
        # ronde = new_round.add_pairs()
        # start_tournament = Tournament.get_by_id(ronde, id=0)


    # def generateur(matches):
    #     for players in matches:
    #         yield players
    #
    # matches = [['1', '7'], ['5', '8'], ['4', '3'], ['6', '2']]
    # couple = generateur(matches)
    # print(next(couple))

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
    # actions = (("Créer un tournoi", NewTournamentController()), ("Saisir / modifier la liste des joueurs",
    #                                                              PlayersCreationController()), ("Démarrer le tournoi", NewRoundController()))
    app = ApplicationController()
    app.start()
    # app.start(actions)
    # one_menu = HomeMenuController()
    # one_menu.__call__()
    # one_menu.actions_elements = actions
    # for indice, sujet in enumerate(one_menu.actions_elements):
    #     print(indice, sujet[1])