from audioop import mul
import multipliers



amountOfPortions = input("How many portions we're made")

# SCHOOL INFORMATION -- FOOD

# WORKING
def meatMealProtein():

    meatAns = input("Which protein does the meal have? Fish, Pig, Cow, Chicken or Sausage?")

    if (meatAns == "Fish"):
        return multipliers.fish
    elif (meatAns == "Pig"):
        return multipliers.pig
    elif (meatAns == "Cow"):
        return multipliers.cow
    elif (meatAns == "Chicken"):
        return multipliers.chicken
    elif (meatAns == "Sausage"):
        return multipliers.sausage
# WORKING
def veggieMealProtein():

    veggieAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veggieAns == "Soygrits"):
        return multipliers.soyGrits
    elif (veggieAns == "Tofu"):
        return multipliers.tofu
    elif (veggieAns == "Vegetables"):
        return multipliers.vegetables
    elif (veggieAns == "Broad bean"):
        return multipliers.broadBean
# WORKING
def veganMealProtein():

    veganAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veganAns == "Soygrits"):
        return multipliers.soyGrits
    elif (veganAns == "Tofu"):
        return multipliers.tofu
    elif (veganAns == "Vegetables"):
        return multipliers.vegetables
    elif (veganAns == "Broad bean"):
        return multipliers.broadBean


#Needs A LOOP. Currently only runs meatmealside variable. Same thing will be done to functions veggiemeal and veganmeal
def meatmeal():
    
    meatMealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    
    if (meatMealSide == "Rice"):
        return multipliers.rice
    elif (meatMealSide == "Pasta"):
        return multipliers.pasta
    elif (meatMealSide == "Potato"):
        return multipliers.potato
    elif (meatMealSide == "Vegetables"):
        return multipliers.vegetables

    Egg = input("Does the meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return multipliers.egg
    elif (Egg == "No"):
        return 0

    Dairy = input ("Does the meal have cream? | Yes or No")
    if (Dairy == "Yes"):
        return multipliers.cream
    elif (Dairy == "No"):
        return 0

    Co2OfMeatMeal = amountOfPortions * (meatMealProtein + meatMealSide + Egg + Dairy)
    return Co2OfMeatMeal

# Needs a loop
def veggiemeal():

    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    Co2OfVeggieMeal = (amountOfPortions * (veggieMealProtein + veggiemealSide + Egg + Dairy))
    return Co2OfVeggieMeal

# In progress
def veganmeal():
   
    veganmealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    return (amountOfPortions * (veganMealProtein + veganmealSide))

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
    amountKG = input("The amount of surplus in KG")
    meat = (((meatMealProtein) /1000*170)/170)*1000*amountKG
    veggie = (((veggieMealProtein)/1000*170)/170)*1000*amountKG
    vegan = (((veganMealProtein)/1000*170)/170)*amountKG*1000
    sides = amountKG #=((=VLOOKUP(E8,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E14,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E20,Kertoimet!B145:C148,2,FALSE)/1000*150)/150)/3*amountKG*1000
    salad = multipliers.aPortionOfSalad / 150 * 1000 * amountKG
    bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
    dessert = ((multipliers.aPortionOfKisel + multipliers.aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + sides + salad + bread + dessert

# IN PROGRESS
def foodDistribution():
    costOfaMeal =  str(input("Cost of the meal in €"))
    meatMealsSold = str(input("The amount of meat meals sold"))
    veggieMealsSold = str(input("The amount of veggie meals sold"))
    veganMealsSold = str(input("The amount of vegan meals sold"))
    meat = meatMealsSold/costOfaMeal #* (F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30),J19*(F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30))
    veggie = veggieMealsSold/costOfaMeal #* (F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30),J22*(F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30))
    vegan = veganMealsSold/costOfaMeal #*(F19+F20+Kertoimet!C178+1.5/1000*30),J25*(F19+F20+Kertoimet!C178+1.5/1000*30))
    return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan

# IN PROGRESS
def electricity():
    cookingAndCentralKitchen = foodDistribution.amountOfMeals or foodDistribution.costOfaMeal + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C82*I30,Kertoimet!C56*Kertoimet!C82*I30)
    cookingAndHeatingKitchen =  foodDistribution.costOfaMeal or foodDistribution.amountOfMeals + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C83*I31,Kertoimet!C56*Kertoimet!C83*I31)
    return cookingAndCentralKitchen + cookingAndHeatingKitchen

# IN PROGRESS
def overview():
    cafeteriaConsumption = electricity.cookingAndCentralKitchen + electricity.cookingAndHeatingKitchen
    surplusFoodCO2Footprint = surplusFood.meat + surplusFood.veggie + surplusFood.vegan + surplusFood.sides + surplusFood.salad + surplusFood.bread + surplusFood.dessert
    foodDistributionCO2Footprint = foodDistribution.meat + foodDistribution.veggie + foodDistribution.vegan
    foodCO2Footprint = meatmeal.Co2OfMeatMeal + veggiemeal.Co2OfVeggieMeal + veganmeal.Co2OfVeganMeal + dessert.Co2OfDessert + others.Co2OfOthers
    return cafeteriaConsumption + surplusFoodCO2Footprint + foodDistributionCO2Footprint + foodCO2Footprint 
    
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
    ryeBread = int(amountOfPortions) * ((multipliers.ryeBread/1000)*30)
    wheatBread = int(amountOfPortions) * ((multipliers.wheatBread/1000)*30)
    salad = int(amountOfPortions) * (multipliers.aPortionOfSalad)
    return ryeBread + wheatBread + salad

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
    pancakes = int(amountOfPortions) * multipliers.aPortionOfPancakes
    kisel = int(amountOfPortions) * multipliers.aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal

#In progress (Cannot sum functions for some reason)
personalLunch = amountOfPortions * (drinks + carboHydrates + dessert)
total = (personalLunch + drinks + others + foodWaste)