
class HomeMenuView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("**********                      M E N U                     **********")
        print("-"*70)
        # à partir de la méthode items de la class menu
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    def get_user_choice(self):
        # tant que le choix est valide
        while True:
            # afficher le menu au gestionnaire
            self._display_menu()
            # demander au gestionnaire de faire un choix
            choice = input("Indiquez votre choix : ")
            # valider le choix du gestionnaire
            # le in ci dessous est géré par le __contains__ de la class menu
            if choice in self.menu:
                # le choice est géré par le __getitem__ de la class menu
                return self.menu[choice]


# collece des éléments de création du tournoi
class TournamentCreationView:
    #     def __init__(self):
    def get_tournament_elements(self):
        print("-"*70)
        print("Pour enregister le tournoi, merci de compléter les champs suivants :")
        print("-"*70)

    def get_tournament_name(self):
        name = input("Nom du tournoi ? ").upper()
        return name

    def get_tournament_place(self):
        place = input("Lieu du tournoi ? ").upper()
        return place

    def get_tournament_start_date(self):
        start_date = input("date du tournoi, ou du début de tournoi (jj/mm/aaaa) ? ")
        return start_date

    def get_tournament_end_date(self):
        end_date = input("date de fin de tournoi, ou même date si un seul jour (jj/mm/aaaa) ? ")
        return end_date

    def get_tournament_time(self):
        time_control = input("Quelle contrôle de temps choisissez vous pour ce tournoi ? \n"
                             "Bullet, blitz, ou coup rapide ? ")
        return time_control

    def get_trournament_description(self):
        description = input("Commentaires éventuels ? ")
        return description

    def check_name_view(self):
        print("!" * 70)
        print("!               Merci de saisir un nom pour ce tournoi               !")
        print("!" * 70)

    def check_place_view(self):
        print("!" * 70)
        print("!           Merci de saisir un nom de lieu pour ce tournoi           !")
        print("!" * 70)

    def check_start_date_view(self):
        print("!" * 70)
        print("! Merci de saisir une date de tournoi, ou de début de tournoi valide !")
        print("!" * 70)

    def check_end_date_view(self):
        print("!" * 70)
        print("! Merci de saisir une date de fin de tournoi valide (même date si jour unique) !")
        print("!" * 70)

    def info_tournament_recorded(self, numero):
        print('"' * 70)
        print(f"         ------INFO-----> Tournoi enregistré sous l'ID {numero}.           ")
        print('"' * 70)

    def info_trounament_present(self):
        print('"' * 70)
        print("         ------INFO-----> Tournoi déjà présent dans la base.        ")
        print('"' * 70)


class PlayersElementsView:

    def __init__(self, counter=1):
        self.counter = counter
        self.name = None
        self.first_name = None
        self.sex = None
        self.birth = None
        self.ranking = None

    def size_team(self):
        print("-"*70)
        print("Combien de joueurs voulez vous enregistrer ?")
        print("          Nombre pair obligatoire           ")
        print("-"*70)
        number = input("Nombre de joueurs : ")
        return number

    def get_player_elements(self):
        print("-"*70)
        print(f"Pour enregister le joueur {self.counter}, merci de compléter les champs suivants :")
        print("-"*70)

    def get_new_ranking(self):
        print("-"*70)
        print(f"Pour modifier le rang d'un joueur, merci de compléter les champs suivants :")
        print("-"*70)

    def get_player_name(self):
        self.name = input("Nom de famille du joueur ? ").upper()
        return self.name

    def get_player_first_name(self):
        self.first_name = input("Prénom du joueur ? ").capitalize()
        return self.first_name

    def get_player_birth(self):
        self.birth = input(f"Date de naissance de {self.first_name} {self.name} (jj/mm/aaaa) ? ")
        return self.birth

    def get_player_sex(self):
        self.sex = input(f"Sexe de {self.first_name} {self.name} (F ou M) ? ")
        return self.sex

    def get_player_ranking(self):
        self.ranking = input(f"Classement de {self.first_name} {self.name} ? ")
        return self.ranking

    def add_player_points_view(self, round_number):
        print("-"*70)
        print("Pour enregister les points du match, merci de compléter le champ suivant :")
        print("-"*70)
        # récupérer les éléments
        print("Round n°"+round_number)
        point = input(f"Résultats de {self.first_name} {self.name} ? ")

    def check_player_name(self):
        print("!" * 37)
        print("! Merci de saisir un nom de famille !")
        print("!" * 37)

    def check_player_first_name(self):
        print("!" * 29)
        print("! Merci de saisir un prénom !")
        print("!" * 29)

    def check_player_birth(self):
        print("!" * 29)
        print("! Merci de saisir une date valide (jj/mm/aaaa) !")
        print("!" * 29)

    def check_player_ranking(self):
        print("!" * 37)
        print("! Le classement doit être un nombre !")
        print("!" * 37)

    def pair_mandatory(self):
        print("!" * 35)
        print("! Désolé, nombre pair obligatoire !")
        print("!" * 35)

    def info_player_present(self):
        print('"' * 70)
        print('"------INFO-----> Joueur déjà présent. Seul le rang a été modifié."')
        print('"' * 70)
        print("")

    def first_players_pair(self):
        print("*" * 70)
        print("*        Les premières paires de joueurs sont les suivantes.         *")
        print("*    Vous allez être redirigé vers le menu pour lancer le round.     *")
        print("*                               __  __                               *")
        print("*                                 \/                                 *")

    def couple_in_our_pairs(self, player_1, player_2):
        print(f'{player_1} <---&---> {player_2}')

    def ranking_modified(self):
            print('-'*70)
            print("Modification de rang enregistrée.")
            print("Vous allez être redirigé vers le menu principal.")
            print('-' * 70)

    def player_not_found(self):
            print('-'*70)
            print("Désolé, ce joueur n'existe pas.")
            print("Vous allez être redirigé vers le menu principal.")
            print('-' * 70)

class RoundsElementsView:

    # def __init__(self):
    #     self.number = None

    def no_round_remaining(self):
        print("°" * 70)
        print("°                   Tous les matches ont été joués                   °")
        print("°           Vous allez être redirigé sur le menu principal           °")
        print("°" * 70)

    def all_rounds_remaining(self, number):
        print("*" * 70)
        print(f"Il reste tous les {number} rounds à jouer.")

    def how_many_rounds(self, rounds_remaining):
        print("*" * 70)
        print(f"Il reste {rounds_remaining} round(s) à jouer.")

    def print_pairs(self, pairs):
        print("*" * 70)
        print(" Les paires de joueurs sont : ")
        for couple in pairs:
            print(f'{couple[0]} <---&---> {couple[1]}')


class MatchesElementsView:

    def wrong_input(self):
        print("Désolé, erreur de commande.")

    def game_finished(self):
        print("")
        print("------> JEU TERMINÉ")
        print("")

    def results_input_announcement(self):
        print('"'*70)
        print("Vous allez procéder à la saisie des résultats")
        print("")

    def input_results_finished(self):
        print('-'*70)
        print("Saisie des résultats terminée.")
        print("vous allez être redirigé vers le menu pour lancer le round.")
        print('-'*70)

class ReportsElementsView:

    def wrong_input(self):
        print("Désolé, erreur de commande.")

    def report_all_actors_title(self):
        print("'"*70)
        print("'          R A P P O R T  D E  T O U S  L E S  A C T E U R S         '")
        print("'" * 70)
        print("")
        print(" Liste de tous les acteurs en base de données :")
        print("-----> par ordre alphabétique : ")

    def actors_by_alpha_view(self, actors_by_alpha):
        for element in actors_by_alpha:
            print(f"{element['name']} {element['first_name']}")

    def all_actors_by_ranking_view(self, actors_by_rank):
        for element in actors_by_rank:
            print(f"{element['name']} {element['first_name']}, rang : {element['ranking']}")

    def report_all_actors_ranking(self):
        print("")
        print("-----> par classement : ")

    def tournements_list_view(self):
        print("-" * 70)
        print("Liste du(des) tournoi(s) enregistré(s) :")

    def players_in_tournament(self):
        print("-"*70)
        print("Liste de tous les joueurs du tournoi :")

    def players_by_alpha(self,result_by_alpha):
        print("")
        print("-----> par ordre alphabétique : ")
        for element in result_by_alpha:
            print(f"{element['name']} {element['first_name']}")
        print("")

    def players_by_ranking(self, result_by_ranking):
        print("-----> par classement : ")
        for element in result_by_ranking:
            print(f"{element['ranking']}, {element['name']} {element['first_name']}")
        print("")

    def players_by_scrore_title(self):
        print("-----> par nombre de points gagnés : ")

    def players_by_score_print(self, player, points):
        print(f"{player} a totalisé {points} point(s).")

    def rounds_and_matches_title(self):
        print("-"*70)
        print("Liste de tous les rounds et matches du(des) tournoi(s) :")

    def rounds_and_matches_part_1(self, component):
        print(f"Pour le tournoi {component[0]}, les matches du round {component[1]} sont : ")

    def rounds_and_matches_part_2(self, i):
        print(f" joueurs = {i[0]}, score = {i[1]}")