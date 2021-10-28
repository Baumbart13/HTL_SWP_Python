from src.Baumbart13.Utils import menu as Menu

menu = Menu.Menu()


def createMainMenu():
    """Creates the main menu. Will automatically be called inside of play"""
    menu.reset()
    menu.addMenuEntry('play', skirmishMenu, 'Play the Rock, Paper, Scissors, Lizard, Spock!')
    menu.addMenuEntry('view', statsMenu, 'Enter the stats-menu')


def createStatsMenu():
    """Creates the stats menu. Statistics are manageable here"""
    menu.reset()
    menu.addMenuEntry('view', stats_view, 'Take a look at some stats')
    menu.addMenuEntry('save', stats_save, 'Save your temporarily saved file permanently')
    menu.addMenuEntry('del', stats_delete, 'Delete all permanently saved stats')

    menu.editEntryDesc('x', 'Go back to the game\'s main menu')
    menu.editEntryAction('x', mainMenu)


def createPlayMenu():
    menu.reset()
    menu.addMenuEntry()




def stats_view():
    pass


def stats_save():
    pass


def stats_delete():
    pass




def statsMenu():
    """The menu for the stats"""


def skirmishMenu():
    """The cycle of a game"""
    x = input(menu.show())
    x = menu.getEntry(x)
    x.get('action')()


def mainMenu():
    """This is the main method for the game. Here the game will be initialized and the main menu will be shown."""
    createMainMenu()
    x = input(menu.show())
    x = menu.getEntry(x)
    x.get('action')()


if __name__ == '__main__':
    mainMenu()
