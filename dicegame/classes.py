from random import randint
import os

from .graphics import DIE_WIDTH
from .display import display_dices, display_dices_owners, display_winner


class Dice:
    """Class representing dice and it's behaviour

    Attributes:
        _value (int): value of the dice

    Methods:
        roll(self):
            Return dice rolled value
    """
    def __init__(self):
        """Initialize an instance of Dice."""
        self._value = None

    @property
    def value(self):
        """int: Return the value of dice"""
        return self._value

    def roll(self):
        """Returns the rolled dice value

        Returns:
            Integer value from [1,6] space

        """
        self._value = randint(1, 6)
        return self._value


class Player:
    """Class representing player

        Attributes:
            _name (str): name of the player
            _dice (Dice): dice object assigned to the player
            _counter (int): points scored through rounds

        Methods:
            increment_counter(self):
                Increments '_counter' value by 1
        """
    def __init__(self, name: str):
        """Initialization of the Player class

        Args:
            name (str): Name of the player
        """
        self._name = name
        self._dice = Dice()
        self._counter = 0

    def __gt__(self, other):
        return self.dice.value > other.dice.value

    def __eq__(self, other):
        return self.dice.value == other.dice.value

    @property
    def name(self):
        """Returns the name of the player"""
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def dice(self):
        """Returns the dice object"""
        return self._dice

    @property
    def counter(self):
        """Returns player counter"""
        return self._counter

    def increment_counter(self):
        """Increments player winning rounds by 1"""
        self._counter += 1


class DiceGame:
    """Class representing Dice Game

    Attributes:
        _players (list[Player]): List containing all players participating in the game

    Methods:
        play(self):
            Starts and manage the game
    """

    WINNING_SCORE = 3

    def __init__(self, names: list[str]):
        """Initialization of the DiceGame class

        Args:
            names (list[str]): List containing players names

        Raises:
            TypeError:
                If 'names' value is not a list, or
                If list elements are not a string
            ValueError:
                If string element of the list is too long
        """
        if not isinstance(names, list):
            raise TypeError("List is expected type")
        else:
            for name in names:
                if not isinstance(name, str):
                    raise TypeError(f"String is expected type but got {type(name)}")
                if len(names) > DIE_WIDTH:
                    raise ValueError(f"'{name}' name is too long - max length is {DIE_WIDTH} ")

            self._players = []
            for name in names:
                self._players.append(Player(name))

    def play(self):
        """Manages the process of the game

        Game last till one, or more players scores enough points after the round.
        WINNING_SCORE defines number of score needed to win.
        """

        os.system("cls")

        print("Welcome to the roll the dice game!")
        display_dices([1, 6])
        input("\n\nPress ENTER to start the first round ...")
        os.system("cls")

        while not any(player.counter == self.WINNING_SCORE for player in self._players):

            for player in self._players:
                player.dice.roll()

            names = []
            results = []
            for player in self._players:
                names.append(player.name)
                results.append(player.dice.value)

            max_roll = max(player.dice.value for player in self._players)
            winners = []
            for player in self._players:
                if player.dice.value == max_roll:
                    player.increment_counter()
                    winners.append(player)

            if len(winners) == 1:
                winner = winners[0].name
            else:
                winner = " and ".join(winner.name for winner in winners)
            display_dices_owners(names)
            display_dices(results)
            print()
            display_winner(len(self._players), winner)
            print()
            print("Score:")
            for player in self._players:
                print(f"{player.name}: {player.counter}")
            input("\n\nPress ENTER to start the next round ...")
            os.system('cls')
        game_winners = []
        for player in self._players:
            if player.counter == self.WINNING_SCORE:
                game_winners.append(player.name)
        print(f"{' and '.join(game_winners)} wins the game!!")
