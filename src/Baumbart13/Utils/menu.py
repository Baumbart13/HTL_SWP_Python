import sys

class Menu:
    """
    Holds various menu-entries. Comes with the default entry of exiting the program.
    The structure of an entry is {'cmd':str,'action':function,'desc':str}
    """

    def __init__(self):
        self.menuEntries = [{'cmd':'x','action':sys.exit, 'desc':'Exit the program'}]

    def show(self):
        s = ""
        for i in range(0, len(self.menuEntries)):
            s += '[' + self.menuEntries[i]['cmd'] + '] - '
            s += self.menuEntries[i]['desc'] + '\n'
        return s

    def getEntry(self, cmd:str):
        for i in range(0, len(self.menuEntries)):
            if(self.menuEntries[i]['cmd']==cmd):
                return self.menuEntries[i]

    def addMenuEntry(self, cmd:str, action, desc:str, index=0):
        """
        :param cmd The command that will be used to take the action
        :param action The function/method that will be called
        :param desc A description about the function provided for the user
        :returns nothing. This method's type is void
        """
        self.menuEntries.insert(index, {'cmd':cmd, 'action':action, 'desc':desc})

    def reset(self):
        while(len(self.menuEntries)>1):
            if(self.menuEntries[-1]['cmd']=='x'):
                self.menuEntries[-1], self.menuEntries[0]
            self.menuEntries.pop()