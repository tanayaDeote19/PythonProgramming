
#dir
x=[1,2,34,5]
print(dir(x))

print(x.__class__)

#__dict__
class Person:
    def __init__(self,name,id,age):
        print("Constructor is being called")
        self.name=name
        self.id=id
        self.age=age


TD=Person("tanaya",2,20)
print(TD.__dict__)


#help()

print(help(Person))


