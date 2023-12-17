class Animal:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species


class Dog(Animal):
    def showDetails(self):
        print(f"Name:{self.name}\nColor:{self.color}\nSpecies:{self.species}")


dog=Dog("John","Black","Dog")
dog.showDetails()




