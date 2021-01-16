import sys
sys.path.insert(1, '.\\games\\')

import games

def help():
    helpfile = open(".\\data\\print\\help\\gamepicker", "r")
    print(helpfile.read())
    helpfile.close()

def main():
    string = str(input("--> ")).lower()
    if string == "lotto":
        games.lottosim.main()
    elif string == "blackjack":
        games.blackjack.real()
    elif string == "guessnr":
        games.guessnr.main()
    elif string == "slotmachine":
        games.slotmachine.main()
    elif string == "help":
        help()
