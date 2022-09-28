from functools import total_ordering
from operator import mul
import multipliers

class userInputs():

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

    """Airconditiontype=float(input("What type of Airconditioning?removal or removal and insertional both"))
    HoursPerDay=float(input("Hours"))"""

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
    postalInput=float(input("What is the Amount(Euros) of Postal waste you produce?"))

def userEmissionEnergy():
    
    #Electricity consumption
    #kgCO2e/MWh
    ElectricityconsumptionEmission = userInputs.ElectricityconsumptionMWhUserInput*multipliers.AverageElectricity
    ZeroEmissionGreenElectricityEmission = userInputs.ZeroEmissionGreenElectricityUserInput*multipliers.ZeroEmissionGreenElectricity

    ElectricityHeatingEmission = userInputs.ElectricityHeatingInput*multipliers.DistrictHeating
    DistrictHeatingEmission = userInputs.DistrictHeatingInput*multipliers.ElectricityHeating
    ZeroEmissionDistrictHeatingEmission = userInputs.ZeroEmissionDistrictHeatingInput*multipliers.ZeroEmissionDistrictHeating

    DistrictCoolingEmission = userInputs.DistrictCoolingInput*multipliers.DistrictCooling
    ElectricCoolingEmission = userInputs.ElectricCoolingInput*multipliers.ElectricityCooling
    totalElectricC02 = ElectricityconsumptionEmission + ZeroEmissionDistrictHeatingEmission + ZeroEmissionGreenElectricityEmission + ElectricityHeatingEmission + DistrictHeatingEmission + ElectricCoolingEmission + DistrictCoolingEmission
    print(totalElectricC02)
    return totalElectricC02

    #return ElectricityconsumptionEmission + ZeroEmissionDistrictHeatingEmission + ZeroEmissionGreenElectricityEmission + ElectricityHeatingEmission + DistrictHeatingEmission + ElectricCoolingEmission + DistrictCoolingEmission


"""def AircoditionarTypeuserInput(AircoditionarTypeAnswer):
    if (AircoditionarTypeAnswer == "removal"):
        return multipliers.OnlyExit
    elif(AircoditionarTypeAnswer == "removal and insertional"):
        return multipliers.EntryAndExit
    
    HoursPerDayEmission = userInputs.HoursPerDay*multipliers.Ventilation.HoursPerDay
    
    return HoursPerDayEmission"""
    
def userEmissionMixedWaste():
    
    MixedWasteEmission = userInputs.MixedWasteInput*multipliers.mixedWaste
    EnergyWasteEmission = userInputs.EnergyWasteInput*multipliers.energyWaste
    BioWasteEmission = userInputs.BioWasteInput*multipliers.bioWaste
    CardboardEmission = userInputs.CardboardInput*multipliers.Cardboard
    GlassEmission = userInputs.GlassInput*multipliers.Glass
    MetalEmission = userInputs.MetalInput*multipliers.Metal
    PlasticEmission = userInputs.PlasticInput*multipliers.Plastic
    PaperEmission = userInputs.PaperInput*multipliers.Paper
    ElectricityRecycableEmission = userInputs.ElectricityRecycableInput*multipliers.ElectricityRecycable
    HazardousEmission = userInputs.HazardousInput*multipliers.Hazardous
    
    TotalwasteCO2 = MixedWasteEmission + EnergyWasteEmission + BioWasteEmission + CardboardEmission + GlassEmission + MetalEmission + PlasticEmission + PaperEmission + ElectricityRecycableEmission + HazardousEmission
    print(TotalwasteCO2)
    return TotalwasteCO2
    #return MixedWasteEmission + EnergyWasteEmission + BioWasteEmission + CardboardEmission + GlassEmission + MetalEmission + PlasticEmission + PaperEmission + ElectricityRecycableEmission + HazardousEmission
    #class acquisitions:
    #kgCO2e/kpl

def userEmissionAquisitions():

    phoneEmission = userInputs.phoneInput*multipliers.phone
    LaptopEmission = userInputs.LaptopInput*multipliers.laptop
    TabletEmission = userInputs.TabletInput*multipliers.tablet
    DesktopComputerEmission = userInputs.DesktopComputerInput*multipliers.desktopComputer
    MultifunctionPrinterEmission = userInputs.MultifunctionPrinterInput*multipliers.multifunctionPrinter
    PrinterEmission = userInputs.PrinterInput*multipliers.printer

    

    OfficeChairEmission = userInputs.OfficeChairInput*multipliers.officeChair
    ChairEmission = userInputs.ChairInput*multipliers.chair
    metalFrameTableEmission = userInputs.metalFrameTableInput*multipliers.metalFrameTable
    electricDeskEmission = userInputs.electricDeskInput*multipliers.electricDesk

    paperKgEmission = userInputs.paperKgInput*multipliers.paperKg
    TotalItemAquisitionCO2 = phoneEmission + LaptopEmission + TabletEmission + DesktopComputerEmission + MultifunctionPrinterEmission + PrinterEmission + OfficeChairEmission + ChairEmission + metalFrameTableEmission + electricDeskEmission + paperKgEmission
    print(TotalItemAquisitionCO2)
    return TotalItemAquisitionCO2
    #return phoneEmission + LaptopEmission + TabletEmission + DesktopComputerEmission + MultifunctionPrinterEmission + PrinterEmission + OfficeChairEmission + ChairEmission + metalFrameTableEmission + electricDeskEmission + paperKgEmission
    
    #item/kgCO2e

def userEmissionItems():

    EbookEmission = userInputs.EbookInput*multipliers.eBook
    BookEmission = userInputs.BookInput*multipliers.book


    CleaningEmission = userInputs.CleaningInput*multipliers.Cleaning
    internetAndPhonesEmission = userInputs.internetAndPhonesInput*multipliers.internetAndPhones
    postalEmission = userInputs.postalInput*multipliers.postal
    TotalItemEmmission = EbookEmission + BookEmission + CleaningEmission + internetAndPhonesEmission + postalEmission
    print(TotalItemEmmission)
    return TotalItemEmmission
    #return EbookEmission + BookEmission + CleaningEmission + internetAndPhonesEmission + postalEmission 

userEmissionEnergy()
userEmissionMixedWaste()
userEmissionAquisitions()
userEmissionItems()