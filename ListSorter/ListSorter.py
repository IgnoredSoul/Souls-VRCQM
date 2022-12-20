import os, shutil, time

def CreateFolders():
    if not(os.path.exists("./Input")):
        os.mkdir("./Input")
    if not(os.path.exists("./Output")):
        os.mkdir("./Output")

def SortList(file):

    # Yeah
    duplicated = ""
    dCount = 0
    lCount = 0

    # Print Sorting Said File
    print(f"Sorting {file}")

    # Get Lines
    with open(file, 'r', encoding="utf-8") as f:
        global lines
        lines = sorted(f.readlines())

    # Sort And Write To File
    with open(file, 'w', encoding="utf-8") as f:
        for line in lines:
            if not line in duplicated: # Make Sure Its Not A Duplicate
                duplicated = line # Assign To Duplicate
                f.write(line) # Write
                lCount += 1 # Line Count ++
            else:
                dCount += 1 # Duplicate Count ++

def SortFile(file):

    # Print Moving Said File
    print(f'Moving {file}\n')

    if not (os.path.exists(f'./Output/{WorldName}')): os.mkdir(f'./Output/{WorldName}')
    shutil.move(f'./Input/{file}', f'./Output/{WorldName}/{FileName}')

CreateFolders()

for file in os.listdir("./Input"):
    global WorldName
    global FileName
    
    if "WorldObjectsList" in file:
        WorldName = file.split("WorldObjectsList")[0][:-3]
        FileName = file.rsplit(' ', 1)[1]
    elif "WorldUdonList" in file:
        WorldName = file.split("WorldUdonList")[0][:-3]
        FileName = file.rsplit(' ', 1)[1]
    elif "WorldObjectList" in file:
        WorldName = file.split("WorldObjectList")[0][:-3]
        FileName = file.rsplit(' ', 1)[1]
    else:
        exit()

    print(file)
    SortList(f'./Input/{file}')
    SortFile(file)