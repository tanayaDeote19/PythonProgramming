class Animal:
    def setName(self,name,species):
        self.name=name
        self.species=species

    def getName(self):
        print(f"{self.name}: {self.species}")


dog=Animal()
dog.setName("Tom","Dog")
dog.getName()










