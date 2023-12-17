try:
    x=int(input("enter a no."))
    a=[1,2,3,4,5,6,7,8]
    print(a[x])

except ValueError:
    print("Entered value is not integer")

except IndexError:
    print("Enter an appropriate index")

print("Program Finished")
