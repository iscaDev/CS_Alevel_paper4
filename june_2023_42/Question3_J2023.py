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


