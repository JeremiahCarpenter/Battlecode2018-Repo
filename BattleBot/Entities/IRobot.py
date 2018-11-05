import battlecode as bc
import random
import sys
import traceback
from Controls.MissionControl import *

class IRobot:
    """This is the IRobot"""
    def __init__(self, gameControl, unitControl, pathfindingControl, missionControl, unit, unitType, mapControl):
        self.gameControl = gameControl
        self.unitControl = unitControl
        self.pathfindingControl = pathfindingControl
        self.missionControl = missionControl
        self.mapControl = mapControl

        # Reference to the Battlecode unit object that the server side code tracks
        self.unit = unit
        self.unit_type = unitType

        # Current mission dictates the robot's actions for the turn
        self.mission = None

        # Location that the robot will move to, regardless of what the mission type is
        self.target_location = None
        self.path = None

        # List of directions to reach the target location
        self.path = None

        # Round that the current mission started on
        self.mission_start_round = 0

        # To allow for Missions that have a secondary action
        self.perform_second_action = False

        # Last Position
        self.lastPosition = None
        self.directions = list(bc.Direction)

    # Actoins that will be ran at the end of every robot's turn
    def run(self):
        """This will run the unit actions at the end of the turn"""
        pass

    def update_mission(self):
        """Updates the Mission"""
        # If there is no mission, get one based on the unit type
        # Set round, target location
        # If mission isn't mining print obtaining mission

    def reset_mission(self):
        "Resets the mission"
        self.performSecondAction = False
        self.mission = None

    #TODO Check that the next direction is still possible. If not, recalculate
    def update_path_to_target(self):
        """Updates path to target"""
        # Unit isn't garrisoned, have target location and has path that isn't 0
        # set path through method call from pathfinding control

    def follow_path(self):
        """Allows you to follow the path"""
        # have a path > 0 set direction; 
        ## check if not garrisoned and try to move a direction - pop path
        ## Otherwise pick random movement and update path to target

        # else:
        # pass
        

    def isStuck(self):
        # If not position false

        # If last position equal to current True

        # Otherwise False

    def has_reached_destination(self):
        """Shows if you have reach destination"""
        # If target location is nothing False

        # Else - Nested if(first True, second False)

    def try_move(self, direction):
        """Tries to move"""
        # If not ready to move False

        # If can't move False

        return True

    def try_attack(self, targetRobotId):
        "Tries to attack"
        #TODO check to see if heat is low enough
        # If can't attack False

        return True

    def self_destruct(self):

    # Default Missions
    def idle(self):
        """Checks to see if unit is idle"""

    def one_random_movement(self):
        """Gives a random movement"""
        # set direction
        # Ready to move, can move, and move robot calls

    def random_movement(self):
        """Walks robot randomly"""
        # Unit has no location
        ## Path is none or equal to 0

        # Has reached destination; reset mission

    def destroy_target(self):
        """Attempts to destroy target"""
        # hasn't performed second action and has no location
        ## has not path or equal to 0

        # has reached destination try attacking and reset mission
        # Otherwise follow path
