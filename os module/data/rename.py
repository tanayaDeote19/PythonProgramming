import os

if (not os.path.exists("data")):
    os.mkdir("data")


for i in range (1,100):
    os.rename(f"data/Day{i+1}",f"data/Have fun{i+1}")