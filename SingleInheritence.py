class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    print("Animal makes sound.")


class Cat(Animal):

  def __init__(self, name, species):
    super().__init__(name, species)

  def make_sound(self):
    print("Meow Meow.")
    # return super().make_sound()


my_animal = Animal("Cat", "Pet")
my_animal.make_sound()

my_cat = Cat("Tom", "Pet")
my_cat.make_sound()
