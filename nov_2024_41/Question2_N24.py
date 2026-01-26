class Horse:
    def __init__(self, nameP, MaxHeightP, SuccessP):
        self.__Name = nameP # Name as STRING
        self.__MaxFenceHeight = MaxHeightP # MaxFenceHeight as INTEGER
        self.__PercentageSuccess = SuccessP # PercentageSuccess as INTEGER
    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    def Success(self, heightP, riskP):
        if heightP > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.20
        else:
            if riskP == 1:
                return self.__PercentageSuccess
            elif riskP == 2:
                return self.__PercentageSuccess * 0.9
            elif riskP == 3:
                return self.__PercentageSuccess * 0.8
            elif riskP == 4:
                return self.__PercentageSuccess * 0.7
            else:
                return self.__PercentageSuccess * 0.6

class Fence:
    def __init__(self, heightP, riskP):
        self.__Height = heightP # Height as INTEGER
        self.__Risk = riskP # Risk as INTEGER
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk


# main program
Horses = [] # Array of type Horse
horse1 = Horse("Beauty", 150, 72)
horse2 = Horse("Jet", 160, 65)
Horses.append(horse1)
Horses.append(horse2)
print(Horses[0].GetName())
print(Horses[1].GetName())

Course = [] # Array of type Fence
for i in range(4):
    height = int(input("Please enter the height of the fence: "))
    while height < 70 or height > 180:
        height = int(input("Please enter valid height value: "))
    risk = int(input("Please enter the risk of the fence: "))
    while risk < 1 or risk > 5:
        risk = int(input("Please enter the valid risk value: "))
    Course.append(Fence(height, risk))

