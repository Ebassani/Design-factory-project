import multipliers

class userInputs:
    #Electricity(Megawatts)
    ElectricityconsumptionMWhUserInput=float(input("MegaWattsHour"))
    ZeroEmissionGreenElectricityUserInput=float(input("Percantage"))
    #heating(Megawatts)
    ElectricHeatinginput=float(input("MegaWattsHour"))
    DistrictHeatinginput=float(input("MegaWattsHour"))
    PercentageThatIsRenewableInput=float(input("Percantage"))
    #Cooling(Megawatts)
    DistrictCoolingInput=float(input("MegaWattsHour"))
    ElectricCoolingInput=float(input("MegaWattsHour"))
    #Airconditioning(Time)
    AirconditionPerDay=float(input("What type of Airconditioning?removal or removal and insertional both"))
    HoursPerDay=float(input("Hours"))
    #WasteDistribution(Wieght)
    MixedWasteInput=float(input("Kilograms"))
    EnergyWasteInput=float(input("Kilograms"))
    BioWasterInput=float(input("Kilograms"))
    CardboardWaste=float(input("Kilograms"))
    GlassWaste=float(input("Kilograms"))
    MetalWaste=float(input("Kilograms"))
    PlasticWaste=float(input("Kilograms"))
    PaperWaste=float(input("Kilograms"))
    ElectricAppliancesWaste=float(input("Kilograms"))
    HazardousWaste=float(input("Kilograms"))
    #ItemsWaste(Amount)
    #ITRelatedItems
    MobilephoneWaste=float(input("Pieces"))
    LaptopWaste=float(input("Pieces"))
    ComputerMonitorWaste=float(input("Pieces"))
    TabletWaste=float(input("Pieces"))
    DesktopComputerWaste=float(input("Pieces"))
    MultifunctionPrinterWaste=float(input("Pieces"))
    PrinterWaste=float(input("Pieces"))
    #furtniture(Amount)
    OfficeChairWaste=float(input("Pieces"))
    ChairWaste=float(input("Pieces"))
    TableWaste=float(input("Pieces"))
    ElectrictableWaste=float(input("Pieces"))
    #Material(Amount)
    PaperItemWasteWaste=float(input("Pieces"))
    EbookWaste=float(input("Pieces"))
    BookWaste=float(input("Pieces"))
    #OtherItems(Euros)
    ClearoutAmount=float(input("Euros"))
    InternetPhoneAmount=float(input("Euros"))
    PostiAmount=float(input("Euros"))

class userEmissionEnergy(multipliers.energy):
    #kgCO2e
    ElectricityconsumptionEmission = userInputs.ElectricityconsumptionMWhUserInput*multipliers.energy.AverageElectricity
    ZeroEmissionGreenElectricityEmission = userInputs.ZeroEmissionGreenElectricityUserInput*multipliers.energy.ZeroEmissionGreenElectricity

    
