import os, shutil

def checker(line):
    if "VRCPlayer" in line or "_Application" in line or "UserInterface" in line or "PlayerManager" in line:
        return True
    return False

if not(os.path.exists("./Input")):
    os.mkdir("./Input")
    input = "Created Input Folder, Press Enter To Continue..."
if not(os.path.exists("./Worlds")):
    os.mkdir("./Worlds")

# for file in os.listdir("./Input"):
#     if(file.endswith(".txt")):
#         with open(f"./Input/{file}", 'r') as o:
#             with open(f'./Output/{file[:-4]}.txt', 'w') as s:
#                 for line in sorted(o):
#                     if not checker(line):
#                         s.write(line)

for file in os.listdir("./Output"):
    if "GameObjectList" in file:
        name = file.split("GameObjectList")[0][:-3]
        if not(os.path.exists(f"./Worlds/{name}")): os.mkdir(f"./Worlds/{name}")
        shutil.move(f"./Output/{file}", f"./Worlds/{name}")
    if "UdonKeyList" in file:
        name = file.split("UdonKeyList")[0][:-3]
        if not(os.path.exists(f"./Worlds/{name}")): os.mkdir(f"./Worlds/{name}")
        shutil.move(f"./Output/{file}", f"./Worlds/{name}")

print("Finished")

