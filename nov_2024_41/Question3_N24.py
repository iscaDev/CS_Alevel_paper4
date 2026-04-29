LinkedList = [] # global
for i in range(20):
    LinkedList.append([-1, i+1])
LinkedList[19][1] = -1
FirstNode = -1 # global
FirstEmpty = 0 # global

def InsertData():
    global FirstNode, FirstEmpty, LinkedList
    for i in range(5):
        num = int(input("Please enter a positive integer:"))