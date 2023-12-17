def function():
    try:
        a = [1, 2, 3, 4, 5, 6]
        x = int(input("Enter index"))
        print(a[x])
        return 1
    except:
        print("Some Error has Occured")
        return 0

    finally:
        print("Finally")

x=function()
print(x)