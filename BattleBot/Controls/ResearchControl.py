import random
import sys
import traceback

import battlecode as bc
from .StrategyControl import *

# Keeps track of research progress
# Research determined by strategy selected
# Research can be added individually
# Research can only be removed from the queue, cancelling ALL progress
class ResearchControl:
    """Research Control"""
    def __init__(self, gameControl, strategyControl):
        self.gameControl = gameControl
        self.strategyControl = strategyControl

    def isRocketResearch(self):

    def UpdateResearchQueue(self):

    def AddResearchToQueue(self, branch):

    def ClearResearchQueue(self):

    def isCurrentResearchNearCompletion(self):
        # Returns a bool if the current number of rounds left 
        # for current research is less than or equal to a percentage

    def GetResearchBranchTurns(self, branch, level):
        # Nested If to determine unit's current level and duration of the next upgrade

    def GetBranchName(self, branch):
        # Retrieves branch name based off branch Enum