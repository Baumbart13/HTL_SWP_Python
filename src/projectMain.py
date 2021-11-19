import src.Baumbart13.Utils.menu as Menu
import src.Baumbart13.RPS.rps
import sys

menu = Menu.Menu()

def createMenu():
    menu.reset()
    menu.addMenuEntry('rps', src.Baumbart13.RPS.rps.mainMenu, 'Enter the menu for Rock, Paper, Scissors, Lizard, Spock')


def Main():
    createMenu()
    menu.inputActions()
    Main()


if __name__ == '__main__':
    Main()
