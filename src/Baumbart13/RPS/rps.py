import src.projectMain
from src.Baumbart13.Utils import menu as Menu
from src.Baumbart13.RPS.Signs import *


menu = Menu.Menu()

# creating menus


def createMainMenu():
    """Creates the main menu. Will automatically be called inside of play"""
    menu.reset()
    menu.addMenuEntry('play', skirmishMenu, 'Play the Rock, Paper, Scissors, Lizard, Spock!')
    menu.addMenuEntry('view', statsMenu, 'Enter the stats-menu')

    menu.editEntryDesc('x', "Go back to the main project menu")
    menu.editEntryAction('x', src.projectMain.Main)


def createStatsMenu():
    """Creates the stats menu. Statistics are manageable here"""
    menu.reset()
    menu.addMenuEntry('view', stats_view, 'Take a look at some stats')
    menu.addMenuEntry('save', stats_save, 'Save your temporarily saved file permanently')
    menu.addMenuEntry('del', stats_delete, 'Delete all permanently saved stats')

    menu.editEntryDesc('x', 'Go back to the game\'s main menu')
    menu.editEntryAction('x', mainMenu)


def createSkirmishMenu():
    """Creates the menu for the skirmish against the comp."""
    menu.reset()
    menu.addMenuEntry('r', ROCK, "Choose Rock as your weapon")
    menu.addMenuEntry('r', PAPER, "Choose Paper as your weapon")
    menu.addMenuEntry('r', SCISSORS, "Choose Scissors as your weapon")
    menu.addMenuEntry('r', LIZARD, "Choose Lizard as your weapon")
    menu.addMenuEntry('r', SPOCK, "Choose Spock as your weapon")

    menu.editEntryAction('x', mainMenu)
    menu.editEntryDesc('x', "Go back to game's main menu")


# stats-actions


def stats_view():
    pass


def stats_save():
    pass


def stats_delete():
    pass


# menu-actions


def statsMenu():
    """The menu for the stats"""
    createStatsMenu()
    menu.inputActions()


def skirmishMenu():
    """The cycle of a game"""
    createSkirmishMenu()
    menu.inputActions()


def mainMenu():
    """This is the main method for the game. Here the game will be initialized and the main menu will be shown."""
    createMainMenu()
    menu.inputActions()


if __name__ == '__main__':
    mainMenu()
