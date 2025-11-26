from __future__ import annotations

"""
Minimal simulation model for the Smart Shovel concept.

This is NOT a physical model, but a small, testable state machine that encodes
the main ideas:

- human chooses the mode and work area;
- system checks safety conditions (emergency stop, sensors, safe zone, work area);
- motor runs only when conditions are satisfied.

The goal is to make the safety logic explicit and easy to reason about
in unit tests and documentation.
"""

from dataclasses import dataclass
from enum import Enum, auto


class Mode(str, Enum):
    """Operating modes for the smart shovel."""

    MANUAL = "manual"
    ASSIST = "assist"
    AUTO = "auto"


@dataclass
class SensorState:
    """
    Snapshot of sensor readings.

    Attributes:
        emergency_stop: True if emergency stop button is pressed.
        sensors_ok: True if all critical sensors report valid data.
        safe_zone: True if no human body part or obstacle is in the danger zone.
        in_work_area: True if the shovel is inside the allowed work area.
        human_force: Estimated human effort on the handle (arbitrary units).
    """

    emergency_stop: bool = False
    sensors_ok: bool = True
    safe_zone: bool = True
    in_work_area: bool = True
    human_force: float = 0.0


class SmartShovel:
    """
    Simple logic model for Smart Shovel.

    Key rules:

    - Emergency stop always dominates: if pressed → motor off.
    - If sensors are not OK → motor off (fail-safe).
    - If zone is not safe → motor off.
    - In AUTO mode, shovel must also be inside the allowed work area.
    - In ASSIST mode, motor runs only if human_force is above a threshold.
    - In MANUAL mode, motor is normally off (or could be used for light assistance).

    In this simulation we keep only one boolean state: `motor_on`.
    """

    # Minimal force threshold to consider that the operator is really digging.
    ASSIST_FORCE_THRESHOLD: float = 0.5

    def __init__(self, mode: Mode = Mode.MANUAL) -> None:
        self.mode: Mode = mode
        self.motor_on: bool = False

    def set_mode(self, mode: Mode) -> None:
        """Change operating mode."""
        self.mode = mode
        # As a safety measure, turning off the motor on mode change.
        self.motor_on = False

    def update(self, sensors: SensorState) -> None:
        """
        Update motor_on state based on current mode and sensor readings.

        This method encodes the "safety first" behaviour:
        - any critical violation → motor_off;
        - otherwise, mode-specific logic is applied.
        """
        # Hard safety barriers
        if sensors.emergency_stop or not sensors.sensors_ok or not sensors.safe_zone:
            self.motor_on = False
            return

        if self.mode == Mode.MANUAL:
            # In manual mode we keep the motor off in this simple model.
            # In a more advanced version, this could lightly compensate weight.
            self.motor_on = False

        elif self.mode == Mode.ASSIST:
            # Assist only when operator clearly applies force AND zone is safe.
            if sensors.human_force > self.ASSIST_FORCE_THRESHOLD:
                self.motor_on = True
            else:
                self.motor_on = False

        elif self.mode == Mode.AUTO:
            # Auto mode allowed only inside work area and with safe conditions.
            if sensors.in_work_area:
                self.motor_on = True
            else:
                self.motor_on = False

        else:
            # Unknown mode → safest behaviour.
            self.motor_on = False

    def step(self, sensors: SensorState) -> bool:
        """
        Convenience method:

        - updates the internal state,
        - returns the new `motor_on` value.

        This is useful in small simulations or REPL experiments.
        """
        self.update(sensors)
        return self.motor_on
