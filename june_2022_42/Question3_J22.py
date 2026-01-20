NumbersChoosen=[False for i in range(30)]


class Card:
    # Number as INTEGER
    # Colour as STRING
    def __init__(self, num, color):
        self.__Number = num
        self.__Colour = color
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour


def ChooseCard():
    flag=True
    while flag:
        CardSelected=int(input("Select a card from 1  to 30"))
        if CardSelected<1 or CardSelected>30:
            print("Number must be between 1 and 30")
        elif NumbersChoosen[CardSelected-1]:
            print("Already taken")
        else:
            print("Valid")
            flag=False


# main program

CardArray = []
for i in range(30):
    CardArray.append(Card(0, ""))
try:
    filename="CardValues.txt"
    file=open(filename,"r")
    for x in range(30):
        NumberRead=int(file.readline().strip())
        ColourRead=file.readline().strip()
        CardArray[x]=Card(NumberRead,ColourRead)
    file.close()
except IOError:
    print("File not found")