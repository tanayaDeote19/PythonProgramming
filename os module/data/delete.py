import os

if (not os.path.exists("data")):
    os.mkdir("data")


for i in range (1,100):
    os.remove(f"data/Have fun{i+1}")