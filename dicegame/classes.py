from random import randint
import os

from .graphics import DIE_WIDTH
from .display import display_dices, display_dices_names, display_winner, display_score


class Dice:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 6)
        return self._value


class Player:

    def __init__(self, name: str):
        self._name = name
        self._dice = Dice()
        self._counter = 0

    def __gt__(self, other):
        return self.dice.value > other.dice.value

    def __eq__(self, other):
        return self.dice.value == other.dice.value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def dice(self):
        return self._dice

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def zero_counter(self):
        self._counter = 0


class DiceGame:

    def __init__(self, names: list[str]):

        if not isinstance(names, list):
            raise TypeError("List is expected type")
        else:
            for name in names:
                if not isinstance(name, str):
                    raise TypeError(f"String is expected type but got {type(name)}" )
                if len(names) > DIE_WIDTH:
                    raise ValueError(f"'{name}' name is too long - max length is {DIE_WIDTH} ")

            self._players = []
            for name in names:
                self._players.append(Player(name))

        self._round_num = 0

    def play(self):
        os.system("cls")
        print("Welcome to the roll the dice game!")
        display_dices([1, 6])
        input("\n\nPress ENTER to start the first round ...")
        os.system("cls")

        while not any(player.counter == 2 for player in self._players):

            for player in self._players:
                player.dice.roll()

            names = []
            results = []
            for player in self._players:
                names.append(player.name)
                results.append(player.dice.value)

            max_roll = max(player.dice.value for player in self._players)
            winners = []
            losers = []
            for player in self._players:
                if player.dice.value == max_roll:
                    winners.append(player)
                else:
                    losers.append(player)
            if len(winners) == 1:
                winners[0].increment_counter()
            for loser in losers:
                loser.zero_counter()

            winner = winners[0]
            display_dices_names(names)
            display_dices(results)
            print()
            display_winner(len(self._players), winner.name)
            print()
            display_score(self._players)
            input("\n\nPress ENTER to start the next round ...")
            os.system('cls')

        print("Game has ended")
