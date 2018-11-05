import random
import sys
import traceback

# Will keep track of enemy units/structures
# Frequently is updated by robots based upon their range of vision
# Keep in mind targets are not absolute, just last known locations
class EnemyTrackingControl:
    """This is the enemy tracking control"""
    def __init__(self, gameControl)
    self.game_control = gameControl