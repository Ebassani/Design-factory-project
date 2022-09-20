#Traffic variables 
#Common variables, used in multiple classes
AverageElectricity = 281.00




#flights:
    #kgCO2e/hkm
shortFlightUnder463km = 0.2595*2+0.2595*2
longFligtsOverHomelandOver463km = (0.178*2)+(0.178*0.2)
longFlightsAbroadOver463km = (0,149*2)+(0.149*0.2)
longFlightsOver3700km = (0.135*2)+(0.135*0.2)

    
#carTraffic:
    #kgCO2e/km
unknownFuel = 0.152*1.2
diesel = 0.141*1.2
petrol = 0.159*1.2
naturalGas = 0.0701*1.2
bioGas = 0.95*4.5/100
electricCar = 0.0188/100*(AverageElectricity)+0.00195
hybrid = 0.114*1.2
chargingHybrid = 0.084*1.2

#businessAndClassTrips:
    #kgCO2e/hkm
carFerryAndCruiseShip = 0.144*1.2
    #kgCO2e/€
rentalBus = 0.574*1.2
hotelStays = 0.18
taxi = 0.18

# otherVehicles:
    #kgCO2e/hkm
Motorcycle = 0.112*1.2
Moped = 0.068*1.2
MopedCar = 0.128*1.2
ElectricKickboardRent = 0.0452
ElectricBicycle = 0.0012*(AverageElectricity/1000)

    #kgCO2e/km
ATV = 2.673
Tractor = 2.679
SnowMobile = 1.469

#publicTransport:
    #kgCO2e/hkm
BusLongDistance = 0.053*1.2
TrainLongDistance = 0
TrainShortDistance = 0
BusShortDistance = 0.053*1.2
Metro = 0
Tram = 0

    #kgCO2e/€
TrainAbroad = 0.100
BusAbroad = 0.180

#Infrastructure variables

#energy:
    #Electricity consumption
    #kgCO2e/MWh
AverageElectricity = 281.00
ZeroEmissionGreenElectricity = 0
    #Sellers emissionmultiplier!!

    #Heating
DistrictHeating = 267.00
ZeroEmissionDistrictHeating = 0
    #Sellers emissionmultiplier!!
ElectricityHeating = 400.00

    #Cooling
DistrictCooling = 72*1.2
ZeroEmissionCooling = 0
    #Sellers emissionmultiplier!!
ElectricityCooling = AverageElectricity

    #Ventilation kWh/(m3/s)
EntryAndExit = 2.00
OnlyExit = 1.00
    #(m3/s)/m2
OutdoorAirFlow = 0.00035

    #Cafeteria energy consumption
    #MWh/day
PrepationAndCentralKitchen = 0.258
PrepationAndHeatingKitchen = 0.179
    #MVh a portion/meal
PreparationAndCentralKitchenPerMeal = 0.00031
PreparationAndHeatingKitchenPerMeal = 0.00061

    #Trash / kgCO2e/kg
mixedWaste = 0.410
energyWaste = 0.411
bioWaste = 0.069
Cardboard = 0.060
Glass = 0.570
Metal = 0.130
Plastic = 0.070
Paper = 1.050
ElectricityRecycable = 0.720
ProblemWaste = 1.410

#class acquisitions:
    #kgCO2e/kpl
phone = 60
laptop = 350
computerScreen = 510
tablet = 100
desktopComputer = 199.8
multifunctionPrinter = 410
printer = 77.8

officeChair = 34
chair = 9
metalFrameTable = 218
electricDesk = 254
paperKg = 0.905
    #kgCO2e/item
eBook = 0.08
book = 1.2

Cleaning = 0.1
internetAndPhones = 0.28
postal = 0.5


    #Food variables

#kgCO2e/kg
#Meats
cow = 15
fish = 1.5
chicken = 5
pig = 5
sausage = 5.62
#Vegeterian/Vegan
soyGrits = 1.2
broadBean = 0.89
tofu = 2
vegetables = 0.2
#Drinks
oatDrink = 0.23
milk = 1.1
coffee = 0.6
tea = 0.3
#Carbohydrates
pasta = 0.034
rice = 5
potato = 0.2
rootVegetables = 0.3
#Other
cheese = 10
egg = 2.5
cream = 3.181
cucumber = 2
tomato = 3
ryeBread = 1.3
wheatBread = 1.7

#Desserts / kgCO2/kg
#class kisel:
PotatoFlour = 0.396
Berries = 0.200
Sugar = 1.100
PortionOfKisel = (Berries/1000*400)+(Sugar/1000*63.75)+(PotatoFlour/1000*20)/4 

#pancakes
Flour = 1.130
Milk = 1.100
Eggs = 2.500
Sugar = 1.100
aPortionOfPancakes = ((Flour/1000*195)+(Milk/1000*500)+(Eggs/1000*180)+(Sugar/1000*12))/6

#class salad:
Cucumber = 2.000
Carrot = 0.300
Tomato = 3.000
aPortionOfSalad = (Cucumber/1000*50)+(Carrot/1000*50)+(Tomato/1000*50)