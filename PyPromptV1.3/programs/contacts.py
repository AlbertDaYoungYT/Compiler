LOGS = ".\\data\\logs\\"
log = open(LOGS+"contacts.log", "w")
log.write("")
log.close()
log = open(LOGS+"contacts.log", "a")
def main(string):
    file = open(".\\programs\\AppData\\contacts.db", "a")
    if string[1] == "add":
        AddContact(string[2], string[3])
    elif string[1] == "find":
        FindContact(string[2], string[3])
    elif string[1] == "list":
        ListAll()
    elif string[1] == "help":
        help()

def AddContact(Number, Name):
    log.write("Writing Contact..\n")
    file.write(Number + "||" + Name)
    file.close()
    log.write("Done\n")

def FindContact(Number, Name):
    log.write("Searching for contact...\n")
    for line in file:
        line = line.split("||")
        if Number == line[0] and Name == line[1]:
            log.write("Found contact\n")
            print("Name: " + line[1])
            print("Number: " + line[0])
        else:
            log.write("Not Match.\n")
            pass

def ListAll():
    log.write("Listing all contacts...\n")
    for line in file:
        line = line.split("||")
        print("Name: " + line[1])
        print("Number: " + line[0])
        print()
    log.write("Done\n")

def help():
    helpfile = open(".\\data\\print\\help\\contacts", "r")
    print(helpfile.read())
    helpfile.close()
log.close()