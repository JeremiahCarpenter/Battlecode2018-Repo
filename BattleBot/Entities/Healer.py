import random
import sys
import traceback
import battlecode as bc
from Controls.MissionControl import *
from .IRobot import IRobot

class Healer(IRobot):
    """This is the healer robot"""
    # Change init definition to include any controls needed in the constructor as neeeded
    # EX: eventually need to access the targeting and pathfinding controls
    def __init__(self, gameControl, unitControl, pathfindingControl, missionControl, unit, mapControl):
        super().__init__(gameControl, unitControl, pathfindingControl, \
        missionControl, unit, bc.UnitType.Healer, mapControl)

    def run(self):
        self.update_mission()
        # Tons of checks will be implemented here to suit the capabilities for the healer

    def TryHeal(self, targetUnitId):
        "Tries to heal units"
        #TODO Check if heat is too low
        # Can't heal print message and return False

        # call for healing
        return True

    def TryOvercharge(self, targetUnitId):
        """Tries to user overcharge"""
        # Check for overcharge research


        # Check cooldown of Overcharge ability


        # Check to see if you can overcharge a given unit

        # Call Overcharge ability
        return True