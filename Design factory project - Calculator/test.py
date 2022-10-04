import multipliers


#test environment where you can test the features of the code
#keep this file empty :)
amountOfPortions = input("How many portions we're made")


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
    pancakes = int(amountOfPortions) * multipliers.aPortionOfPancakes
    kisel = int(amountOfPortions) * multipliers.aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal

#In progress (Cannot sum functions for some reason)
personalLunch = int(amountOfPortions) * (drinks() + carboHydrates() + dessert())
total = (personalLunch + drinks() + others() + foodWaste())

