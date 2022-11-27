import os

for file in os.listdir("./Input"):
    with open(f"./Input/{file}", 'r', encoding="utf-8") as o:
        with open(f'./Output/{file[:-4]}.txt', 'w', encoding="utf-8") as s:
            for line in sorted(o):
                s.write(line)