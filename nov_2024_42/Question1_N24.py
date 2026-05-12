class EventItem:
    def __init__(self, nameP, typeP, difficultyP):
        self.__EventName = nameP # EventName as String
        self.__Type = typeP # Type as String
        self.__Difficulty = difficultyP # Difficulty as Integer

    def GetName(self):
        return self.__EventName
    def GetEventType(self):
        return self.__Type
    def GetDifficulty(self):
        return self.__Difficulty

class Character:
    def __init__(self, nameP, jumpP, swimP, runP, driveP):
        self.__CharacterName = nameP # CharacterName as String
        self.__Jump = jumpP # Jump as Integer
        self.__Swim = swimP # Swim as Integer
        self.__Run = runP # Run as Integer
        self.__Drive = driveP # Drive as Integer

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, typeP, difficultyP):
        chance = 0
        if typeP == "Jump":
            chance = self.__Jump
        elif typeP == "Swim":
            chance = self.__Swim
        elif typeP == "Run":
            chance = self.__Run
        else:
            chance = self.__Drive
        if chance >= difficultyP:
            return 100
        else:
            diff = difficultyP - chance
            if diff == 1:
                return 80
            elif diff == 2:
                return 60
            elif diff == 3:
                return 40
            elif diff == 4:
                return 20
            else:
                return 0



# main code
Group = [] # array of type EventItem
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

tarz_score = 0
geni_score = 0
for item in Group:
    tarz = Tarz.CalculateScore(item.GetEventType(), item.GetDifficulty())
    geni = Geni.CalculateScore(item.GetEventType(), item.GetDifficulty())
    if tarz > geni:
        print("Tarz won the event: ", item.GetName())
        tarz_score += 1
    elif geni > tarz:
        print("Geni won the event: ", item.GetName())
        geni_score += 1
    else:
        print("The event ", item.GetName(), " is draw.")

if tarz_score > geni_score:
    print("Tarz won the group with points: ", tarz_score)
elif geni_score > tarz_score:
    print("Geni won the group with points: ", geni_score)
else:
    print("The group is draw")