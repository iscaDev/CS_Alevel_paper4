def ReadData():
    filename = input("Please enter the file name: ")
    try:
        f = open(filename, "r")
        arr = []
        for line in f:
            arr.append(line)
        f.close()
        return arr
    except FileNotFoundError:
        print("File not found")

def SplitData(DataArray):
    red = []
    green = []
    blue = []
    orange = []
    yellow = []
    pink = []
    for i in range(len(DataArray)):
        arr = DataArray[i].split(",")
        num = int(arr[0])
        color = arr[1].strip()
        if color == "red":
            red.append(num)
        elif color == "green":
            green.append(num)
        elif color == "blue":
            blue.append(num)
        elif color == "orange":
            orange.append(num)
        elif color == "yellow":
            yellow.append(num)
        else:
            pink.append(num)

    StoreData(red, "Red.txt")
    StoreData(green, "Green.txt")
    StoreData(blue, "Blue.txt")
    StoreData(orange, "Orange.txt")
    StoreData(yellow, "Yellow.txt")
    StoreData(pink, "Pink.txt")

def StoreData(DataToStore, fname):
    try:
        f = open(fname, "w")
        for each in DataToStore:
            f.write(str(each))
            f.write("\n")
        f.close()
    except FileNotFoundError:
        print("File not found")


SplitData(ReadData())