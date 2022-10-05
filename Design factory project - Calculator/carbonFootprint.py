from multipliers import *
from transport import *
from food import *
from infrastructure import *

def foodEmissions():
    return Co2OfMeat + Co2OfVeggieMeal + Co2OfVeganMeal + Dessert + Others

def transportEmissions():
    return flights + publicTransportEmission + publicTransportEmissionAbroad + BusinessAndClassTrips + Car

def infraEnergyEmissions():
    return EnergyEmission

def infraProcurementEmissions():
    return  userEmissionAquisition + userEmissionItem

def infraMixedWasteEmissions():
    return UserEmissionMixedWaste