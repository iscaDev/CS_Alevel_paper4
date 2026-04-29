LinkedList = [] # global
for i in range(20):
    LinkedList.append([-1, i+1])
LinkedList[19][1] = -1
FirstNode = -1 # global
FirstEmpty = 0 # global

def InsertData():
    global FirstNode, FirstEmpty, LinkedList
    for j in range(5):
        if FirstEmpty != -1:
            newnode = FirstEmpty
            FirstEmpty = LinkedList[newnode][1]
            LinkedList[newnode][0] = int(input("Please enter a positive integer: "))
            LinkedList[newnode][1] = FirstNode
            FirstNode = newnode

def OutputLinkedList():
    global FirstNode
    currentNode = FirstNode
    while currentNode != -1:
        print(LinkedList[currentNode][0], end=" ")
        currentNode = LinkedList[currentNode][1]

def RemoveData(par):
    global FirstNode, FirstEmpty, LinkedList
    if LinkedList[FirstNode][0] == par:
        newFirst = LinkedList[FirstNode][1]
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = newFirst
    else:
        if FirstEmpty != -1:
            currentPointer = FirstNode
            previousNode = -1
            while currentPointer != -1 and LinkedList[currentPointer][0] != par:
                previousNode = currentPointer
                currentPointer = LinkedList[currentPointer][1]
            if LinkedList[currentPointer][0] == par:
                LinkedList[previousNode][1] = LinkedList[currentPointer][1]
                LinkedList[currentPointer][0] = -1
                LinkedList[currentPointer][1] = FirstEmpty
                FirstEmpty = currentPointer


# main program
InsertData()
OutputLinkedList()

RemoveData(5)
print("After")
OutputLinkedList()