import os

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


for file in os.listdir("./Input"):

    print(file)
    SortList(f'./Input/{file}')