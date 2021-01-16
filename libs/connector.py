import sys
sys.path.insert(1, '.\\programs\\')

import programs

def help():
    helpfile = open(".\\data\\print\\help\\connector", "r")
    print(helpfile.read())
    helpfile.close()

def ExternalCommand(TextInput):
    string = TextInput.lower()
    string = string.split()
    if string[0] == "motion":
        programs.pycam.main()
    elif string[0] == "get":
        if string[1] == "computer":
            if string[2] == "info":
                programs.computer.inputCommand(str(input("->> ")))
    elif string[0] == "converter":
        programs.converter.inputCommand(str(input("->> ")))
    elif string[0] == "controller":
        programs.pycontroller.main()
    elif string[0] == "7zip":
        programs.zip.main()
    elif string[0] == "contact":
        programs.contacts.main(string)
    elif string[0] == "games":
        programs.gamepicker.main()
    elif string[0] == "ytdown":
        programs.ytdownloader.main()
    elif string[0] == "help":
        help()
