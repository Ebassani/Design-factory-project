import multipliers


#test environment where you can test the features of the code
#keep this file empty :)
amountOfPortions = input("How many portions of the food was made?")

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

def veganmeal():
   
    veganmealSide = input("Choose the side of the meal. Rice, Pasta, Potato or Vegetables")
    if (veganmealSide == "Rice"):
        return multipliers.rice
    elif (veganmealSide == "Pasta"):
        return multipliers.pasta
    elif (veganmealSide == "Potato"):
        return multipliers.potato
    elif (veganmealSide == "Vegetables"):
        return multipliers.vegetables
    

veganMealProtein()
veganmeal()

FunctionSum = (sum(veganMealProtein + veganmeal))
print (FunctionSum * amountOfPortions)