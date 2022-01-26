class Node:

    def __init__(self, item=0):
        self.item = item
        self.nextNode = Node()
        self.prevNode = Node()


class BaumList:
    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.length = 0

    def addFirst(self, item):
        newNode = Node(item)
        newNode.nextNode = self.first

        if self.last is None:
            self.last = newNode
        self.first.prevNode = newNode

    def addLast(self, item):
        newNode = Node(item)

        if self.first is None:
            self.first = newNode

        if self.last is not None:
            self.last.nextNode = newNode

    def get(self, index):
        if index >= self.length:
            raise Exception("Index out of range")

        if index > self.length * 0.5:
            currIndex = self.length - 1
            n = self.last
            while n is not None:
                if currIndex == index:
                    return n.item
                n = n.prev
                currIndex -= 1
        else:
            currIndex = 0
            n = self.first
            while n is not None:
                if currIndex == index:
                    return n.item
                n = n.next
                currIndex += 1
        return 0

    def remove(self, index):
        if index > self.length:
            raise Exception("Index out of range")

        if index > self.length * 0.5:
            currIndex = self.length - 1
            n = self.last
            while n is not None:
                if currIndex == index:
                    n.prevNode.nextNode = n.nextNode
                    n.nextNode.prevNode = n.prevNode
                    del(n)
                    break
                currIndex -= 1
        else:
            currIndex = 0
            n = self.first
            while n is not None:
                if currIndex == index:
                    n.nextNode.prevNode = n.prevNode
                    n.prevNode.nextNode = n.nextNode
                    del(n)
                    break
                currIndex += 1
        return