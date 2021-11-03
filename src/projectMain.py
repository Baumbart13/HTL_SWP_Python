import src.Baumbart13.Utils.menu as Menu
import src.Baumbart13.RPS.rps


menu = Menu.Menu()


def createMenu():
    menu.addMenuEntry('rps', src.Baumbart13.RPS.rps.mainMenu, 'Enter the menu for Rock, Paper, Scissors, Lizard, Spock')


def Main():
    createMenu()
    x = input(menu.show())
    x = menu.getEntry(x)
    x.get('action')()
    print('Bye World')


if __name__ == '__main__':
    Main()
