import os, time

if __name__ == '__main__':
    try:
        os.system("cls")
        os.system("adb.exe kill-server")
        os.system("adb.exe push C:/Users/Jakei/source/repos/GRIM/GRIM/bin/Debug/GRIM.dll /sdcard/Android/data/com.vrchat.oculus.quest/files/Mods");
        os.system("adb shell am force-stop com.vrchat.oculus.quest")
        time.sleep(2)
        os.system("adb.exe shell monkey -p com.vrchat.oculus.quest -v 1")
        os.system("cls")
        time.sleep(3)
        os.system("cls")
        os.system("title Watching MelonLoader Logs")
        os.system(f"adb.exe logcat -v raw MelonLoader:I *:S")
    except Exception as e: print(f"\n\n{e}\n\n")
