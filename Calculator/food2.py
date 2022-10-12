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
        return float(0)
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
    ryeBread = (float(amountOfPortions) * 1.3/1000*30)
    wheatBread = (float(amountOfPortions) * 1.7/1000*30)
    salad = float(amountOfPortions) * 0.265
    return (float(amountOfPortions) * (ryeBread + wheatBread + salad))

#The next couple classes use complicated formulas in excel which I have no motivation to do right now because they look like hell on earth :DDDDDD
#Includes surplusfood foodDistribution and electricity

# IN PROGRESS
def surplusFood():
    amountKG = float(input("The amount of surplus in KG"))
    meat = (((meatMeal) /1000*170)/170)*1000*amountKG
    veggie = (((veggieMeal)/1000*170)/170)*1000*amountKG
    vegan = (((veganMeal)/1000*170)/170)*amountKG*1000
    sides = float((((meatMealSide/1000*150)/150)+((veggieMealSide/1000*150)/150)+((veganMealSide)/1000*150)/150)/3*amountKG*1000)
    salad = aPortionOfSalad / 150 * 1000 * amountKG
    bread = (ryeBread + wheatBread) / 2 * amountKG
    dessert = ((aPortionOfKisel + aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + float(sides) + salad + bread + dessert
SurplusFood = surplusFood()

# IN PROGRESS
def foodDistribution():
    costOfaMeal =  float(input("Cost of the meal in €"))
    meatMealsSold = float(input("The amount of meat meals sold"))
    veggieMealsSold = float(input("The amount of veggie meals sold"))
    veganMealsSold = float(input("The amount of vegan meals sold"))
    meat = float(meatMealsSold/costOfaMeal * (meatMeal + meatMealSide + meatMealEgg + meatMealDairy + aPortionOfSalad + 1.5/1000*30))
    veggie = veggieMealsSold/costOfaMeal * (veggieMeal + veggieMealSide + veggieMealEgg + veggieMealDairy + aPortionOfPancakes+1.5/1000*30)
    vegan = veganMealsSold/costOfaMeal *(veganMeal + veganMealSide +aPortionOfSalad+1.5/1000*30)
    return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan
FoodDistribution = foodDistribution()

# IN PROGRESS
def electricity():
    amountofmealsCentral = float(input("How many meals we're made combined?"))
    amountOfMealsHeating = float(input("How many meals we're made combined?"))
    cookingAndCentralKitchen = averageElectricity * PreparationAndCentralKitchenPerMeal * amountofmealsCentral
    cookingAndHeatingKitchen = averageElectricity * PreparationAndHeatingKitchenPerMeal * amountOfMealsHeating
    return cookingAndCentralKitchen + cookingAndHeatingKitchen
Electricity = electricity()


# IN PROGRESS
def overview():
    cafeteriaConsumption = Electricity
    surplusFoodCO2Footprint = SurplusFood
    foodDistributionCO2Footprint = FoodDistribution
    foodCO2Footprint = Co2OfMeat + Co2OfVeggieMeal + veganMealSide + Dessert + Others
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
    water1 = float(amountOfPortions) * 0
    milk1 = float(amountOfPortions) * ((milk/1000)*170)
    oatMilk1 = float(amountOfPortions) * ((oatDrink/1000)*170)
    coffee1 = float(amountOfPortions) * ((coffee/1000)*170)
    tea1 = float(amountOfPortions) * ((tea/1000)*170)
    return water1 + milk1 + oatMilk1 + coffee1 + tea1 
Drinks = drinks()

#Working
def others():
    ryeBreadEmission = float(amountOfPortions) * ((ryeBread/1000)*30)
    wheatBreademission = float(amountOfPortions) * ((wheatBread/1000)*30)
    saladEmission = float(amountOfPortions) * (aPortionOfSalad)
    return ryeBreadEmission + wheatBreademission + saladEmission
Others = others()

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
    pancakes = float(amountOfPortions) * aPortionOfPancakes
    kisel = float(amountOfPortions) * aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal
Dessert = dessert()

#In progress (Cannot sum functions for some reason)
personalLunch = float(amountOfPortions) * (Drinks + Carbohydrates + Dessert)
total = (personalLunch + Drinks + Others + FoodWaste)




#Riku N