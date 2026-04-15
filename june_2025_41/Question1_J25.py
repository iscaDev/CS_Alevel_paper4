Queue = [-1 for i in range(20)] # global
HeadPointer = -1 # global
TailPointer = -1 # global
NumberItems = 0 # global

def Enqueue(par):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems >=20:
        return False
    else:
        if HeadPointer == -1:
            HeadPointer += 1
            TailPointer += 1
            Queue[TailPointer] = par
        else:
            TailPointer += 1
            if TailPointer == 20:
                TailPointer == 0
            Queue[TailPointer] = par
        NumberItems += 1
        return True

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -1
    else:
        temp = HeadPointer
        HeadPointer += 1
        NumberItems -= 1
        if HeadPointer == 20:
            HeadPointer = 0
        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1
        return Queue[HeadPointer]


# main program
for j in range(25):
    status = Enqueue(j+1)
    if status:
        print(j+1, "Successful")
    else:
        print(j+1, "Unsuccessful")

print(Dequeue())
print(Dequeue())