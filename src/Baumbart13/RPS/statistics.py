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
        self.text = self._toStringFromLists()
        self._weapons = []
        self._humanVsComp = []
        self._noTurns = 0

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

    def _toStringFromLists(self):
        out = "[{ts}] noTurns: {noTurns}\n".format(
            ts=self.timestamp,
            noTurns=len(self.turns))

        for fo in fighOutcome:
            out.join("[{ts}] {foName}: {foAmount}\n".format(
                ts=self.timestamp,
                foName=fo.name,
                foAmount=len(self.getWins(fo)))
            )

        for w in Weapon:
            out.join("[{ts}] {wName}: {wAmount}\n".format(
                ts=self.timestamp,
                wName=w.getName(),
                wAmount=len(self.getSymbols(w)))
            )
        return out

    def _toStringFromStats(self):
        out = "[{ts}] noTurns: {noTurns}\n".format(
            ts=self.timestamp,
            noTurns=self._noTurns
        )
        for i in range(len(self._humanVsComp)):
            out.join("[{ts}] {foName}: {foAmount}\n".format(
                ts=self.timestamp,
                foName=self._humanVsComp[i]['foStr'],
                foAmount=self._humanVsComp[i]['foAmount']
            ))
        for i in range(len(self._weapons)):
            out.join("[{ts}] {wName}: {wAmount}\n".format(
                ts=self.timestamp,
                wName=self._weapons[i]['wName'],
                wAmount=self._weapons[i]['wAmount']
            ))

    def saveToFile(self, savegameName: str):
        f = open(savegameName, 'w')
        return

    def saveToFile(self):
        filePath = "./saves"

    def readStats(self, path: str):
        self.text = self._toStringFromStats()

        f = open(path, 'r')
        line = f.readline()
        self.timestamp = line[line.index('[') + 1:line.index(']')]
        self._noTurns = line[line.index(':') + 2:]
        self._humanVsComp = []
        for i in range(len(fighOutcome)):
            line = f.readline()
            foStr = line[line.index(']') + 2:line.index(':')]
            foAmount = line[line.index(':') + 2:]
            self._humanVsComp.append({'foStr': foStr, 'foAmount': foAmount})

        self._weapons = []
        for i in range(len(Weapon)):
            line = f.readline()
            wStr = line[line.index(']') + 2:line.index(':')]
            wAmount = line[line.index(':') + 2:]
            self._weapons.append({'wStr': wStr, 'wAmount': wAmount})
        return


class Turn:
    def __init__(self, player: Weapon, comp: Weapon):
        if not isinstance(comp, Weapon) or not isinstance(player, Weapon):
            raise Exception("The weapons must be type of Weapon")
        self.actions = {'player': player, 'comp': comp}
        self.outcome = player.fights(comp)
