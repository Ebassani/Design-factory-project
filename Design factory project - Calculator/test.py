import multipliers


#test environment where you can test the features of the code
#keep this file empty :)
amountOfPortions = input("How many portions of the food was made?")

def surplusFood():
    amountKG = input("The amount of surplus in KG")
    meat = (((meatMealProtein) /1000*170)/170)*1000*amountKG
    veggie = (((veggieMealProtein)/1000*170)/170)*1000*amountKG
    vegan = (((veganMealProtein)/1000*170)/170)*amountKG*1000
    sides = amountKG #=((=VLOOKUP(E8,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E14,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E20,Kertoimet!B145:C148,2,FALSE)/1000*150)/150)/3*amountKG*1000
    salad = multipliers.aPortionOfSalad / 150 * 1000 * amountKG
    bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
    dessert = ((multipliers.PortionOfKisel + multipliers.aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + sides + salad + bread + dessert