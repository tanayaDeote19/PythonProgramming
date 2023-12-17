#They are used to work with file objects and their positions with file
with open("file.txt","r") as f:

    #seek() change the location of pointer
    f.seek(3)

    #tell() gives the position upto which the location is seeked
    print(f.tell())

    data=f.read(3)
    print(data)
