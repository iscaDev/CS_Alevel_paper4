import random

def PrintArray(arrP):
    output = ""
    for num in arrP:
        output += str(num) + " "
    print(output)

def BubbleSort(arrP):
    array = arrP
    length = len(array)
    for i in range(length):
        swapped = False
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:
            break
    return array

def RecursiveBinarySearch(arrP, lowerP, upperP, toFind):
    low = lowerP
    high = upperP
    if low <= high:
        mid = (low+high)//2
        if arrP[mid] == toFind:
            return mid
        elif arrP[mid] > toFind:
            return RecursiveBinarySearch(arrP, low, mid - 1, toFind)
        else:
            return RecursiveBinarySearch(arrP, mid + 1, high, toFind)
    else:
        return -1

# main program
arr = []
for i in range(20):
    num = random.randint(0,100)
    while num in arr:
        num = random.randint(0,100)
    arr.append(num)

PrintArray(arr)
print("Sorted")
arr = BubbleSort(arr)
PrintArray(arr)
n = int(input("Enter an integer: "))
returnValue = RecursiveBinarySearch(arr, 0, 19, n)
if returnValue == -1:
    print("Not found")
else:
    print("Found at position", returnValue)