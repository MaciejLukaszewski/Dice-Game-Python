from dicegame import DiceGame


def main():

    player_human = "MadWrath"
    player_human_2 = "LittleP"
    player_pc = "UnicCor"

    players_list = [
                    player_human,
                    player_pc,
                    player_human_2
    ]

    game = DiceGame(players_list)
    game.play()
    exit()


if __name__ == "__main__":
    main()
    exit()
