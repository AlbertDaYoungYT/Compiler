from libs import installer as install
from os.path import expanduser
from zipfile import ZipFile
from gtts import gTTS
import socket
import shutil
import uuid
import time
import glob
import wget
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            print("Creating Folder")
            os.makedirs(directory)
            print("done")
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def firstStart():
    try:
        f = open(".pycheck", "r")
    except FileNotFoundError:
        print("'PackageCheck' file not found")
        print("Creating 'PackageCheck' file")
        print("done")
        print("")
        print("Installing Packages")
        install.installPacks()
        print("")
        print("done")
        f = open(".pycheck", "w")
        f.write("1")
    else:
        f = open(".pycheck", "r")
        if f.read() == "1":
            f.close()
            print("'PackageCheck' file found")

def textToSpeech(Text, FileName):
    tts = gTTS(str(Text))
    createFolder('./mp3/')
    tts.save('./mp3/' + FileName)
    print("done")

def simpleCalculator():
    print("Initiating Calculator")
    
    def add(x, y):
        return x + y
    
    # This function subtracts two numbers
    def subtract(x, y):
        return x - y
    
    # This function multiplies two numbers
    def multiply(x, y):
        return x * y
    
    # This function divides two numbers
    def divide(x, y):
        return x / y
    
    
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ->")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: ->"))
        num2 = float(input("Enter second number: ->"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")

def remember(Name, Value):
    createFolder('./memory/')
    if os.path.exists('./memory/'+Name):
        print("Error Path Exists")
        print("Do you want to overwrite it?")
        overwrite = str(input("->"))
        overwrite = overwrite.lower()
        if overwrite == "yes":
            print("Creating File")
            f = open('./memory/'+Name, "w")
            f.write(Value)
            f.close()
            print("done")
        elif overwrite == "no":
            pass
        else:
            print("Invalid Response")
    else:
        print("Creating File")
        f = open('./memory/'+Name, "w")
        f.write(Value)
        f.close()
        print("done")

def ipconfig():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    uuidhex = uuid.uuid1()
    print("IPconfig")
    print("-----------------------------------")
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print("")
    print(f"UUID Hex : {uuidhex}")
    print("-----------------------------------")

##def showWebcam()            OOoohh a sneak peak

def notCommand():
    print("This command is not a 'internal' or 'external' command")
    print("Or its not implemented")

