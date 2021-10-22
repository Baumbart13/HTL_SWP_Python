from src.Baumbart13.Utils import menu as Menu

menu = Menu.Menu()

def play():
    pass

def createMainMenu():
    menu = Menu.Menu()
    menu.addMenuEntry('p', play, 'Play the Rock, Paper, Scissors, Lizard, Spock!')

def createPlayMenu():
    menu.reset()

def main():
    pass

createMainMenu()
print(menu.show())