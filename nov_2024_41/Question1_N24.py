def ReadData():
    arr = [] # local
    try:
        f = open("Data.txt", "r")
        for line in f:
            arr.append(line.strip())
        f.close()
        return arr
    except FileNotFoundError:
        print("File not found")

def FormatArray(arrP):
    returnString = ""
    for item in arrP:
        returnString += item + " "
    return returnString

def CompareStrings(str1, str2):
    i = 0
    current1 = str1[i]
    current2 = str2[i]
    while current1 == current2:
        i += 1
        current1 = str1[i]
        current2 = str2[i]
    if current1 > current2:
        return 2
    else:
        return 1

def Bubble(arrP):
    for i in range(0, len(arrP)-1):
        for j in range(0, len(arrP)-i-1):
            status = CompareStrings(arrP[j], arrP[j+1])
            if status == 2:
                temp = arrP[j]
                arrP[j] = arrP[j+1]
                arrP[j+1] = temp
    return arrP

# main program
print(FormatArray(ReadData()))
print(FormatArray(Bubble(ReadData())))