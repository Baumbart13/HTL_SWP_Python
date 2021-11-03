from src.Baumbart13.RPS.Signs import Weapon


class Counter:
    def __init__(self):
        self.games = []
    def addGame(self, g):
        if not isinstance(g, Game):
            raise Exception("g must be type of Game")
        self.games.append(g)


class Game:
    def __init__(self):
        self.turns = []


    def addTurn(self, t):
        if not isinstance(t, Turn):
            raise Exception("t needs to be type of Turn")
        self.turns.append(t)


class Turn:
    def __init__(self, weaponP1: Weapon, weaponP2: Weapon):
        if not isinstance(weaponP2, Weapon) or not isinstance(weaponP1, Weapon):
            raise Exception("The weapons must be type of Weapon")
        self.actions = {'player': weaponP1, 'comp': weaponP2}
        self.outcome = weaponP1.fights(weaponP2)
