#Traffic variables 

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

