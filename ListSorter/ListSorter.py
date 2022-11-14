#!/usr/bin/python
import sys, os, shutil

def Error():
    print("Invalid Args")
    print("""
    Argv X)  VRCPlayer | _Application | UserInterface | PlayerManager
    Argv 1)  VRCPlayer | _Application
    """)
    input("Press Enter To Continue...")
    exit()

def Linechecker(line):
    if "VRCPlayer" in line or "_Application" in line or "UserInterface" in line or "PlayerManager" in line:
        return True
    return False

def Linechecker2(line):
    if "VRCPlayer" in line or "_Application" in line:
        return True
    return False

def CreateFolders():
    if not(os.path.exists("./Input")):
        os.mkdir("./Input")
    if not(os.path.exists("./Output")):
        os.mkdir("./Output")
    if not(os.path.exists("./Worlds")):
        os.mkdir("./Worlds")

def SortList(file, checkS):
    duplicated = ""
    dCount = 0
    print(f"Sorting {file}")
    if(file.endswith(".txt")):
        with open(f"./Input/{file}", 'r') as o:
            with open(f'./Output/{file[:-4]}.txt', 'w') as s:
                for line in sorted(o):
                    if not line in duplicated:
                        if checkS == False and not Linechecker(line):
                            duplicated = line
                            s.write(line)
                        if checkS == True and not Linechecker2(line):
                            duplicated = line
                            s.write(line)
                    else:
                        dCount+=1
    print(f"Duplicate Text - {dCount}")

def FileSort(file):
    print(f"Moving {file}")
    if "GameObjectList" in file:
        name = file.split("GameObjectList")[0][:-3]
        if not(os.path.exists(f"./Worlds/{name}")): os.mkdir(f"./Worlds/{name}")
        shutil.move(f"./Output/{file}", f"./Worlds/{name}")
    if "UdonKeyList" in file:
        name = file.split("UdonKeyList")[0][:-3]
        if not(os.path.exists(f"./Worlds/{name}")): os.mkdir(f"./Worlds/{name}")
        shutil.move(f"./Output/{file}", f"./Worlds/{name}")

if __name__ == "__main__":
    buff = None
    try:
        if(len(sys.argv) > 2):
            Error()
        if(len(sys.argv) == 2):
            buff = bool(sys.argv[1])
    except:
        Error()

    CreateFolders()
    for file in os.listdir("./Input"):
        if(buff != None):
            SortList(file, True)
        if(buff == None):
            SortList(file, False)
        os.remove(f"./Input/{file}")
    for file in os.listdir("./Output"):
        FileSort(file)