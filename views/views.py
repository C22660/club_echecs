
class HomeMenuView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("**********      MENU PRINCIPAL      **********")
        print("-"*50)
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

    def get_tournament_date(self):
        date = input("date(s) du tournoi ? ")
        return date

    def get_tournament_time(self):
        time_control = input("Quelle contrôle de temps choisissez vous pour ce tournoi ? \n"
                     "Bullet, blitz, ou coup rapide ? ")
        return time_control

    def get_trournament_description(self):
        description = input("Commentaires éventuels ? ")
        return description

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
        # self.counter += 1

    def get_new_ranking(self):
        print("-"*70)
        print(f"Pour modisfier le rang d'un joueur, merci de compléter les champs suivants :")
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


class PlayersModificationView:

    def __init__(self):
        self.name = None
        self.first_name = None
        self.birth = None
        self.ranking = None