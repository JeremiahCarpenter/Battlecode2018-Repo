import battlecode as bc
import random
import sys
import traceback

class IStructure:
    """This is the IStructure interface"""
    def __init__(self, gameControl, unitControl, unit, missionControl):
        self.gameControl = gameControl
        self.unitControl = unitControl
        self.missionControl = missionControl
        self.unit = unit
        self.mission = None

    def UpdateMission(self):
        """Updates the Mission"""
        if(self.unit.structure_is_built() and self.mission == None):
            self.mission = self.missionControl.get_mission(self.unit.unitType)
            self.mission_start_round = self.gameControl.round()
            self.target_location = None
            print("Structure with id {} obtaining new mission {}".format(\
                self.unit.id, self.mission.action))
