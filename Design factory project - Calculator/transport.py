import multipliers

class userInputs:
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

    #Liters
    ATVUserInput = float(input("Liters consumed"))
    TractorUserInput = float(input("Liters consumed"))
    SnowMobile = float(input("Liters consumed"))
    #Public transport
    #pkm
    BusLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    BusShortDistanceUserInput = float(input("Distance * Amount of passengers"))

    TrainLongDistanceUserInput = float(input("Distance * Amount of passengers"))
    TrainShortDistanceUserInput = float(input("Distance * Amount of passengers"))
    
    MetroUserInput = float(input("Distance * Amount of passengers"))
    TramUserInput = float(input("Distance * Amount of passengers"))






#TRANSPORT
class userEmissionsFlights(multipliers.flights):
    #kgCO2e
    shortFlightUnder463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFligtsOverHomelandOver463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFlightsAbroadOver463kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km
    longFlightsOver3700kmEmission = userInputs.shortFlightUnder463kmUserInput*multipliers.flights.shortFlightUnder463km

class userEmissionsPublicTransport:
    #kgCO2e
    BusShortDistanceEmission = userInputs.BusShortDistanceUserInput*multipliers.publicTransport.BusShortDistance
    BusLongDistanceEmission = userInputs.BusLongDistanceUserInput*multipliers.publicTransport.BusLongDistance
    TrainLongDistanceEmission = userInputs.TrainLongDistanceUserInput*multipliers.publicTransport.TrainLongDistance
    TrainShortDistanceEmission = userInputs.TrainShortDistanceUserInput*multipliers.publicTransport.TrainShortDistance
    MetroEmission = userInputs.MetroUserInput*multipliers.publicTransport.Metro
    TramEmission = userInputs.TramUserInput*multipliers.publicTransport.Tram
    TrainAbroadEmission = userInputs.TrainAbroadUserInput*multipliers.publicTransport.TrainAbroad
    BusAbroadEmission = userInputs.BusAbroadUserInput*multipliers.publicTransport.BusAbroad

class userEmissionsCarTraffic:      
    #kgCO2e
    unknownFuelEmission = userInputs.unknownFuelUserInput*multipliers.carTraffic.unknownFuel
    dieselEmission = userInputs.dieselUserInput*multipliers.carTraffic.diesel
    petrolEmission = userInputs.petrolUserInput*multipliers.carTraffic.petrol
    naturalGasEmission = userInputs.naturalGasUserInput*multipliers.carTraffic.naturalGas
    bioGasEmission = userInputs.bioGasUserInput*multipliers.carTraffic.bioGas
    electricCarEmission = userInputs.electricCarUserInput*multipliers.carTraffic.electricCar
    hybridEmission = userInputs.hybridUserInput*multipliers.carTraffic.hybrid
    chargingHybridEmission = userInputs.chargingHybridUserInput*multipliers.carTraffic.chargingHybrid
    
class userEmissionsBusinessAndClassTrips:
    #kgCO2e
    rentalBusEmission = userInputs.rentalBusUserInput*multipliers.businessAndClassTrips.rentalBus
    hotelStaysEmission = userInputs.hotelStaysUserInput*multipliers.businessAndClassTrips.hotelStays
    taxiEmission = userInputs.taxiUserInput*multipliers.businessAndClassTrips.taxi

class userEmissionsOtherVehicles:
    #kgCO2e
    MopedEmission = userInputs.MopedUserInput*multipliers.otherVehicles.Moped
    MopedCarEmission = userInputs.MopedCarUserInput*multipliers.otherVehicles.MopedCar
    MotorcycleEmission = userInputs.MotorcycleUserInput*multipliers.otherVehicles.Motorcycle
    ElectricKickboardRentEmission = userInputs.ElectricKickboardRentUserInput*multipliers.otherVehicles.ElectricKickboardRent
    ElectricBicycleEmission = userInputs.ElectricBicycleUserInput*multipliers.otherVehicles.ElectricBicycle



class publicTransport:
    #kgCO2e
    BusLongDistanceEmission = 0.053*1.2
    BusShortDistanceEmission = 0.053*1.2

    TrainLongDistanceEmission = 0
    TrainShortDistanceEmission = 0

    MetroEmission = 0
    TramEmission = 0

