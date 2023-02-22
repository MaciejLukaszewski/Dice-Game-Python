import os

from dicegame import Dice, Player
from dicegame import display_dices_names, display_dices
from dicegame.graphics import DIE_WIDTH


def main():

    player_human = Player("MadWrath", True)
    player_human_2 = Player("LittleP", True)
    player_pc = Player("PC", False)

    players_list = [
                    player_human,
                    player_pc,
                    player_human_2
    ]

    print("\tWELCOME TO DICE GAME")
    display_dices([1, 6])
    input("\n\nPress any key to start the first round ...")
    os.system('cls')

    while not any(player.counter == 0 for player in players_list):

        for player in players_list:
            player.dice.roll()

        names = []
        results = []
        for player in players_list:
            names.append(player.name)
            results.append(player.dice.value)

        players_list = sorted(players_list)
        winner = players_list[-1]

        display_dices_names(names)
        display_dices(results)
        print()
        print(f"\t\t{winner.name} WINS")

        input("\n\nPress any key to start the next round ...")
        os.system('cls')
        #for player.dice.value in players_list:



if __name__ == "__main__":
    main()
    exit()
