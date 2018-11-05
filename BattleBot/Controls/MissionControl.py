import random
import sys
import traceback

import battlecode as bc
from enum import Enum
from .StrategyControl import *

class Missions(Enum):
    "Missions"

class MissionTypes(Enum):
    "Mission Types"

class Mission:
    "Selected Mission"

class MissionInformation:
    "Mission Information"
    def __init__(self):
        self.map_location = None
        self.unit_id = None
        self.unit = None
        self.isRocket = False

# Handles creation/management of missions
class MissionControl:
    "Mission Control"
    def __init__(self, gameControl, strategyControl, mapControl, researchControl):
        # Initialization Code Here

    # Adds a new mission
    def AddMission(self, mission, mission_type, mission_information):
        "Adds Mission"

    # Pops the highest priority mission for the selected unit from the queue and is returned
    def GetMission(self, unit_type):
        "Retrieves Mission"
        # Return mission based on type of unit
        # Mission will be selected based off of strategy selected

    def AddBuildingMission(self, structure):


        return builtMission

    def AddFactoryBlueprintMission(self, location):


        return builtMission

    def AddRocketBlueprintMission(self, location):


        return builtMission

    def GetMarsLocation(self):
        location = self.map_control.GetRandomMarsNode()
        return location

    def AddNewWorkerMission(self):
        # Determine what mission to assign based off of strategy

        return builtMission

    def AddNewHealerMission(self):
        # Determine what mission to assign based off of strategy

        return builtMission

    def AddNewCombatMission(self):

        return builtMission

    def AddNewFactoryMission(self):
        # Handle Production Chance based off of strategy

        return builtMission

    def AddNewRocketMission(self):

        return builtMission