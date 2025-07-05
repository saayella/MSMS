# 🏰 Mythical Species Preservation System (MSPS)

A fantasy-biological simulation platform where mythical creatures are cared for, studied, and preserved within a living sanctuary. This project blends magical lore with object-oriented design, AI-inspired behavior modeling, and visual simulation using Python.

---

## 🌍 Overview

**MSPS** is a simulation and management system for a mythical sanctuary that houses unique magical species like dragons, phoenixes, unicorns, and more. Each creature has its own personality, biological needs, magical abilities, and emotional states. The system models their daily lives, care routines, magical events, and behaviors — all in an interactive, expanding world.

---

## 🎯 Key Features

- 🐉 **Creature Management**: Define and track multiple mythical species with unique stats and magical behaviors.
- 💬 **Autonomous Behavior**: Creatures make decisions based on mood, energy, health, and personality.
- 🧙 **Sanctuary Simulation**: Time passes in days; users must manage care, resources, and events.
- 🎮 **Interactive Interface**: (In development) Graphical UI using PyGame to view, care, and interact with creatures.
- 🤖 **AI Integration**: Simple decision trees power creature behavior; expandable to predictive models or reinforcement learning.
- 🌦 **Dynamic Events**: Randomized magical phenomena, visitor interactions, and seasonal changes influence gameplay.
- 📦 **State Persistence**: Save and load sanctuary state using JSON (optional).

---

## 🧱 Project Structure

```bash
msps/
├── core/
│   ├── creature.py         # Base Creature class + subclasses (Dragon, Phoenix, etc.)
│   ├── sanctuary.py        # The main ecosystem and day simulator
│   └── caretaker.py        # Human caretakers with skill levels
│
├── ai/
│   ├── behavior.py         # Decision logic for creature actions
│   └── mood_predictor.py   # Optional ML for mood forecasting
│
├── ui/
│   ├── cli.py              # Command line version for early testing
│   └── pygame_main.py      # Visual simulation (in progress)
│
├── data/
│   └── creatures.json      # Sanctuary save/load data
│
└── main.py                 # Entry point
