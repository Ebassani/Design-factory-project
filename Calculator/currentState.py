

sizeOfBuilding = float(input("The size of the building in square meters"))
usersOfBuilding = float(input("The number of people who use the building"))
currentCO2Footprint = float(input("Current CO2 footprint"))

wantedCO2reduction = float(input("Wanted reduction to CO2 emission in %"))

CO2reduction = (currentCO2Footprint*(wantedCO2reduction/100))
wantedCarbonFootprint = (currentCO2Footprint)(currentCO2Footprint*(wantedCO2reduction/100))