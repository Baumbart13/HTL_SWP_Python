import src.Baumbart13.Utils.menu as Menu
import src.Baumbart13.RPS

menu = Menu.Menu()

def createMenu():
    menu.addMenuEntry('rps', src.Baumbart13.RPS.rps.main, 'Enter the menu for Rock Paper Scissors, Lizard, Spock')

def rockPaperScissors():
    RPS.rps.main()

if __name__=='__main__':
    createMenu()

x = input(menu.show())
x = menu.getEntry(x)
print(x['action'])()