class Node:

    def __init__(self, item=None):
        self.item = item
        self.nextNode: Node = None
        self.prevNode: Node = None


class BaumList:
    def __init__(self):
        self.first: Node = Node()
        self.last: Node = Node()
        self.clear()
        self._count: int = 0

    def _checkElementIndex(self, index: int):
        if not self._isElementIndex(index):
            raise Exception("Index out of bounds")

    def _checkPositionIndex(self, index: int):
        if not self._isPositionIndex(index):
            raise Exception("Index out of bounds")

    def _isElementIndex(self, index: int):
        return 0 <= index < self._count

    def _isPositionIndex(self, index: int):
        return 0 <= index <= self._count

    def length(self):
        return self._count

    def count(self):
        return self._count

    def _linkFirst(self, item):
        f: Node = self.first
        newNode: Node = Node(item)
        newNode.nextNode = f
        f = newNode
        if f is None:
            self.last = newNode
        else:
            f.prevNode = newNode
        self._count += 1

    def _linkLast(self, item):
        l: Node = self.last
        newNode: Node = Node(item)
        newNode.prevNode = l
        self.last = newNode
        if l is None:
            self.first = newNode
        else:
            l.nextNode = newNode
        self._count += 1

    def _linkBefore(self, item, succ: Node):
        assert succ is not None
        pred: Node = succ.prevNode
        newNode: Node = Node(item)
        newNode.prevNode = pred
        newNode.nextNode = succ
        succ.prevNode = newNode
        if pred is None:
            self.first = newNode
        else:
            pred.nextNode = newNode
        self._count += 1

    def _unlinkFirst(self, f: Node):
        assert f == self.first and f is not None
        element = f.item
        next: Node = f.nextNode
        f.item = None
        f.nextNode = None
        del f.item
        del f.nextNode
        del f
        self.first = next
        if next is None:
            self.last = None
        else:
            next.prevNode = None
        self._count -= 1
        return element

    def _unlinkLast(self, l: Node):
        assert l == self.last and l is not None
        element = l.item
        prev: Node = l.prevNode
        l.item = None
        l.prevNode = None
        del l.item
        del l.prevNode
        del l
        self.last = prev
        if prev is None:
            self.first = None
        else:
            prev.nextNode = None
        self._count -= 1
        return element

    def _unlink(self, x: Node):
        assert x is not None
        element = x.item
        next: Node = x.nextNode
        prev: Node = x.prevNode
        if prev is None:
            self.first = next
        else:
            prev.nextNode = next
            x.prevNode = None
        if next is None:
            self.last = prev
        else:
            next.prevNode = prev
            x.nextNode = None
        x.item = None
        self._count -= 1
        return element

    def add(self, item):
        self._linkLast(item)
        return True

    def addLast(self, item):
        self._linkLast(item)

    def addFirst(self, item):
        self._linkFirst(item)

    def remove(self, item):
        if item is None:
            x: Node = self.first
            while x is not None:
                if x.item is None:
                    self._unlink(x)
                    return True
                x = x.nextNode
        else:
            x: Node = self.first
            while x is not None:
                # We want to compare equality of the element, not the address
                if item == x.item:  # TODO: Probably needs to be updated
                    self._unlink(x)
                    return True
                x = x.nextNode

    def removeBack(self):
        value = self.last.item
        newLast = self.last.prevNode
        newLast.nextNode = None
        self.last = newLast
        return value

    def removeFront(self):
        value = self.first.item
        newFirst = self.first.nextNode
        newFirst.prevNode = None
        self.first = newFirst
        return value

    def getFirst(self):
        f = self.first
        if f is None:
            raise Exception("There is no such element")
        return f.item

    def getLast(self):
        l = self.last
        if l is None:
            raise Exception("There is no such element")
        return l.item

    def get(self, index):  # TODO: update this method
        l = self.length()
        if index >= l:
            raise Exception("Index out of bounds")
        if index < 0:
            index = l + index

        # start from right, go to left
        currNode = self.last
        currIndex = l - 1
        if index > l * 0.5:
            # currIndex = l-1 # redundant
            # currNode = self.last # redundant
            while currNode.prevNode is not None:
                currNode = currNode.prevNode
                currIndex -= 1
                if currIndex == index:
                    return currNode.item
                if currIndex < 0:
                    raise Exception("Index out of bounds")
        # start from left, go to right
        else:
            currIndex = 0
            currNode = self.first
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
                currIndex += 1
                if currIndex == index:
                    return currNode.item
                if currIndex >= l:
                    raise Exception("Index out of bounds")

    def removeFirst(self):
        f = self.first
        if f is None:
            raise Exception("There is no such element")
        return self._unlinkFirst(f.item)

    def removeLast(self):
        l = self.last
        if l is None:
            raise Exception("There is no such element")
        return self._unlinkLast(l.item)

    def hasElement(self, item):
        currNode = self.first
        while currNode.nextNode is not None:
            if currNode.item == item:
                return True
            currNode = currNode.nextNode
        return False

    def clear(self):
        x: Node = self.first
        while x is not None:
            next: Node = x.nextNode
            x.item = None
            x.nextNode = None
            x.prevNode = None
            del x.item
            del x.nextNode
            del x.prevNode
            x = next
        self.first = self.last = None
        self._count = 0

    def toPythonList(self):
        l = []
        currNode = self.first
        l.append(currNode.item)
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
            l.append(currNode.item)
        return l

    def reverse(self):
        l = self.toPythonList()
        self.clear()
        for i in range(len(l) - 1, -1, -1):
            self.addFirst(l[i])

    def toString(self):
        currNode = self.first
        string = '['
        if currNode is None:
            return string + ']'
        string = string + str(currNode.item)
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
            string = string + ", " + str(currNode.item)
        return string + ']'
