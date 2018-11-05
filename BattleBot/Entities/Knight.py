import random
import sys
import traceback
import battle as bc
from Controls.MissionControl import *
from .IRobot import IRobot

class Knight(IRobot):
    """Thi sis the Knight Unit"""
    # change init definition to include any controllers needed in the constructor as we need them
    # it will eventually need access to targeting and pathfinding controls
    def __init__(self, gameControl, unitControl, pathfindingControl, missionControl, unit):
        super().__init__(gameControl, unitControl, pathfindingControl, missionControl, \
        unit, bc.UnitType.Knight, mapControl)
        self.mission = None
        self.target_location = None
        self.path = None
        self.is_garrisoned = False

    def run(self):
        self.update_mission()

        #TODO Refer to comments
        # If we have a mission. 
        # Determine which Mission is active and call appropriate self calls for the actions

    def is_enemy_sighted(self):
        """Alerts when enemy is spotted"""
        #TODO Determine if this unit is able to see an enemy
        #TODO Refactor code to IRobot so that all robots can sight enemies

    def try_attack(self, target_robot_id):
        """Tries to attack"""
        #TODO check is heat is low enough/comments below implement
        # Attack isn't ready, print message and False
        # Can't attack, print message and False
        # Attack!!! True

    def try_javelin(self, target_robot_id):
        """Tries to use Javelin Attack"""
        #TODO See Comments Below
        # Checks that the knight has been fully researched. 
        # If not False
        # Javelin isn't ready, print message and False
        # Cannot target enemy with Javelin
        # Use Javelin against Target True