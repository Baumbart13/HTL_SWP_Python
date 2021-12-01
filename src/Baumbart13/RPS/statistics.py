import datetime

from src.Baumbart13.RPS.Signs import Weapon
from src.Baumbart13.RPS.fightOutcome import fighOutcome


class Counter:
    def __init__(self):
        self.games = []

    def addGame(self, g):
        if not isinstance(g, Game):
            raise Exception("g must be type of Game")
        self.games.append(g)

    def NoWins(self, fo: fighOutcome):
        """Opponent = COMP
        You = Human
        Equal = Draw"""
        fightOutcomeSum = 0
        for g in self.games:
            for t in g.turns:
                if t.outcome == fo:
                    fightOutcomeSum += 1
        return fightOutcomeSum

    def NoSymbols(self, w: Weapon):
        symbolsSum = 0
        for g in self.games:
            for t in g.turns:
                if t.actions['player'] == w or t.actions['comp'] == w:
                    symbolsSum += 0
        return symbolsSum


class Game:
    def __init__(self):
        self.turns = []
        self.timestamp = datetime.datetime.now()

    def addTurn(self, t):
        if not isinstance(t, Turn):
            raise Exception("t needs to be type of Turn")
        self.turns.append(t)

    def getWins(self, fo: fighOutcome):
        wins = []
        for t in self.turns:
            if t.outcome == fo:
                wins.append(t)
        return wins

    def getSymbols(self, w: Weapon):
        symbols = []
        for t in self.turns:
            if t.actions['player'] == w or t.actions['comp'] == w:
                symbols.append(t)
        return symbols

    def toString(self):
        out = "[{ts}] noTurns: {noTurns}\n" \
              "[{ts}] playerWins: {playerWins}\n" \
              "[{ts}] compWins: {compWins}\n".format(
            ts=self.timestamp,
            noTurns = len(self.turns))

        for fo in fighOutcome:
            out += "[{ts}] {foName}: {foAmount}\n".format(ts = self.timestamp,
                                                          foName = fo.getName(),
                                                          foAmount = len(self.getWins(fo)))

        for w in Weapon:
            out += "[{ts}] {wName}: {wAmount}\n".format(ts = self.timestamp,
                                                        wName = w.getName(),
                                                        wAmount = len(self.getSymbols(w)))
        return out


class Turn:
    def __init__(self, weaponP1: Weapon, weaponP2: Weapon):
        if not isinstance(weaponP2, Weapon) or not isinstance(weaponP1, Weapon):
            raise Exception("The weapons must be type of Weapon")
        self.actions = {'player': weaponP1, 'comp': weaponP2}
        self.outcome = weaponP1.fights(weaponP2)
