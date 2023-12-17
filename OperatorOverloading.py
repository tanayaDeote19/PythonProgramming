class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i+{self.j}+{self.k}K"

    def __add__(self, other):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
x=Vector(1,2,3)
a=Vector(1,2,3)
print(a.__str__())
print(a.__add__(x))

