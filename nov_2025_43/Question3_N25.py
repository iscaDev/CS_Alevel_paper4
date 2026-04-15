def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements <= 0:
        return 0
    NewArray = ArrayCopy[1:]
    if ArrayCopy[0] == DataToFind:
        return 1+RecursiveCount(NewArray, NumberElements-1, DataToFind)
    else:
        return RecursiveCount(NewArray, NumberElements-1, DataToFind)

def SplitData(par):
    splitted = []
    line = ""
    for i in range(len(par)):
        if par[i] == ";":
            splitted.append(line)
            line = ""
        else:
            line += par[i]
    return splitted


# main program
arr = [0,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(arr, 10, 0))
var = "x=0;y=1;x=x+y;y++;"
splittedArray = SplitData(var)
for each in splittedArray:
    print(each)