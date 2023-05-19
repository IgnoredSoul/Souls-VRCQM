import os, shutil

def split_string_at_words(string) -> list:
    words_to_split:list = [" - GameObjectList", " - UdonKeyList"]
    split_string:list = string.split(words_to_split[0])
    
    for word in words_to_split[1:]: # Bullshit I found on stackoverflow
        split_string:list = [item.split(word) for item in split_string]
        split_string:list = [item for sublist in split_string for item in sublist]
    
    return split_string

def get_longest_word(listA: list) -> str:
    longest_word:str = ''

    for word in listA:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

def get_longest_words(listA: list, listB: list) -> str:
    longest_word:str = ''

    for word in listA:
        if len(word) > len(longest_word):
            longest_word = word

    for word in listB:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

def center_word(word: str, length: int) -> str:
    centered_word:str = word.center(length)
    return centered_word

def save_gameobject_list(input_file: str, output_file: str) -> None:
    active_list:list = []
    inactive_list:list = []

    filter_words:list = [
        '!ftraceLightmaps',
        'Avatar_createdEyeTarget_1',
        'Avatar_createdEyeTarget_2',
        'FpsCounter',
        'UserInterface'
    ]

    with open(input_file, 'r', encoding="UTF-8") as file:
        active:bool = False

        for line in file:
            if '=============================== ACTIVE LIST ===============================' in line:
                active = True
                continue
            elif '============================== INACTIVE LIST ==============================' in line:
                active = False
                continue
            
            if active:
                if any(word in line for word in filter_words):
                    continue
                active_list.append(line.strip())
            else:
                if any(word in line for word in filter_words):
                    continue
                inactive_list.append(line.strip())

    active_list.sort()
    inactive_list.sort()

    length:int = len(get_longest_words(active_list, inactive_list)) + 2

    with open(output_file, 'w', encoding="UTF-8") as file:
        file.write(f"┏{'━' * length}┓\n")
        file.write(f"┃{center_word('DUMPED BY IGNOREDSOUL', length)}┃\n")
        file.write(f"┃{center_word('ACTIVE LIST', length)}┃\n")
        file.write(f"┣{'━' * length}┫\n")

        for word in active_list:
            file.write(f"┃{center_word(word, length)}┃\n")

        file.write(f"┣{'━' * length}┨\n")
        file.write(f"┃{center_word('INACTIVE LIST', length )}┃\n")
        file.write(f"┣{'━' * length}┫\n")

        for word in inactive_list:
            file.write(f"┃{center_word(word, length)}┃\n")
        file.write(f"┗{'━' * length}┛")

def save_udon_list(input_file: str, output_file: str) -> None:
    udonlist:list = []
    with open(input_file, 'r', encoding="UTF-8") as file:
        for line in file:
            udonlist.append(line.strip())

    udonlist.sort()
    length:int = len(get_longest_word(udonlist)) + 2
    with open(output_file, 'w', encoding="UTF-8") as file:
        file.write(f"┏{'━' * length}┓\n")
        file.write(f"┃{center_word('DUMPED BY IGNOREDSOUL', length)}┃\n")
        file.write(f"┃{center_word('UDON KEY LIST', length)}┃\n")
        file.write(f"┣{'━' * length}┫\n")

        for word in udonlist:
            file.write(f"┃{center_word(word, length)}┃\n")

        file.write(f"┗{'━' * length}┛")

# Make sure folders exist before continuing
paths = ["./Raw", "./Worlds"]
for path in paths:
    if not(os.path.exists(path)): os.mkdir(path)

for file in os.listdir("./Raw"):
    if file.endswith(".txt"):
        # Make their respected folders
        folder_name:str = split_string_at_words(file)[0]
        if not(os.path.exists(f"./Worlds/{folder_name}")): os.mkdir(f"./Worlds/{folder_name}")

        # Sort and save GameObject's
        if "gameobject" in file.lower():
            save_gameobject_list(f"./Raw/{file}", f"./Worlds/{folder_name}/{file}")
        
        # Sort and save UdonEvents
        elif "udon" in file.lower():
            save_udon_list(f"./Raw/{file}", f"./Worlds/{folder_name}/{file}")

        shutil.move(f"./Raw/{file}", f"./Sorted/{file}")
