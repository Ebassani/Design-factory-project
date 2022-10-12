from audioop import mul
import Calculator.multipliers
from Calculator import multipliers

amountOfPortions = float(input("How many portions we're made"))

# SCHOOL INFORMATION -- FOOD

# WORKING
def meatMealProtein():

    meatAns = input("Which protein does the meat meal have? Fish, Pig, Cow, Chicken or Sausage?")

    if (meatAns == "Fish"):
        return ((multipliers.fish)/1000*170)
    elif (meatAns == "Pig"):
        return ((multipliers.pig)/1000*170)
    elif (meatAns == "Cow"):
        return ((multipliers.cow)/1000*170)
    elif (meatAns == "Chicken"):
        return ((multipliers.chicken)/1000*170)
    elif (meatAns == "Sausage"):
        return ((multipliers.sausage)/1000*170)

    return 0
# WORKING
def veggieMealProtein():

    veggieAns = input("Which protein does the veggie meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veggieAns == "Soygrits"):
        return ((multipliers.soyGrits)/1000*170)
    elif (veggieAns == "Tofu"):
        return ((multipliers.tofu)/1000*170)
    elif (veggieAns == "Vegetables"):
        return ((multipliers.vegetables)/1000*170)
    elif (veggieAns == "Broad bean"):
        return ((multipliers.broadBean)/1000*170)
    
    return 0
# WORKING


def meatmealSide():
    
    meatMealSide = input("Choose the side of the meat meal. Rice, pasta, potato or vegetables")
    
    if (meatMealSide == "Rice"):
        return ((multipliers.rice)/1000*150)
    elif (meatMealSide == "Pasta"):
        return ((multipliers.pasta)/1000*150)
    elif (meatMealSide == "Potato"):
        return ((multipliers.potato)/1000*150)
    elif (meatMealSide == "Vegetables"):
        return ((multipliers.vegetables)/1000*150)
    
    return 0

def meatmealEgg():
    Egg = input("Does the meat meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return ((multipliers.egg)/1000*105)
    elif (Egg == "No"):
        return 0

def meatmealDairy():

    Dairy = input ("Does the meat meal have cream? | Yes or No")
    if (Dairy == "Yes"):
        return ((multipliers.cream)/1000*105)
    elif (Dairy == "No"):
        return 0

def Co2OfMeatMeal():
    Co2OfMeatMeal = amountOfPortions * (meatMealProtein() + meatmealSide() + meatmealEgg() + meatmealDairy())
    return Co2OfMeatMeal


def veggiemealSide():

    veggiemealSide = input("Choose the side of the veggie meal. Rice, pasta, potato or vegetables")
    if (veggiemealSide == "Rice"):
        return ((multipliers.rice)/1000*150)
    elif (veggiemealSide == "Pasta"):
        return ((multipliers.pasta)/1000*150)
    elif (veggiemealSide == "Potato"):
        return ((multipliers.potato)/1000*150)
    elif (veggiemealSide == "Vegetables"):
        return ((multipliers.vegetables)/1000*150)

    return 0
def veggiemealEgg():
    Egg = input("Does the veggie meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return ((multipliers.egg)/1000*105)
    elif (Egg == "No"):
        return 0

    return 0

def veggiemealDairy():
    Dairy = input ("Does the veggie meal have dairy products? | Yes or No")
    if (Dairy == "Yes"):
        return ((multipliers.cream)/1000*105)
    elif (Dairy == "No"):
        return 0
    
    return 0

def Co2ofVeggieMeal():
    co2 = (int(amountOfPortions) * (veggieMealProtein() + veggiemealSide() + veggiemealEgg()) + veggiemealDairy())
    return co2

def veganMealProtein():

    veganAns = input("Which protein does the vegan meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veganAns == "Soygrits"):
        return ((multipliers.soyGrits)/1000*170)
    elif (veganAns == "Tofu"):
        return ((multipliers.tofu)/1000*170)
    elif (veganAns == "Vegetables"):
        return ((multipliers.vegetables)/1000*170)
    elif (veganAns == "Broad bean"):
        return ((multipliers.broadBean)/1000*170)

    return 0

def veganmealSide():
   
    veganmeal = input("Choose the side of the vegan meal. Rice, Pasta, Potato or Vegetables")
    if (veganmeal == "Rice"):
        return ((multipliers.rice)/1000*170)
    elif (veganmeal == "Pasta"):
        return ((multipliers.pasta)/1000*170)
    elif (veganmeal == "Potato"):
        return ((multipliers.potato)/1000*170)
    elif (veganmeal == "Vegetables"):
        return ((multipliers.vegetables)/1000*170)
    
def Co2OfVeganMeal():
      return (int(amountOfPortions) * (veganmealSide() + veganMealProtein()))

# WORKING
def dessert():

    pancake = int(amountOfPortions) * 0.206
    kisel = int(amountOfPortions) * 0.040
    return (int(amountOfPortions) * (pancake + kisel))

# WORKING
def others():
    
    ryeBread = (int(amountOfPortions) * 1.3/1000*30)
    wheatBread = (int(amountOfPortions) * 1.7/1000*30)
    salad = int(amountOfPortions) * 0.265
    return (int(amountOfPortions) * (ryeBread + wheatBread + salad))


#The next couple classes use complicated formulas in excel which I have no motivation to do right now because they look like hell on earth :DDDDDD
#Includes surplusfood foodDistribution and electricity


# IN PROGRESS
def surplusFood():
    print ("Information for calculating surplusfood")
    amountKG = int(input("The amount of surplus in KG"))
    meat = (((meatMealProtein()) /1000*170)/170)*1000*amountKG
    veggie = (((veggieMealProtein())/1000*170)/170)*1000*amountKG
    vegan = (((veganMealProtein())/1000*170)/170)*amountKG*1000
    sides = (((meatmealSide()/1000*150)/150)+((veggiemealSide()/1000*150)/150)+((veganmealSide())/1000*150)/150)/3*amountKG*1000
    salad = (multipliers.aPortionOfSalad) / 150 * 1000 * amountKG
    bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
    dessert = ((multipliers.aPortionOfKisel + multipliers.aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + sides + salad + bread + dessert

# IN PROGRESS
def foodDistribution():
    print("Information to calculate food distribution")
    costOfaMeal =  int(input("Cost of the meal in €"))
    meatMealsSold = int(input("The amount of meat meals sold"))
    veggieMealsSold = int(input("The amount of veggie meals sold"))
    veganMealsSold = int(input("The amount of vegan meals sold"))
    meat = meatMealsSold/costOfaMeal * ((meatMealProtein() + meatmealSide() + meatmealEgg() + meatmealDairy() + multipliers.aPortionOfSalad) + 1.5/1000*30)
    veggie = veggieMealsSold/costOfaMeal * ((veggieMealProtein() + veggiemealSide() + veggiemealEgg() + veggiemealDairy() + multipliers.aPortionOfPancakes) + 1.5 / 1000 * 30)
    vegan = veganMealsSold/costOfaMeal * ((veganMealProtein() + veganmealSide() + multipliers.aPortionOfSalad) + 1.5 / 1000 * 30)
    return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan

# IN PROGRESScs
def electricity():
    print("Information to calculate electricity")
    amountofmealsCentral = int(input("How many meals we're made in central and heating kitchen combined?"))
    amountOfMealsHeating = int(input("How many meals we're made in preparation and heating kitchen combined?"))
    cookingAndCentralKitchen = multipliers.AverageElectricity * multipliers.PreparationAndCentralKitchenPerMeal*amountofmealsCentral
    cookingAndHeatingKitchen = multipliers.AverageElectricity * multipliers.PreparationAndHeatingKitchenPerMeal*amountOfMealsHeating
    return cookingAndCentralKitchen + cookingAndHeatingKitchen

# IN PROGRESS
def overview():
    cafeteriaConsumption = electricity()
    surplusFoodCO2Footprint = surplusFood()
    foodDistributionCO2Footprint = foodDistribution()
    foodCO2Footprint = (Co2OfMeatMeal() + Co2ofVeggieMeal() + veganmealSide() + dessert() + others())
    return cafeteriaConsumption + surplusFoodCO2Footprint + foodDistributionCO2Footprint + foodCO2Footprint 
    
#Food info - Personal

# WORKING
def drinks():
    water1 = float(amountOfPortions) * 0
    milk1 = float(amountOfPortions) * ((milk/1000)*170)
    oatMilk1 = float(amountOfPortions) * ((oatDrink/1000)*170)
    coffee1 = float(amountOfPortions) * ((coffee/1000)*170)
    tea1 = float(amountOfPortions) * ((tea/1000)*170)
    return water1 + milk1 + oatMilk1 + coffee1 + tea1 
Drinks = drinks()

#Working
def others():
    ryeBread = int(amountOfPortions) * ((multipliers.ryeBread/1000)*30)
    wheatBread = int(amountOfPortions) * ((multipliers.wheatBread/1000)*30)
    salad = int(amountOfPortions) * (multipliers.aPortionOfSalad)
    return ryeBread + wheatBread + salad

# Works when personallunch works

def foodWaste():
    ans = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
    if (ans == "Not at all"):
        return 0
    elif (ans == "Half a plate"):
        return (personalLunch + Drinks + Others)/1.5
    elif (ans == "Over a half a plate"):
        return (personalLunch + Drinks + Others)/2.5
FoodWaste = foodWaste()

def foodWaste():
    answer = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
    if answer:
        answer = "Not at all"
        return 0
    
    elif answer:
        answer = "Half a plate"
        return (personalLunch + drinks + others)/1.5

    elif answer:
        answer = "Over a half a plate"
        return (personalLunch + drinks + others)/2.5

    return 0


# Working
def proteins():
    fish1 = float(amountOfPortions) * ((fish/1000)*170)
    cow1 = float(amountOfPortions) * ((cow/1000)*170)
    pig1 = float(amountOfPortions) * ((pig/1000)*170)
    chicken1 = float(amountOfPortions) * ((chicken/1000)*170)
    sausage1 = float(amountOfPortions) * ((sausage/1000)*170)
    soy1 = float(amountOfPortions) * (soyGrits/1000*170)
    broadBean1 = float(amountOfPortions) * (broadBean/1000*170)
    tofu1 = float(amountOfPortions) * (tofu/1000*170)
    vegetables1 = float(amountOfPortions) * (vegetables/1000*170)
    Egg1 = float(amountOfPortions) * (egg/1000*60)
    cream1 = float(amountOfPortions) * (cream/1000*60)
    proteinsTotal = fish1 + cow1 + pig1 + chicken1 + sausage1 + soy1 + broadBean1 + tofu1 + vegetables1 + Egg1 + cream1
    return proteinsTotal
Proteins = proteins()

# Working
def carboHydrates():
    potato1 = float(amountOfPortions) * (potato/1000*150)
    rice1 = float(amountOfPortions) * (rice/1000*100)
    pasta1 = float(amountOfPortions) * (pasta/1000*120)
    rootVegetables1 = float(amountOfPortions) * (rootVegetables/1000*150)
    carboHydratesTotal = potato1 + rice1 + pasta1 + rootVegetables1
    return carboHydratesTotal
Carbohydrates = carboHydrates()

# Working
def dessert(): 
    pancakes = int(amountOfPortions) * multipliers.aPortionOfPancakes
    kisel = int(amountOfPortions) * multipliers.aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal

#In progress (Cannot sum functions for some reason)

personalLunch = float(amountOfPortions) * (Drinks + Carbohydrates + Dessert)
total = (personalLunch + Drinks + Others + FoodWaste)

#personalLunch = int(amountOfPortions) * (drinks() + carboHydrates() + dessert())
#total = (personalLunch + drinks() + others() + foodWaste())





#Riku N
