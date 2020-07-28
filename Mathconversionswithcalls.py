def option1(): #main menu
    print("Welcome to my conversion calculator!")
    print("Select from the following options")
    print("1. Temp conversion")
    print("2. Imperial distance conversion")
    print("3. Kitchen measurements conversion")
    print("Exit to exit this application")
    print("")
    o1val = input(":")
    if o1val == "1":
        tempcalc()
    elif o1val == "2":
        discalc()
    elif o1val == "3":
        option1_3()
    elif o1val == "Exit":
        import sys
        sys.exit()
    elif o1val =="exit":
        import sys
        sys.exit()
    else:
        option1()
def tempcalc():
    print("")
    print("1. F to C")
    print("2. C to F")
    print("Exit to return to main menu")
    print("")
    temp = input(":")
    if temp == "1":
        tempcalcf()
    elif temp == "2":
        tempcalcc()
    elif temp == "Exit":
        tempcalcexit()
    elif temp == "exit":
        tempcalcexit()
    else:
        print("Please select a valid option")
        tempcalc()
def discalc():
    print("")
    print("Which conversion do you need?")
    print("1. Feet to Meters")
    print("2. Meters to Feet")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    print("")
    imper = input(":")
    if imper == "1":
        discalcftm()
    elif imper == "2":
        discalcmtf()
    elif imper == "3":
        discalcmtk()
    elif imper == "4":
        discalcktm()
    elif imper == "Exit":
        discalcexit()
    elif imper == "exit":
        discalcexit()
    else:
        print("Please select a valid option")
        discalc()
def option1_3():
    print("option3 filler")
    option1()
def tempcalcf():
    while True: #error handling for strings
        try:
            temp1 = float(input("What is the temp in F: "))
            ftoc = float((temp1-32.00) * .5556)
            print("")
            print("%.2fF is equal to %.2fC" % (temp1, ftoc))
            print("")
            tempcalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def tempcalcc():
    while True:
        try:
            temp2 = float(input("What is the temp in C: "))
            ctof = float(temp2 * 1.8 +32)
            print("")
            print("%.2fC is equal to %.2fF" % (temp2, ctof))
            print("")
            tempcalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def tempcalcexit():
    print(">>>>>>>>Leaving Temp Conversion<<<<<<<<")
    option1()
def discalcftm():
    while True:
        try:
            feet = float(input("How many feet?:"))
            feet2 = float(feet / 3.281)
            print("")
            print("%.2f feet is equal to %.2f meters" % (feet, feet2))
            print("")
            discalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def discalcmtf():
    while True:
        try:
            meter = float(input("How many meters?:"))
            meter2 = float(meter * 3.281)
            print("")
            print("%.2f meters is equal to %.2f feet" % (meter, meter2))
            print("")
            discalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def discalcmtk():
    while True:
        try:
            mile = float(input("How many miles?:"))
            mile2 = float(mile * 1.609 )
            print("")
            print("%.2f miles is equal to %.2f kilometers" % (mile, mile2))
            print("")
            discalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def discalcktm():
    while True:
        try:
            kmeter = float(input("How many kilometers?:"))
            kmeter2 = float(kmeter / 1.609)
            print("")
            print("%.2f kilometers is equal to %.2f miles" % (kmeter, kmeter2))
            print("")
            discalc()
        except ValueError:
            print("That is not a valid number.... Try Again")
def discalcexit():
    print("")
    print(">>>>>>>>Leaving Imperial Conversion<<<<<<<<")
    print("")
    option1()
option1()
