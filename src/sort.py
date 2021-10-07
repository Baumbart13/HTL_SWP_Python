def bubbleSort(list):
    for i in range(0, len(list)-1):
        for j in range(0,len(list)-i-1):
            if(list[j] > list[j+1]):
                list[j],list[j+1]
    return list

def insertionSort(list):
    j = -1
    key = list[0]

    for i in range(1, len(list)):
        key = list[i]
        j = i-1

        while(j >= 0 and list[j] > key):
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

def selectionSort(list):
    for i in range(0, len(list)):
        min = i

        for j in range(i+1, len(list)):
            if(list[min] > list[j]):
                min = j
        key = list[min]

        while(min > i):
            list[min] = list[min-1]
            min -= 1
        list[i] = key
    return list

# warum miassn ma schu wieda algorithmen machn? meina
# wer sudat, weat ned pudat

if __name__ == "__main__":
    mList = [2,5,8,6,4,8,9,10]

    bList = bubbleSort(mList)
    iList = insertionSort(mList)
    sList = selectionSort(mList)

    print(mList)
    print(bList)
    print(iList)
    print(sList)