from .graphics import DICE_ART
from .graphics import DIE_HEIGHT
from .graphics import DIE_WIDTH
from .graphics import DIE_FACE_SEPARATOR

def display_dices(values: list[int]):

    for row_number in range(DIE_HEIGHT):
        row = []
        for value in values:
            row.append(DICE_ART[value][row_number])
        print(DIE_FACE_SEPARATOR.join(row))


def display_dices_names(names: list[str], return_str=False):

    row = []
    separator = []
    for name in names:
        if len(name) > DIE_WIDTH:
            raise ValueError("To long name")
        else:
            separator.append(DIE_WIDTH * "-")
            name_position = DIE_WIDTH - len(name)
            front_sep = int(name_position / 2) * " "
            rear_sep = (int(name_position / 2) + name_position % 2) * " "
            row.append(front_sep + name + rear_sep)
    name_str = DIE_FACE_SEPARATOR.join(row)
    separator_str = DIE_FACE_SEPARATOR.join(separator)
    if return_str:
        return separator_str + "\n" + name_str + "\n" + separator_str
    else:
        print(separator_str)
        print(name_str)
        print(separator_str)


def display_winner(players_num: int, winner: str):

    if not (isinstance(players_num, int) and isinstance(winner, str)):
        raise TypeError()
    free_space = (players_num * (DIE_WIDTH + len(DIE_FACE_SEPARATOR)) - len(DIE_FACE_SEPARATOR))
    output = winner + " WINS!!"

    print(output.center(int(free_space)))


def display_score(players):
    print("Score:")
    for player in players:
        print(f"{player.name}: {player.counter}")

