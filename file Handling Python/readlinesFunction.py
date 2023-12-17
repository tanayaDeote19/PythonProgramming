f=open('file3.txt',"r")
while True:
    line=f.readline()
    print(line)
    if not line:
        break