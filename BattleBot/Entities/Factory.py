import random
import sys
import traceback
import battlecode as bc
from Controls.MissionControl import *
from .IStructure import IStructure

class Factory(IStructure):
    """This is the factory"""
    def __init__(self, gameControl, unitControl, unit, missionControl):
        super(Factory, self).__init__(gameControl, unitControl, unit, missionControl)

        self.roundStartProduction = 0
        self.isWorking = False
        self.directions = list(bc.Direction)
        self.workerUnits = None

    def run(self):
        self.UpdateMission()
        # Implement code below to handle the run-time behavior of the factory

    def try_reproduce_robot(self, unit_type):
        """This tries to produce robots"""
        # If factory is producing print message about being occupied and how long is left False

        # Call Produce robot
        return True

    def try_garrison(self, unit_id):
        """Tries to garrison unit"""
        #TODO creat garrison units function        
        return True

    def try_unload_units(self):
        """"Tries to unload the units"""
        # Set Garrison and count garrisoned
        # If units are garrisoned print how many and choose random direction
        ## if its able to unload units garrisoned pass the unit and direction print out the unit True
        ## Otherwise fails to unload and print message False

        # Otherwise False