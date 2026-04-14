class BoardObject:
    def __init__(self, codeP, valueP):
        self.__Code = codeP # Code as String
        self.__Value = valueP # Value as Integer
    def GetCode(self):
        return self.__Code
    def GetValue(self):
        return self.__Value

class Board:
    def __init__(self):
        self.__TheBoard = [[BoardObject("-", 0) for i in range(10)] for j in range(10)]
    def GetObject(self, row, column):
        return self.__TheBoard[row][column]
    def SetObject(self, BoardObject, row, column):
        self.__TheBoard[row][column] = BoardObject
    def DisplayBoard(self):
        for i in range(10):
            line = ""
            for j in range(10):
                line += self.__TheBoard[i][j].GetCode() + " "
            print(line)
        


# main program
Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)
Board1 = Board()
Board1.SetObject(Object1, 0, 0)
Board1.SetObject(Object2, 9, 9)
Board1.SetObject(Object3, 4, 5)
Board1.SetObject(Object4, 2, 2)
Board1.SetObject(Object5, 8, 7)
Board1.DisplayBoard()

row = int(input("Please enter the row position: "))
while row<0 or row>9:
    row = int(input("Please re-enter the row position: "))
column = int(input("Please enter the column position: "))
while column<0 or column>9:
    column = int(input("Please re-enter the column position: "))

if Board1.GetObject(row, column) == BoardObject("-", 0):
    print("Miss")
else:
    print("Code: ", Board1.GetObject(row, column).GetCode(), "Value: ", Board1.GetObject(row, column).GetValue())
