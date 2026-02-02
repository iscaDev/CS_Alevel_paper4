Stack = ["-1" for i in range(20)] # Array of STRING
TopOfStack = -1 # global

def Push(par):
    global TopOfStack, Stack
    if TopOfStack >= 19:
        print(-1)
    else:
        Stack[TopOfStack+1] = par
        TopOfStack += 1
        return 1

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        print("-1")
    else:
        temp = TopOfStack
        TopOfStack -= 1
        return Stack[temp]

def ReadData(FileName):
    try:
        f = open(FileName, "r")
        for line in f:
            if Push(line.strip()) == -1:
                print("Stack full")
        f.close()
    except FileNotFoundError:
        print("File not found")

def Calculate():
    global Stack, TopOfStack
    total = int(Stack[0])
    for j in range(len(Stack)-2):
        if Stack[j+1] == "+":
            total += int(Stack[j+2])
        elif Stack[j+1] == "-":
            total -= int(Stack[j+2])
        elif Stack[j+1] == "/":
            total /= int(Stack[j+2])
        elif Stack[j+1] == "*":
            total *= int(Stack[j+2])
        else:
            total = total ** int(Stack[j+2])
    return total

# main program
file = input("Enter file name: ")
ReadData(file)
print(Calculate())