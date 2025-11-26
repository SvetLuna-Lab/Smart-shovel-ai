
---

## 4. Дизайн: `design/README.md`

Просто текстовый файл с описанием, куда потом можно добавить картинки/чертежи.

```markdown
# Design notes (Smart Shovel)

This folder collects high-level design materials for the **Smart Shovel** concept.

## Mechanical design

- Reinforced handle with space for:
  - force sensors (strain gauges),
  - wiring,
  - emergency stop button.
- Shovel blade (spade) with:
  - bracket for the actuator (electric motor + gearbox),
  - mounting points for proximity sensors (downwards / sideways).
- Optional support element or small wheel / mini-chassis:
  - to carry part of the weight,
  - to reduce load on the operator's back.

## Electronics

- Microcontroller or single-board computer (e.g. STM32 / Raspberry Pi / similar).
- Motor driver for the shovel actuator.
- Sensors:
  - force sensors on the handle,
  - IMU (accelerometer + gyroscope),
  - proximity / distance sensors (ultrasonic / IR / small lidar),
  - work-area marker sensor (optional, e.g. simple tags).

## Wiring and protection

- Cable routing inside or along the handle.
- Protective housings for:
  - electronics,
  - connectors,
  - sensors near the blade (dust / moisture / impact protection).

## Future additions

- CAD sketches of the mechanical structure.
- Schematics of the electronics and PCB.
- Block diagrams and sequence diagrams for control and safety logic.
