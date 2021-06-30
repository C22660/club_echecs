import time

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
                   ("Autres rounds", OtherRoundsController()), ("Rapport du tournoi", ReportController())
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
            print("!"*70)
            print("!               Merci de saisir un nom pour ce tournoi               !")
            print("!" * 70)
            name = self.view.get_tournament_name()
        place = self.view.get_tournament_place()
        while not check_names(place):
            print("!"*70)
            print("!           Merci de saisir un nom de lieu pour ce tournoi           !")
            print("!" * 70)
            name = self.view.get_tournament_place()
        date = self.view.get_tournament_date()
        while not check_tournament_date(date):
            print("!"*70)
            print("!           Merci de saisir un nom de lieu pour ce tournoi           !")
            print("!" * 70)
            name = self.view.get_tournament_place()
        time_control = self.view.get_tournament_time()
        description = self.view.get_trournament_description()

        new_tournament = Tournament(name, place, date, time_control, description)
        enregistrement = new_tournament.add_tournament_inputs()
        if enregistrement:
            numero = new_tournament.id
            print('"'*70)
            print(f"         ------INFO-----> Tournoi enregistré sous l'ID {numero}.           ")
            print('"' * 70)
        else:
            print('"' * 70)
            print("         ------INFO-----> Tournoi déjà présent dans la base.        ")
            print('"' * 70)

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
                print('"' * 70)
                print('"         ------INFO-----> Joueur déjà présent dans la base.          ')
                print('"' * 70)
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
        print("*"*70)
        print(" Les paires de joueurs sont : ")
        # passer par la view car résultat :(12, 'MOUIL', 'Jule') <---&---> (11, 'POLIU', 'Lucienne')
        for couple in our_pairs[1]:
            print(f'{couple[0]} <---&---> {couple[1]}')

        # 6 passage de ces paires à la class Round
        new_round = Round(1, our_pairs[0])

        # 7 on récupère les rondes sous la bonne mise en forme, et on l'adresse à Tournament
        # la class Tournament est "réveillée" par la @classmethode et récupère les infos contenues dans sa base
        rondes = new_round.add_pairs()
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        tournoi.add_rounds(rondes)

        return MatchesController()

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

class MatchesController:
    """Contrôle le lancement et l'arrêt des macthes, gère l'ajout des résultats et leurs sauvegardes dans la base
        du tournoi en cours (round correspondant)
         """

    # def __init__(self):
    #     self.view = views.PlayersElementsView()

    def __call__(self):

        # la class Tournament est "réveillée" par la @classmethode et récupère les infos contenues dans sa base
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        # on démarre les matches et donc on ajoute l'heure et la date de démarrage
        lancement = input("Quand vous souhaitez lancer les matches, saisissez G (comme Go) : ")
        while lancement not in ("g", "G"):
            print("Erreur de commande.")
            input(lancement)
        else:
            tournoi.start_current_round()
        print("-"*70)
        print("------> JEU EN COURS                                                ")
        print("-"*70)
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
        # on récupère dans le round de la base tournoi, la partie relative au matches
        matches = tournoi.extract_match_to_add_scores()
        print("matches = tournoi.extract_match_to_add_scores()")
        print(matches)
        # Le gestionnaire va saisir les scores
        print('"'*70)
        print("Vous allez procéder à la saisie des résultats")
        for i in matches[0]:
            match = MatchResults(i)
            print(match.get_players_by_id())
            saisie = input("Saisissez l'ID gagnant ou N pour matche nul : ")
            print(type(saisie))
            print("-" * 47)
            # match.check_input_winner()
            match.set_winner(saisie)
            print(match.player_1_id, match.player_2_id)
            print("type self id")
            print(type(match.player_1_id))
        results_matches = MatchResults.matches
        print("ds home results_matches")
        print(results_matches)
        tournoi.save_scored_matches(results_matches)
        # print(tournoi.rounds)
        # if match.set_winner(saisie):
        #     pass
        # else:
        #     return saisie
        # 3 retour au menu général
        return HomeMenuController()



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


class OtherRoundsController:
    """une fois les premiers matches réalisés, collecte la synthèse des matches depuis la base tournoi
        et met à jour les scores dans la class joueurs pour générer de nouvelles paires, puis un nouveau round.

        Par défaut, l'id du tournoi est le tournoi en cours, soit le dernier des tournois enregistrés"""

    id_tournament = len(Tournament.users)

    def __init__(self, id_tournament=id_tournament):
        self.id_tournament = id_tournament

    def __call__(self):
        tournoi = Tournament.get_by_id(id=self.id_tournament)
        result = tournoi.extract_match_to_add_scores()
        rounds_remaining = tournoi.number_of_rounds_decrement()
        if rounds_remaining == 0:
            print("°"*70)
            print("°                   Tous les matches ont été joués                   °")
            print("°           Vous allez être redirigé sur le menu principal           °")
            print("°" * 70)
            time.sleep(3)
            return HomeMenuController()
        else:
            print(f"Il reste {rounds_remaining} round(s) à jouer.")
            # result comprend une liste des matches et le numéro du round
            matches = result[0]
            round_number = result[1]
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

            # Une fois les paires effectuées (avec les points puis rangs si nécessaire, affichage à l'écran
            our_pairs = preparation_even.sort_players_points()
            print("*" * 70)
            print(" Les paires de joueurs sont : ")
            for couple in our_pairs[1]:
                print(f'{couple[0]} <---&---> {couple[1]}')

            # passage de ces paires à la class Round
            new_round = Round(round_number+1, our_pairs[0])

            # on récupère les rondes sous la bonne mise en forme, et on l'adresse à Tournament
            # la class Tournament est "réveillée" par la @classmethode et récupère les infos contenues dans sa base
            rondes = new_round.add_pairs()
            id_current_tournament = len(Tournament.users)
            tournoi = Tournament.get_by_id(id=id_current_tournament)
            tournoi.add_rounds(rondes)

            return MatchesController()


class ReportController:
    """Gère le rapport final du tournois"""

    id_tournament = len(Tournament.users)

    def __init__(self, id_tournament=id_tournament):
        self.id_tournament = id_tournament
        self.player_by_alpha = []

    def __call__(self):
        # # --- Liste de tous les acteurs ---
        print("'"*70)
        print("'                        R  A  P  P  O  R  T                         '")
        print("'" * 70)
        print("")
        print("1 - Liste de tous les acteurs en base de données :")
        # par alpha
        print("-----> par ordre alphabétique : ")
        actor = Player.get_by_id(id=1)
        actors_by_alpha = actor.all_actors_by_alpha()
        for element in actors_by_alpha:
            print(f"{element['name']} {element['first_name']}")
        # par rang
        print("")
        print("-----> par classement : ")
        actor = Player.get_by_id(id=1)
        actors_by_rank = actor.all_actors_by_ranking()
        for element in actors_by_rank:
            print(f"{element['name']} {element['first_name']}, rang : {element['ranking']}")

        #--- Liste de tous les joueurs d'un tournoi ---
        print("-"*70)
        print("2 - Liste de tous les joueurs du tournoi :")
        id_current_tournament = len(Tournament.users)
        tournoi = Tournament.get_by_id(id=id_current_tournament)
        player_by_alpha = tournoi.extract_players()
        for p in player_by_alpha:
            player = Player.get_by_id(id=p)
            result = player.all_players_by_alpha_and_ranking()
            self.player_by_alpha.append(result)
        print("")
        print("-----> par ordre alphabétique : ")
        result_by_alpha = sorted(self.player_by_alpha, key=lambda k: k['name'])
        for element in result_by_alpha:
            print(f"{element['name']} {element['first_name']}")
        print("")
        print("-----> par classement : ")
        result_by_alpha = sorted(self.player_by_alpha, key=lambda k: k['ranking'], reverse=True)
        for element in result_by_alpha:
            print(f"{element['ranking']}, {element['name']} {element['first_name']}")
        print("")
        print("-----> par nombre de points gagnés : ")
        tournoi = Tournament.get_by_id(id=self.id_tournament)
        result = tournoi.sum_score_of_players()
        for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
            # print(k, v)
            # print(f"Le joueur {k} totalise {v} point(s).")
            player = Player.get_by_id(id=k)
            print(f"{player} a totalisé {v} point(s).")

        #--- Liste de tous les tournois ---
        print("-"*70)
        print("2 - Liste du(des) tournoi(s) enregistré(s) :")
        print(tournoi.extract_all_tournaments())

        #--- Liste de tous les matches et round des tournois ---
        print("-"*70)
        print("3 - Liste de tous les rounds et matches du(des) tournoi(s) :")
        all_matches = tournoi.extract_all_matches_to_report()
        for component in all_matches:
            # print(index, component)
            print(f"Pour le tounoi {component[0]}, les matches du round {component[1]} sont : ")
            for i in component[2]:
                print(f" joueurs = {i[0]}, score = {i[1]}")
        #     print(component)
        # # ([f"Pour le round {rounds_per_tournament['Round']}, les matches sont (joueurs et scores) :"
        # #                           f" {rounds_per_tournament['matches']}."])

        return HomeMenuController()

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