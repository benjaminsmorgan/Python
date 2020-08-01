tspdict = {"tbsp" : .3334, "cup" : .0208333, "pint" : .01041666, "quart" : 0.0052083333} 
tbspdict = {"tsp" : 3, "cup" : .0625, "pint" : .03125, "quart" : .015625}
cupdict = {"tsp" : 48, "tbsp" : 16, "pint" : .5, "quart" : .25}
pintdict = {"tsp" : 96, "tbsp" : 32, "cup" : 2, "quart" : .5}
quartdict = {"tsp" : 192, "tbsp" : 64, "cup" : 4, "pint" : 2}
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
        volcalc()
    elif o1val == "Exit":
        import sysexit
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
def volcalc():
    print("")
    vol_1 = float(input("Enter starting volume:"))
    print("")
    print("1. Teaspoon")
    print("2. Tablespoon")
    print("3. Cup")
    print("4. Pint")
    print("5. Quart")
    #print("6. Gallons")
    #print("7. Pounds")
    print("10. Exit")
    vol_2 = input("Select the starting unit:")
    vol_3 = input("Select the end unit: ")
    if vol_2 == vol_3:
        print("Thats the same unit...")
        volcalc()
    elif vol_2 == "1":
        volcalctsp(vol_1, vol_2, vol_3)
    elif vol_2 == "2":
        volcalctbsp(vol_1, vol_2, vol_3)
    elif vol_2 == "3":
        volcalccup(vol_1, vol_2, vol_3)
    elif vol_2 == "4":
        volcalcpint(vol_1, vol_2, vol_3)
    elif vol_2 == "5":
        volcalcquart(vol_1, vol_2, vol_3)
    #elif vol_2 == "6":
        #volcalcgal(vol_1, vol_2, vol_3)
    #elif vol_2 == "7":
        #volcalclbs(vol_1, vol_2, vol_3)
    elif vol_2 == "exit":
        option1()
def volcalctsp(vol_1, vol_2, vol_3): #TSP to ALL
    if vol_3 == "2": #tablespoons
        x = tspdict.get("tbsp")
        y = (x * vol_1)
        print("%d Teaspoons is equal to %.2f Tablespoons" % (vol_1, y))
        volcalc()
    elif vol_3 == "3": #cups
        x = tspdict.get("cup")
        y = (x * vol_1)
        print("%d Teaspoons is equal to %.2f Cups" % (vol_1, y)) 
        volcalc()   
    elif vol_3 == "4": #pints
        x = tspdict.get("pint")
        y = (x * vol_1)
        print("%d Teaspoons is equal to %.2f pints" % (vol_1, y)) 
        volcalc()
    elif vol_3 == "5": #pints
        x = tspdict.get("quart")
        y = (x * vol_1)
        print("%d Teaspoons is equal to %.2f quarts" % (vol_1, y)) 
        volcalc() 
    else:
        print("A valid option was not selected")
        volcalc()            
def volcalctbsp(vol_1, vol_2, vol_3): #TBSP to ALL
    if vol_3 == "1": #teasspoon
        x = tbspdict.get("tsp")
        y = (x * vol_1)
        print("%d Tablespoons is equal to %.2f Teaspoons" % (vol_1, y))
        volcalc()
    elif vol_3 == "3": #cups
        x = tbspdict.get("cup")
        y = (x * vol_1)
        print("%d Tablespoons is equal to %.2f Cups" % (vol_1, y)) 
        volcalc()   
    elif vol_3 == "4": #pints
        x = tbspdict.get("pint")
        y = (x * vol_1)
        print("%d Tablespoons is equal to %.2f pints" % (vol_1, y)) 
        volcalc()
    elif vol_3 == "5": #pints
        x = tbspdict.get("quart")
        y = (x * vol_1)
        print("%d Tablespoons is equal to %.2f quarts" % (vol_1, y)) 
        volcalc() 
    else:
        print("A valid option was not selected")
        volcalc()        
def volcalccup(vol_1, vol_2, vol_3): #cup to ALL
    if vol_3 == "1": #teasspoon
        x = cupdict.get("tsp")
        y = (x * vol_1)
        print("%d Cups is equal to %.2f Teaspoons" % (vol_1, y))
        volcalc()
    elif vol_3 == "2": #tablespoons
        x = cupdict.get("tbsp")
        y = (x * vol_1)
        print("%d Cups is equal to %.2f Tablespoons" % (vol_1, y)) 
        volcalc()   
    elif vol_3 == "4": #pints
        x = cupdict.get("pint")
        y = (x * vol_1)
        print("%d Cups is equal to %.2f pints" % (vol_1, y)) 
        volcalc()
    elif vol_3 == "5": #quarts
        x = cupdict.get("quart")
        y = (x * vol_1)
        print("%d Cups is equal to %.2f quarts" % (vol_1, y)) 
        volcalc() 
    else:
        print("A valid option was not selected")
        volcalc()                 
def volcalcpint(vol_1, vol_2, vol_3): #pint to ALL
    if vol_3 == "1": #teasspoon
        x = pintdict.get("tsp")
        y = (x * vol_1)
        print("%d Pints is equal to %.2f Teaspoons" % (vol_1, y))
        volcalc()
    elif vol_3 == "2": #cupstablespoons
        x = pintdict.get("tbsp")
        y = (x * vol_1)
        print("%d Pints is equal to %.2f Tablespoons" % (vol_1, y)) 
        volcalc()   
    elif vol_3 == "3": #cups
        x = pintdict.get("cup")
        y = (x * vol_1)
        print("%d Pints is equal to %.2f Cups" % (vol_1, y)) 
        volcalc()
    elif vol_3 == "5": #quarts
        x = pintdict.get("quart")
        y = (x * vol_1)
        print("%d Pints is equal to %.2f quarts" % (vol_1, y)) 
        volcalc() 
    else:
        print("A valid option was not selected")
        volcalc()             
def volcalcquart(vol_1, vol_2, vol_3): #quart to ALL
    if vol_3 == "1": #teasspoon
        x = quartdict.get("tsp")
        y = (x * vol_1)
        print("%d Quarts is equal to %.2f Teaspoons" % (vol_1, y))
        volcalc()
    elif vol_3 == "2": #cupstablespoons
        x = quartdict.get("tbsp")
        y = (x * vol_1)
        print("%d Quarts is equal to %.2f Tablespoons" % (vol_1, y)) 
        volcalc()   
    elif vol_3 == "3": #cups
        x = quartdict.get("cup")
        y = (x * vol_1)
        print("%d Quarts is equal to %.2f Cups" % (vol_1, y)) 
        volcalc()
    elif vol_3 == "4": #quarts
        print(quartdict.get("pint")*vol_1)
        volcalc() 
    else:
        print("A valid option was not selected")
        volcalc()                    
def volcalcexit():
    print(">>>>>>>>Leaving Volume Conversion<<<<<<<<")
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