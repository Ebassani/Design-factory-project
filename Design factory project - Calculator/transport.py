import multipliers

def userInputs():
    #Car
    carUserInput = float(input("Distance"))
    carFuelUserInput = input("Which fuel was used in car (unknown, diesel, petrol, natural gas, bio gas, electric car, hybrid, charging hybrid")
    #Fligts
    shortFlightUnder463kmUserInput = float(input("Distance * Amount of passengers"))
    longFligtsOverHomelandOver463kmUserInput = float(input("Distance * Amount of passengers"))
    longFlightsAbroadOver463kmUserInput = float(input("Distance * Amount of passengers"))
    longFlightsOver3700kmUserInput = float(input("Distance * Amount of passengers"))  
    #Public transport
    BusShortDistanceUserInput = float(input("Distance * Amount of passengers"))
    BusLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    TrainLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    TrainShortDistanceUserInput = float(input("Distance * Amount of passengers"))
    MetroUserInput = float(input("Distance * Amount of passengers"))
    TramUserInput = float(input("Distance * Amount of passengers"))
    #Public transport(abroad)
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
    ElectricKickboardRentUserInput = float(input("Distance"))
    ElectricBicycleUserInput = float(input("Distance"))
    BicycleUserInput = float(input("Distance"))
    KickboardUserInput = float(input("Distance"))

    #Liters
    ATVUserInput = float(input("Liters consumed"))
    TractorUserInput = float(input("Liters consumed"))
    SnowMobile = float(input("Liters consumed"))
    #Public transport
    #pkm
    BusAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    BusAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))

    TrainAbroadLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    TrainAbroadShortDistanceUserInput = float(input("Distance * Amount of passengers"))
    
    MetroAbroadUserInput = float(input("Distance * Amount of passengers"))
    TramAbroadUserInput = float(input("Distance * Amount of passengers"))

    return shortFlightUnder463kmUserInput + longFligtsOverHomelandOver463kmUserInput + longFlightsAbroadOver463kmUserInput + longFlightsOver3700kmUserInput + BusShortDistanceUserInput + BusLongDistanceUserInput + TrainLongDistanceUserInput + TrainShortDistanceUserInput + MetroUserInput + TramUserInput + TrainAbroadUserInput + BusAbroadUserInput + unknownFuelUserInput + dieselUserInput + petrolUserInput + naturalGasUserInput + bioGasUserInput + electricCarUserInput + hybridUserInput + chargingHybridUserInput + rentalBusUserInput + hotelStaysUserInput + taxiUserInput + MopedUserInput + MopedCarUserInput + MotorcycleUserInput + ElectricKickboardRentUserInput + ElectricBicycleUserInput + BicycleUserInput + KickboardUserInput + ATVUserInput + TractorUserInput + SnowMobile + BusAbroadLongDistanceUserInput + BusAbroadShortDistanceUserInput + TrainAbroadLongDistanceUserInput + TrainAbroadShortDistanceUserInput + MetroAbroadUserInput + TramAbroadUserInput + carUserInput + carFuelUserInput
    
def carFuelUserInput(carFuelAnswer):
    if (carFuelAnswer == "unknown"):
        return multipliers.unknownFuel
    elif (carFuelAnswer == "diesel"):
        return multipliers.diesel
    elif (carFuelAnswer == "petrol"):
        return multipliers.petrol
    elif (carFuelAnswer == "natural gas"):
        return multipliers.naturalGas
    elif (carFuelAnswer == "bio gas"):
        return multipliers.bioGas
    elif (carFuelAnswer == "electric car"):
        return multipliers.electricCar
    elif (carFuelAnswer == "hybrid"):
        return multipliers.hybrid
    elif (carFuelAnswer == "chargingHybrid"):
        return multipliers.chargingHybrid





#TRANSPORT
def car():
    carEmission = userInputs.carUserInput*userInputs.carFuelUserInput
    return carEmission

def userEmissionsFlights():
    #kgCO2e
    shortFlightUnder463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFligtsOverHomelandOver463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFlightsAbroadOver463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFlightsOver3700kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    return shortFlightUnder463kmEmission + longFligtsOverHomelandOver463kmEmission + longFlightsAbroadOver463kmEmission + longFlightsOver3700kmEmission

def userEmissionsPublicTransport():
    #kgCO2e
    BusShortDistanceEmission = userInputs.BusShortDistanceUserInput*multipliers.publicTransport.BusShortDistance
    BusLongDistanceEmission = userInputs.BusLongDistanceUserInput*multipliers.publicTransport.BusLongDistance
    TrainLongDistanceEmission = userInputs.TrainLongDistanceUserInput*multipliers.publicTransport.TrainLongDistance
    TrainShortDistanceEmission = userInputs.TrainShortDistanceUserInput*multipliers.publicTransport.TrainShortDistance
    MetroEmission = userInputs.MetroUserInput*multipliers.publicTransport.Metro
    TramEmission = userInputs.TramUserInput*multipliers.publicTransport.Tram
    TrainAbroadEmission = userInputs.TrainAbroadUserInput*multipliers.publicTransport.TrainAbroad
    BusAbroadEmission = userInputs.BusAbroadUserInput*multipliers.publicTransport.BusAbroad
    return BusShortDistanceEmission + BusLongDistanceEmission + TrainLongDistanceEmission + TrainShortDistanceEmission + MetroEmission + TramEmission + TrainAbroadEmission + BusAbroadEmission
def userEmissionsCarTraffic():      
    #kgCO2e
    unknownFuelEmission = userInputs.unknownFuelUserInput*multipliers.carTraffic.unknownFuel
    dieselEmission = userInputs.dieselUserInput*multipliers.carTraffic.diesel
    petrolEmission = userInputs.petrolUserInput*multipliers.carTraffic.petrol
    naturalGasEmission = userInputs.naturalGasUserInput*multipliers.carTraffic.naturalGas
    bioGasEmission = userInputs.bioGasUserInput*multipliers.carTraffic.bioGas
    electricCarEmission = userInputs.electricCarUserInput*multipliers.carTraffic.electricCar
    hybridEmission = userInputs.hybridUserInput*multipliers.carTraffic.hybrid
    chargingHybridEmission = userInputs.chargingHybridUserInput*multipliers.carTraffic.chargingHybrid
    return unknownFuelEmission + dieselEmission + petrolEmission + naturalGasEmission + bioGasEmission + electricCarEmission + hybridEmission + chargingHybridEmission
    
def userEmissionsBusinessAndClassTrips():
    #kgCO2e
    rentalBusEmission = userInputs.rentalBusUserInput*multipliers.businessAndClassTrips.rentalBus
    hotelStaysEmission = userInputs.hotelStaysUserInput*multipliers.businessAndClassTrips.hotelStays
    taxiEmission = userInputs.taxiUserInput*multipliers.businessAndClassTrips.taxi
    return rentalBusEmission + hotelStaysEmission + taxiEmission

def userEmissionsOtherVehicles():
    #kgCO2e
    MopedEmission = userInputs.MopedUserInput*multipliers.otherVehicles.Moped
    MopedCarEmission = userInputs.MopedCarUserInput*multipliers.otherVehicles.MopedCar
    MotorcycleEmission = userInputs.MotorcycleUserInput*multipliers.otherVehicles.Motorcycle
    ElectricKickboardRentEmission = userInputs.ElectricKickboardRentUserInput*multipliers.otherVehicles.ElectricKickboardRent
    ElectricBicycleEmission = userInputs.ElectricBicycleUserInput*multipliers.otherVehicles.ElectricBicycle
    BicycleEmission = userInputs.BicycleUserInput*0
    Kickboard = userInputs.KickboardUserInput*0
    return MopedEmission + MopedCarEmission + MotorcycleEmission + ElectricKickboardRentEmission + ElectricBicycleEmission + BicycleEmission + Kickboard



def publicTransport():
    #kgCO2e
    BusAbroadLongDistanceEmission = userInputs.BusShortDistanceUserInput*multipliers.publicTransport.BusShortDistance
    BusAbroadShortDistanceEmission = userInputs.BusLongDistanceUserInput*multipliers.publicTransport.BusLongDistance
    TrainAbroadLongDistanceEmission = userInputs.TrainLongDistanceUserInput*multipliers.publicTransport.TrainLongDistance
    TrainAbroadShortDistanceEmission = userInputs.TrainShortDistanceUserInput*multipliers.publicTransport.TrainShortDistance
    MetroAbroadEmission = userInputs.MetroUserInput*multipliers.publicTransport.Metro
    TramAbroadEmission = userInputs.TramUserInput*multipliers.publicTransport.Tram
    return BusAbroadLongDistanceEmission + BusAbroadShortDistanceEmission + TrainAbroadLongDistanceEmission + TrainAbroadShortDistanceEmission + MetroAbroadEmission + TramAbroadEmission

