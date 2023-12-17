with open("sample.txt","w") as f:
    f.write("Hey! How You Doing")
    f.truncate(4)


with open("sample.txt","r") as f:
    print(f.read())
    