Animal = ["" for i in range(20)] # Global Array of STRING
Colour = ["" for j in range(10)] # Global Array of STRING
AnimalTopPointer = 0 # Global, INTEGER
ColourTopPointer = 0 # Global INTEGER

def PushAnimal(animalP):
    global AnimalTopPointer, Animal
    if AnimalTopPointer >= 20:
        return False
    else:
        Animal[AnimalTopPointer] = animalP
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer, Animal
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        f = open("AnimalData.txt", "r")
        name = f.readline()