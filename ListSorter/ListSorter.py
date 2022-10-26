import os

if not(os.path.exists("./Input")):
    os.mkdir("./Input")
    input = "Created Input Folder, Press Enter To Continue..."
if not(os.path.exists("./Output")):
    os.mkdir("./Output")

for file in os.listdir("./Input"):
    if(file.endswith(".txt")):
        with open(f"./Input/{file}", 'r') as o:
            with open(f'./Output/{file[:-4]}.txt', 'w') as s:
                for line in sorted(o):
                    s.write(line)