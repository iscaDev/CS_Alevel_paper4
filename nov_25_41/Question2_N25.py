class Train:
    def __init__(self, idP, routeP):
        self.__TrainIDNumber = idP # TrainIDNumber as String
        self.__Route = routeP # Route as INTEGER

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber
    def GetRoute(self):
        return self.__Route

class Station:
    def __init__(self, idP, platformsP):
        self.__StationID = idP # StationID as STRING
        self.__NumberPlatforms = platformsP # NumberPlatforms as INTEGER
        self.__Trains = [] # array of TRAIN
        self.__NumberTrains = 0 # NumberTrains as INTEGER

    def AddTrain(self, Train):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        else:
            self.__Trains.append(Train)
            self.__NumberTrains += 1
            return True

    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"
        else:
            output = "The trains at station " + self.__StationID + " are: \n"
            for i in range(len(self.__Trains)):
                add = self.__Trains[i].GetTrainIDNumber() + " on route number" + str(self.__Trains[i].GetRoute()) + "\n"
                output += add
            return output


train1 = Train("12ADV", 134)
train2 = Train("33ART", 20)
train3 = Train("9FKF", 3)
train4 = Train("21VBC", 24)
station1 = Station("STH", 2)
station2 = Station("NTH", 1)
a = station1.AddTrain(train1)
if not a:
    print("Station is full")
b = station1.AddTrain(train2)
if not b:
    print("Station is full")
c = station1.AddTrain(train3)
if not c:
    print("Station is full")
d = station2.AddTrain(train4)
if not d:
    print("Station is full")
print(station1.GetTrains())
print(station2.GetTrains())