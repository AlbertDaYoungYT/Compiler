LOGS = ".\\data\\logs\\"
log = open(LOGS+"import.log", "w")
log.write("")
log.close()
log = open(LOGS+"import.log", "a")
try:
    log.write("Trying to import modules...\n")
    from libs import installer as install
    from time import gmtime, strftime
    from os.path import expanduser
    from zipfile import ZipFile
    from datetime import date
    from gtts import gTTS
    import numpy as np
    import binascii
    import random
    import base64
    import serial
    import socket
    import shutil
    import math
    import uuid
    import time
    import glob
    import wget
    import wmi
    import cv2
    import vlc
    import os
except ModuleNotFoundError:
    log.write("Failed to import modules\nTrying to install modules...\n")
    import os
    os.system('cmd /c "pip install opencv-python"')
    os.system('cmd /c "pip install numpy"')
    os.system('cmd /c "pip install binascii"')
    os.system('cmd /c "pip install serial"')
    os.system('cmd /c "pip install glob"')
    os.system('cmd /c "pip install wget"')
    os.system('cmd /c "pip install base64"')
    os.system('cmd /c "pip install gTTS"')
    os.system('cmd /c "pip install python-vlc"')
    os.system('cmd /c "pip install wmi"')
    log.write("Modules installed successfully\n")
finally:
    log.write("Importing modules...\n")
    from libs import installer as install
    from time import gmtime, strftime
    from os.path import expanduser
    from zipfile import ZipFile
    from datetime import date
    from gtts import gTTS
    import numpy as np
    import binascii
    import random
    import base64
    import serial
    import socket
    import shutil
    import math
    import uuid
    import time
    import glob
    import wget
    import wmi
    import cv2
    import vlc
    import os
log.write("Success\n")

log.write("Getting date..\n")
try:
    now = date.today()
except Execption as e:
    log.write("ERROR: "+str(e)+"\n")
    log.write("Trying to fix error...\n")
    from datetime import date
    now = date.today()
finally:
    now = date.today()
log.write("Done\n")
log.close()

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            print("Creating Folder")
            os.makedirs(directory)
            print("done")
    except OSError:
        print ('Error: Creating directory. ' +  directory)

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

def advancedCalculator():
    class calci(object):

        def add(self,num1,num2):
            answer = num1 + num2
            print('Sum = ',answer)
        def sub(self,num1,num2):
            answer = num1 - num2
            print('Difference = ',answer)
        def mul(self,num1,num2):
            answer = num1 * num2
            print('Product = ',answer)
        def div(self,num1,num2):
            answer = num1 / num2
            print('Quotient = ',answer)
        def sinrad(self,num):
            answer = math.sin(num)
            print("Sine (%f) = %f" %(num,answer))
        def cosrad(self,num):
            answer = math.cos(num)
            print("Cosine(%f) = %f" %(num,answer))
        def tanrad(self,num):
            answer = math.tan(num)
            print("Tan(%f) = %f" %(num,answer))
        def cosecrad(self,num):
            answer = 1/(math.sin(num))
            print("Sine(%f = %f" %(num,answer))
        def secrad(self,num):
            answer = 1/(math.cos(num))
            print("Sec(%f) = %f" %(num,answer))
        def cotrad(self,num):
            answer = 1/(math.tan(num))
            print("Cot(%f) = %f" %(num,answer))
        def sindeg(self,num):
            answer = math.sin(math.radians(num))
            print("Sin(%f) in degrees = %f" %(num,answer))
        def cosdeg(self,num):
            answer = math.cos(math.radians(num))
            print("Cos(%f) in degrees = %f" %(num,answer))
        def tandeg(self,num):
            answer = math.tan(math.radians(num))
            print("Tan(%f) in degrees = %f" %(num,answer))
        def cosecdeg(self,num):
            answer = 1/(math.sin(math.radians(num)))
            print("Cosec(%f) in degrees = %f" %(num,answer))
        def secdeg(self,num):
            answer = 1/(math.cos(math.radians(num)))
            print("Sec(%f) in degrees = %f" %(num,answer))
        def cotdeg(self,num):
            answer = 1/(math.tan(math.radians(num)))
            print("Cot(%f) in degrees = %f" %(num,answer))
        def ln(self,num):
            answer = math.log(num)
            print("ln(%f) = %f" %(num,answer))
        def logten(self,num):
            answer = math.log10(num)
            print("log10(%f) = %f" %(num,answer))
        def logbasex(self,num,x):
            answer = math.log(num,x)
            print("log base(%f)(%f) = %f" %(x,num,answer))
        def squareroot(self,num):
            answer = math.sqrt(num)
            print("Square Root(%f) = %f " %(num,answer))
        def pie(self):
            print( 'pi = ',math.pi)
        def powerof(self,num,raiseby):
            answer = math.pow(num,raiseby)
            print("%f ^ (%f) = %f" %(num,raiseby,answer) )
    calc = calci()
    print('welcome to casio')
    print("Here's a list of choices")
    print('*'*60)
    print("1 : Addition  \t\t   12 : Sine in degrees")
    print("2 : Subtraction \t   13 : Cosine in degrees")
    print("3 : Multiplication\t   14 : Tan in degrees")
    print("4 : Division  \t\t   15 : Cosecant in degrees")
    print("5 : Sine in radians\t   16 : Secant in degrees")
    print("6 : Coisne in radians\t   17 : Cot in degrees")
    print("7 : Tan in radians\t   18 : Natural log")
    print("8 : Cosecant in radians    19 : Base 10 log")
    print("9 : Secant in radians\t   20 : Log base 'x'")
    print("10 : Cot in radians\t   21 : Square root")
    print("11 : pi \t\t   22 : Power of")
    print("23 : exit")
    print('*'*60)
    choice = ""
    while True:
        try:
            choice = int(input('enter a number of your choice from the above list : '))
        except:
            print("Enter a valid number")
        if choice == 1:
            n1 = float(input('enter the first number to add : '))
            n2 = float(input('enter the second number to add : '))
            calc.add(n1,n2)
        elif choice == 2:
            n1 = float(input('enter the first number to subtract : '))
            n2 = float(input('enter the second number to subtract : '))
            calc.sub(n1,n2)
        elif choice == 3:
            n1 = float(input('enter the first number to multiply : '))
            n2 = float(input('enter the second number to multiply : '))
            calc.mul(n1,n2)
        elif choice == 4:
            n1 = float(input('enter the first number to divide : '))
            n2 = float(input('enter the second number to divide : '))
            calc.div(n1,n2)
        elif choice == 5:
            n = float(input('enter a number to find its sine in rad: '))
            calc.sinrad(n)
        elif choice == 6:
            n = float(input('enter a number to find its cos in rad: '))
            calc.cosrad(n)
        elif choice == 7:
            n = float(input('enter a number to find its tan in rad : '))
            calc.tanrad(n)
        elif choice == 8:
            n = float(input('enter a number to find its cosec in rad : '))
            calc.cosecrad(n)
        elif choice == 9:
            n = float(input('enter a number to find its sec in rad : '))
            calc.secrad(n)
        elif choice == 10:
            n = float(input('enter a number to find its cot in rad : '))
            calc.cotrad(n)
        elif choice == 11:
            calc.pie()
        elif choice == 12:
            n = float(input('enter a number to find its sine in deg : '))
            calc.sindeg(n)
        elif choice == 13:
            n =float(input('enter a number to find its cos in deg : '))
            calc.cosdeg(n)
        elif choice == 14:
            n = float(input('enter a number to find its tan in deg : '))
            calc.tandeg(n)
        elif choice == 15:
            n =float(input('enter a number to find its cosec in deg : '))
            calc.cosecdeg(n)
        elif choice == 16:
            n = float(input('enter a number to find its sec in deg : '))
            calc.secdeg(n)
        elif choice == 17:
            n = float(input('enter a number to find its cot in deg : '))
            calc.cotdeg(n)
        elif choice == 18:
            n =float(input('enter a number to find its natural deg : '))
            calc.ln(n)
        elif choice == 19:
            n = float(input('enter a number to find its log to base 10 : '))
            calc.logten(n)
        elif choice == 22:
            n = float(input('enter a number  : '))
            po = float(input('enter its power : '))
            calc.powerof(n,po)
        elif choice == 21:
            n = float(input('enter a number to find its square root : '))
            calc.squareroot(n)
        elif choice == 20:
            base = float(input('enter base value : '))
            n = float(input('enter a number to find its log to the given base value: '))
            calc.logbasex(n,base)
        elif choice == 23:
            break
        else:
            print("WARNING : Enter a valid input from the list above")

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

def speak(String, Output):
    createFolder("./data/audio")
    tts = gTTS(String)
    tts.save("./data/audio/"+Output)

def vlccd(track):
    c = wmi.WMI()
    instance = vlc.Instance()
    player = instance.media_player_new()
    medialist = instance.media_list_new()
    listplayer = instance.media_list_player_new()
    listplayer.set_media_player(player)

    for cdrom in c.Win32_CDROMDrive():
        if track == "all":
            for i in range (1,35):
                track = instance.media_new("cdda:///"+cdrom.Drive.replace(":", ":/"), (":cdda-track=" + str(i)))
                medialist.add_media(track)
        else:
            track = instance.media_new("cdda:///"+cdrom.Drive.replace(":", ":/"), (":cdda-track=" + str(track)))
    listplayer.set_media_list(medialist)
    listplayer.play()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            listplayer.stop()

def vlcdvd():
    c = wmi.WMI()
    def setup_player(name):
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(name)
        player.set_media(media)
        player.video_set_scale(player.video_get_height()+player.video_get_width())
        player.play()
    
    for cdrom in c.Win32_CDROMDrive():
        setup_player('dvd:///'+cdrom.Drive.replace(":", ":/")) # for no disc menu: 'dvdsimple:///O:/' for audio cd: 'cdda:///O:/' -  "O:/" is the optical drive

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            player.Stop()

def SocketClient(ipaddr, portnr):
    HOST = ipaddr  # The server's hostname or IP address
    PORT = portnr        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(str(input("--> "))))
        data = s.recv(1024)

    print('Received', repr(data))

def SocketServer(ipaddr, portnr):
    HOST = ipaddr  # Standard loopback interface address (localhost)
    PORT = portnr        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)

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

def showWebcam(Cam, WindowName):
    print("Too Stop Press \"q\"")
    cap = cv2.VideoCapture(int(Cam))

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow(str(WindowName),gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def webcamEdge(Thre1, Thre2, Cam, WindowName):
    print("Too Stop Press \"q\"")
    cap = cv2.VideoCapture(int(Cam))

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edge = cv2.Canny(frame, Thre1, Thre2)

        cv2.imshow(WindowName, edge)

        if cv2.waitKey(20) == ord('q'):  # Introduce 20 milisecond delay. press q to exit.
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def imageEdge(Thre1, Thre2, WindowName, FileName):
    print("Too Stop Press \"q\"")

    while(True):
        # Capture frame-by-frame
        frame = cv2.imread(FileName)

        # Our operations on the frame come here
        frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edge = cv2.Canny(frame, Thre1, Thre2)

        cv2.imshow(WindowName, edge)

        if cv2.waitKey(20) == ord('q'):  # Introduce 20 milisecond delay. press q to exit.
            break

def PyTime(TimeMode):
    t = time.localtime()
    current_time = time.strftime(TimeMode, t)
    print(current_time)

def notCommand():
    print("This command is not a 'internal' or 'external' command")
    print("Or its not implemented")

def importScript(ScriptName):
    file = open("./libs/connector.py", "a")
    scriptConnect = open("./libs/"+ScriptName+".config", "r")
    print("writing")
    for line in scriptConnect:
        file.write(line)
    file.close()
    scriptConnect.close()
    print("done")

def runScript(ScriptName):
    os.system('cmd /c "python {ScriptName}"')

def PyDatetime(DateMode):
    dt = now.strftime(DateMode)
    print(dt)

def serialWrite(Baud, ComPort, Char):
    ser = serial.Serial(ComPort, int(Baud))
    UpperChar = Char.upper()
    ser.write(bytes(UpperChar))

def serialRead(Baud, ComPort, KeepAsFile):
    ser = serial.Serial(ComPort, int(Baud))
    KeepAsFile = bool(KeepAsFile)
    while True:
        data = ser.read()
        if KeepAsFile == "True":
            f = open("serial.log", "a")
            f.write(str(data)+"\n")
        elif KeepAsFile == "False":
            if cv2.waitKey(20) == ord('q'):  # Introduce 20 milisecond delay. press q to exit.
                break
    f.close()
    ser.close()

def PyCmdEncode(String, Codex):
    if Codex == "binary":
        binaryString = ' '.join(bin(ord(char)).split('b')[1].rjust(8, '0') for char in String)
        print(binaryString)
    elif Codex == "base64":
        base64String = base64.b64encode(String.encode('ascii')).decode('ascii')
        print(base64String)
    elif Codex == "hex":
        hexString = binascii.hexlify(bytes(String.encode()))
        print(hexString)

def PyCmdDecode(String, Codex):
    if Codex == "binary":
        binaryString = ''.join(chr(int(binary, 2)) for binary in String.split(' '))
        print(binaryString)
    elif Codex == "base64":
        base64String = base64.b64decode(String.encode('ascii')).decode('ascii')
        print(base64String)
    elif Codex == "hex":
        hexString = binascii.unhexlify(String.decode())
        print(hexString)

def jokes():
    jokesLst = ["What goes up and down but does not move?\nStairs",
        "Where should a 500 pound alien go?\nOn a diet",
        "What did one toilet say to the other?\nYou look a bit flushed.",
        "Why did the picture go to jail?\nBecause it was framed.",
        "What did one wall say to the other wall?\nI'll meet you at the corner. ",
        "What did the paper say to the pencil?\nWrite on! ",
        "What do you call a boy named Lee that no one talks to?\nLonely ",
        "What gets wetter the more it dries?\nA towel.",
        "Why do bicycles fall over?\nBecause they are two-tired! ",
        "Why do dragons sleep during the day?\nSo they can fight knights! ",
        "What did Cinderella say when her photos did not show up?\nSomeday my prints will come!",
        "Why was the broom late?\nIt over swept! ",
        "What part of the car is the laziest?\nThe wheels, because they are always tired!",
        "What did the stamp say to the envelope?\nStick with me and we will go places!",
        "What is blue and goes ding dong?\nAn Avon lady at the North Pole! ",
        "Were you long in the hospital?\nNo, I was the same size I am now! ",
        "Why couldn't the pirate play cards?\nBecause he was sitting on the deck!",
        "What did the laundryman say to the impatient customer?\nKeep your shirt on!",
        "What's the difference between a TV and a newspaper?\nEver tried swatting a fly with a TV? ",
        "What did one elevator say to the other elevator?\nI think I'm coming down with something!",
        "Why was the belt arrested?\nBecause it held up some pants!",
        "Why was everyone so tired on April 1st?\nThey had just finished a March of 31 days.",
        "Which hand is it better to write with?\nNeither, it's best to write with a pen!",
        "Why can't your nose be 12 inches long?\nBecause then it would be a foot!",
        "What makes the calendar seem so popular?\nBecause it has a lot of dates!",
        "Why did Mickey Mouse take a trip into space?\nHe wanted to find Pluto!",
        "What is green and has yellow wheels?\nGrass…..I lied about the wheels!",
        "What is it that even the most careful person overlooks?\nHer nose!",
        "Did you hear about the robbery last night?\nTwo clothes pins held up a pair of pants!",
        "Why do you go to bed every night?\nBecause the bed won't come to you! ",
        "Why did Billy go out with a prune?\nBecause he couldn't find a date!",
        "Why do eskimos do their laundry in Tide?\nBecause it's too cold out-tide!",
        "How do you cure a headache?\nPut your head through a window and the pane will just disappear!",
        "What has four wheels and flies?\nA garbage truck! ",
        "What kind of car does Mickey Mouse's wife drive?\nA minnie van!",
        "Why don't traffic lights ever go swimming?\nBecause they take too long to change!",
        "Why did the man run around his bed?\nTo catch up on his sleep!",
        "Why did the robber take a bath before he stole from the bank?\nHe wanted to make a clean get away!",
        "What did the spider do on the computer?\nMade a website! ",
        "What did the computer do at lunchtime?\nHad a byte! ",
        "What does a baby computer call his father?\nData! ",
        "Why did the computer keep sneezing?\nIt had a virus!",
        "What is a computer virus?\nA terminal illness!",
        "Why was the computer cold?\nIt left it's Windows open!",
        "Why was there a bug in the computer?\nBecause it was looking for a byte to eat?",
        "Why did the computer squeak?\nBecause someone stepped on it's mouse!",
        "What do you get when you cross a computer and a life guard?\nA screensaver!",
        "Where do all the cool mice live?\nIn their mousepads",
        "What do you get when you cross a computer with an elephant?\nLots of memory! ",
        "Why didn't the quarter roll down the hill with the nickel?\nBecause it had more cents.",
        "Why was the math book sad?\nBecause it had too many problems. ",
        "What kind of meals do math teachers eat?\nSquare meals!",
        "Teacher: Now class, whatever I ask, I want you to all answer at once. How much is six plus 4?\nClass: At once! ",
        "Why didn't the two 4's want any dinner?\nBecause they already 8!",
        "What is a math teacher's favorite sum?\nSummer!",
        "What is a butterfly's favorite subject at school?\nMothematics.",
        "What do you get when you divide the circumference of a Jack-o-lantern by its diameter?\nPumpkin Pi!",
        "What did zero say to the number eight?\nNice belt.",
        "Teacher: Why are you doing your multiplication on the floor?\nStudent: You told me not to use tables.",
        "What did the tornado say to the sports car?\nWant to go for a spin!",
        "What kind of shorts to clouds wear?\nThunderwear!",
        "What's a tornado's favorite game?\nTwister!",
        "What did one volcano say to the other volcano?\nI lava you!",
        "What bow can't be tied?\nA rainbow!",
        "What falls but never hits the ground?\nThe temperature!",
        "How do hurricanes see?\nWith one eye!",
        "What did the cloud say to the lightning bolt?\nYou're shocking! ",
        "What happens when the fog disperses in California?\nUCLA!",
        "How hot is it?\nIt's so hot, when I turned on my lawn sprinkler, all I got was steam!",
        "Who does everyone listen to, but no one believes?\nThe weather reporter",
        "What is the opposite of a cold front?\nA warm back"]
    print(random.choice(jokesLst))

