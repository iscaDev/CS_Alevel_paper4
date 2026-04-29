class Horse:
    def __init__(self, nameP, heightP, successP):
        self.__Name = nameP # Name as String
        self.__MaxFenceHeight = heightP # MaxFenceHeight as Integer
        self.__PercentageSuccess = successP # PercentageSuccess as Integer

    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, heightF, riskF):
        PercentageChance = 0
        if heightF > self.__MaxFenceHeight:
            PercentageChance = 0.20*self.__PercentageSuccess
        else:
            if riskF == 1:
                PercentageChance = self.__PercentageSuccess
            elif riskF == 2:
                PercentageChance = 0.9*self.__PercentageSuccess
            elif riskF == 3:
                PercentageChance = 0.8*self.__PercentageSuccess
            elif riskF == 4:
                PercentageChance = 0.7*self.__PercentageSuccess
            else:
                PercentageChance = 0.6*self.__PercentageSuccess
        return PercentageChance

class Fence:
    def __init__(self, heightP, riskP):
        self.__Height = heightP # Height as Integer
        self.__Risk = riskP # Risk as Integer

    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk


# main program
Horses = []
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))
print(Horses[0].GetName())
print(Horses[1].GetName())

Course = []
for i in range(4):
    height = int(input(f"Pleas enter the height of the fence {i+1}: "))
    while height <70 or height>180:
        height = input(f"Pleas enter the height of the fence {i+1}: ")
    risk = int(input(f"Pleas enter the risk of the fence {i+1}: "))
    while risk<1 or risk>5:
        risk1 = int(input(f"Pleas enter the risk of the fence {i+1}: "))
    Course.append(Fence(height, risk))

for j in range(4):
    horse1 = f"The horse {Horses[0].GetName()} at fence {j+1} has a {Horses[0].Success(Course[j].GetHeight(), Course[j].GetRisk())} % chance of success"
    print(horse1)
for k in range(4):
    horse2 = f"The horse {Horses[1].GetName()} at fence {k+1} has a {Horses[1].Success(Course[k].GetHeight(), Course[k].GetRisk())} % chance of success"
    print(horse2)

total1 = 0
for _ in range(4):
    total1 += (Horses[0].Success(Course[_].GetHeight(), Course[_].GetRisk()))
average1 = total1/4
print(f"The horse {Horses[0].GetName()} has an average {average1} chance of jumping over all four fences")
total2 = 0
for l in range(4):
    total2 += (Horses[1].Success(Course[l].GetHeight(), Course[l].GetRisk()))
average2 = total2/4
print(f"The horse {Horses[1].GetName()} has an average {average2} chance of jumping over all four fences")
if average1>average2:
    print(f"The {Horses[0].GetName()} has the highest average chance of success")
else:
    print(f"The {Horses[1].GetName()} has the highest average chance of success")