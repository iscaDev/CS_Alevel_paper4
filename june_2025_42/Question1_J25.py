Stack = ["-1" for i in range(20)] # global
TopOfStack = -1 # global

def Push(par):
    global TopOfStack, Stack
    if TopOfStack >= 19:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = par
        return 1

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return "-1"
    else:
        temp = Stack[TopOfStack]
        TopOfStack -= 1
        return temp

def ReadData(fnameP):
    global Stack, TopOfStack
    try:
        f = open(fnameP, "r")
        for line in f:
            status = Push(line.strip())
            if status == -1:
                print("Stack full")
        f.close()
    except FileNotFoundError:
        print("File not found")

def Calculate():
    global Stack, TopOfStack
    total = int(Pop())
    flag = True
    while flag:
        operator = Pop()
        number = Pop()
        if operator == "-1":
            flag = False
        else:
            if operator == "+":
                total += int(number)
            elif operator == "*":
                total *= int(number)
            elif operator == "/":
                total /= int(number)
            elif operator == "^":
                total **= int(number)
            else:
                total -= int(number)
    return total

filename = input("Enter file name: ")
ReadData(filename)
print(Calculate())