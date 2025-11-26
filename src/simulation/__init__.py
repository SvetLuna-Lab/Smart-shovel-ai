"""
Simulation subpackage for Smart Shovel.

Contains a very simple, testable model of:
- operating modes (Manual / Assist / Auto),
- safety conditions,
- motor control logic.
"""

from .smart_shovel_sim import Mode, SensorState, SmartShovel

__all__ = ["Mode", "SensorState", "SmartShovel"]
