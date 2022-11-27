import os, sys, argparse, time

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

#endregion

#region Checks
if(len(sys.argv) <= 1):
    os.system("python VRCH.py -h")

if(args.move):
    fileLoc = input("Drag file here.\n> ")
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
