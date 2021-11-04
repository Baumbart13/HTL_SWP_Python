import time

# for-loop needs  46.87406945228577
# doing "[value]*noElements":  1.441084384918213
# appending the elements in a for-loop:  49.3338360786438
# extending the elements in a for-loop:  67.87569308280945
# using "map":  62.11240601539612

NoElements = 500000000 # allocating about 4Gigs of memory

def runThis():
    print('Measuring times, that are needed to fill a container with 1 specific value')

    start = time.time()
    arr = [int]*NoElements
    for i in range(0, NoElements):
        arr[i] = 3
    end = time.time()
    del(arr)
    print('for-loop needs ', end-start)

    start = time.time()
    arr = [3]*NoElements
    end = time.time()
    del(arr)
    print('doing "[value]*noElements": ', end-start)

    arr = []
    start = time.time()
    for i in range(0, NoElements):
        arr.append(3)
    end = time.time()
    del(arr)
    print('appending the elements in a for-loop: ', end-start)

    arr = []
    start = time.time()
    for i in range(0, NoElements):
        arr.extend([3])
    end = time.time()
    del(arr)
    print('extending the elements in a for-loop: ', end-start)

    arr = [int]*NoElements
    start = time.time()
    arr = list(map(lambda x: 3, arr))
    end = time.time()
    del(arr)
    print('using "map": ', end-start)

    print('done')

if __name__=='__main__':
    runThis()