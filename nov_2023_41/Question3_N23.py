class Character:
    def __init__(self, nameP, xP, yP):
        self.__Name = nameP # Name as STRING
        self.__XPosition = xP # XPosition as INTEGER
        self.__YPosition = yP # YPosition as INTEGER
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition
    def SetXPosition(self, x):
        self.__XPosition = self.__XPosition + x
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        if self.__XPosition < 0:
            self.__XPosition = 0
    def SetYPosition(self, y):
        self.__YPosition = self.__YPosition + y
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        if self.__YPosition < 0:
            self.__YPosition = 0
    def Move(self, directP):
        if directP == "up":
            self.SetYPosition(10)
        elif directP == "down":
            self.SetYPosition(-10)
        elif directP == "left":
            self.SetXPosition(-10)
        else:
            self.SetXPosition(10)

class BikeCharacter(Character):
    def __init__(self, nameP, xP, yP):
        super().__init__(nameP, xP, yP)
    def Move(self, directP):
        if directP == "up":
            self.SetYPosition(20)
        elif directP == "down":
            self.SetYPosition(-20)
        elif directP == "left":
            self.SetXPosition(-20)
        else:
            self.SetXPosition(20)


# main program
Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)
characterV = input("Which character: Jack or Karla?")
direct = input("Which direction: up, down, left, or right?")
if characterV == "Jack" or characterV == "jack":
    Jack.Move(direct)
    print(f"Jack's new position is X={Jack.GetXPosition()} Y={Jack.GetYPosition()}")
elif characterV == "Karla" or characterV == "karla" :
    Karla.Move(direct)
    print(f"Karla's new position is X={Karla.GetXPosition()} Y={Karla.GetYPosition()}")
else:
    print("Invalid input")