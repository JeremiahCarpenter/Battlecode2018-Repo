import battlecode as bc
import random
from Entities import *
from Controls.MissionControl import Missions

# Keeps a list of friendly units
# Iterates over all units, running their "Run" methods one at a time
# Can prioritize units by importance or any other activation order chosen
# Responsible for putting units back into the queue if a healer resets CD
class UnitControl:
    """Unit Control"""
    def __init__(self, gameControl, strategyControl, pathfindingControl, missionControl, mapControl, researchControl):
        self.gameControl = gameControl
        self.strategyControl = strategyControl
        self.pathfindingControl = pathfindingControl
        self.missionControl = missionControl
        self.mapControl = mapControl
        self.researchControl = researchControl

        self.robots = []
        self.structures = []

        self.workerCount = 0
        self.factoryCount = 0
        self.rocketCount = 0
        self.mustBuildRocket = False

    def UpdateUnits(self):
        """Updates Units"""
        self.__delete_killed_units()
        self.__add_unregistered_units()