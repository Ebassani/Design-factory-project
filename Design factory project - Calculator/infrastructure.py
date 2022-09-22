from operator import mul
import multipliers

def userInputs():

    #Electricity(Megawatts)

    ElectricityconsumptionMWhUserInput=float(input("MegaWattsHour"))
    ZeroEmissionGreenElectricityUserInput=float(input("Percantage"))
    #heating(Megawatts)

    ElectricityHeatingInput=float(input("MegaWattsHour"))
    DistrictHeatingInput=float(input("MegaWattsHour"))
    ZeroEmissionDistrictHeatingInput=float(input("Percantage"))

    #Cooling(Megawatts)
    
    DistrictCoolingInput=float(input("MegaWattsHour"))
    ElectricCoolingInput=float(input("MegaWattsHour"))

    #Airconditioning(Time)

    #AirconditionPerDay=float(input("What type of Airconditioning?removal or removal and insertional both"))
    #HoursPerDay=float(input("Hours"))

    #WasteDistribution(Wieght)

    MixedWasteInput=float(input("Kilograms"))
    EnergyWasteInput=float(input("Kilograms"))
    BioWasteInput=float(input("Kilograms"))
    CardboardInput=float(input("Kilograms"))
    GlassInput=float(input("Kilograms"))
    MetalInput=float(input("Kilograms"))
    PlasticInput=float(input("Kilograms"))
    PaperInput=float(input("Kilograms"))
    ElectricityRecycableInput=float(input("Kilograms"))
    HazardousInput=float(input("Kilograms"))

    #ItemsWaste/trash(Amount)
    #ITRelatedItems

    phoneInput=float(input("Pieces"))
    LaptopInput=float(input("Pieces"))
    computerScreenInput=float(input("Pieces"))
    TabletInput=float(input("Pieces"))
    DesktopComputerInput=float(input("Pieces"))
    MultifunctionPrinterInput=float(input("Pieces"))
    PrinterInput=float(input("Pieces"))

    #furtniture(Amount)

    OfficeChairInput=float(input("Pieces"))
    ChairInput=float(input("Pieces"))
    metalFrameTableInput=float(input("Pieces"))
    electricDeskInput=float(input("Pieces"))
    

    #Material(Amount)

    paperKgInput=float(input("Kilograms"))
    EbookInput=float(input("Pieces"))
    BookInput=float(input("Pieces"))

    #OtherItems(Euros)

    CleaningInput=float(input("Euros"))
    internetAndPhonesInput=float(input("Euros"))
    postalInput=float(input("Euros"))

def userEmissionEnergy():
    
    #Electricity consumption
    #kgCO2e/MWh
    ElectricityconsumptionEmission = userInputs.ElectricityconsumptionMWhUserInput*multipliers.energy.verageElectricity
    ZeroEmissionGreenElectricityEmission = userInputs.ZeroEmissionGreenElectricityUserInput*multipliers.energy.ZeroEmissionGreenElectricity

    ElectricityHeatingEmission = userInputs.ElectricityHeatingInput*multipliers.Heating.DistrictHeating
    DistrictHeatingEmission = userInputs.DistrictHeatingInput*multipliers.Heating.ElectricityHeating
    ZeroEmissionDistrictHeatingEmission = userInputs.ZeroEmissionDistrictHeatinginput*multipliers.Heating.ZeroEmissionDistrictHeating

    DistrictCoolingEmission = userInputs.DistrictCoolinginput*multipliers.Cooling.DistrictCooling
    ElectricCoolingEmission = userInputs.ElectricCoolingInput*multipliers.Cooling.ElectricityCooling

    #AirconditionPerDay
    #HoursPerDay

def userEmissionMixedWaste():
    
    MixedWasteEmission = userInputs.MixedWasteInput*multipliers.Trash.MixedWaste
    EnergyWasteEmission = userInputs.EnergyWasteInput*multipliers.Trash.EnergyWaste
    BioWasteEmission = userInputs.BioWasteInput*multipliers.Trash.BioWaste
    CardboardEmission = userInputs.CardboardInput*multipliers.Trash.Cardboard
    GlassEmission = userInputs.GlassInput*multipliers.Trash.Glass
    MetalEmission = userInputs.MetalInput*multipliers.Trash.Metal
    PlasticEmission = userInputs.PlasticInput*multipliers.Trash.Plastic
    PaperEmission = userInputs.PaperInput*multipliers.Trash.Paper
    ElectricityRecycableEmission = userInputs.ElectricityRecycableInput*multipliers.Trash.ElectricityRecycable
    HazardousEmission = userInputs.HazardousInput*multipliers.Trash.Hazardous

    #class acquisitions:
    #kgCO2e/kpl

def userEmissionAquisitions():

    phoneEmission = userInputs.phoneInput*multipliers.acquisitions.phone
    LaptopEmission = userInputs.LaptopInput*multipliers.acquisitions.Laptop
    TabletEmission = userInputs.TabletInput*multipliers.acquisitions.Tablet
    DesktopComputerEmission = userInputs.DesktopComputerInput*multipliers.acquisitions.DesktopComputer
    MultifunctionPrinterEmission = userInputs.MultifunctionPrinterInput*multipliers.acquisitions.MultifunctionPrinter
    PrinterEmission = userInputs.PrinterInput*multipliers.acquisitions.Printer


    OfficeChairEmission = userInputs.OfficeChairInput*multipliers.acquisitions.OfficeChair
    ChairEmission = userInputs.ChairInput*multipliers.acquisitions.Chair
    metalFrameTableEmission = userInputs.metalFrameTableInput*multipliers.acquisitions.metalFrameTable
    electricDeskEmission = userInputs.electricDeskInput*multipliers.acquisitions.electricDesk

    paperKgEmission = userInputs.paperKgInput*multipliers.acquisitions.paperKg
    
    #item/kgCO2e

def userEmissionItems():

    EbookEmission = userInputs.EbookInput*multipliers.item.Ebook
    BookEmission = userInputs.BookInput*multipliers.item.Book


    CleaningEmission = userInputs.CleaningInput*multipliers.item.Cleaning
    internetAndPhonesEmission = userInputs.internetAndPhonesInput*multipliers.item.internetAndPhones
    postalEmission = userInputs.postalInput*multipliers.item.postal