import random

def main():
    UserGuess = []
    print("See if you can guess a random number between 1 and 50 in 5 guesses")
    print("The Prize is 5000 credits")
    print("Press Enter to start")
    input()
    ComputerGuess = random.randrange(1, 51)

    while len(UserGuess) <= 4:
        UserInput = int(input("-> "))
        if int(UserInput) == int(ComputerGuess):
            win()
        elif UserInput > 50:
            print("ERROR")
        else:
            print("Try again")
            UserGuess.append(UserInput)
    
    print("You Lose")
    print("Number was "+str(ComputerGuess))

def win():
    print("You Win")
    print("+5000 Credits")
    f = open(".\\games\\AppData\\credits.libdata", "r")
    past = f.read()
    f.close()
    f = open(".\\.\\games\\AppData\\credits.libdata", "w")
    f.write(str(int(past)+5000))
    f.close()