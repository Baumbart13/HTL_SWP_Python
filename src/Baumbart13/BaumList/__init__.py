import random


def _isSorted(baumList) -> bool:
    for i in range(1, len(baumList), 1):
        if baumList[i - 1] > baumList[i]:
            print(f"Error on index {i} and {i-1}")
            return False
    return True


def _isSortedReversed(baumList) -> bool:
    baumList.reverse()
    return _isSorted(baumList)


def _testSpecificLinkedList():
    from src.Baumbart13.BaumList.LinkedBaumList import LinkedBaumList
    print('==== Asserting main functionality of LinkedBaumList ====')
    l = LinkedBaumList()
    print('init -                   "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'

    l.addFront(2)
    print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.addBack(3)
    print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'
    assert str(l) == '[1, 2, 3]'

    l.removeBack()
    print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.removeFirst()
    print('removeFront() -         "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    l.addBack(3)
    l.remove(index=1)
    print('remove(1) -          "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.reverse()
    print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.clear()
    print('clear() -                "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'


def _testSpecificArrayList():
    from src.Baumbart13.BaumList.ArrayBaumList import ArrayBaumList
    print('\n\n===== Asserting main functionality of ArrayBaumList ====')
    l = ArrayBaumList()
    print('init -                   "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'

    l.addFront(2)
    print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.addBack(3)
    print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'
    assert str(l) == '[1, 2, 3]'

    l.removeBack()
    print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.removeFirst()
    print('removeFront() -         "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    l.addBack(3)
    l.remove(index=1)
    print('remove(index=1) -    "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.reverse()
    print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.sortAsc()
    print('sortAsc() -          "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.sortDesc()
    print('sortDesc() -         "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.clear()
    print('clear() -                "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'


def _testLinkedList():
    from time import perf_counter_ns as timestamp
    rng = random.Random()
    noElements = 10_000
    print(f"Creating python-list with {noElements} elements")
    l = [int(rng.random() * noElements * 10) for i in range(noElements)]

    from src.Baumbart13.BaumList.LinkedBaumList import LinkedBaumList
    print("Converting python-list to LinkedBaumList")
    ll = LinkedBaumList.fromPythonList(l)

    print("Measuring sorting time")
    start = timestamp()
    ll.sortAsc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSorted(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(stop - start)} ns for execution")

    print("Converting python-list to LinkedBaumList")
    ll = LinkedBaumList.fromPythonList(l)
    print("Measuring sorting time")
    start = timestamp()
    ll.sortDesc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSortedReversed(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(stop-start)} ns for execution")

def _testArrayList():
    from time import perf_counter_ns as timestamp
    rng = random.Random()
    noElements = 10_000
    print(f"Creating python-list with {noElements} elements")
    l = [int(rng.random() * noElements * 10) for i in range(noElements)]

    from src.Baumbart13.BaumList.ArrayBaumList import ArrayBaumList
    print("Converting python-list to ArrayBaumList")
    ll = ArrayBaumList.fromPythonList(l)

    print("Measuring sorting time")
    start = timestamp()
    ll.sortAsc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSorted(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(stop - start)} ns for execution")

    print("Converting python-list to LinkedBaumList")
    ll = ArrayBaumList.fromPythonList(l)
    print("Measuring sorting time")
    start = timestamp()
    ll.sortDesc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSortedReversed(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(stop-start)} ns for execution")


if __name__ == '__main__':
    # from src.Baumbart13.BaumList.ArrayBaumList import ArrayBaumList as myList
    # ll = myList.fromPythonList([12, 11, 13, 5, 6])
    # print(f"Before sort\t'{ll.toPythonList()}'")
    # ll.sortAsc()
    # print(f"After sort\t'{ll.toPythonList()}'")
    # ll = myList.fromPythonList([12, 11, 13, 5, 6])
    # print(f"Before sort\t'{ll.toPythonList()}'")
    # ll.sortDesc()
    # print(f"After sort\t'{ll.toPythonList()}'")

    #_testSpecificLinkedList()
    #_testLinkedList()
    _testArrayList()
    #_testSpecificArrayList()
