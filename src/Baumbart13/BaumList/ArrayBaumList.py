from array import array as pyArr


class ArrayBaumList:
	def __init__(self):
		self.array: pyArr = None
		self._count = 0
		self._capacity = 0
		self.clear()

	def __len__(self) -> int:
		return self._count

	def __str__(self) -> str:
		return self.toString()

	def __contains__(self, item) -> bool:
		return self.hasElement(item=item)

	def __copy__(self):
		return self.clone()

	def __getitem__(self, index: int):
		return self.get(index=index)

	def __setitem__(self, index: int, item):
		self.add(index=index, item=item)

	def clone(self):
		pass

	def length(self) -> int:
		return self._count

	def count(self) -> int:
		return self._count

	def capacity(self) -> int:
		return self._capacity

	def add(self, index: int, item):
		pass

	def addBack(self, item):
		pass

	def addFront(self, item):
		pass

	def remove(self, item=None, index: int = None):
		pass

	def removeBack(self):
		pass

	def removeFront(self):
		pass

	def removeFirst(self):
		return self.removeFront()

	def removeLast(self):
		return self.removeBack()

	def getFront(self):
		pass

	def getBack(self):
		pass

	def get(self, index: int):
		pass

	def set(self, index: int, item):
		pass

	def hasElement(self, item) -> bool:
		pass

	def indexOf(self, item) -> int:
		pass

	def lastIndexOf(self, item) -> int:
		pass

	def push(self, item):
		self.addFront(item=item)

	def pushBack(self, item):
		self.addBack(item=item)

	def pop(self):
		return self.removeBack()

	def popFront(self):
		return self.removeFront()

	def enqueue(self, item):
		self.addFront(item=item)

	def dequeue(self):
		return self.removeBack()

	def clear(self):
		"""Removes all elements, but remains the same capacity"""
		self.array.clear()
		self._count = 0

	def toPythonList(self) -> list:
		pass

	@classmethod
	def fromPythonList(cls, l: list):
		pass

	def reverse(self):
		pass

	def toString(self) -> str:
		pass
