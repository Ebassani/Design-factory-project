import multipliers


#test environment where you can test the features of the code
#keep this file empty :)
amountOfPortions = input("How many portions of the food was made?")

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
    
    return 0

def veggiemeal():

    veggiemealSide = input("Choose the side of the meal. Rice, pasta, potato or vegetables")
    if (veggiemealSide == "Rice"):
        return multipliers.rice
    elif (veggiemealSide == "Pasta"):
        return multipliers.pasta
    elif (veggiemealSide == "Potato"):
        return multipliers.potato
    elif (veggiemealSide == "Vegetables"):
        return multipliers.vegetables

    return 0

def veggiemealEgg():
    Egg = input("Does the meal have eggs? | Yes or No")
    if (Egg == "Yes"):
        return multipliers.egg
    elif (Egg == "No"):
        return 0

    return 0

def veggiemealDairy():
    Dairy = input ("Does the meal have dairy products? | Yes or No")
    if (Dairy == "Yes"):
        return multipliers.cream
    elif (Dairy == "No"):
        return 0
    
    return 0

def Co2ofVeggieMeal():
    co2 = (int(amountOfPortions) * (veggieMealProtein() + veggiemeal() + veggiemealEgg()) + veggiemealDairy())
    return co2

#print (Co2ofVeggieMeal())

def dessert(): 
    pancakes = int(amountOfPortions) * multipliers.aPortionOfPancakes
    kisel = int(amountOfPortions) * multipliers.aPortionOfKisel
    dessertTotal = pancakes + kisel
    return dessertTotal

print(dessert())