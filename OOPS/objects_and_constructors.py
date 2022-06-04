class Employee:
    def __init__(self, name, salary): #Constructor
        self.name = name
        self.salary = salary
    
    def printInfo(self):
        print(f"{self.name} has {self.salary} salary.")


# Objects
employee1 = Employee("Hanan", 10000000)
employee2 = Employee("Amir", 1000000)
employee1.printInfo()
employee2.printInfo()