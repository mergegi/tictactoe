def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(0, passnum, 1):
            j = i + 1
            if aList[i]<aList[i+1]:
                temp = aList[i]
                aList[i] = aList[j]
                aList[j] = temp
    return aList

aList = [54,26,93,17,77,31,44,55,20]
print("Original list:" + str(aList))
print("Sorted List:" + str(bubbleSort(aList)))
