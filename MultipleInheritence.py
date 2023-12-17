class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name="", species="", breed=""):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print("Meow...")


d = Dog("Dog", "Doggerman")
d.make_sound()
print(d.species)

a = Animal("Mouse", "german")
a.make_sound()
print(a.species)
c = Cat("")
c.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
