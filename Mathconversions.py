#this thing does some conversions, this is the first actual app I've written in this language and the first since I nearly failed c++ in HS 10+ years ago
print("Welcome to my conversion calculator!")
print("Select from the following options")
print("1. Temp conversion")
print("2. Imperial distance conversion")
print("3. Kitchen measurements conversion")
print("Exit to exit this application")
print("")
option1 = input("Please Select one of the listed options: ")
while option1 != "Exit" and option1 != "exit":
    while option1 == "1":
        print("1. F to C")
        print("2. C to F")
        temp = input("Option?: ")
        if temp == "1":
            while True: #error handling for strings
                try:
                    temp1 = float(input("What is the temp in F: "))
                    ftoc = float((temp1-32.00) * .5556)
                    print("")
                    print("%.2fF is equal to %.2fC" % (temp1, ftoc))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif temp == "2":
            while True:
                try:
                    temp2 = float(input("What is the temp in C: "))
                    ctof = float(temp2 * 1.8 +32)
                    print("")
                    print("%.2fC is equal to %.2f" % (temp2, ctof))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif temp == "Exit":
            print("")
            print(">>>>>>>>Leaving Temp conversion<<<<<<<<")
            print("")
            option1 = "Exit"
        elif temp == "exit":
            print("")
            print(">>>>>>>>Leaving Temp conversion<<<<<<<<")
            print("")
            option1 = "Exit"
        else:
            print("Please select a valid option")
    while option1 == "2":
        print("Which conversion do you need?")
        print("1. Feet to Meters")
        print("2. Meters to Feet")
        print("3. Miles to Kilometers")
        print("4. Kilometers to Miles")
        imper = input("Option?:")
        if imper == "1":
            while True:
                try:
                    feet = float(input("How many feet?:"))
                    feet2 = float(feet / 3.281)
                    print("")
                    print("%.2f feet is equal to %.2f meters" % (feet, feet2))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif imper == "2":
            while True:
                try:
                    meter = float(input("How many meters?:"))
                    meter2 = float(meter * 3.281)
                    print("")
                    print("%.2f meters is equal to %.2f feet" % (meter, meter2))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif imper == "3":
            while True:
                try:
                    mile = float(input("How many miles?:"))
                    mile2 = float(mile * 1.609 )
                    print("")
                    print("%.2f miles is equal to %.2f kilometers" % (mile, mile2))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif imper == "4":
            while True:
                try:
                    kmeter = float(input("How many kilometers?:"))
                    kmeter2 = float(kmeter / 1.609)
                    print("")
                    print("%.2f kilometers is equal to %.2f miles" % (kmeter, kmeter2))
                    print("")
                    break
                except ValueError:
                    print("That is not a valid number.... Try Again")
        elif imper == "Exit":
            print("")
            print(">>>>>>>>Leaving Imperial Conversion<<<<<<<<")
            print("")
            option1 = "Exit"
        elif imper == "exit":
            print("")
            print(">>>>>>>>Leaving Imperial Conversion<<<<<<<<")
            print("")
            option1 = "Exit"
        else:
            print("Please select a valid option")    
    while option1 == "3":
        print("")
        print(">>>>>>>>This is still under development sorry!<<<<<<<<")
        print("")
        option1 = "Exit"
    else:
        print("Select from the following options")
        print("1. Temp conversion")
        print("2. Imperial distance conversion")
        print("3. Kitchen measurements conversion")
        print("Exit to exit this application")
        print("")
        option1 = input("Please Select one of the listed options: ")
