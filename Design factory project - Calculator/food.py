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
    meat = amountKG #=(=VLOOKUP(E7,Kertoimet!B126:C130,2,FALSE)/1000*170)/170)*1000*amountKG
    veggie = amountKG #=(=VLOOKUP(E13,Kertoimet!B133:C136,2,FALSE)/1000*170)/170)*amountKG*1000
    vegan = amountKG #=(=VLOOKUP(E19,Kertoimet!B133:C136,2,FALSE)/1000*170)/170)*amountKG*1000
    sides = amountKG #=((=VLOOKUP(E8,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E14,Kertoimet!B145:C148,2,FALSE)/1000*150)/150+(=VLOOKUP(E20,Kertoimet!B145:C148,2,FALSE)/1000*150)/150)/3*amountKG*1000
    salad = multipliers.salad / 150 * 1000 * amountKG
    bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
    dessert = ((multipliers.kisel + multipliers.pancakes)/2)/150*1000*amountKG

class foodDistribution:
    costOfaMeal =  input("Cost of the meal in €")
    amountOfMeals = input("The amount of meals sold")
    meat = "temp"#=IF(I19<>"",I19/J17*(F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30),J19*(F7+F8+F9+F10+Kertoimet!C178+1.5/1000*30))
    veggie = "temp"#=IF(I22<>"",I22/J17*(F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30),J22*(F13+F14+F15+F16+Kertoimet!C178+1.5/1000*30))
    vegan = "formula"#=IF(I25<>"",I25/J17*(F19+F20+Kertoimet!C178+1.5/1000*30),J25*(F19+F20+Kertoimet!C178+1.5/1000*30))

class electricity:
    cookingAndCentralKitchen = foodDistribution.amountOfMeals or foodDistribution.costOfaMeal + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C82*I30,Kertoimet!C56*Kertoimet!C82*I30)
    cookingAndHeatingKitchen =  foodDistribution.costOfaMeal or foodDistribution.amountOfMeals + "formula" #=IF(Kertoimet!D58<>"",Kertoimet!C58*Kertoimet!C83*I31,Kertoimet!C56*Kertoimet!C83*I31)

class overview:
    cafeteriaConsumption = electricity.cookingAndCentralKitchen + electricity.cookingAndHeatingKitchen
    surplusFoodCO2Footprint = surplusFood.meat + surplusFood.veggie + surplusFood.vegan + surplusFood.sides + surplusFood.salad + surplusFood.bread + surplusFood.dessert
    foodDistributionCO2Footprint = foodDistribution.meat + foodDistribution.veggie + foodDistribution.vegan
    foodCO2Footprint = meatmeal.Co2OfMeatMeal + veggiemeal.Co2OfVeggieMeal + veganmeal.Co2OfVeganMeal + dessert.Co2OfDessert + others.Co2OfOthers

    
#Food info - Personal


class drinks:
    water = amountOfPortions * 0
    milk = amountOfPortions * ((multipliers.milk/1000)*170)
    oatMilk = amountOfPortions * ((multipliers.oatDrink/1000)*170)
    coffee = amountOfPortions * ((multipliers.coffee/1000)*170)
    tea = amountOfPortions * ((multipliers.tea/1000)*170)
    drinkTotal = water + milk + oatMilk + coffee + tea 

class others:
    ryeBread = amountOfPortions * ((multipliers.ryeBread/1000)*30)
    wheatBread = amountOfPortions * ((multipliers.wheatBread/1000)*30)
    salad = amountOfPortions * multipliers.salad
    othersTotal = ryeBread + wheatBread + salad

def foodWaste(ans):
    ans = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
    if ans:
        ans = "Not at all"
        return 0
    
    elif ans:
        ans = "Half a plate"
        return (personalLunch + drinks.drinkTotal + others.othersTotal)/1.5

    elif ans:
        ans = "Over a half a plate"
        return (personalLunch + drinks.drinkTotal + others.othersTotal)/2.5

class proteins:
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
    proteinsTotal = fish + cow + pig + chicken + sausage + soy + broadBean + tofu + vegetables + Egg + cream

class carboHydrates:
    potato = amountOfPortions * (multipliers.potato/1000*150)
    rice = amountOfPortions * (multipliers.rice/1000*100)
    pasta = amountOfPortions * (multipliers.pasta/1000*120)
    rootVegetables = amountOfPortions * (multipliers.rootVegetables/1000*150)
    totalCarboHydrates = potato + rice + pasta + rootVegetables

class dessert: 
    pancakes = amountOfPortions * multipliers.pancakes
    kisel = amountOfPortions * multipliers.kisel
    totalDessert = pancakes + kisel

personalLunch = amountOfPortions * (proteins.proteinsTotal + carboHydrates.totalCarboHydrates + dessert.totalDessert)
total = (personalLunch + drinks.drinkTotal + others.othersTotal + foodWaste)