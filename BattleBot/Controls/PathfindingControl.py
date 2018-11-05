import random
import sys
import traceback
import battlecode as bc
import collections import deque
from .GraphNode import GraphNode

# For a given robot and destination determines the best route to take
# Returns an array of direction to the selected unit
# Unit will follow direction until it determines it needs a new path
# More efficient than running pathfinding every turn and more adaptive than running it once
#TODO Need comparisons from different forms of pathfinding if we have time
class PathfindingControl:
    def __init__(self, gameControl, mapControl):
        self.gameControl = gameControl
        self.mapControl = mapControl
        self.plan = []
        self.Directions = [bc.Direction.North, bc.Direction.East, bc.Direction.South, bc.Direction.West]
        self.earthBlockedNodes = []

    def FindPathDestination(self, planet, currentLocation, destination):
        
        return path

    def Explore(self, planet, node):

        return discovered
    
    def ChangeDirection(self, planet, node, directoin):

        return newLocation

    def AlreadyExplored(self, node, explored):
        
        return isExplored

    def AlreadyFrontier(self, node, frontier):

        return notInFrontier

    def IsNodeVacant(self, node, blockedLocations):

        return nodeVacant

    def blockEarthNodes(self):

        return blockedNodes