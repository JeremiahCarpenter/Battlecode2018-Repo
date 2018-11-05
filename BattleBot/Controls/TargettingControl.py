import battlecode as bc
import random
import sys
import traceback

from Entities import *
from Controls.EnemyTrackingControl import *

# Given unit, target type to prioritize and an enemy list
# Determines highest priority location to move towards
# Can apply to workers looking for a build location, healers looking for allies, or rangers looking for targets
# Starting off focus simply by returning the closest or most valuable target
class TargettingControl:
    def __init__(self, gameControl, mapControl, strategyControl, unitControl, enemyTrackingControl):
        self.gameControl = gameControl
        self.mapControl = mapControl
        self.strategyControl = strategyControl
        self.unitControl = unitControl
        self.enemyTrackingControl  = enemyTrackingControl
        self.enemyRobots = []
        self enemyStructures = []
        self.ally = gameControl.team()
        self.roundLimit = 10

    # Updates units for death or if they need to be added to target queue
    def UpdateUnits(self):
        self.DeleteKilledUnits()
        self.AddUnregisteredEnemyUnits()
        self.RemoveRegisteredEnemyUnits()

    # Delete units that have died
    def RemoveKilledUnits(self):
        pass

    # Stores units and structures for enemy units
    def AddUnregisteredEnemyUnits(self):
        # if there are not enemy units print message
        
        # if isn't 0
        ## Iterate through enemyUnits; Iterate through enemyRobots; If array is at index 0 already registered
        ### print message and set currentRound to the 1st index break
        ## Otherwise for enemyStructures check if its registered otherwise register unit

        return

    # Removes an enemy unite from the queue
    def RemoveRegisteredEnemyUnits(self):
        # Have no enemies print message and return

        # Have enemies print how many and iterate through enemyRobots; if currentRound
        ## minus the unit greater or equal to round limit

    # Prioritizes enemy units for targeting
    def GetNearbyPriority(self, unit):
        # Set location, best score, score and assign sense nearby units to nearbyUnits then iterate through
        ## if unit is an enemy; Rocket 100, Knight 80, Worker 60 and rest 40
        ## if score higher then bestScore, assign score to bestScore and enemy to bestRobot
        return bestTarget

    # Sets global prioritization of enemy units
    def GetGlobalPriorityEnemy():
        bestScore = 0
        score = 0
        # Iterate through Queue and assign values for enemy unit priority
        # Rocket 100, Knight 80, Worker 60 and rest 40
        # if score higher than bestScore, assign score to bestScore and enemy to bestRobot
        return bestTarget

    def RegisterUnit(self, unit):
        # Handle Units based off of type to use the append method-NOTE- Don't forget structures
        # Will want to do condition check for each unit type and apped the Unit Type example below
        if unit.unit_type = bc.UnitType.Worker:
            self.enemyRobots.append(Worker(self.gameControl, self, unit))