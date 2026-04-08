TreeArray = [] # global
for i in range(50):
    TreeArray.append([-1, -1, -1]) # this array represents each node
RootPointer = -1
FreeNode = 0

def AddNode(par):
    global FreeNode, RootPointer, TreeArray
    if FreeNode <= 49:
        TreeArray[FreeNode][0] = -1
        TreeArray[FreeNode][1] = par
        TreeArray[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            placed = False
            CurrentNode = RootPointer
            while not placed:
                if par < TreeArray[CurrentNode][1]: # goes left
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0] = FreeNode
                        placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][0]
                else: # goes right (equal or higher)
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2] = FreeNode
                        placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")

def WriteAllToFile():
    global TreeArray
    try:
        f = open("Tree.txt", "w")
        for each in TreeArray:
            line = ""
            line += str(each[0]) + "," + str(each[1]) + "," + str(each[2]) + "\n"
            f.write(line)
        f.close()
    except FileNotFoundError:
        print("File not found")

# main program
try:
    f = open("TreeData.txt", "r")
    for line in f:
        AddNode(int(line))
    f.close()
except FileNotFoundError:
    print("File not found")

WriteAllToFile()