import src.projectMain
from src.Baumbart13.Utils import menu as Menu
from src.Baumbart13.RPS.Signs import *
from src.Baumbart13.RPS.fightOutcome import fighOutcome


menu = Menu.Menu()

# creating menus


def _createMainMenu():
    """Creates the main menu. Will automatically be called inside of play"""
    menu.reset()
    menu.addMenuEntry('play', skirmishMenu, 'Play the Rock, Paper, Scissors, Lizard, Spock!')
    menu.addMenuEntry('view', statsMenu, 'Enter the stats-menu')

    menu.editEntryDesc('x', "Go back to the main project menu")
    menu.editEntryAction('x', src.projectMain.Main)


def _createStatsMenu():
    """Creates the stats menu. Statistics are manageable here"""
    menu.reset()
    menu.addMenuEntry('view', stats_view, 'Take a look at some stats')
    menu.addMenuEntry('save', stats_save, 'Save your temporarily saved file permanently')
    menu.addMenuEntry('del', stats_delete, 'Delete all permanently saved stats')

    menu.editEntryDesc('x', 'Go back to the game\'s main menu')
    menu.editEntryAction('x', mainMenu)


def _createSkirmishMenu():
    """Creates the menu for the skirmish against the comp."""
    menu.reset()
    menu.addMenuEntry('rock', Weapon.ROCK, "Choose Rock as your weapon")
    menu.addMenuEntry('paper', Weapon.PAPER, "Choose Paper as your weapon")
    menu.addMenuEntry('scissors', Weapon.SCISSORS, "Choose Scissors as your weapon")
    menu.addMenuEntry('lizard', Weapon.LIZARD, "Choose Lizard as your weapon")
    menu.addMenuEntry('spock', Weapon.SPOCK, "Choose Spock as your weapon")

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
    _createStatsMenu()
    menu.inputActions()


def skirmishMenu():
    """The cycle of a game"""
    _createSkirmishMenu()

    while True:
        canDoAction = False
        x = input(menu.show())
        while not canDoAction:
            for i in range(0, len(menu.menuEntries)):
                if menu.menuEntries[i]['cmd'] == x:
                    canDoAction = True
                    break
            if not canDoAction:
                print("'", x, "'is an unknown command, please try again")
                x = input(menu.show())
        x = menu.getEntry(x)
        if x.get('action') == mainMenu:
            x.get('action')()
        player_weapon = x.get('action')
        comp_weapon = getRandomWeapon()
        outcome = player_weapon.fights(comp_weapon)
        if outcome == fighOutcome.Equal:
            print("It's a draw!")
        elif outcome == fighOutcome.YouWin:
            print("You win this round! {PLAYER:'", player_weapon.getName(), "'> COMP:'", comp_weapon.getName(), "'}")
        elif outcome == fighOutcome.OpponentWins:
            print("COMP wins this round! {PLAYER:'", player_weapon.getName(), "'< COMP:'", comp_weapon.getName(), "'}")
        else:
            raise Exception("I've got a bad feeling about this")


def mainMenu():
    """This is the main method for the game. Here the game will be initialized and the main menu will be shown."""
    _createMainMenu()
    menu.inputActions()


if __name__ == '__main__':
    mainMenu()
