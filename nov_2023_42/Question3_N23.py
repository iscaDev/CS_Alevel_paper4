from datetime import datetime

class Character:
    def __init__(self, name, birth, intelligenceP, speedP):
        self.__CharacterName = name # CharacterName as STRING
        self.__DateOfBirth = birth # DateOfBirth as DATE
        self.__Intelligence = intelligenceP # Intelligence as REAL
        self.__Speed = speedP # Speed as INTEGER
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    def SetIntelligence(self, intelligence):
        self.__Intelligence = intelligence
    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1
    def ReturnAge(self):
        age = 2023 - self.__DateOfBirth.year
        return age


class MagicCharacter(Character):
    def __init__(self, name, birth, intelligenceP, speedP, elementP):
        super().__init__(name, birth, intelligenceP, speedP)
        self.__Element = elementP
    def Learn(self):
        if self.__Element == "fire" or self.__Element.lower() == "water":
            self.SetIntelligence(self.GetIntelligence()*1.2)
        elif self.__Element == "earth":
            self.SetIntelligence(self.GetIntelligence()*1.3)
        else:
            self.SetIntelligence(self.GetIntelligence()*1.1)


# main program
dateOfbirth1=datetime(2019, 1, 1)
FirstCharacter = Character("Royal", dateOfbirth1, 70, 30 )
FirstCharacter.Learn()
print(f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")
dateOfbirth2=datetime(2018, 3, 3)
FirstMagic = MagicCharacter("Light", dateOfbirth2, 75, 22, "fire" )
FirstMagic.Learn()
print(f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")