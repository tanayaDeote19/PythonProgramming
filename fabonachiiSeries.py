def fabonachii(n):
    a, b = 0, 1
    print(a, b, end=" ")
    i = 0
    while i < n:
        sum = a + b
        print(sum, end=" ")
        a = b
        b = sum
        i = i + 1


n=int(input("Enter a number"))
fabonachii(n)