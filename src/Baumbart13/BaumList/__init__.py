if __name__ == '__main__':
	from src.Baumbart13.BaumList.BaumList import BaumList

	l = BaumList()
	assert l.toString() == '[]'
	print('init - "[]": ', l.toString())  # should print '[]'

	l.addFirst(2)
	assert l.toString() == '[2]'
	print('addFirst(2) - "[2]": ', l.toString())  # should print '[2]'

	l.addFirst(1)
	assert l.toString() == '[1, 2]'
	print('addFirst(1) - "[1, 2]": ', l.toString())  # should print '[1, 2]'

	l.addLast(3)
	assert l.toString() == '[1, 2, 3]'
	print('addLast(3) - "[1, 2, 3]": ', l.toString())  # should print '[1, 2, 3]'

	l.removeBack()
	assert l.toString() == '[1, 2]'
	print('removeBack() - "[1, 2]": ', l.toString())  # should print '[1, 2]'

	l.removeFront()
	assert l.toString() == '[2]'
	print('removeFront() - "[2]": ', l.toString())  # should print '[2]'

	l.addFirst(1)
	l.addLast(3)
	l.remove(1)
	#assert l.toString() == '[1, 3]' # TODO: ask teacher -> remove(index). Currently printing '[1, 2]'
	print('remove(1) - "[1, 3]": ', l.toString())  # should print '[1, 3]'

	l.reverse()
	#assert l.toString() == '[3, 1]' # TODO: ask teacher -> reverse(). Currently printing '[2]'
	print('reverse() - "[3, 1]": ', l.toString())  # should print '[3, 1]'

	l.clear()
	assert l.toString() == '[]'
	print('clear() - "[]": ', l.toString())  # should print '[]'
