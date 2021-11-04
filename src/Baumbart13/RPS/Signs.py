import src.Baumbart13.RPS.fightOutcome as FO
from random import randint


class Weapon:
    """
    Rock == 1 << 0
    Paper == 1 << 1
    Scissors == 1 << 2
    Lizard == 1 << 3
    Spock == 1 << 4
    """

    def __init__(self, allValues: int, ownValue: int):
        if not isinstance(allValues, int):
            raise Exception('"allValues" must be an integer')
        if not isinstance(ownValue, int):
            raise Exception('"ownValues" must be an integer')
        self.allValues = allValues
        self.ownValue = ownValue

    def fights(self, w):
        if not isinstance(w, Weapon):
            raise Exception('A weapon can only fight against another weapon. Duh')
        if self.ownValue == w.ownValue:
            return FO.fighOutcome.Equal
        if (w.allValues & self.ownValue) == self.ownValue:
            return FO.fighOutcome.OpponentWins
        return FO.fighOutcome.YouWin

    def getName(self):
        if self.ownValue == ROCK().ownValue:
            return "Rock"
        if self.ownValue == PAPER().ownValue:
            return "Paper"
        if self.ownValue == SCISSORS().ownValue:
            return "Scissors"
        if self.ownValue == LIZARD().ownValue:
            return "Lizard"
        if self.ownValue == SPOCK().ownValue:
            return "Spock"


def ROCK():
    """Returns the Weapon ROCK"""
    return Weapon((1 << 0) | (1 << 3) | (1 << 2), 1 << 0)
def PAPER():
    """Returns the Weapon PAPER"""
    return Weapon((1 << 1) | (1 << 0) | (1 << 4), 1 << 1)
def SCISSORS():
    """Returns the Weapon SCISSORS"""
    return Weapon((1 << 2) | (1 << 1) | (1 << 3), 1 << 2)
def LIZARD():
    """Returns the Weapon Lizard"""
    return Weapon((1 << 3) | (1 << 4) | (1 << 1), 1 << 3)
def SPOCK():
    """Returns the Weapon Spock"""
    return Weapon((1 << 4) | (1 << 2) | (1 << 0), 1 << 4)


def getRandomWeapon():
    weapons = [ROCK(), PAPER(), SCISSORS(), LIZARD(), SPOCK()]
    return weapons[randint(0, len(weapons)-1)]
