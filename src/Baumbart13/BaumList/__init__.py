import random


def _isSorted(baumList) -> bool:
	for i in range(1, len(baumList), 1):
		if baumList[i - 1] > baumList[i]:
			return False
	return True


def _isSortedReversed(baumList) -> bool:
	baumList.reverse()
	return _isSorted(baumList)


def _testSpecificLinkedList():
	from src.Baumbart13.BaumList.LinkedBaumList import LinkedBaumList
	print('==== Asserting main functionality of LinkedBaumList ====')
	l = LinkedBaumList()
	assert str(l) == '[]'
	print('init -                   "[]" :', str(l))  # should print '[]'

	l.addFront(2)
	assert str(l) == '[2]'
	print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'

	l.addFront(1)
	assert str(l) == '[1, 2]'
	print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'

	l.addBack(3)
	assert str(l) == '[1, 2, 3]'
	print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'

	l.removeBack()
	assert str(l) == '[1, 2]'
	print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'

	l.removeFirst()
	assert str(l) == '[2]'
	print('removeFront() -         "[2]" :', str(l))  # should print '[2]'

	l.addFront(1)
	l.addBack(3)
	l.remove(index=1)
	assert str(l) == '[1, 3]'
	print('remove(1) -          "[1, 3]" :', str(l))  # should print '[1, 3]'

	l.reverse()
	assert str(l) == '[3, 1]'
	print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'

	l.clear()
	assert str(l) == '[]'
	print('clear() -                "[]" :', str(l))  # should print '[]'


def _testSpecificArrayList():
	from src.Baumbart13.BaumList.ArrayBaumList import ArrayBaumList
	print('\n\n===== Asserting main functionality of ArrayBaumList ====')
	l = ArrayBaumList()
	assert str(l) == '[]'
	print('init -                   "[]" :', str(l))  # should print '[]'

	l.addFront(2)
	assert str(l) == '[2]'
	print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'

	l.addFront(1)
	assert str(l) == '[1, 2]'
	print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'

	l.addBack(3)
	assert str(l) == '[1, 2, 3]'
	print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'

	l.removeBack()
	assert str(l) == '[1, 2]'
	print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'

	l.removeFirst()
	assert str(l) == '[2]'
	print('removeFront() -         "[2]" :', str(l))  # should print '[2]'

	l.addFront(1)
	l.addBack(3)
	l.remove(index=1)
	assert str(l) == '[1, 3]'
	print('remove(1) -          "[1, 3]" :', str(l))  # should print '[1, 3]'

	l.reverse()
	assert str(l) == '[3, 1]'
	print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'

	l.clear()
	assert str(l) == '[]'
	print('clear() -                "[]" :', str(l))  # should print '[]'


def _testLinkedList():
	from time import perf_counter as timestamp
	rng = random.Random()
	noElements = 10_000
	l = [int(rng.random()*noElements*10)for i in range(noElements)]
	from src.Baumbart13.BaumList.LinkedBaumList import LinkedBaumList
	ll = LinkedBaumList.fromPythonList(l)
	start = timestamp()
	ll.sortAsc()
	stop = timestamp()
	sorted = _isSorted(ll)
	assert sorted
	print(f"List is {'sorted' if sorted else 'unsorted'}")


if __name__ == '__main__':
	_testSpecificLinkedList()
# _testSpecificArrayList()
