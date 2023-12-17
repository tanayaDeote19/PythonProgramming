double=lambda  x:x*x

cube=lambda  x:x*x*x

print(double(5))
print(cube(5))

#multiple arguement can be passed
avg= lambda x,y,z: (x+y+z)/3
print(avg(3,4,2))


def function(fx,value):
    print(6+fx(3))

#lambda function can also be passed as parameter
function(cube,5)
#OR
function(lambda  x:x*x*x,5)


