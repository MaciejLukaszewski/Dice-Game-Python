from graphics import DICE_ART
from graphics import DIE_HEIGHT
from graphics import DIE_WIDTH
from graphics import DIE_FACE_SEPARATOR

def display_dices(values: list[int]) -> None:

    for row_number in range(DIE_HEIGHT):
        row = []
        for value in values:
            row.append(DICE_ART[value][row_number])
        print(DIE_FACE_SEPARATOR.join(row))


def display_dices_names(names: list[str]):

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
    print(separator_str)
    print(name_str)
    print(separator_str)


display_dices_names(["MadWrath", "PC"])
display_dices([2, 5])