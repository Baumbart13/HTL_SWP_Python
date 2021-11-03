import sys


class Menu:
    """
    Holds various menu-entries. Comes with the default entry of exiting the program.
    The structure of an entry is {'cmd':str,'action':function,'desc':str}
    """

    def __init__(self):
        self.menuEntries = [{'cmd': 'x', 'action': sys.exit, 'desc': 'Exit the program'}]

    def show(self):
        """Returns all menu entries' commands and their descriptions"""
        s = ""
        for i in range(0, len(self.menuEntries)):
            s += '[' + self.menuEntries[i]['cmd'] + '] - '
            s += self.menuEntries[i]['desc'] + '\n'
        return s

    def getEntry(self, cmd: str):
        for i in range(0, len(self.menuEntries)):
            if (self.menuEntries[i]['cmd'] == cmd):
                return self.menuEntries[i]

    def editEntryDesc(self, cmd: str, newDesc: str):
        for i in range(0, len(self.menuEntries)):
            if (self.menuEntries[i]['cmd'] == cmd):
                self.menuEntries[i]['desc'] = newDesc
                return
        raise Exception("Cannot edit non-existing command's description")

    def editEntryAction(self, cmd: str, newAction):
        for i in range(0, len(self.menuEntries)):
            if (self.menuEntries[i]['cmd'] == cmd):
                self.menuEntries[i]['action'] = newAction
                return
        raise Exception("Cannot edit non-existing command's action")

    def addMenuEntry(self, cmd: str, action, desc: str, index=0):
        """
        :param cmd The command that will be used to take the action
        :param action The function/method that will be called
        :param desc A description about the function provided for the user
        :returns nothing. This method's type is void
        """
        self.menuEntries.insert(index, {'cmd': cmd, 'action': action, 'desc': desc})

    def reset(self):
        """Deletes all Entries but the exit-Entry"""
        self.menuEntries.clear()
        self.addMenuEntry('x', sys.exit, 'Exit the program')

    def inputActions(self):
        x = input(self.show())
        newX = (-1, x)
        for i in range(0, len(self.menuEntries)):
            if self.menuEntries[i]['cmd'] == x:
                newX = (i, self.menuEntries[i]['cmd'])
        if x == newX[1]:
            print("'", x, "' is an unknown command, please try again")
            self.inputActions()
        newX = self.getEntry(x)
        newX.get('action')
