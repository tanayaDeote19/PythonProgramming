#Reading a file
# f = open("file.txt","r")
# # x=f.read()
# # print(x)

#writing a file
# f = open("file.txt","w")
# f.write("HEY")
# f.close()


#if file does not exist,in write mode file is created
f = open("file1.txt","w")
f.write("HEY")
f.close()


#appending a file
# f = open("file.txt","a")
# f.write("HEY")
# f.close()

#Using with keyword appending a file
# with open("file.txt","a"):
#     f.write("how are you")
