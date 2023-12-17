x = int(input("Enter 1st value"))
y = int(input("Enter 2nd value"))

choice = int(input("Enter your choice: 1.add 2.Sub 3.Mul 4.Div 5.Modulus"))

if choice == 1:
  print("Addition:", x + y)

if choice == 2:
  print("Sub:", x - y)

if choice == 3:
  print("Multiplication:", x * y)

if choice == 4:
  print("Division:", x / y)

if choice == 5:
  print("Modulus:", x % y)