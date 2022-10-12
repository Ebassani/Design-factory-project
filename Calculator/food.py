from Calculator import multipliers


# SCHOOL INFORMATION -- FOOD
# Meal independant functions
def mealSide(mealSide):
    # veggiemealSide = input("Choose the side of the veggie meal. Rice, pasta, potato or vegetables")
    if mealSide == "Rice":
        return multipliers.rice / 1000 * 150
    elif mealSide == "Pasta":
        return multipliers.pasta / 1000 * 150
    elif mealSide == "Potato":
        return multipliers.potato / 1000 * 150
    elif mealSide == "Vegetables":
        return multipliers.vegetables / 1000 * 150

    return 0


def mealEgg(egg):
    # Egg = input("Does the meat meal have eggs? | Yes or No")
    if egg == "Yes":
        return multipliers.egg / 1000 * 105
    elif egg == "No":
        return 0


def mealDairy(dairy):
    # dairy = input("Does the meat meal have cream? | Yes or No")
    if dairy == "Yes":
        return multipliers.cream / 1000 * 105
    elif dairy == "No":
        return 0


# Meat meal
def meatMealProtein(meatAns):
    # meatAns = input("Which protein does the meat meal have? Fish, Pig, Cow, Chicken or Sausage?")

    if meatAns == "Fish":
        return multipliers.fish / 1000 * 170
    elif meatAns == "Pig":
        return multipliers.pig / 1000 * 170
    elif meatAns == "Cow":
        return multipliers.cow / 1000 * 170
    elif meatAns == "Chicken":
        return multipliers.chicken / 1000 * 170
    elif meatAns == "Sausage":
        return multipliers.sausage / 1000 * 170

    return 0


def co2OfMeatMeal(amountOfPortions, meatMealProtein, meatmealSide, meatmealEgg, meatmealDairy):
    return amountOfPortions * (meatMealProtein + meatmealSide + meatmealEgg + meatmealDairy)


# Veggie meal
def vegMealProtein(vegAns):
    # veggieAns = input("Which protein does the veggie meal have? Soygrits, Tofu, Vegetables or Broad bean?")

    if vegAns == "Soygrits":
        return multipliers.soyGrits / 1000 * 170
    elif vegAns == "Tofu":
        return multipliers.tofu / 1000 * 170
    elif vegAns == "Vegetables":
        return multipliers.vegetables / 1000 * 170
    elif vegAns == "Broad bean":
        return multipliers.broadBean / 1000 * 170

    return 0


def co2ofVeggieMeal(amountOfPortions, veggieMealProtein, veggiemealSide, veggiemealEgg, veggiemealDairy):
    co2 = (amountOfPortions * (veggieMealProtein + veggiemealSide + veggiemealEgg + veggiemealDairy))
    return co2


# Vegan meal
def veganmealSide(veganmeal):
    # veganmeal = input("Choose the side of the vegan meal. Rice, Pasta, Potato or Vegetables")
    if veganmeal == "Rice":
        return multipliers.rice / 1000 * 170
    elif veganmeal == "Pasta":
        return multipliers.pasta / 1000 * 170
    elif veganmeal == "Potato":
        return multipliers.potato / 1000 * 170
    elif veganmeal == "Vegetables":
        return multipliers.vegetables / 1000 * 170


def co2OfVeganMeal(amountOfPortions, veganmealSide, veganMealProtein):
    veganmeal = (amountOfPortions * (veganmealSide + veganMealProtein))
    return veganmeal


# WORKING
# def dessert(amountOfPortions, dessertTotal):
#     pancake = amountOfPortions * 0.206
#     kisel = amountOfPortions * 0.040
#     dessertTotal = amountOfPortions * (pancake + kisel)
#     return dessertTotal
#
#
# # WORKING
# def others(amountOfPortions,othersTotal):
#     ryeBread = (amountOfPortions * 1.3 / 1000 * 30)
#     wheatBread = (amountOfPortions * 1.7 / 1000 * 30)
#     salad = amountOfPortions * 0.265
#     othersTotal = amountOfPortions * (ryeBread + wheatBread + salad)
#     return othersTotal
#
#
# # The next couple classes use complicated formulas in excel which I have no motivation to do right now because they look like hell on earth :DDDDDD
# # Includes surplusfood foodDistribution and electricity
#
#
# # IN PROGRESS
# def surplusFood(amountKG):
#     # amountKG = int(input("The amount of surplus in KG"))
#     meat = (((meatMealProtein()) / 1000 * 170) / 170) * 1000 * amountKG
#     veggie = (((veggieMealProtein()) / 1000 * 170) / 170) * 1000 * amountKG
#     vegan = (((veganMealProtein()) / 1000 * 170) / 170) * amountKG * 1000
#     sides = (((meatmealSide() / 1000 * 150) / 150) + ((veggiemealSide() / 1000 * 150) / 150) + (
#                 (veganmealSide()) / 1000 * 150) / 150) / 3 * amountKG * 1000
#     salad = (multipliers.aPortionOfSalad) / 150 * 1000 * amountKG
#     bread = (multipliers.ryeBread + multipliers.wheatBread) / 2 * amountKG
#     dessert = ((multipliers.aPortionOfKisel + multipliers.aPortionOfPancakes) / 2) / 150 * 1000 * amountKG
#     return meat + veggie + vegan + sides + salad + bread + dessert
#
#
# # IN PROGRESS
# def foodDistribution(meat, veggie, vegan):
#     print("Information to calculate food distribution")
#     costOfaMeal = int(input("Cost of the meal in €"))
#     meatMealsSold = int(input("The amount of meat meals sold"))
#     veggieMealsSold = int(input("The amount of veggie meals sold"))
#     veganMealsSold = int(input("The amount of vegan meals sold"))
#     meat = meatMealsSold / costOfaMeal * ((
#                                                       meatMealProtein() + meatmealSide() + meatmealEgg() + meatmealDairy() + multipliers.aPortionOfSalad) + 1.5 / 1000 * 30)
#     veggie = veggieMealsSold / costOfaMeal * ((
#                                                           veggieMealProtein() + veggiemealSide() + veggiemealEgg() + veggiemealDairy() + multipliers.aPortionOfPancakes) + 1.5 / 1000 * 30)
#     vegan = veganMealsSold / costOfaMeal * (
#                 (veganMealProtein() + veganmealSide() + multipliers.aPortionOfSalad) + 1.5 / 1000 * 30)
#     return costOfaMeal + meatMealsSold + veggieMealsSold + veganMealsSold + meat + veggie + vegan
#
#
# # IN PROGRESScs
# def electricity():
#     print("Information to calculate electricity")
#     amountofmealsCentral = int(input("How many meals we're made in central and heating kitchen combined?"))
#     amountOfMealsHeating = int(input("How many meals we're made in preparation and heating kitchen combined?"))
#     cookingAndCentralKitchen = multipliers.AverageElectricity * multipliers.PreparationAndCentralKitchenPerMeal * amountofmealsCentral
#     cookingAndHeatingKitchen = multipliers.AverageElectricity * multipliers.PreparationAndHeatingKitchenPerMeal * amountOfMealsHeating
#     return cookingAndCentralKitchen + cookingAndHeatingKitchen
#
#
# # IN PROGRESS
# def overview(totalOverview):
#     cafeteriaConsumption = electricity()
#     surplusFoodCO2Footprint = surplusFood()
#     foodDistributionCO2Footprint = foodDistribution()
#     foodCO2Footprint = (co2OfMeatMeal() + co2ofVeggieMeal() + veganmealSide() + dessert() + others())
#     totalOverview = cafeteriaConsumption + surplusFoodCO2Footprint + foodDistributionCO2Footprint + foodCO2Footprint
#     return totalOverview
#
#
# # Food info - Personal
#
#
# # WORKING
# def drinks(amountOfPortions):
#     water1 = float(amountOfPortions) * 0
#     milk1 = float(amountOfPortions) * ((milk / 1000) * 170)
#     oatMilk1 = float(amountOfPortions) * ((oatDrink / 1000) * 170)
#     coffee1 = float(amountOfPortions) * ((coffee / 1000) * 170)
#     tea1 = float(amountOfPortions) * ((tea / 1000) * 170)
#     return water1 + milk1 + oatMilk1 + coffee1 + tea1
#
#
# Drinks = drinks()
#
#
# # Working
# def others(amountOfPortions):
#     ryeBread = int(amountOfPortions) * ((multipliers.ryeBread / 1000) * 30)
#     wheatBread = int(amountOfPortions) * ((multipliers.wheatBread / 1000) * 30)
#     salad = int(amountOfPortions) * (multipliers.aPortionOfSalad)
#     return ryeBread + wheatBread + salad
#
#
# # Works when personallunch works
#
# def foodWaste(ans):
#     # ans = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
#     if (ans == "Not at all"):
#         return 0
#     elif (ans == "Half a plate"):
#         return (personalLunch + Drinks + others) / 1.5
#     elif (ans == "Over a half a plate"):
#         return (personalLunch + Drinks + others) / 2.5
#
#
# FoodWaste = foodWaste('Not at all')
#
#
# def foodWaste(answer):
#     # answer = input("How much did you throw away? (Not at all | Half a plate | Over half a plate)")
#     if answer:
#         answer = "Not at all"
#         return 0
#
#     elif answer:
#         answer = "Half a plate"
#         return (personalLunch + drinks + others) / 1.5
#
#     elif answer:
#         answer = "Over a half a plate"
#         return (personalLunch + drinks + others) / 2.5
#
#     return 0
#
#
# # Working
# def proteins(amountOfPortions):
#     fish1 = float(amountOfPortions) * ((fish / 1000) * 170)
#     cow1 = float(amountOfPortions) * ((cow / 1000) * 170)
#     pig1 = float(amountOfPortions) * ((pig / 1000) * 170)
#     chicken1 = float(amountOfPortions) * ((chicken / 1000) * 170)
#     sausage1 = float(amountOfPortions) * ((sausage / 1000) * 170)
#     soy1 = float(amountOfPortions) * (soyGrits / 1000 * 170)
#     broadBean1 = float(amountOfPortions) * (broadBean / 1000 * 170)
#     tofu1 = float(amountOfPortions) * (tofu / 1000 * 170)
#     vegetables1 = float(amountOfPortions) * (vegetables / 1000 * 170)
#     Egg1 = float(amountOfPortions) * (egg / 1000 * 60)
#     cream1 = float(amountOfPortions) * (cream / 1000 * 60)
#     proteinsTotal = fish1 + cow1 + pig1 + chicken1 + sausage1 + soy1 + broadBean1 + tofu1 + vegetables1 + Egg1 + cream1
#     return proteinsTotal
#
#
# Proteins = proteins(1)
#
#
# # Working
# def carboHydrates(amountOfPortions):
#     potato1 = float(amountOfPortions) * (potato / 1000 * 150)
#     rice1 = float(amountOfPortions) * (rice / 1000 * 100)
#     pasta1 = float(amountOfPortions) * (pasta / 1000 * 120)
#     rootVegetables1 = float(amountOfPortions) * (rootVegetables / 1000 * 150)
#     carboHydratesTotal = potato1 + rice1 + pasta1 + rootVegetables1
#     return carboHydratesTotal
#
#
# Carbohydrates = carboHydrates(1)
#
#
# # Working
# def dessert(amountOfPortions):
#     pancakes = int(amountOfPortions) * multipliers.aPortionOfPancakes
#     kisel = int(amountOfPortions) * multipliers.aPortionOfKisel
#     dessertTotal = pancakes + kisel
#     return dessertTotal
#
#
# # In progress (Cannot sum functions for some reason)
#
# personalLunch = 1
# total = 2
#
# # personalLunch = int(amountOfPortions) * (drinks() + carboHydrates() + dessert())
# # total = (personalLunch + drinks() + others() + foodWaste())
#
#
# # Riku N
