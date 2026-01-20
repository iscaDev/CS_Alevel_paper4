# globals


# class def
class Vehicle:

    def __init__(self, id, maximumS, AmountIncrease):
        self.__ID = id # ID as STRING
        self.__MaxSpeed = maximumS # MaxSpeed as INTEGER
        self.__CurrentSpeed = 0 # CurrentSpeed initialised to 0
        self.__IncreaseAmount = AmountIncrease # IncreaseAmount as INTEGER
        self.__HorizontalPosition = 0 # HorizontalPosition initialised to 0


    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP
    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, id, maximumS, AmountIncrease, Vchange, MaximumH):
        super().__init__(self, id, maximumS, AmountIncrease)
        self.__VerticalChange = Vchange # VerticalChange as INTEGER
        self.__MaxHeight = MaximumH # MaxHeight as INTEGER
        self.__VerticalPosition = 0 # VerticalPosition as INTEGER
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        if self.GetCurrentSpeed() > self.GetMaxSpeed():
            self.SetCurrentSpeed(self.GetMaxSpeed())
        self.SetCurrentSpeed(self.GetCurrentSpeed() + self.GetIncreaseAmount())
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())


# functions and procs
def OutputCurrentPosition():
    


# main program
