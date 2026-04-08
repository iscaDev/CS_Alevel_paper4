NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 0:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(1, NumberElements):
        key = IntegerArray[i]
        j = i - 1
        while j >= 0 and key < IntegerArray[j]:
            IntegerArray[j+1] = IntegerArray[j]
            j -= 1
        IntegerArray[j+1] = key
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        mid = (First + Last) // 2
        if IntegerArray[mid] == ToFind:
            return mid
        elif IntegerArray[mid] > ToFind:
            return BinarySearch(IntegerArray, First, mid - 1, ToFind)
        else:
            return BinarySearch(IntegerArray, mid + 1, Last, ToFind)


# main program
print("Recursive")
print(RecursiveInsertion(NumberArray, 7))
print("iterative")
print(IterativeInsertion(NumberArray, 7))
status = BinarySearch(NumberArray, 0, 6, 644)
if status == -1:
    print("Not found")
else:
    print(status)