import os, shutil, re

if not(os.path.exists("./Finder")):
    os.mkdir("./Finder")

worldArray = []
nameArray = []

with open(f"./Finder/world.txt", 'r') as World:
    with open(f"./Finder/names.txt", 'r') as Find:
        for lineWorld in World:
            worldArray.append(lineWorld.lower())
        for lineFind in Find:
            nameArray.append(lineFind.lower())

i = 1
buff = None

for object in worldArray:
    for word in nameArray:
        for split in object.split("/"):
            if split == word:
                print(f"{split} | {word}")
            else:
                i+=1