HashTable = [] # global
Spare = [] # global
PointerOfSpare = 0

class NewRecord:
    def __init__(self, keyP, item1P, item2P):
        self.Key = keyP # Key as Integer
        self.Item1 = item1P # Item1 as Integer
        self.Item2 = item2P # Item2 as Integer

def Initialise():
    global HashTable, Spare
    for i in range(200):
        HashTable.append(NewRecord(-1, -1, -1))
    for i in range(100):
        Spare.append(NewRecord(-1, -1, -1))

def CalculateHash(keyfield):
    return keyfield % 200

def InsertIntoHash(recordP):
    global HashTable, Spare, PointerOfSpare
    hashvalue = CalculateHash(recordP.Key)
    if HashTable[hashvalue] == NewRecord(-1, -1, -1):
        HashTable[hashvalue] = recordP
    else:
        Spare[PointerOfSpare] = recordP
        PointerOfSpare += 1

def CreateHashTable():
    global HashTable, Spare, PointerOfSpare
    try:
        f = open("HashData.txt","r")
        for line in f:
            items = line.split(",")
            key = int(items[0])
            item1 = int(items[1])
            item2 = int(items[2])
            InsertIntoHash(NewRecord(key, item1, item2))
        f.close()
    except FileNotFoundError:
        print("File not found")

def PrintSpare():
    for i in range(PointerOfSpare+1):
        print(Spare[i].Key)

Initialise()
CreateHashTable()
PrintSpare()