i=0
f=open('file1.txt',"r")
while True:
    line=f.readline()
    i=i+1
    print(line)
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print(f"Marks in string is {m1}")
    print(f"Marks in string is {m2}")
    print(f"Marks in string is {m3}\n")

