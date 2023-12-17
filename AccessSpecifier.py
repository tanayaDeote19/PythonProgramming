class Employee:
    def __init__(self, name):
        self.__name = name   #Private Variable


    def __showName(self):      #Private Method
        print(f"Name: {self.__name}")


class Employee2:
    def __init__(self, name):
        self._name = name

    def _showName(self):
        print(f"Name: {self._name}")

a=Employee("Tanaya")
(a._Employee__showName())

b = Employee2("Alice")
b._showName()
