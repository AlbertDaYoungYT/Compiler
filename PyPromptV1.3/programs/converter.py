def inputCommand(TextInput):
    string = TextInput.lower()
    string = string.split()
#-------------------SPEED--------------------#
    if string[0] == "km/h-mph":
        print(0.6213712*int(string[1]))
    elif string[0] == "mph-km/h":
        print(0.6213712/int(string[1]))
    elif string[0] == "km/h-ms":
        print(0.2777778*int(string[1]))
    elif string[0] == "ms-km/h":
        print(0.2777778/int(string[1]))
    elif string[0] == "km/h-knot":
        print(0.5399568*int(string[1]))
    elif string[0] == "knot-km/h":
        print(0.5399568/int(string[1]))
#--------------------------------------------#
    elif string[0] == "mph-ms":
        print(0.4470400*int(string[1]))
    elif string[0] == "ms-mps":
        print(0.4470400/int(string[1]))
    elif string[0] == "mps-knot":
        print(0.8689762*int(string[1]))
    elif string[0] == "knot-mps":
        print(0.8689762/int(string[1]))
#--------------------------------------------#
    elif string[0] == "knot-ms":
        print(1.943844*int(string[1]))
    elif string[0] == "ms-knot":
        print(1.943844*int(string[1]))
#--------------------------------------------#
#--------------------------------------------#
    if string[0] == "c-f":
        print(33.80000*int(string[1]))
    elif string[0] == "f-c":
        print(33.80000/int(string[1]))
    elif string[0] == "f-k":
        print(255.9278*int(string[1]))
    elif string[0] == "k-f":
        print(255.9278/int(string[1]))
    elif string[0] == "c-k":
        print(274.1500*int(string[1]))
    elif string[0] == "k-c":
        print(274.1500/int(string[1]))
#--------------------------------------------#
#--------------------------------------------#