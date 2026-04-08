import random

Stack = [None for i in range(30)] # array of INTEGER
TopOfStack = -1 # global

def Push(par):
    global TopOfStack, Stack
    if TopOfStack >= 29:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = par
        return True

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return -999
    else:
        temp = TopOfStack
        TopOfStack -= 1
        return Stack[temp]

def FindValues():
    global Stack, TopOfStack
    largest = Pop()
    smallest = largest
    returnValue = smallest
    while returnValue != -999:
         if returnValue > largest:
             largest = returnValue
         if returnValue < smallest:
             smallest = returnValue
         returnValue = Pop()
    print("The largest number is ", largest)
    print("The smallest number is ", smallest)

# main program
for i in range(40):
    x = random.randint(0,1000)
    status = Push(x)
    if not status:
        print("Stack full")
        break
FindValues()