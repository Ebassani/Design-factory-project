class flights:
    shortFlightUnder463km = 0.2595*2+0.2595*2
    longFligtsOverHomelandOver463km = (0.178*2)+(0.178*0.2)
    longFlightsAbroadOver463km = (0,149*2)+(0.149*0.2)
    longFlightsOver3700km = (0.135*2)+(0.135*0.2)
    
class carTraffic:
    #kgCO2e/km
    unknownFuel = 0.152*1.2
    diesel = 0.141*1.2
    petrol = 0.159*1.2
    naturalGas = 0.0701*1.2
    bioGas = 0.95*4.5/100
    electricCar = 0.0188/100*(AverageElectricity)+0.00195
    hybrid = 0.114*1.2
    chargingHybrid = 0.084*1.2

class businessAndClassTrips:
    #kgCO2e/hkm
    carFerryAndCruiseShip = 0.144*1.2
    #kgCO2e/€
    rentalBus = 0.574*1.2
    hotelStays = 0.18
    taxi = 0.18

class acquisitions:
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