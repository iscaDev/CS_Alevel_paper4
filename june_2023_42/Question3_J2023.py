EmployeeArray = [] # EmployeeArray as Array of object type Employee

class Employee:
    def __init__(self, Pay, Num, Job):
        self.__HourlyPay = Pay # HourlyPay as REAL
        self.__EmployeeNumber = Num # EmployeeNumber as STRING
        self.__JobTitle = Job # JobTitle as STRING
        self.__PayYear2022 = [0.0 for i in range(52)] # PayYear2022 as Array of REAL
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self, WeekNum, NumHours):
        pay = self.__HourlyPay * NumHours
        self.__PayYear2022[WeekNum-1] = pay
    def GetTotalPay(self):
        return sum(self.__PayYear2022)

class Manager(Employee):
    def __init__(self, Pay, Num, Job, Bonus):
        super().__init__(Pay, Num, Job)
        self.__BonusValue = Bonus # BonusValue as REAL
    def SetPay(self, WeekNumV, NumHoursV):
        NumHours = NumHoursV * (1 + self.__BonusValue / 100)
        super().SetPay(WeekNumV, NumHours)

# functions and procedures
def is_bonus(temp):
    try:
        BonusA = float(temp)
        return True
    except:
        return False

def EnterHours():
    try:
        file = open("HoursWeek1.txt", "r")
        for x in range(8):
            IDV = file.readline()
            Hours = float(file.readline())
            for j in range(8):
                if EmployeeArray[j].GetEmployeeNumber() == IDV:
                    EmployeeArray[j].SetPay(1, Hours)
    except IOError:
        print("HoursWeek1.txt not found")

# main program
PayV = 0.0
ID = ""
BonusV = 0.0
Title = ""
Temp = ""

try:
    f = open("Employees.txt", "r")
    for i in range(8):
        PayV = float(f.readline().strip())
        ID = f.readline()
        Temp = f.readline()
        if is_bonus(Temp):
            BonusV = float(Temp)
            Title = f.readline()
            EmployeeArray.append(Manager(PayV, ID, Title, BonusV))
        else:
            Title = Temp
            EmployeeArray.append(Employee(PayV, ID, Title))
    f.close()
except IOError:
    print("File doesn't exist")
