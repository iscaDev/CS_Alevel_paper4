class Animal:
    def __init__(self, nameP, soundP, sizeP, intelligenceP):
        self.__Name = nameP # Name as STRING
        self.__Sound = soundP # Sound as STRING
        self.__Size = sizeP # Size as INTEGER
        self.__Intelligence = intelligenceP # Intelligence as INTEGER
    def Description(self):
        description = f"The animal's name is {self.__Name}, it makes a {self.__Sound}, its size is {self.__Size}, and its intelligence level is {self.__Intelligence}"
        return description

class Parrot(Animal):
    def __init__(self, nameP, soundP, sizeP, intelligenceP, wingP, wordsP):
        super().__init__(nameP, soundP, sizeP, intelligenceP)
        self.__WingSpan = wingP # WingSpan as INTEGER
        self.__NumberWords = wordsP # NumberWords as INTEGER
    def ChangeNumberWords(self, num):
        self.__NumberWords = self.__NumberWords + num
    def Description(self):
        description = f"The animal's name is {self.__Name}, it makes a {self.__Sound}, its size is {self.__Size}, and its intelligence level is {self.__Intelligence}. It has a wingspan of {self.__WingSpan}cm and can say {self.__NumberWords} words."
        return description

class Wolf(Animal):
    def __init__(self, nameP, soundP, sizeP, intelligenceP, territoryP):
        super().__init__(nameP, soundP, sizeP, intelligenceP)
        self.__TerritorySize = territoryP # TerritorySize as INTEGER
    def SetTerritorySize(self, size):
        self.__TerritorySize = self.__TerritorySize + size
    def Description(self):
        description = f"The animal's name is {self.__Name}, it makes a {self.__Sound}, its size is {self.__Size}, and its intelligence level is {self.__Intelligence}. Its territory is {self.__TerritorySize} square miles."
        return description

# main program
parrot = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
wolf = Wolf("Nighteyes", "Howl", 8, 7, 100)
horse = Animal("Copper", "Neigh", 10, 6)
wolf.SetTerritorySize(-20)
parrot.ChangeNumberWords(2)
print(parrot.Description())
print(wolf.Description())
print(horse.Description())