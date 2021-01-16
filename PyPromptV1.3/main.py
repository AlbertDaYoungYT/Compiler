import checkCommands
import getpass
import os

while True:
    print()
    checkCommands.inputCommand(str(input(os.environ['COMPUTERNAME']+"::"+getpass.getuser()+"||"+os.path.dirname(os.path.realpath(__file__))+"-}> ")))