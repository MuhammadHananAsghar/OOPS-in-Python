class Person:
    def __init__(self, name):
        self._name = name

    def skinCharacs(self, color, age):
        print(f"{self._name} has {color} and of {age}.")

    def jobDetails(self, salary, job):
        print(f"{self._name} is doing {job} for {salary}Rs salary.")


class Student(Person):
    def __init__(self, name):
        super().__init__(name)


st1 = Student("Muhammad Hanan")
st1.skinCharacs("Brown", 22)
st1.jobDetails(10000000, "CEO")