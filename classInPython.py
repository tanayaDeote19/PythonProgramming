class Person:
    def __init__(self,name,id,age):
        print("Constructor is being called")
        self.name=name
        self.id=id
        self.age=age

    def details(self):
        print(f"Hey.\nI am {self.name}.My id no. is {self.id} and I am {self.age} yrs old\n")



MG=Person("Maitreya",1,20)
MG.details()
TD=Person("tanaya",2,20)
TD.details()