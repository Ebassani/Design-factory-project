import multipliers
amountOfPortions = input("How many portions we're made")

# SCHOOL INFORMATION -- FOOD

class meatmeal:

    meatMealProtein = input("Which protein does the meal have? Fish, Pig, Cow, Chicken or Sausage?")
    meatMealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    Co2OfMeatMeal = amountOfPortions * (meatMealProtein + meatMealSide + Egg + Dairy)

class veggiemeal:
    veggiemealProtein = input("Which protein does the meal have? Soybean, Tofu, vegetables or horse bean?")
    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    Co2OfVeggieMeal = amountOfPortions * (veggiemealProtein + veggiemealSide + Egg + Dairy)

class veganmeal:
    veganmealProtein = input("Which protein does the meal have? Soybean, Tofu, vegetables or horse bean?")
    veganmealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Co2OfVeganMeal = amountOfPortions * (veganmealProtein + veganmealSide)

class dessert:
    pancake = amountOfPortions * 0.206
    kisel = amountOfPortions * 0.040
    Co2OfDessert = amountOfPortions * (pancake + kisel)

class others:
    ryeBread = (amountOfPortions * 1.3/1000*30)
    wheatBread = (amountOfPortions * 1.7/1000*30)
    salad = amountOfPortions * 0.265
    Co2OfOthers = amountOfPortions * (ryeBread + wheatBread + salad)

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
    meat = "formula"
    veggie = "formula"
    vegan = "formula"

class electricity:
    cookingAndCentralKitchen = foodDistribution.amountOfMeals or foodDistribution.costOfaMeal + "formula"
    cookingAndHeatingKitchen =  foodDistribution.costOfaMeal or foodDistribution.amountOfMeals + "formula"

class overview:
    cafeteriaConsumption = electricity.cookingAndCentralKitchen + electricity.cookingAndHeatingKitchen
    surplusFoodCO2Footprint = surplusFood.meat + surplusFood.veggie + surplusFood.vegan + surplusFood.sides + surplusFood.salad + surplusFood.bread + surplusFood.dessert
    foodDistributionCO2Footprint = foodDistribution.meat + foodDistribution.veggie + foodDistribution.vegan
    foodCO2Footprint = meatmeal.Co2OfMeatMeal + veggiemeal.Co2OfVeggieMeal + veganmeal.Co2OfVeganMeal + dessert.Co2OfDessert + others.Co2OfOthers