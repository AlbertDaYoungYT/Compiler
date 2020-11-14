from libs import installer as install
from libs import tpiupdate as update
from libs import connector
import commands as c
import shutil
import os

def inputCommand(TextInput):
    string = TextInput.lower()
    string = string.split()
    if string[0] == "folder":
        c.createFolder(string[1])
    elif string[0] == "firststart":
        c.firstStart()
    elif TextInput.lower() == "can you make me a cup of coffee":
        print("I can't im a Tea pot")
    elif TextInput.lower() == "can you make me a cup of Tea":
        print("I can't im a coffee pot")
    elif string[0] == "speak":
        c.textToSpeech(string[1], string[2])
    elif string[0] == "calculator":
        c.simpleCalculator()
    elif string[0] == "tpi":
        if string[1] == "install":
            if string[2] == "all":
                if str(input("Are You Sure? ")).lower() == "yes":
                    print("This can take sevral minutes")
                    install.installPacks()
            else:
                install.tpiInstaller(string[2])
        elif string[1] == "update":
            update.update()
    elif string[0] == "write":
        c.remember(string[1], string[2])
    elif string[0] == "ipget":
        c.ipconfig()
    elif string[0] == "load":
        with open(string[1], "r") as f:
            for line in f:
                print(line)
    elif string[0] == "move":
        shutil.move(string[1], string[2])
    elif string[0] == "bring":
        shutil.move(string[1], os.path.dirname(os.path.realpath("__file__")))
    elif string[0] == "clear":
        clear = lambda: os.system('cls')
        clear()
    elif string[0] == "exit":
        exit()
    elif string[0] == "del":
        if string[1] == "run.bat" or string[1] == "main.py" or string[1] == "commands.py" or string[1] == "checkCommands.py":
            print("You can't delete 'main' files")
        else:
            os.remove(string[1])
    elif string[0] == "help":
        print("""firststart  Initiates fiststart
tpi         tpi is the package installer
folder      Creates a folder
speak       Creates a audio file with TTS
calculator  Initiates the build in calculator
write       Writes a file
load        Reads all file contents
move        Moves a file from A to B
bring       Moves a file to PyPrompt's directory
clear       Clears the output
del         Deletes a file or directory
exit        Closes the Command Promt""")
    else:
        connector.externalCommand(TextInput)