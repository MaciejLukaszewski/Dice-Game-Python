from random import randint


class Dice:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 6)


class Player:

    def __init__(self, ishuman: bool):
        self.dice = Dice()
        self.counter = 10
        self.ishuman = ishuman

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1


