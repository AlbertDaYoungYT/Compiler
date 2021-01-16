from libs import installer as install
from libs import tpiupdate as update
from libs import connector
import commands as c
import subprocess
import shutil
import time
import os

def inputCommand(TextInput):
    string = TextInput.lower()
    string = string.split()
    try:
        if TextInput.lower() == "can you make me a cup of coffee":
            print("I can't im a Tea pot")
        elif TextInput.lower() == "can you make me a cup of Tea":
            print("I can't im a coffee pot")
        elif TextInput.lower() == "do you get tired":
            print("zzzzzzzz")
            time.sleep(0.5)
            print("Bang!!")
            time.sleep(0.1)
            print("POWER NAP!!")
            time.sleep(0.3)
            print("you were saying")
            time.sleep(0.5)
        elif string[0] == "calculator":
            if string[1] == "s":
                c.simpleCalculator()
            elif string[1] == "a":
                c.advancedCalculator()
            else:
                print("INITIATING ERROR: Enter S or A")
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
            elif string[1] == "import":
                c.importScript(string[2])
            else:
                print("INITIATING ERROR: Enter install, update or import")
        elif string[0] == "write":
            c.remember(string[1], string[2])
        elif string[0] == "ipget":
            c.ipconfig()
        elif string[0] == "opencv":
            if string[1] == "cam":
                c.showWebcam(string[2], string[3])
            elif string[1] == "canny":
                if string[2] == "edge":
                    if string[3] == "cam":
                        c.webcamEdge(string[4], string[5], string[6], string[7])
                    elif string[3] == "image":
                        c.imageEdge(string[4], string[5], string[6], string[7])
                    else:
                        print("INITIATING ERROR: Enter cam or image")
                else:
                    print("INITIATING ERROR: Enter edge")
            elif string[1] == "help":
                print("""COMMAND: opencv cam CAM_NR WINDOW_NAME""")
                print("""COMMAND: opencv canny cam THRESH1 THRESH2 CAM_NR WINDOW_NAME""")
                print("""COMMAND: opencv canny image THRESH1 THRESH2 WINDOW_NAME LOCATION""")
            else:
                print("INITIATING ERROR: Enter cam or canny")
        elif string[0] == "date":
            c.PyDatetime(string[1])
        elif string[0] == "time":
            c.PyTime()
        elif string[0] == "socket":
            if string[1] == "client":
                c.SocketClient(string[2], string[3])
            elif string[1] == "server":
                c.SocketServer(string[2], string[3])
            elif string[1] == "help":
                print("""COMMAND: socket client IP PORT""")
                print("""COMMAND: socket server IP PORT""")
            else:
                print("INITIATING ERROR: Enter client or server")
        elif string[0] == "play":
            if string[1] == "cd":
                c.vlccd(string[2])
            elif string[1] == "dvd":
                c.vlcdvd()
            elif string[1] == "help":
                print("""COMMAND: play cd TRACK""")
                print("""COMMAND: play dvd """)
            else:
                print("INITIATING ERROR: Enter cd or dvd")
        elif string[0] == "pyino":
            if string[1] == "read":
                c.serialRead(string[2], string[3], string[4])
            elif string[1] == "write":
                c.serialWrite(string[2], string[3], string[4])
            elif string[1] == "help":
                print("""COMMAND: pyino read BAUD COM_PORT KEEP_AS_FILE""")
                print("""COMMAND: pyino write BAUD COM_PORT CHAR""")
            else:
                print("INITIATING ERROR: Enter read or write")
        elif string[0] == "pycodex":
            if string[1] == "encode":
                c.PyCmdEncode(string[2], string[3])
            elif string[1] == "decode":
                c.PyCmdDecode(string[2], string[3])
            elif string[1] == "help":
                print("""COMMAND: pycodex encode STRING CODEX""")
                print("""COMMAND: pycodex decode STRING CODEX""")
            else:
                print("INITIATING ERROR: Enter encode or decode")
        elif string[0] == "pyjoke":
            c.jokes()
        elif string[0] == "read":
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
        elif string[0] == "speak":
            if string[1] != "help":
                c.speak(string[1], string[2])
            elif string[1] == "help":
                print("""COMMAND: speak STRING OUTPUT""")
        elif string[0] == "osc":
            if string[1] == "h":
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif string[1] == "s":
                os.system("shutdown /s /t 1")
            elif string[1] == "r":
                os.system("shutdown /r /t 1")
            elif string[1] == "help":
                print("""COMMAND: osc h""")
                print("""COMMAND: osc s""")
                print("""COMMAND: osc r""")
            else:
                print("INITIATING ERROR: Enter H, S or R")
        elif string[0] == "run":
            if string[1] == "cmd":
                os.system("C:\\Windows\\System32\\cmd.exe")
            elif string[1] == "script":
                clear = lambda: os.system('cls')
                clear()
                c.runScript(string[2])
            elif string[1] == "help":
                print("""COMMAND: run cmd""")
                print("""COMMAND: run script SCRIPT_NAME""")
            else:
                print("INITIATING ERROR: Enter cmd or script")
        elif string[0] == "color":
            os.system("color "+string[1])
        elif string[0] == "del":
            if string[1] == "run.bat" or string[1] == "main.py" or string[1] == "commands.py" or string[1] == "checkCommands.py":
                print("You can't delete 'main' files")
            else:
                os.remove(string[1])
        elif string[0] == "display":
            if string[1] == "all":
                if string[2] == "commands":
                    print("""
    MAIN:
    calculator  Initiates a calculator in s/a (simple or advanced)
    tpi         Tpi is the package install for PyPrompt
    write       Writes a file
    ipget       Prints the ip of the machine and other info
    opencv      OpenCV is an open source image processer for Python
    date/time   Prints the time or date
    socket      Socket is an network communication device
    play        Play is a VLC powered cd and dvd reader
    pyino       Is the communication between the Computer and an Arduino
    pycodex     Is an encoder and decoder of binary/base64/hex
    pyjoke      Prints a random joke
    read        Reads all the content of a file
    move        Moves a file from A to B
    bring       Moves a file from A to the main PrPrompt folder
    clear       Clears the command line
    exit        Exits the command line
    speak       Speak is powered by Google TTS and can say any sentence
    osc         Is OperatingSystemCommands and can h/s/r (Hypernate/Sleep/Restart) the computer
    run         Runs the cmd or a Python script
    color       Changes the color of the command line
    del         Deletes a file WARNING DONT DELETE MAIN FILES

    Connector Commands:
    motion      Initiates the motion cam software
    get         |get computer info| initiates the info software
    controller  Gets live input from a PS4 controller
    7zip        Initiates the zip software
    contact     Intiates the PhoneBook software
    """)
        elif string[0] == "help":
            print("""
    tpi         tpi is the package installer
    ---install  Dowmnloads the specified module
    ------all   Installs all the nesesary modules
    ---update   Updates the downloads database
    ---import   Imports and installs the modules
    calculator  Initiates the build in calculator in simple or advanced
    ---s        Initiates the simple version
    ---a        Initiates the advanced version
    ipget       Prints the ip of the machine and other info
    date/time   Prints time or date in any format
    pyjoke      Prints a random joke (Some of the jokes are not funny)
    write       Writes a file
    load        Reads all file contents
    move        Moves a file from A to B
    bring       Moves a file to PyPrompt's directory
    clear       Clears the output
    del         Deletes a file or directory
    exit        Closes the Command Promt
    You can also type 'display all commands' to get all the commands
    or type [command] help to get help with that command""")
        elif string[0]:
            for char in TextInput:
                if char == "+":
                    final = TextInput.split(char)
                    print(int(final[0]) + int(final[1]))
                    break
                elif char == "-":
                    final = TextInput.split(char)
                    print(int(final[0]) - int(final[1]))
                    break
                elif char == "*":
                    final = TextInput.split(char)
                    print(int(final[0]) * int(final[1]))
                    break
                elif char == "/":
                    final = TextInput.split(char)
                    print(int(final[0]) / int(final[1]))
                    break
        else:
            connector.ExternalCommand(TextInput)
    except IndexError:
        print("COMMAND ERROR: Command to long or to short")