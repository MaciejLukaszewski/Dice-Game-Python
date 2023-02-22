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

    def __init__(self, name: str, ishuman: bool):
        self._name = name
        self.dice = Dice()
        self.counter = 10
        self.ishuman = ishuman

    def __gt__(self, other):
        return self.dice.value > other.dice.value

    def __eq__(self, other):
        return  self.dice.value == other.dice.value
    @property
    def name(self):
        return self._name

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        if self.counter <= 0:
            raise ValueError("Decrementing zero number is not allowed")
        else:
            self.counter -= 1


