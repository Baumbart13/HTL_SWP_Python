import src.Baumbart13.RPS.fightOutcome as FO
from random import randint
import enum


class Weapon(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5

    def __init__(self, val: int):
        if not isinstance(val, int):
            raise Exception('"val" must be an integer')
        self.weaponNumber = val

    def fights(self, w):
        if not isinstance(w, Weapon):
            raise Exception('A weapon can only fight against another weapon. Duh')
        if self.weaponNumber == w.weaponNumber:
            return FO.fighOutcome.Equal
        if w.weaponNumber % 2 > self.weaponNumber % 2:
            return FO.fighOutcome.OpponentWins
        return FO.fighOutcome.YouWin

    def getName(self):
        return self.name


def getRandomWeapon():
    weapons = [Weapon.ROCK, Weapon.PAPER, Weapon.SCISSORS, Weapon.LIZARD, Weapon.SPOCK]
    return weapons[randint(0, len(weapons) - 1)]
