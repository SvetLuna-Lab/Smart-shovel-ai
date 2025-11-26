# Smart Shovel – AI-assisted safety shovel concept
![CI](https://github.com/SvetLuna-Lab/Smart-shovel-ai/actions/workflows/ci.yml/badge.svg)

**Smart Shovel** is a concept of a semi-robotic hand tool  
designed to reduce physical load and improve safety during digging work.

The idea is simple:

- a shovel with **sensors** (force, position, proximity),
- a small **actuator** to assist the operator,
- a **controller** with basic AI-style logic,
- and strict **safety limits** so the system never acts freely against the operator.

The system is intended as an educational example for:

- occupational safety / safety engineering (BJD),
- introductory robotics and cyber-physical systems,
- discussions about *“AI as a tool, not a replacement for human decisions”*.

## Goals

- Reduce physical strain on the worker.
- Decrease the risk of injuries (hits to legs, accidental contact with people).
- Lower the chance of damaging underground utilities.
- Keep the **human in control** of decisions (where and why to dig).

## Operating modes

- **Manual** – behaves almost like a normal shovel; the actuator minimally compensates weight.
- **Assist** – when the operator clearly applies force and the zone is safe,  
  the actuator adds part of the effort to protect the back and joints.
- **Auto / Pattern** – semi-automatic digging along a predefined trench/shape  
  inside a marked safe area, with continuous obstacle checks and emergency stop.

## Safety concept

Smart Shovel includes:

- obstacle and human presence detection in the impact zone;
- work-area boundaries (no digging outside a safe polygon);
- emergency stop button;
- logic: on any anomaly → **motor off**, system goes to a safe state.

In this concept, the AI/logic does **not** decide “to dig or not” instead of the person.  
The human sets the mode and the work area; the system executes the task with built-in safety barriers.

## Documentation

See the Russian documentation for details:

- `docs/overview_ru.md` – project overview and goals
- `docs/safety_analysis.md` – risk and safety analysis
- `docs/control_logic.md` – control logic and operating modes
