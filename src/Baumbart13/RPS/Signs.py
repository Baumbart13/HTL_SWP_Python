import fightOutcome


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
            return fightOutcome.fighOutcome.Equal
        if (w.allValues & self.ownValue) == self.ownValue:
            return fightOutcome.fighOutcome.OpponentWins
        return fightOutcome.fighOutcome.YouWin


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
