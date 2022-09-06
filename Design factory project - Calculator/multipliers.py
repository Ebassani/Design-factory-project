#Traffic variables 
#Common variables, used in multiple classes
AverageElectricity = 281.00

class flights:
    #kgCO2e/hkm
    shortFlightUnder463km = 0.2595*2+0.2595*2
    longFligtsOverHomelandOver463km = (0.178*2)+(0.178*0.2)
    longFlightsAbroadOver463km = (0,149*2)+(0.149*0.2)
    longFlightsOver3700km = (0.135*2)+(0.135*0.2)
    
class otherVehicles:
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

class publicTransport:
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

class energy:
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






