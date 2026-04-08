class Bird:
    def __init__(self, distanceP, speciesP):
        self.__DistancePerHour = distanceP # DistancePerHour as Real
        self.__Species = speciesP # Species as String
        self.__XPosition = 500.0 # XPosition as Real
        self.__YPosition = 500.0 # YPosition as Real

    def GetSpecies(self):
        return self.__Species
    def GetPosition(self):
        output = "X = " + str(self.__XPosition) + " " + "Y = " + str(self.__YPosition)
        return output
    def Move(self, directionP, minutesP):
        distanceTravelled = self.__DistancePerHour / 60 * minutesP
        if directionP == "N":
            self.__YPosition += distanceTravelled
        elif directionP == "S":
            self.__YPosition -= distanceTravelled
        elif directionP == "E":
            self.__XPosition += distanceTravelled
        else:
            self.__XPosition -= distanceTravelled


# main program
bird1 = Bird(71.0, "Cockatiel")
bird2 = Bird(56.0, "Macaw")
print(f"{bird1.GetSpecies()}: {bird1.GetPosition()}")
print(f"{bird2.GetSpecies()}: {bird2.GetPosition()}")
choice = input("Which one would you choose: Cockatiel or Macaw? ")
while choice != "Cockatiel" and choice != "Macaw":
    choice = input("Which one would you choose: Cockatiel or Macaw? ")
direction = input("Which direction would you choose? ")
while direction != "N" and direction != "S" and direction != "E" and direction != "W":
    direction = input("Which direction would you choose? ")
time = int(input("Please enter the time, in minutes "))
while time <= 0 or type(time) != int :
    time = input("Please enter the time, in minutes ")
if choice == "Cockatiel":
    bird1.Move(direction, time)
    print(f" Updated: {bird1.GetSpecies()}: {bird1.GetPosition()}")
else:
    bird2.Move(direction, time)
    print(f" Updated: {bird2.GetSpecies()}: {bird2.GetPosition()}")