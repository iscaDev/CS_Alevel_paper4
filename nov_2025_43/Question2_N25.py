Queue = ["" for i in range(100)] # global
QueueHead = -1 # global
QueueTail = -1 # global
NumberItems = 0
NewString = "" # global

def Enqueue(par):
    global Queue, QueueHead, QueueTail, NumberItems
    if QueueTail >= 99:
        return False
    else:
        if QueueHead == -1:
            QueueHead = 0
        QueueTail += 1
        Queue[QueueTail] = par
        NumberItems += 1
        return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return "False"
    else:
        temp = QueueHead
        QueueHead += 1
        NumberItems -= 1
        return Queue[temp]

def ReadData():
    global Queue
    try:
        f = open("BinaryData.txt", "r")
        for line in f:
            just = Enqueue(line.strip())
        f.close()
    except FileNotFoundError:
        print("File not found")

def Compress():
    global NewString
    first = Dequeue()
    while NumberItems > 0 and first != "False":
        count = 1
        nextBit = Dequeue()
        while nextBit == first:
            count += 1
            first = nextBit
            nextBit = Dequeue()
        NewString += first + str(count)
        first = nextBit

# main program
ReadData()
Compress()
print(NewString)