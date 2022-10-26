import os, time

if __name__ == '__main__':
    try:
        os.system("cls")
        os.system("title Watching MelonLoader Logs")
        os.system(f"adb.exe logcat -v raw MelonLoader:I *:S")
    except Exception as e: print(f"\n\n{e}\n\n")