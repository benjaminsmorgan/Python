dictdict = {1 : {2 : .3334, 3 : .0208333, 4 : .01041666, 5 : 0.0052083333}, #teaspoons to tbsp, cups, pints, quarts
            2 : {1 : 3, 3 : .0625, 4 : .03125, 5 : .015625}, #tbsps to otheres
            3 : {1 : 48, 2 : 16, 4 : .5, 5 : .25}, #cups to others
            4 : {1 : 96, 2 : 32, 3 : 2, 5 : .5}, #pints to others
            5 : {1 : 192, 2 : 64, 3 : 4, 4 : 2}} #quarts to others
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
    vol_2 = int(input("Select the starting unit:"))
    vol_3 = int(input("Select the end unit: "))
    if vol_2 != vol_3:
        x = dictdict[vol_2][vol_3]
        print(x * vol_1)
        volcalc()
    else:
        print("Thats the same unit")
        volcalc()
volcalc()