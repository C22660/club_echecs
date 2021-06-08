class HomeMenuView:

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("Bienvenue à la création de notre nouveau tournoi.")
        print("*"*50)
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