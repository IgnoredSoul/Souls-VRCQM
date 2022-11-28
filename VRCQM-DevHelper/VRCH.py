import os, sys, argparse, time, json

#region Args
parser = argparse.ArgumentParser(description="-h The help screen... Dumbass")

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
#endregion

#region Checks
if(len(sys.argv) <= 1):
    os.system("python VRCH.py -h")

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

if(args.console):
    os.system("title Watching MelonLoader Logs")
    os.system(f"adb.exe logcat -v raw MelonLoader:I *:S")
#endregion
