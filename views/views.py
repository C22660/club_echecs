

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
        name = input("Nom du tournoi ? ")
        place = input("Lieu du tournoi ? ")
        date = input("date(s) du tournoi ? ")
        return name, place, date

class PlayersElementsView:

    def get_player_elements(self):
        print("-"*70)
        print("Pour enregister le tournoi, merci de compléter les champs suivants :")
        print("-"*70)
        name = input("Nom du joueur ? ").upper()
        while not name in string.ascii_letters:
            print("!"*37)
            print("! Merci de saisir un nom de famille !")
            print("!" * 37)
            name = input("Nom du joueur ? ").upper()
        first_name = input("Prénom du joueur ? ").capitalize()
        birth = input(f"Date de naissance de {first_name} {name} ? ")
        sex = input(f"Sexe de {first_name} {name} (F ou M) ? ")
        ranking = input(f"Classement de {first_name} {name} ? ")
        while not ranking.isdigit():
            print("!"*37)
            print("! Le classement doit être un nombre !")
            print("!" * 37)
            ranking = input(f"Classement de {first_name} {name} ? ")


        return name, first_name, birth, sex, ranking

    def add_player_points_view(self, round_number, first_name, name):
        print("-"*70)
        print("Pour enregister les points du match, merci de compléter le champ suivant :")
        print("-"*70)
        # récupérer les éléments
        print("Round n°"+round_number)
        point = input(f"Résultats de {first_name} {name} ? ")
