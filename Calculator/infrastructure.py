from functools import total_ordering
from operator import mul
from Calculator.multipliers import *

"""#class userInputs():

    #Electricity(Megawatts)

ElectricityconsumptionMWhUserInput=float(input("Whats your average Electricity Consumption?"))
ZeroEmissionGreenElectricityUserInput=float(input("How much percent of it is Renewable?"))
    #heating(Megawatts)

ElectricityHeatingInput=float(input("How much is your Electricity Consumption for Heating?"))
DistrictHeatingInput=float(input("How much Electricity is used in District Heating?"))
ZeroEmissionDistrictHeatingInput=float(input("What percent of the used Electricity is renewable?"))

    #Cooling(Megawatts)
    
DistrictCoolingInput=float(input("How much eletricity consumption you have for District Cooling?"))
ElectricCoolingInput=float(input("How much eletricity consumption you have for Electric Cooling?"))

    #Airconditioning(Time)


Airconditiontype=float(input("What type of Airconditioning?removal or removal and insertional both"))
HoursPerDay=float(input("Hours"))

    #WasteDistribution(Wieght)

MixedWasteInput=float(input("What is the amount(kg) of Mixed Waste you produce?"))
EnergyWasteInput=float(input("What is the amount(kg) of Energy Waste you produce?"))
BioWasteInput=float(input("What is the amount(kg) of Bio Waste you produce?"))
CardboardInput=float(input("What is the amount(kg) of Cardboard Waste you produce?"))
GlassInput=float(input("What is the amount(kg) of Mixed Glass you produce?"))
MetalInput=float(input("What is the amount(kg) of Mixed Metal you produce?"))
PlasticInput=float(input("What is the amount(kg) of Mixed Plastic you produce?"))
PaperInput=float(input("What is the amount(kg) of Paper Waste you produce?"))
ElectricityRecycableInput=float(input("What is the amount(kg) of Recycable Electric Waste you produce?"))
HazardousInput=float(input("What is the amount(kg) of Hazardous Waste you produce?"))

    #ItemsWaste/trash(Amount)
    #ITRelatedItems

phoneInput=float(input("What is the Amount(pieces) of Phone waste you produce?"))
LaptopInput=float(input("What is the Amount(pieces) of Laptop waste you produce?"))
computerScreenInput=float(input("What is the Amount(pieces) of Computer Screen waste you produce?"))
TabletInput=float(input("What is the Amount(pieces) of Tablets waste you produce?"))
DesktopComputerInput=float(input("What is the Amount(pieces) of Desktop Computers waste you produce?"))
MultifunctionPrinterInput=float(input("What is the Amount(pieces) of Multifuctions Printer waste you produce?"))
PrinterInput=float(input("What is the Amount(pieces) of Printer waste you produce?"))

    #furtniture(Amount)

OfficeChairInput=float(input("What is the Amount(pieces) of Office Chair waste you produce?"))
ChairInput=float(input("What is the Amount(pieces) of Chair waste you produce?"))
metalFrameTableInput=float(input("What is the Amount(pieces) of Metal Table waste you produce?"))
electricDeskInput=float(input("What is the Amount(pieces) of Electric Desk waste you produce?"))
    

    #Material(Amount)

paperKgInput=float(input("What is the Amount(Kg) of Paper waste you produce?"))
EbookInput=float(input("What is the Amount(pieces) of Ebook waste you produce?"))
BookInput=float(input("What is the Amount(pieces) of Book waste you produce?"))

    #OtherItems(Euros)

CleaningInput=float(input("What is the Amount(Euros) of Cleaning Equipment waste you produce?"))
internetAndPhonesInput=float(input("What is the Amount(Euros) of Internet and Phone waste you produce?"))
postalInput=float(input("What is the Amount(Euros) of Postal waste you produce?"))"""


def userEmissionEnergy(electricityconsumptionEmission, zeroEmissionGreenElectricityEmission, electricityHeatingEmission,
                       zeroEmissionDistrictHeatingEmission, districtCoolingEmission, electricCoolingEmission):
    # Electricity consumption
    # kgCO2e/MWh
    electricityconsumptionEmission = electricityconsumptionEmission * averageElectricity
    zeroEmissionGreenElectricityEmission = zeroEmissionGreenElectricityEmission * ZeroEmissionGreenElectricity

    electricityHeatingEmission = electricityHeatingEmission * DistrictHeating
    # DistrictHeatingEmission = DistrictHeatingInput*ElectricityHeating
    zeroEmissionDistrictHeatingEmission = zeroEmissionDistrictHeatingEmission * ZeroEmissionDistrictHeating

    districtCoolingEmission = districtCoolingEmission * DistrictCooling
    electricCoolingEmission = electricCoolingEmission * ElectricityCooling
    return electricityconsumptionEmission + zeroEmissionDistrictHeatingEmission + \
           zeroEmissionGreenElectricityEmission + electricityHeatingEmission + \
           electricCoolingEmission + districtCoolingEmission


def AircoditionarTypeuserInput(HoursPerDay, AircoditionarTypeAnswer):
    if (AircoditionarTypeAnswer == "removal"):
        return OnlyExit
    elif (AircoditionarTypeAnswer == "removal and insertional"):
        return EntryAndExit

    HoursPerDayEmission = HoursPerDay * AircoditionarTypeAnswer

    return HoursPerDayEmission


def userEmissionMixedWaste(MixedWasteEmission, EnergyWasteEmission, BioWasteEmission):
    MixedWasteEmission = MixedWasteEmission * mixedWaste
    EnergyWasteEmission = EnergyWasteEmission * energyWaste
    BioWasteEmission = BioWasteEmission * bioWaste
    # CardboardEmission = CardboardInput*Cardboard
    # GlassEmission = GlassInput*Glass
    # MetalEmission = MetalInput*Metal
    # PlasticEmission = PlasticInput*Plastic
    # PaperEmission = PaperInput*Paper
    # ElectricityRecycableEmission = ElectricityRecycableInput*ElectricityRecycable
    # HazardousEmission = HazardousInput*Hazardous

    TotalwasteCO2 = MixedWasteEmission + EnergyWasteEmission + BioWasteEmission
    return TotalwasteCO2
    # return MixedWasteEmission + EnergyWasteEmission + BioWasteEmission + CardboardEmission + GlassEmission + MetalEmission + PlasticEmission + PaperEmission + ElectricityRecycableEmission + HazardousEmission
    # class acquisitions:
    # kgCO2e/kpl


def userEmissionAquisitions():
    hello = True
    # phoneEmission = phoneInput*phone
    # LaptopEmission = LaptopInput*laptop
    # TabletEmission = TabletInput*tablet
    # DesktopComputerEmission = DesktopComputerInput*desktopComputer
    # MultifunctionPrinterEmission = MultifunctionPrinterInput*multifunctionPrinter
    # PrinterEmission = PrinterInput*printer

    # OfficeChairEmission = OfficeChairInput*officeChair
    # ChairEmission = ChairInput*chair
    # metalFrameTableEmission = metalFrameTableInput*metalFrameTable
    # electricDeskEmission = electricDeskInput*electricDesk

    # paperKgEmission = paperKgInput*paperKg
    # TotalItemAquisitionCO2 = phoneEmission + LaptopEmission + TabletEmission + DesktopComputerEmission + MultifunctionPrinterEmission + PrinterEmission + OfficeChairEmission + ChairEmission + metalFrameTableEmission + electricDeskEmission + paperKgEmission
    # return TotalItemAquisitionCO2
    # return phoneEmission + LaptopEmission + TabletEmission + DesktopComputerEmission + MultifunctionPrinterEmission + PrinterEmission + OfficeChairEmission + ChairEmission + metalFrameTableEmission + electricDeskEmission + paperKgEmission

    # item/kgCO2e


# userEmissionAquisition = userEmissionAquisitions()

def userEmissionItems():
    hello = True
    # EbookEmission = EbookInput*eBook
    # BookEmission = BookInput*book

    # CleaningEmission = CleaningInput*Cleaning
    # internetAndPhonesEmission = internetAndPhonesInput*internetAndPhones
    # postalEmission = postalInput*postal
    # TotalItemEmmission = EbookEmission + BookEmission + CleaningEmission + internetAndPhonesEmission + postalEmission
    # return TotalItemEmmission
    # return EbookEmission + BookEmission + CleaningEmission + internetAndPhonesEmission + postalEmission
