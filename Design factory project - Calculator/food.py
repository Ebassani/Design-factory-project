from audioop import mul
from multipliers import *



amountOfPortions = float(input("How many portions we're made"))

# SCHOOL INFORMATION -- FOOD

# WORKING
def meatMealProtein():
    meatAns = input("Which protein does the meal have? Fish, Pig, Cow, Chicken or Sausage?")
    if (meatAns == "Fish"):
        return fish
    elif (meatAns == "Pig"):
        return pig
    elif (meatAns == "Cow"):
        return cow
    elif (meatAns == "Chicken"):
        return chicken
    elif (meatAns == "Sausage"):
        return sausage
    return 0
meatMeal = meatMealProtein()



# WORKING
def veggieMealProtein():
    veggieAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")
    if (veggieAns == "Soygrits"):
        return soyGrits
    elif (veggieAns == "Tofu"):
        return tofu
    elif (veggieAns == "Vegetables"):
        return vegetables
    elif (veggieAns == "Broad bean"):
        return broadBean
    return 0
veggieMeal = veggieMealProtein()




def meatmealSide():
    meatMealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    if (meatMealSide == "Rice"):
        return rice
    elif (meatMealSide == "Pasta"):
        return pasta
    elif (meatMealSide == "Potato"):
        return potato
    elif (meatMealSide == "Vegetables"):
        return vegetables
    return 0
meatMealSide = meatmealSide()



def meatmealEgg():
    Egg = input("Does the meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return egg
    elif (Egg == "No"):
        return 0
meatMealEgg = meatmealEgg()



def meatmealDairy():
    Dairy = input ("Does the meal have cream? | Yes or No")
    if (Dairy == "Yes"):
        return cream
    elif (Dairy == "No"):
        return 0
meatMealDairy = meatmealDairy()



def Co2OfMeatMeal():
    Co2OfMeatMeal = amountOfPortions * (meatMeal + meatMealSide + meatMealEgg + meatMealDairy)
    return Co2OfMeatMeal
Co2OfMeat = Co2OfMeatMeal()


def veggiemealSide():
    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    if (veggiemealSide == "Rice"):
        return rice
    elif (veggiemealSide == "Pasta"):
        return pasta
    elif (veggiemealSide == "Potato"):
        return potato
    elif (veggiemealSide == "Vegetables"):
        return vegetables
    return 0
veggieMealSide = veggiemealSide()



def veggiemealEgg():
    Egg = input("Does the meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return egg
    elif (Egg == "No"):
        return 0

    return 0

veggieMealEgg = veggiemealEgg()



def veggiemealDairy():
    Dairy = input ("Does the meal have dairy products? | Yes or No")
    if (Dairy == "Yes"):
        return cream
    elif (Dairy == "No"):
        return 0
    
    return 0

veggieMealDairy = veggiemealDairy()



def Co2ofVeggieMeal():
    co2 = (float(amountOfPortions) * (veganMeal + veggieMealSide + veggieMealEgg) + veggieMealDairy)
    return co2

Co2OfVeggieMeal = Co2ofVeggieMeal()



def veganMealProtein():
    veganAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")
    if (veganAns == "Soygrits"):
        return soyGrits
    elif (veganAns == "Tofu"):
        return tofu
    elif (veganAns == "Vegetables"):
        return vegetables
    elif (veganAns == "Broad bean"):
        return broadBean
    return 0
veganMeal = veganMealProtein()


def veganmealSide():
    veganmeal = input("Choose the side of the meal. Rice, Pasta, Potato or Vegetables")
    if (veganmeal == "Rice"):
        return rice
    elif (veganmeal == "Pasta"):
        return pasta
    elif (veganmeal == "Potato"):
        return potato
    elif (veganmeal == "Vegetables"):
        return vegetables
veganMealSide = veganmealSide()
    

def Co2ofVeganMeal():
    return (float(amountOfPortions) * (veganMealSide + veganMeal))
Co2OfVeganMeal = Co2ofVeganMeal()

# WORKING
def dessert():

    pancake = float(amountOfPortions) * 0.206
    kisel = float(amountOfPortions) * 0.040
    return (float(amountOfPortions) * (pancake + kisel))

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
    amountKG = float(input("The amount of surplus in KG"))
    meat = (((meatMeal) /1000*170)/170)*1000*amountKG
    veggie = (((veggieMeal)/1000*170)/170)*1000*amountKG
    vegan = (((veganMeal)/1000*170)/170)*amountKG*1000
    sides = (((meatMealSide/1000*150)/150)+((veggieMealSide/1000*150)/150)+((veganMealSide)/1000*150)/150)/3*amountKG*1000
    salad = aPortionOfSalad / 150 * 1000 * amountKG
    bread = (ryeBread + wheatBread) / 2 * amountKG
    dessert = ((aPortionOfKisel + aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + float(sides) + salad + bread + dessert

# IN PROGRESS
def foodDistribution():
    costOfaMeal =  int(input("Cost of the meal in €"))
    meatMealsSold = int(input("The amount of meat meals sold"))
    veggieMealsSold = int(input("The amount of veggie meals sold"))
    veganMealsSold = int(input("The amount of vegan meals sold"))
    meat = meatMealsSold/costOfaMeal * (meatMealProtein + meatmealSide + meatmealEgg + meatmealDairy + multipliers.aPortionOfSalad + 1.5/1000*30)
    veggie = veggieMealsSold/costOfaMeal * (veggieMealProtein + veggiemealSide + veggiemealEgg + veggiemealDairy + multipliers.aPortionOfPancakes+1.5/1000*30)
    vegan = veganMealsSold/costOfaMeal *(veganMealProtein + veganmealSide +multipliers.aPortionOfSalad+1.5/1000*30)
    return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan

# IN PROGRESS
def electricity():
    amountofmealsCentral = int(input("How many meals we're made combined?"))
    amountOfMealsHeating = int(input("How many meals we're made combined?"))
    cookingAndCentralKitchen = multipliers.AverageElectricity * multipliers.PreparationAndCentralKitchenPerMeal*amountofmealsCentral
    cookingAndHeatingKitchen = multipliers.AverageElectricity * multipliers.PreparationAndHeatingKitchenPerMeal*amountOfMealsHeating
    return cookingAndCentralKitchen + cookingAndHeatingKitchen

# IN PROGRESS
def overview():
    cafeteriaConsumption = electricity
    surplusFoodCO2Footprint = surplusFood
    foodDistributionCO2Footprint = foodDistribution
    foodCO2Footprint = Co2OfMeatMeal + Co2ofVeggieMeal + veganmealSide + dessert + others
    return cafeteriaConsumption + surplusFoodCO2Footprint + foodDistributionCO2Footprint + foodCO2Footprint 
    
meatMealProtein()
meatmealSide()
meatmealEgg()
meatmealDairy()
Co2OfMeatMeal()
veggieMealProtein()
veggiemealSide()
veggiemealEgg()
veggiemealDairy()
Co2ofVeggieMeal
veganMealProtein()
veganmealSide()
dessert()
others()
surplusFood()
foodDistribution()
electricity()
overview()

#Food info - Personal

# WORKING
def drinks():
    water = int(amountOfPortions) * 0
    milk = int(amountOfPortions) * ((multipliers.milk/1000)*170)
    oatMilk = int(amountOfPortions) * ((multipliers.oatDrink/1000)*170)
    coffee = int(amountOfPortions) * ((multipliers.coffee/1000)*170)
    tea = int(amountOfPortions) * ((multipliers.tea/1000)*170)
    return water + milk + oatMilk + coffee + tea 

#Working
def others():
    ryeBreadEmission = float(amountOfPortions) * ((ryeBread/1000)*30)
    wheatBreademission = float(amountOfPortions) * ((wheatBread/1000)*30)
    saladEmission = float(amountOfPortions) * (aPortionOfSalad)
    return ryeBreadEmission + wheatBreademission + saladEmission
Others = others()

# Works when personallunch works
def foodWaste(ans):
    ans = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
    if ans:
        ans = "Not at all"
        return 0
    
    elif ans:
        ans = "Half a plate"
        return (personalLunch + drinks + others)/1.5

    elif ans:
        ans = "Over a half a plate"
        return (personalLunch + drinks + others)/2.5

    return 0

# Working
def proteins():
    fish = int(amountOfPortions) * ((multipliers.fish/1000)*170)
    cow = int(amountOfPortions) * ((multipliers.cow/1000)*170)
    pig = int(amountOfPortions) * ((multipliers.pig/1000)*170)
    chicken = int(amountOfPortions) * ((multipliers.chicken/1000)*170)
    sausage = int(amountOfPortions) * ((multipliers.sausage/1000)*170)
    soy = int(amountOfPortions) * (multipliers.soyGrits/1000*170)
    broadBean = int(amountOfPortions) * (multipliers.broadBean/1000*170)
    tofu = int(amountOfPortions) * (multipliers.tofu/1000*170)
    vegetables = int(amountOfPortions) * (multipliers.vegetables/1000*170)
    Egg = int(amountOfPortions) * (multipliers.egg/1000*60)
    cream = int(amountOfPortions) * (multipliers.cream/1000*60)
    proteinsTotal = fish + cow + pig + chicken + sausage + soy + broadBean + tofu + vegetables + Egg + cream
    return proteinsTotal

# Working
def carboHydrates():
    potato = int(amountOfPortions) * (multipliers.potato/1000*150)
    rice = int(amountOfPortions) * (multipliers.rice/1000*100)
    pasta = int(amountOfPortions) * (multipliers.pasta/1000*120)
    rootVegetables = int(amountOfPortions) * (multipliers.rootVegetables/1000*150)
    carboHydratesTotal = potato + rice + pasta + rootVegetables
    return carboHydratesTotal

# Working
def dessert(): 
    pancakes = float(amountOfPortions) * aPortionOfPancakes
    kisel = float(amountOfPortions) * aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal
Dessert = dessert()

#In progress (Cannot sum functions for some reason)
personalLunch = int(amountOfPortions) * (drinks() + carboHydrates() + dessert())
total = (personalLunch + drinks() + others() + foodWaste())




#Riku N