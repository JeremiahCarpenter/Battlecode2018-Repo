import random
import sys
import traceback

# Used for tracking Friendly Units
# Utilitzes Map and Strategy Controls
# Handles build priority/locations
# Store these into build queue
# The worker class will make use of this to determine what to build next

class BuildControl:
    """This is the build control"""
    def __init__(self, gameControl, mapControl, strategyControl):
        self.game_control = gameControl
        self.map_control = mapControl
        self.strategy_control = strategyControl