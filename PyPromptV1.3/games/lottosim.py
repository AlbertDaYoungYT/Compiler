import random

def main():
    try:
        credit = open(".\\games\\AppData\\credits.libdata", "r")
    except Exception:
        credit = open(".\\games\\AppData\\credits.libdata", "w")
        credit.write(str(500))
        credit.close()
    finally:
        credit = open(".\\games\\AppData\\credits.libdata", "r")
    print("Welcome to the Lottery")
    print("It Costs 100 Credits to play")
    print("Press Enter to start")
    print()
    print("Credits = "+str(credit.read()))
    print()
    input()
    credit.close()
    credit = open(".\\games\\AppData\\credits.libdata", "r")

    pastCredits = credit.read()
    credit.close()

    Correct = 0
    CMaxLoop = 7
    UMaxLoop = 7
    ComputerGuess = []
    UserGuess = []

    for loop in range(0, CMaxLoop):
        guess = random.randrange(1, 37)
        if guess in ComputerGuess:
            CMaxLoop += 1
        else:
            pass
        ComputerGuess.append(guess)

    print("Pick 7 random numbers from 1-36 (the numbers cant be the same)")

    while len(UserGuess) <= 6:
        UserInput = int(input("-> "))
        if UserInput in UserGuess:
            file = open(".\\data\\print\\msg\\lottosim\\error1")
            print(file.read())
            file.close()
            pass
        elif UserInput > 36:
            file = open(".\\data\\print\\msg\\lottosim\\error2")
            print(file.read())
            file.close()
            pass
        else:
            UserGuess.append(UserInput)

    for User in UserGuess:
        for Comp in ComputerGuess:
            if Comp == User:
                Correct += 1
            else:
                pass

    f = open(".\\games\\AppData\\credits.libdata", "r")

    if Correct == 0:
        file = open(".\\data\\print\\msg\\lottosim\\lose")
        print(file.read())
        file.close()
        credit = open(".\\games\\AppData\\credits.libdata", "w")
        credit.write(str(int(pastCredits)-100))
        credit.close()
    elif Correct == 1:
        file = open(".\\data\\print\\msg\\lottosim\\won50")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+50))
    elif Correct == 2:
        file = open(".\\data\\print\\msg\\lottosim\\won250")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+250))
    elif Correct == 3:
        file = open(".\\data\\print\\msg\\lottosim\\won500")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+500))
    elif Correct == 4:
        file = open(".\\data\\print\\msg\\lottosim\\won2500")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+2500))
    elif Correct == 5:
        file = open(".\\data\\print\\msg\\lottosim\\won10000")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+10000))
    elif Correct == 6:
        file = open(".\\data\\print\\msg\\lottosim\\won200000")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+200000))
    elif Correct == 7:
        file = open(".\\data\\print\\msg\\lottosim\\won1000000")
        print(file.read())
        file.close()
        past = f.read()
        f.close()
        f = open(".\\.\\games\\AppData\\credits.libdata", "w")
        f.write(str(int(past)+1000000))

    f.close()
    print()
    print("Computer: "+str(ComputerGuess))
    print("You: "+str(UserGuess))