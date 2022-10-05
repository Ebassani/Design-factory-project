from multipliers import *

#USER INPUTS
#School work/trips
tripsAndWorkParticipants = float(input("Amount of participants"))
#Car
carDistanceUserInput = float(input("Distance"))
#carFuelUserInput = input("Which fuel was used in car (unknown, diesel, petrol, natural gas, bio gas, electric car, hybrid, charging hybrid: ")
#Fligts(pkm)
shortFlightUnder463kmUserInput = float(input("Distance * Amount of passengers"))
longFligtsOverHomelandOver463kmUserInput = float(input("Distance * Amount of passengers"))
longFlightsAbroadOver463kmUserInput = float(input("Distance * Amount of passengers"))
longFlightsOver3700kmUserInput = float(input("Distance * Amount of passengers"))  
#Public transport(pkm)
BusShortDistanceUserInput = float(input("Distance * Amount of passengers"))
BusLongDistanceUserInput = float(input("Distance * Amount of passengers"))
TrainLongDistanceUserInput = float(input("Distance * Amount of passengers"))
TrainShortDistanceUserInput = float(input("Distance * Amount of passengers"))
MetroUserInput = float(input("Distance * Amount of passengers"))
TramUserInput = float(input("Distance * Amount of passengers"))
#Public transport(abroad)(pkm)
TrainAbroadUserInput = float(input("Distance * Amount of passengers"))
BusAbroadUserInput = float(input("Distance * Amount of passengers"))
#Car Traffic(km)
unknownFuelUserInput = float(input("Distance"))
dieselUserInput = float(input("Distance"))
petrolUserInput = float(input("Distance"))
naturalGasUserInput = float(input("Distance"))
bioGasUserInput = float(input("Distance"))
electricCarUserInput = float(input("Distance"))
hybridUserInput = float(input("Distance"))
chargingHybridUserInput = float(input("Distance"))
#Other
#km
rentalBusUserInput = float(input("Distance"))
#€
hotelStaysUserInput = float(input("Euros"))
taxiUserInput = float(input("Euros"))
#Other vehicles(km)
MopedUserInput = float(input("Distance"))
MopedCarUserInput = float(input("Distance"))
MotorcycleUserInput = float(input("Distance"))
#Liters
ATVUserInput = float(input("Liters consumed"))
TractorUserInput = float(input("Liters consumed"))
SnowMobileUserInput = float(input("Liters consumed"))
#Public transport(pkm)
BusAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
BusAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))
TrainAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
TrainAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))
MetroAbroadUserInput = float(input("Distance * Amount of passengers"))
TramAbroadUserInput = float(input("Distance * Amount of passengers"))
#Other(km)
ElectricKickboardRentUserInput = float(input("Distance"))
ElectricBicycleUserInput = float(input("Distance"))
BicycleUserInput = float(input("Distance"))
KickboardUserInput = float(input("Distance"))
    
def carEmissions():
    carPassengersUserInput = float(input("Number of passengers: "))
    carFuelAnswer = input("Which fuel was used in car (unknown, diesel, petrol, natural gas, bio gas, electric car, hybrid, charging hybrid: ")
    if (carFuelAnswer == "unknown"):
        return carDistanceUserInput*unknownFuel/carPassengersUserInput
    elif (carFuelAnswer == "diesel"):
        return carDistanceUserInput*diesel/carPassengersUserInput
    elif (carFuelAnswer == "petrol"):
        return carDistanceUserInput*petrol/carPassengersUserInput
    elif (carFuelAnswer == "natural gas"):
        return carDistanceUserInput*naturalGas/carPassengersUserInput
    elif (carFuelAnswer == "bio gas"):
        return carDistanceUserInput*bioGas
    elif (carFuelAnswer == "electric car"):
        return carDistanceUserInput*electricCar/carPassengersUserInput
    elif (carFuelAnswer == "hybrid"):
        return carDistanceUserInput*hybrid/carPassengersUserInput
    elif (carFuelAnswer == "chargingHybrid"):
        return (carDistanceUserInput*chargingHybrid)/carPassengersUserInput
carEmissions()
Car = carEmissions()


def userEmissionsFlights():
    #kgCO2e
    shortFlightUnder463kmEmission = shortFlightUnder463kmUserInput*shortFlightUnder463km
    longFligtsOverHomelandOver463kmEmission = longFligtsOverHomelandOver463kmUserInput*shortFlightUnder463km
    longFlightsAbroadOver463kmEmission = longFlightsAbroadOver463kmUserInput*shortFlightUnder463km
    longFlightsOver3700kmEmission = longFlightsOver3700kmUserInput*shortFlightUnder463km
    return shortFlightUnder463kmEmission + longFligtsOverHomelandOver463kmEmission + longFlightsAbroadOver463kmEmission + longFlightsOver3700kmEmission
userEmissionsFlights()
flights = userEmissionsFlights()

def userEmissionsPublicTransport():
    #kgCO2e
    BusShortDistanceEmission = BusShortDistanceUserInput*BusShortDistance
    BusLongDistanceEmission = BusLongDistanceUserInput*BusLongDistance
    TrainLongDistanceEmission = TrainLongDistanceUserInput*TrainLongDistance
    TrainShortDistanceEmission = TrainShortDistanceUserInput*TrainShortDistance
    MetroEmission = MetroUserInput*Metro
    TramEmission = TramUserInput*Tram
    return BusShortDistanceEmission + BusLongDistanceEmission + TrainLongDistanceEmission + TrainShortDistanceEmission + MetroEmission + TramEmission
userEmissionsPublicTransport()
publicTransportEmission = userEmissionsPublicTransport()

def userEmissionsPublicTransportAbroad():
    TrainAbroadEmission = TrainAbroadUserInput*TrainAbroad
    BusAbroadEmission = BusAbroadUserInput*BusAbroad
    return TrainAbroadEmission + BusAbroadEmission
userEmissionsPublicTransportAbroad()
publicTransportEmissionAbroad = userEmissionsPublicTransportAbroad()

def userEmissionsCarTraffic():      
    #kgCO2e
    unknownFuelEmission = unknownFuelUserInput*unknownFuel
    dieselEmission = dieselUserInput*diesel
    petrolEmission = petrolUserInput*petrol
    naturalGasEmission = naturalGasUserInput*naturalGas
    bioGasEmission = bioGasUserInput*bioGas
    electricCarEmission = electricCarUserInput*electricCar
    hybridEmission = hybridUserInput*hybrid
    chargingHybridEmission = chargingHybridUserInput*chargingHybrid
    return unknownFuelEmission + dieselEmission + petrolEmission + naturalGasEmission + bioGasEmission + electricCarEmission + hybridEmission + chargingHybridEmission
carTraffic = userEmissionsCarTraffic()
    
def userEmissionsBusinessAndClassTrips():
    #kgCO2e
    rentalBusEmission = rentalBusUserInput*rentalBus
    hotelStaysEmission = hotelStaysUserInput*hotelStays
    taxiEmission = taxiUserInput*taxi
    return rentalBusEmission + hotelStaysEmission + taxiEmission
userEmissionsBusinessAndClassTrips()
BusinessAndClassTrips = userEmissionsBusinessAndClassTrips()

def schoolCarbonFootprints():
    return Car + flights + publicTransportEmission + publicTransportEmissionAbroad + carTraffic + BusinessAndClassTrips

SchoolCarbonFootprints = schoolCarbonFootprints()

def schoolCarbonFootprintsPerParticipant():
    return SchoolCarbonFootprints/tripsAndWorkParticipants
SchoolCarbonFootprintsPerParticipant = schoolCarbonFootprintsPerParticipant()


def userEmissionsOtherVehicles():
    #kgCO2e
    MopedEmission = MopedUserInput*Moped
    MopedCarEmission = MopedCarUserInput*MopedCar
    MotorcycleEmission = MotorcycleUserInput*Motorcycle
    ATVEmission = ATVUserInput*ATV
    TractorEmission = TractorUserInput*Tractor
    SnowMobileEmission = SnowMobileUserInput*SnowMobile
    return MopedEmission + MopedCarEmission + MotorcycleEmission + ATVEmission + TractorEmission + SnowMobileEmission
userEmissionsOtherVehicles()
UserEmissionsOtherVehicles = userEmissionsOtherVehicles()



def personalPublicTransport():
    #kgCO2e
    BusAbroadLongDistanceEmission = BusShortDistanceUserInput*BusShortDistance
    BusAbroadShortDistanceEmission = BusLongDistanceUserInput*BusLongDistance
    TrainAbroadLongDistanceEmission = TrainLongDistanceUserInput*TrainLongDistance
    TrainAbroadShortDistanceEmission = TrainShortDistanceUserInput*TrainShortDistance
    MetroAbroadEmission = MetroUserInput*Metro
    TramAbroadEmission = TramUserInput*Tram
    return BusAbroadLongDistanceEmission + BusAbroadShortDistanceEmission + TrainAbroadLongDistanceEmission + TrainAbroadShortDistanceEmission + MetroAbroadEmission + TramAbroadEmission
personalPublicTransport()
PersonalPublicTransport = personalPublicTransport()

def otherEmissions():
    ElectricKickboardRentEmission = ElectricKickboardRentUserInput*ElectricKickboardRent
    ElectricBicycleEmission = ElectricBicycleUserInput*ElectricBicycle
    BicycleEmission = BicycleUserInput*0
    Kickboard = KickboardUserInput*0
    return ElectricKickboardRentEmission + ElectricBicycleEmission + BicycleEmission + Kickboard
OtherEmissions = otherEmissions()
otherEmissions()


def tripToSchoolEmissions():
    return UserEmissionsOtherVehicles + PersonalPublicTransport + OtherEmissions