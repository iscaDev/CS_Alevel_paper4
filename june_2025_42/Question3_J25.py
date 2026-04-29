class Animal:
    def __init__(self, nameP, soundP, sizP, intlP):
        self.Name = nameP # Name as String
        self.Sound = soundP # Sound as String
        self.Size = sizP # Size as Integer
        self.Intelligence = intlP # Intelligence as Integer

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}"

class Parrot(Animal):
    def __init__(self, nameP, soundP, sizP, intlP, wingP, wordsP):
        Animal.__init__(self, nameP, soundP, sizP, intlP)
        self.__WingSpan = wingP # WingSpan as Integer
        self.__NumberWords = wordsP # NumberWords as Integer

    def ChangeNumberWords(self, par):
        self.__NumberWords += par

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}. It has a wingspan of {self.__WingSpan}cm and can say {self.__NumberWords} words."

class Wolf(Animal):
    def __init__(self, nameP, soundP, sizP, intlP, territoryP):
        Animal.__init__(self, nameP, soundP, sizP, intlP)
        self.__TerritorySize = territoryP # TerritorySize as Integer

    def SetTerritorySize(self, par):
        self.__TerritorySize += par

    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}. Its territory size is {self.__TerritorySize} square miles."


# main program
parrot = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
wolf = Wolf("Nighteyes", "Howl", 8, 7, 100)
horse = Animal("Copper", "Neigh", 10, 6)

wolf.SetTerritorySize(-20)
parrot.ChangeNumberWords(2)
print(parrot.Description())
print(wolf.Description())
print(horse.Description())