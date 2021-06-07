from models.data.participants import enrolled
from models.players import Player
from models.rounds import Round
from models.evens import Evens


def main():
    # print(len(enrolled))
    for participant in enrolled:
        player = Player(*participant)

    liste = player.generate_first_team()
    # liste = player.generate_another_teams()

    # print(liste)
    for i in liste:
        # print(i)
        print(i[0].__dict__, i[1].__dict__)
        # print(i.__dict__)



            # player_2.add_player()
    # player_2.save_players()
    # print()
    # print(player_2)
    # print(Player.list())

    """Durand = 
    player_1 = Player(name=name, first_name=first_name, birth=birth, sex=sex, ranking=ranking)"""


# A NOTER POUR LE DEMARRAGE
# app = ApplicationController()
# app.start()


if __name__ == '__main__':
    main()