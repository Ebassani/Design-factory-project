from Calculator.multipliers import *

#USER INPUTS
#School work/trips
#tripsAndWorkParticipants = float(input("Amount of participants"))
#Car
#carDistanceUserInput = float(input("Distance"))
#carFuelUserInput = input("Which fuel was used in car (unknown, diesel, petrol, natural gas, bio gas, electric car, hybrid, charging hybrid: ")
#Fligts(pkm)
#shortFlightUnder463kmUserInput = float(input("Distance * Amount of passengers"))
#longFligtsOverHomelandOver463kmUserInput = float(input("Distance * Amount of passengers"))
#longFlightsAbroadOver463kmUserInput = float(input("Distance * Amount of passengers"))
#longFlightsOver3700kmUserInput = float(input("Distance * Amount of passengers"))  
#Public transport(pkm)
#BusShortDistanceUserInput = float(input("Distance * Amount of passengers"))
#BusLongDistanceUserInput = float(input("Distance * Amount of passengers"))
#TrainLongDistanceUserInput = float(input("Distance * Amount of passengers"))
#TrainShortDistanceUserInput = float(input("Distance * Amount of passengers"))
#MetroUserInput = float(input("Distance * Amount of passengers"))
#TramUserInput = float(input("Distance * Amount of passengers"))
#Public transport(abroad)(pkm)
#TrainAbroadUserInput = float(input("Distance * Amount of passengers"))
#BusAbroadUserInput = float(input("Distance * Amount of passengers"))
#Car Traffic(km)
#unknownFuelUserInput = float(input("Distance"))
#dieselUserInput = float(input("Distance"))
#petrolUserInput = float(input("Distance"))
#naturalGasUserInput = float(input("Distance"))
#bioGasUserInput = float(input("Distance"))
#electricCarUserInput = float(input("Distance"))
#hybridUserInput = float(input("Distance"))
#chargingHybridUserInput = float(input("Distance"))
#Other
#km
#rentalBusUserInput = float(input("Distance"))
#€
#hotelStaysUserInput = float(input("Euros"))
#taxiUserInput = float(input("Euros"))
#Other vehicles(km)
#MopedUserInput = float(input("Distance"))
#MopedCarUserInput = float(input("Distance"))
#MotorcycleUserInput = float(input("Distance"))
#Liters
#ATVUserInput = float(input("Liters consumed"))
#TractorUserInput = float(input("Liters consumed"))
#SnowMobileUserInput = float(input("Liters consumed"))
#Public transport(pkm)
#BusAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
#BusAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))
#TrainAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
#TrainAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))
#MetroAbroadUserInput = float(input("Distance * Amount of passengers"))
#TramAbroadUserInput = float(input("Distance * Amount of passengers"))
#Other(km)
#ElectricKickboardRentUserInput = float(input("Distance"))
#ElectricBicycleUserInput = float(input("Distance"))
#BicycleUserInput = float(input("Distance"))
#KickboardUserInput = float(input("Distance"))
    
def carEmissions(Passengers, FuelUsed):
    carPassengersUserInput = Passengers
    carFuelAnswer = FuelUsed
    if (carFuelAnswer == "unknown"):
        return Passengers*unknownFuel/carPassengersUserInput
    elif (carFuelAnswer == "diesel"):
        return Passengers*diesel/carPassengersUserInput
    elif (carFuelAnswer == "petrol"):
        return Passengers*petrol/carPassengersUserInput
    elif (carFuelAnswer == "natural gas"):
        return Passengers*naturalGas/carPassengersUserInput
    elif (carFuelAnswer == "bio gas"):
        return Passengers*bioGas
    elif (carFuelAnswer == "electric car"):
        return Passengers*electricCar/carPassengersUserInput
    elif (carFuelAnswer == "hybrid"):
        return Passengers*hybrid/carPassengersUserInput
    elif (carFuelAnswer == "chargingHybrid"):
        return (Passengers*chargingHybrid)/carPassengersUserInput
carEmissions()
Car = carEmissions()


def userEmissionsFlights(ShortFlightsAnswer, LongFlightsHomelandAnswer, LongFlightsAbroadAnswer, LongFlightsOver3700Answer):
    #kgCO2e
    shortFlightUnder463kmEmission = ShortFlightsAnswer*shortFlightUnder463km
    longFligtsOverHomelandOver463kmEmission = LongFlightsHomelandAnswer*shortFlightUnder463km
    longFlightsAbroadOver463kmEmission = LongFlightsAbroadAnswer*shortFlightUnder463km
    longFlightsOver3700kmEmission = LongFlightsOver3700Answer*shortFlightUnder463km
    return shortFlightUnder463kmEmission + longFligtsOverHomelandOver463kmEmission + longFlightsAbroadOver463kmEmission + longFlightsOver3700kmEmission
userEmissionsFlights()
flights = userEmissionsFlights()

def userEmissionsPublicTransport(ShortDistanceBus, LongDistanceBus, LongDistanceTrain, ShortDistanceTrain, MetroInput, TramInput):
    #kgCO2e
    BusShortDistanceEmission = ShortDistanceBus*BusShortDistance
    BusLongDistanceEmission = LongDistanceBus*BusLongDistance
    TrainLongDistanceEmission = LongDistanceTrain*TrainLongDistance
    TrainShortDistanceEmission = ShortDistanceTrain*TrainShortDistance
    MetroEmission = MetroInput*Metro
    TramEmission = TramInput*Tram
    return BusShortDistanceEmission + BusLongDistanceEmission + TrainLongDistanceEmission + TrainShortDistanceEmission + MetroEmission + TramEmission
userEmissionsPublicTransport()
publicTransportEmission = userEmissionsPublicTransport()

def userEmissionsPublicTransportAbroad(TrainAbroadInput, BusAbroadInput):
    TrainAbroadEmission = TrainAbroadInput*TrainAbroad
    BusAbroadEmission = BusAbroadInput*BusAbroad
    return TrainAbroadEmission + BusAbroadEmission
userEmissionsPublicTransportAbroad()
publicTransportEmissionAbroad = userEmissionsPublicTransportAbroad()

def userEmissionsCarTraffic(UnknownFuelInput, DieselInput, PetrolInput, NaturalGasInput, BioGasInput, ElectricCarInput, HybridInput, ChargingHybridInput):      
    #kgCO2e
    unknownFuelEmission = UnknownFuelInput*unknownFuel
    dieselEmission = DieselInput*diesel
    petrolEmission = PetrolInput*petrol
    naturalGasEmission = NaturalGasInput*naturalGas
    bioGasEmission = BioGasInput*bioGas
    electricCarEmission = ElectricCarInput*electricCar
    hybridEmission = HybridInput*hybrid
    chargingHybridEmission = ChargingHybridInput*chargingHybrid
    return unknownFuelEmission + dieselEmission + petrolEmission + naturalGasEmission + bioGasEmission + electricCarEmission + hybridEmission + chargingHybridEmission
carTraffic = userEmissionsCarTraffic()
    
def userEmissionsBusinessAndClassTrips(RentalBusInput, HotelStaysInput, TaxiInput):
    #kgCO2e
    rentalBusEmission = RentalBusInput*rentalBus
    hotelStaysEmission = HotelStaysInput*hotelStays
    taxiEmission = TaxiInput*taxi
    return rentalBusEmission + hotelStaysEmission + taxiEmission
userEmissionsBusinessAndClassTrips()
BusinessAndClassTrips = userEmissionsBusinessAndClassTrips()

def schoolCarbonFootprints():
    return Car + flights + publicTransportEmission + publicTransportEmissionAbroad + carTraffic + BusinessAndClassTrips

SchoolCarbonFootprints = schoolCarbonFootprints()

#def schoolCarbonFootprintsPerParticipant():
#    return SchoolCarbonFootprints/tripsAndWorkParticipants
#SchoolCarbonFootprintsPerParticipant = schoolCarbonFootprintsPerParticipant()


def userEmissionsOtherVehicles(MopedInput, MopedCarInput, MotorcycleInput, ATVInput, TractorInput, SnowmobileInput):
    #kgCO2e
    MopedEmission = MopedInput*Moped
    MopedCarEmission = MopedCarInput*MopedCar
    MotorcycleEmission = MotorcycleInput*Motorcycle
    ATVEmission = ATVInput*ATV
    TractorEmission = TractorInput*Tractor
    SnowMobileEmission = SnowmobileInput*SnowMobile
    return MopedEmission + MopedCarEmission + MotorcycleEmission + ATVEmission + TractorEmission + SnowMobileEmission
userEmissionsOtherVehicles()
UserEmissionsOtherVehicles = userEmissionsOtherVehicles()



#def personalPublicTransport():
    #kgCO2e
#    BusAbroadLongDistanceEmission = BusShortDistanceUserInput*BusShortDistance
#    BusAbroadShortDistanceEmission = BusLongDistanceUserInput*BusLongDistance
#    TrainAbroadLongDistanceEmission = TrainLongDistanceUserInput*TrainLongDistance
#    TrainAbroadShortDistanceEmission = TrainShortDistanceUserInput*TrainShortDistance
#    MetroAbroadEmission = MetroUserInput*Metro
#    TramAbroadEmission = TramUserInput*Tram
#    return BusAbroadLongDistanceEmission + BusAbroadShortDistanceEmission + TrainAbroadLongDistanceEmission + TrainAbroadShortDistanceEmission + MetroAbroadEmission + TramAbroadEmission
#personalPublicTransport()
#PersonalPublicTransport = personalPublicTransport()

def otherEmissions(ElectricKickboardRentalInput, ElectricBycycleInput, BycycleInput, KickboardInput):
    ElectricKickboardRentEmission = ElectricKickboardRentalInput*ElectricKickboardRent
    ElectricBicycleEmission = ElectricBycycleInput*ElectricBicycle
    BicycleEmission = BycycleInput*0
    Kickboard = KickboardInput*0
    return ElectricKickboardRentEmission + ElectricBicycleEmission + BicycleEmission + Kickboard
OtherEmissions = otherEmissions()
otherEmissions()


#def tripToSchoolEmissions():
#    return UserEmissionsOtherVehicles + PersonalPublicTransport + OtherEmissions

