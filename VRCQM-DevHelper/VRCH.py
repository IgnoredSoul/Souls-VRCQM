import os, sys, argparse, time, json, atexit, subprocess

#region Args
parser = argparse.ArgumentParser()

parser.add_argument(
    "-m",
    "--move",
    help = "Move file to VRChat mods folder",
    action = "store_true"
)

parser.add_argument(
    "-s",
    "--start",
    help = "Starts VRChat",
    action = "store_true"
)

parser.add_argument(
    "-d",
    "--display",
    help = "Display Quest Screen",
    action = "store_true"
)

parser.add_argument(
    "-c",
    "--console",
    help = "Open console",
    action = "store_true"
)


args = parser.parse_args()
#endregion

#region Functions
def saveFile(loc: str):
    JsonData = {
    "LastUsed": loc,
    }
    with open("prev.json", "w") as outfile:
        outfile.write(json.dumps(JsonData, indent=4))

def closeSCRCPY():
    try:
        if(args.display):
            os.system("taskkill /im scrcpy.exe /t /f")
        os.system("adb kill-server")
    except Exception as e:
        print(e)
#endregion

#region Checks
if(len(sys.argv) <= 1):
    os.system("python VRCH.py -h")

atexit.register(closeSCRCPY)

if(args.move):
    if(os.path.exists("prev.json")):
        yn = input("Use previous file? (Y/N)\n> ").lower()
        if(yn == "n"):
            fileLoc = input("Drag file here.\n> ")
            saveFile(fileLoc)
        else:
            with open(f"./prev.json", "r", encoding="utf-8") as read_file:
                settings = json.load(read_file)
                print(settings["LastUsed"])
                fileLoc = settings["LastUsed"]

    else:
        fileLoc = input("Drag file here.\n> ")
        saveFile(fileLoc)
    os.system(f'adb.exe push {fileLoc} /sdcard/Android/data/com.vrchat.oculus.quest/files/Mods')

if(args.start):
    os.system("adb shell am force-stop com.vrchat.oculus.quest")
    time.sleep(2)
    os.system("adb.exe shell monkey -p com.vrchat.oculus.quest -v 1")
    os.system("cls")

if(args.display):
    os.system("start /MIN ./scrcpy/scrcpy.exe -m 800 --crop=1600:900:2017:510")

if(args.console):
    os.system("title Watching MelonLoader Logs")
    os.system(f"adb.exe logcat -v raw MelonLoader:I *:S")
#endregion