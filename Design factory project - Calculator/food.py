from audioop import mul
import multipliers



amountOfPortions = input("How many portions we're made")

# SCHOOL INFORMATION -- FOOD

def meatMealProtein(meatAns):

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

def veggieMealProtein(veggieAns):

    veggieAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veggieAns == "Soygrits"):
        return multipliers.soyGrits
    elif (veggieAns == "Tofu"):
        return multipliers.tofu
    elif (veggieAns == "Vegetables"):
        return multipliers.vegetables
    elif (veggieAns == "Broad bean"):
        return multipliers.broadBean

def veganMealProtein(veganAns):

    veganAns = input("Which protein does the meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if (veganAns == "Soygrits"):
        return multipliers.soyGrits
    elif (veganAns == "Tofu"):
        return multipliers.tofu
    elif (veganAns == "Vegetables"):
        return multipliers.vegetables
    elif (veganAns == "Broad bean"):
        return multipliers.broadBean



def meatmeal():

    meatMealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    Co2OfMeatMeal = amountOfPortions * (meatMealProtein + meatMealSide + Egg + Dairy)
    return Co2OfMeatMeal

def veggiemeal():

    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    Egg = input("Does the meal have eggs?")
    Dairy = input ("Does the meal have dairy products?")
    return (amountOfPortions * (veggiemealProtein + veggiemealSide + Egg + Dairy))

def veganmeal():
   
    veganmealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    return (amountOfPortions * (veganmealProtein + veganmealSide))

def dessert():
    pancake = amountOfPortions * 0.206
    kisel = amountOfPortions * 0.040
    return (amountOfPortions * (pancake + kisel))

def others():
    ryeBread = (amountOfPortions * 1.3/1000*30)
    wheatBread = (amountOfPortions * 1.7/1000*30)
    salad = amountOfPortions * 0.265
    return (amountOfPortions * (ryeBread + wheatBread + salad))

#The next couple classes use complicated formulas in excel which I have no motivation to do right now because they look like hell on earth :DDDDDD
#Includes surplusfood foodDistribution and electricity

def surplusFood():
    amountKG = input("The amount of surplus in KG")
    meat = (((meatMealProtein) /1000*170)/170)*1000*amountKG
    veggie = (((veggiemealProtein)/1000*170)/170)*1000*amountKG
    vegan = (((veganmealProtein)/1000*170)/170)*amountKG*1000
    sides = amountKG #=((=VLOOKUP(E8,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E14,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E20,Kertoimet!B145:C148,2,FALSE)/1000*150)/150)/3*amountKG*1000
    salad = multipliers.aPortionOfSalad / 150 * 1000 * amountKG
    bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
    dessert = ((multipliers.PortionOfKisel + multipliers.aPortionOfPancakes)/2)/150*1000*amountKG
    return meat + veggie + vegan + sides + salad + bread + dessert

def foodDistribution():
    costOfaMeal =  str(input("Cost of the meal in €"))
    meatMealsSold = str(input("The amount of meat meals sold"))
    veggieMealsSold = str(input("The amount of veggie meals sold"))
    veganMealsSold = str(input("The amount of vegan meals sold"))
    meat = meatMealsSold/costOfaMeal #* (F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30),J19*(F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30))
    veggie = veggieMealsSold/costOfaMeal #* (F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30),J22*(F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30))
    vegan = veganMealsSold/costOfaMeal #*(F19+F20+Kertoimet!C178+1.5/1000*30),J25*(F19+F20+Kertoimet!C178+1.5/1000*30))
    return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan

def electricity():
    cookingAndCentralKitchen = foodDistribution.amountOfMeals or foodDistribution.costOfaMeal + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C82*I30,Kertoimet!C56*Kertoimet!C82*I30)
    cookingAndHeatingKitchen =  foodDistribution.costOfaMeal or foodDistribution.amountOfMeals + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C83*I31,Kertoimet!C56*Kertoimet!C83*I31)
    return cookingAndCentralKitchen + cookingAndHeatingKitchen

def overview():
    cafeteriaConsumption = electricity.cookingAndCentralKitchen + electricity.cookingAndHeatingKitchen
    surplusFoodCO2Footprint = surplusFood.meat + surplusFood.veggie + surplusFood.vegan + surplusFood.sides + surplusFood.salad + surplusFood.bread + surplusFood.dessert
    foodDistributionCO2Footprint = foodDistribution.meat + foodDistribution.veggie + foodDistribution.vegan
    foodCO2Footprint = meatmeal.Co2OfMeatMeal + veggiemeal.Co2OfVeggieMeal + veganmeal.Co2OfVeganMeal + dessert.Co2OfDessert + others.Co2OfOthers
    return cafeteriaConsumption + surplusFoodCO2Footprint + foodDistributionCO2Footprint + foodCO2Footprint 
    
#Food info - Personal


def drinks():
    water = amountOfPortions * 0
    milk = amountOfPortions * ((multipliers.milk/1000)*170)
    oatMilk = amountOfPortions * ((multipliers.oatDrink/1000)*170)
    coffee = amountOfPortions * ((multipliers.coffee/1000)*170)
    tea = amountOfPortions * ((multipliers.tea/1000)*170)
    return water + milk + oatMilk + coffee + tea 

def others():
    ryeBread = amountOfPortions * ((multipliers.ryeBread/1000)*30)
    wheatBread = amountOfPortions * ((multipliers.wheatBread/1000)*30)
    salad = amountOfPortions * multipliers.salad

    return ryeBread + wheatBread + salad

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

def proteins():
    fish = amountOfPortions * ((multipliers.fish/1000)*170)
    cow = amountOfPortions * ((multipliers.cow/1000)*170)
    pig = amountOfPortions * ((multipliers.pig/1000)*170)
    chicken = amountOfPortions * ((multipliers.chicken/1000)*170)
    sausage = amountOfPortions * ((multipliers.sausage/1000)*170)
    soy = amountOfPortions * (multipliers.soyGrits/1000*170)
    broadBean = amountOfPortions * (multipliers.broadBean/1000*170)
    tofu = amountOfPortions * (multipliers.tofu/1000*170)
    vegetables = amountOfPortions * (multipliers.vegetables/1000*170)
    Egg = amountOfPortions * (multipliers.egg/1000*60)
    cream = amountOfPortions * (multipliers.cream/1000*60)
    return fish + cow + pig + chicken + sausage + soy + broadBean + tofu + vegetables + Egg + cream

def carboHydrates():
    potato = amountOfPortions * (multipliers.potato/1000*150)
    rice = amountOfPortions * (multipliers.rice/1000*100)
    pasta = amountOfPortions * (multipliers.pasta/1000*120)
    rootVegetables = amountOfPortions * (multipliers.rootVegetables/1000*150)
    return potato + rice + pasta + rootVegetables

def dessert(): 
    pancakes = amountOfPortions * multipliers.pancakes
    kisel = amountOfPortions * multipliers.kisel
    return pancakes + kisel

personalLunch = amountOfPortions * (proteins + carboHydrates + dessert)
total = (personalLunch + drinks + others + foodWaste)