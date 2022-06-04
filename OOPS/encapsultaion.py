class Employee:
    def __init__(self, name, salary):
        # Public: Access Inside and Outside the Class
        self.name = name
        # Private: Access Only Inside Class
        self.__salary = salary
        # Protected: Access in Base Class and Inside Class
        self._salary = salary

    def showSalary(self):
        return self._salary

employee = Employee("Hanan", 1000000)
print(employee.name)
print(employee.showSalary())