""" fonctions sui font les print"""

class MenuEntry:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler
# suppression des str et repr

# le menu est une série d'entrée
class Menu:
    def __init__(self):
        self._entries = {}
        self._autokey = 1

    # handler est pour controller mais pour ne pas confondre
    # la numérotation automatique est définie ici implémenter de 1 à chaque passage
    def add(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1

        self._entries[str(key)] = MenuEntry(option, handler)

    # en obligeant la vue à passer par def items, ça évite qu'il at accès à self._entries
    #  et qu'il puisse le modifier, en générant un itérateurs grace à .items()
    def items(self):
        # renvoi un itérateur à travers les clés et les entrées dans le menu
        return self._entries.items()

    # __contains__ appelé dans la menu def get_user_choice(self): permet de gérer le in pour la vérif
    def __contains__(self, choice):
        return str(choice) in self._entries
    # en complément de __contains__ pour simuler un dictionnaire
    def __getitem__(self, choice):
        return self._entries[choice]

if __name__ == "__main__":
    menu = Menu()
    menu.add("auto", "premiere option menu", lambda: None)
    print(menu._entries)