from .graphics import DICE_ART
from .graphics import DIE_HEIGHT
from .graphics import DIE_WIDTH
from .graphics import DIE_FACE_SEPARATOR


def display_dices(values: list[int]):
    """Prints dice(s) graphic to the console

    Args:
        values (list[int]): list containing integers from 1 to 6, each element represents
        individual dice value

    Raises:
        ValueError: If any element in value list is greater than 6 or lower than 1
    """
    if any(value > 6 for value in values) or any(value < 1 for value in values):
        raise ValueError("Input value should be int from 1 to 6 range")

    for row_number in range(DIE_HEIGHT):
        row = []
        for value in values:
            row.append(DICE_ART[value][row_number])
        print(DIE_FACE_SEPARATOR.join(row))


def display_dices_owners(names: list[str]):
    """Display names of players over the dice(centered)

    Args:
        names (list[str]): list containing strings representing players names

    Raises:
        ValueError: If name string is too long
    """

    if any(len(name) > DIE_WIDTH for name in names):
        raise ValueError(f"Too long name - max {DIE_WIDTH} characters")

    row = []
    separator = []
    for name in names:
        separator.append(DIE_WIDTH * "-")
        name_position = DIE_WIDTH - len(name)
        front_sep = int(name_position / 2) * " "
        rear_sep = (int(name_position / 2) + name_position % 2) * " "
        row.append(front_sep + name + rear_sep)
    name_str = DIE_FACE_SEPARATOR.join(row)
    separator_str = DIE_FACE_SEPARATOR.join(separator)

    print(separator_str)
    print(name_str)
    print(separator_str)


def display_winner(players_num: int, winner: str):
    """Display winner of the game with center alignment

    Args:
        players_num (int): number of players
        winner (str): winners name
    Raises:
        TypeError: If type of 'player_num' and 'winner' in incorrect
    """
    if not (isinstance(players_num, int) and isinstance(winner, str)):
        raise TypeError()
    free_space = (players_num * (DIE_WIDTH + len(DIE_FACE_SEPARATOR)) - len(DIE_FACE_SEPARATOR))
    output = winner + " WINS!!"

    print(output.center(int(free_space)))

