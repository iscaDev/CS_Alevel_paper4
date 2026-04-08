HashTable = [] # global

class Record:
    def __init__(self, keyP, dataP):
        self.Key = keyP # Key as Integer
        self.Data = dataP # Data as String

def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(None, None) for x in range(10)] for y in range(100)]

def Hash(par):
    hashValue = par % 100
    return hashValue

def InsertData(object):
    global HashTable
    position = Hash(object.Key)
    column = 0
    while HashTable[position][column].Key != None:
        column += 1
    HashTable[position][column] = object

def ReadData():
    global HashTable
    try:
        f = open('HashTableData.txt', 'r')
        for line in f:
            items = line.strip().split(',')
            key = int(items[0])
            stringData = items[1]
            InsertData(Record(key, stringData))
        f.close()
    except FileNotFoundError:
        print('HashTableData.txt is not found')

def GetRecord(keyP):
    global HashTable
    HashValue = Hash(keyP)
    for i in range(10):
        if HashTable[HashValue][i].Key == keyP:
            return HashTable[HashValue][i].Data
    return "Not found"

# main program
InitialiseHashTable()
ReadData()
for i in range(5):
    key = int(input("Enter the key: "))
    print(GetRecord(key))