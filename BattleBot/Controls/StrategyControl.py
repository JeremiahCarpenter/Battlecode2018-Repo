from enum import Enum

# Uses all known information from various controls to determine current strategy
# Stores values from enum for easy access
# Use {"Default"} until we are prepared for something more complex
class StrategyControl:
    "Strategy Control"
    def __init__(self, gameControl, mapControl, enemyTrackingControl):
        self.gameControl = gameControl
        self.mapControl = mapControl
        self.enemyTrackingControl = enemyTrackingControl

        self.macroStrategy = MacroStrategies.Default
        self. unitStrategy = UnitStrategies.Default

    # Set default strategy based upon current map
    def SetDefaultStrategy(self):
        """Sets Default Strategy"""
        self.macroStrategy = MacroStrategies.Default
        self.unitStrategy = UnitStrategies.Default

    # Update strategy based upon changes to map, enemies spotted or any other criteria
    def UpdateStrategy(self):


class MacroStrategies(Enum):
    """Macro-Strats"""
    # Will decide upon strategies as group

class UnitStrategies(Enum):
    "Unit Strats"
    # Will decide upon strategies as group