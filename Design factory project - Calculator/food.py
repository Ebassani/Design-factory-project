import multipliers
amountOfPortions = input("How many portions we're made")

class meatmeal:

    meatMealProtein = input("Which protein does the meal have? Fish, Pig, Cow, Chicken or Sausage?")
    meatMealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    Co2OfMeatMeal = amountOfPortions*(meatMealProtein+meatMealSide+Egg+Dairy)

class veggiemeal:
    veggiemealProtein = input("Which protein does the meal have? Soybean, Tofu, vegetables or horse bean?")
    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")

class veganmeal:
    veganmealProtein = input("Which protein does the meal have? Soybean, Tofu, vegetables or horse bean?")
    veganmealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")

class dessert:
    pancake = amountOfPortions# + pancakes from multipliers
    kisel = amountOfPortions# + kisel from multipliers

class others:
    ryeBread = amountOfPortions# + ryebread from multipliers/1000*30
    wheatBread = amountOfPortions# + wheatBread from multipliers/1000*30
    salad = amountOfPortions# + salad from multipliers

#The next couple classes use complicated formulas in excel which I have no motivation to do right now because they look like hell on earth :DDDDDD
#Includes surplusfood foodDistribution and electricity

class surplusFood:
    amountKG = input("The amount of surplus in KG")
    meat = amountKG 
    veggie = amountKG
    vegan = amountKG
    sides = amountKG
    salad = amountKG
    bread = amountKG
    dessert = amountKG

class foodDistribution:
    costOfaMeal =  input("Cost of the meal in €")
    amountOfMeals = input("The amount of meals sold")
    #meat = formula
    #veggie = formula
    #vegan = formula

#class electricity:
    #cookingAndCentralKitchen = amountOfMeals or costOfaMeal + formula
    #cookingAndHeatingKitchen =  costOfaMeal or amountOfMeals + formula

