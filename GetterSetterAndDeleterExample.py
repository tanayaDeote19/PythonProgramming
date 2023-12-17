class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting my name...")
        del self._name

    @name.getter
    def name(self):
        try:
            return self._name
        except AttributeError:
            return "My name has been deleted!"

    @name.setter
    def name(self, new_name):
        print("Renaming myself...")
        self._name = new_name


John = Person('John')
print(f'My name is: {John.name}')

del John.name
print(John.name)

John.name = 'Peter'
print(f'My new name is: {John.name}')