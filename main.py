import os

from dicegame import Dice, Player, DiceGame
from dicegame import display_dices_names, display_dices
from dicegame.graphics import DIE_WIDTH


def main():

    player_human = "MadWrath"
    player_human_2 = "LittleP"
    player_pc = "PC"

    players_list = [
                    player_human,
                    player_pc,
                    player_human_2
    ]

    game = DiceGame(players_list)
    game.play()
    exit()
        #for player.dice.value in players_list:


if __name__ == "__main__":
    main()
    exit()
