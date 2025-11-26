from __future__ import annotations

"""
Basic tests for Smart Shovel control logic.

We verify that:
- safety barriers dominate (emergency stop, unsafe zone, bad sensors),
- assist mode reacts to human_force threshold,
- auto mode depends on being inside the work area.
"""

import pytest

from src.simulation.smart_shovel_sim import Mode, SensorState, SmartShovel


def test_emergency_stop_always_turns_motor_off():
    shovel = SmartShovel(mode=Mode.ASSIST)
    sensors = SensorState(
        emergency_stop=False,
        sensors_ok=True,
        safe_zone=True,
        in_work_area=True,
        human_force=1.0,
    )

    shovel.update(sensors)
    assert shovel.motor_on is True

    # Now emergency stop is pressed → motor must be off
    sensors.emergency_stop = True
    shovel.update(sensors)
    assert shovel.motor_on is False


def test_sensors_failure_turns_motor_off():
    shovel = SmartShovel(mode=Mode.AUTO)
    sensors = SensorState(
        emergency_stop=False,
        sensors_ok=True,
        safe_zone=True,
        in_work_area=True,
        human_force=0.0,
    )

    shovel.update(sensors)
    assert shovel.motor_on is True

    sensors.sensors_ok = False
    shovel.update(sensors)
    assert shovel.motor_on is False


def test_unsafe_zone_turns_motor_off():
    shovel = SmartShovel(mode=Mode.AUTO)
    sensors = SensorState(
        emergency_stop=False,
        sensors_ok=True,
        safe_zone=True,
        in_work_area=True,
        human_force=0.0,
    )

    shovel.update(sensors)
    assert shovel.motor_on is True

    sensors.safe_zone = False
    shovel.update(sensors)
    assert shovel.motor_on is False


def test_assist_mode_respects_force_threshold():
    shovel = SmartShovel(mode=Mode.ASSIST)
    sensors = SensorState(
        emergency_stop=False,
        sensors_ok=True,
        safe_zone=True,
        in_work_area=True,
        human_force=0.0,
    )

    shovel.update(sensors)
    assert shovel.motor_on is False

    sensors.human_force = shovel.ASSIST_FORCE_THRESHOLD + 0.1
    shovel.update(sensors)
    assert shovel.motor_on is True

    sensors.human_force = shovel.ASSIST_FORCE_THRESHOLD - 0.1
    shovel.update(sensors)
    assert shovel.motor_on is False


def test_auto_mode_requires_work_area():
    shovel = SmartShovel(mode=Mode.AUTO)
    sensors = SensorState(
        emergency_stop=False,
        sensors_ok=True,
        safe_zone=True,
        in_work_area=True,
        human_force=0.0,
    )

    shovel.update(sensors)
    assert shovel.motor_on is True

    sensors.in_work_area = False
    shovel.update(sensors)
    assert shovel.motor_on is False
