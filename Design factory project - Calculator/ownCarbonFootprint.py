from multipliers import *
from transport import *
from food import *
from infrastructure import *
from currentState import *

def schoolTrips():
    schoolTrips = (input("Have you been on school trips(Yes or No) "))
    if (schoolTrips == "Yes"):
        return SchoolCarbonFootprintsPerParticipant
    if (schoolTrips == "No"):
        return 0
SchoolTrips = schoolTrips()

def ownTransportEmissions():
    schoolTrips = (input("Have you been on school trips(Yes or No) "))
    if (schoolTrips == "Yes"):
        return Car + PersonalPublicTransport + OtherEmissions + UserEmissionsOtherVehicles + SchoolTrips
    if (schoolTrips == "No"):
        return Car + PersonalPublicTransport + OtherEmissions + UserEmissionsOtherVehicles

def ownInfraEmissions():
    ownInfraEmissions = (input("(Yes or No) "))
    if (ownInfraEmissions == "Yes"):
        return (EnergyEmission + UserEmissionMixedWaste + userEmissionAquisition + userEmissionItem)/usersOfBuilding
    if (ownInfraEmissions == "No"):
        return 0
OwnInfraEmissions = ownInfraEmissions()

def energyConsumption():
    if (OwnInfraEmissions > 0):
        return EnergyEmission/usersOfBuilding
    if (OwnInfraEmissions == 0):
        return 0

def wasteTreatment():
    if (OwnInfraEmissions > 0):
        return UserEmissionMixedWaste/usersOfBuilding
    if (OwnInfraEmissions == 0):
        return 0

def Acquisitions():
    if (OwnInfraEmissions > 0):
        return (userEmissionAquisition+userEmissionItem)/usersOfBuilding
    if (OwnInfraEmissions == 0):
        return 0
