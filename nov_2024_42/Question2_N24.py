class Queue:
    def __init__(self):
        self.QueueArray = [] # QueueArray as array of Integers
        self.HeadPointer = 0 # HeadPointer as Integer
        self.TailPointer = 0 # TailPointer as Integer

def Enqueue(AQueue, TheData):
    if AQueue.TailPointer > 99:
        return -1
    else:
        if AQueue.HeadPointer == -1:
            AQueue.HeadPointer += 1
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.TailPointer += 1
        return 1

def ReturnAllData():
    returnString = ""
    for j in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        returnString += str(TheQueue.QueueArray[j]) + " "
    return returnString

def Dequeue():
    if TheQueue.HeadPointer == TheQueue.TailPointer:
        return -1
    else:
        TheQueue.HeadPointer += 1
        return TheQueue.QueueArray[TheQueue.HeadPointer-1]


# main program
TheQueue = Queue()
TheQueue.HeadPointer = -1
TheQueue.TailPointer = 0
for i in range(100):
    TheQueue.QueueArray.append(-1)

for j in range(10):
    num = int(input("Please enter an integer greater than zero: "))
    while num < 0:
        num = int(input("Please enter an integer greater than zero: "))
    temp = Enqueue(TheQueue, num)
    if temp == -1:
        print("Queue is empty")
    else:
        print("Integer is stored")
print(ReturnAllData())

print(Dequeue())
print(Dequeue())
print(ReturnAllData())