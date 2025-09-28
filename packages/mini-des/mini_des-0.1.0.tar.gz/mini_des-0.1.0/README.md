# mini-des: A Minimalist Agent-Based Discrete-Event Simulation Engine

[![PyPI Version](https://badge.fury.io/py/mini-des.svg)](https://badge.fury.io/py/mini-des)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`mini-des` is a lightweight Python framework for building simulations. It combines the computational efficiency of **Discrete-Event Simulation (DES)** with the flexible and intuitive modeling paradigm of **Agent-Based Modeling (ABM)**.

This engine empowers you to model systems as a collection of autonomous agents that interact with each other over time, making it ideal for simulating scenarios in logistics, manufacturing, autonomous systems, and more.

## 🔬 Core Philosophy: Agent-Based Modeling on an Event-Driven Core

`mini-des` is built on a hybrid philosophy that gives you the best of both worlds:

*   **Event-Based Core:** The simulation is driven by an event queue managed by a Min-Heap. The simulation clock doesn't advance in fixed steps; it "jumps" directly to the time of the next scheduled event. This is efficient for systems that have periods of inactivity.

*   **Agent-Based Paradigm:** You model your system's components as `SimulationEntity` objects, or "agents". Each agent is autonomous: it encapsulates its own state and defines its own behavior. There is no central "god" object dictating actions.

*   **Decentralized Interaction:** Agents communicate and react to each other through a **publish-subscribe mechanism**. An agent can subscribe to specific events from another agent. When that event occurs, the subscribing agent is notified and can react accordingly. This decentralized approach provides flexibility and makes it easy to model complex, emergent behaviors.

## ✨ Key Features

*   **Hybrid Simulation Model:** Enjoy the performance of DES while building your models with the intuitive, object-oriented approach of ABM.

*   **Continuous Visualization Support:** Although the engine is discrete, it's designed for continuous visualization. By implementing the optional `interpolate()` method on your agents, you can calculate and display an agent's state (e.g., its physical position during a "Move" event) at any given moment, creating smooth animations.

*   **Intelligent Event Cancellation:** Agents can cancel events that are already scheduled. The engine is smart about this: before an event is cancelled, it will automatically call the agent's `interpolate()` method. This ensures the agent's state is updated to the precise moment of cancellation, preventing logical inconsistencies.

*   **Flexible API:** The API is designed to be simple and explicit, allowing you to focus on your model's logic rather than boilerplate code.

## 📦 Installation

```bash
pip install mini-des
```

For developers, or to run the examples, it's recommended to perform an editable install from the cloned repository:

```bash
# 1. Clone the repository
git clone https://github.com/littleQiu22/minimalist-discrete-event-simulation-engine.git
cd minimalist-discrete-event-simulation-engine

# 2. Create and activate a virtual environment (recommended)

# 3. Perform an editable install
pip install -e .
```

## 🚀 Example: Production Line Simulation

This project includes a detailed example simulating a modern automated production line.

### Scenario

The simulation features one autonomous robot and multiple manufacturing machines located at different positions along a track.
- The **robot's** goal is to keep all machines supplied with raw materials.
- It starts at a **staging area (position 0)** where it can pick up raw materials and drop off finished products.
- Each **machine** has its own production cycle time. When it receives raw material, it starts manufacturing. Once finished, it holds the product and waits for the robot to pick it up.
- The robot must autonomously decide which machine to serve next, managing its multi-slot tray to transport both raw materials and finished products efficiently.

### How to Run the Example

Ensure you have performed the installation steps above. Then, from the **root directory of the project**, run the following command:

```bash
python -m examples.production_line.main
```

You will see a real-time text-based dashboard in your terminal, showing the status of the robot and each machine, updated multiple times per second.

## 🛠️ Getting Started: Building Your First Agent

To build your own agent-based model, the main task is to create classes that inherit from `SimulationEntity` and implement its core methods.

Here is the basic structure of an agent:

```python
from minides import SimulationEntity, SimulationEvent

class MyAgent(SimulationEntity[MyAgentData]):
    # MyAgentData would be a dataclass holding this agent's state

    def handle_event(self, event: SimulationEvent) -> None:
        # --- MANDATORY ---
        # This method is called when one of THIS agent's own events is finished.
        # e.g., "My 'Move' event just completed, and my position is now X, 
        # what should I do next?"
        if event.type == "Move":
            # Decide what to do after moving
            self.schedule_event(type="DoWork", end_time=self.current_time + 10, data={})

    def on_event_received(self, event: SimulationEvent) -> None:
        # --- OPTIONAL ---
        # This is called when an agent you SUBSCRIBED to has an event.
        # e.g., "I just received a notification that 'OtherAgent'
        # finished its 'TaskComplete' event. I should react to that."
        pass

    def interpolate(self) -> None:
        # --- OPTIONAL ---
        # This calculates the agent's state for the current simulation time,
        # usually for an in-progress event.
        # e.g., "My 'Move' event is 50% done. My current position
        # should be halfway between the start and end points."
        # This is crucial for smooth visualization and correct state on cancellation.
        pass
```

### Core API Reference

When creating your agents, you will primarily interact with these three methods:

1.  **`handle_event(self, event)` (Mandatory Override)**
    - **Purpose:** Defines the agent's core reactive logic to its *own* completed actions. This is where you chain events together to create complex behaviors.
    - **When it's called:** Automatically by the engine when an event scheduled by this agent reaches its `end_time`.

2.  **`interpolate(self)` (Optional Override)**
    - **Purpose:** Calculates the agent's state at the current simulation time, typically for an event that is still in progress.
    - **When it's called:**
        - By the engine just before an event is cancelled via `cancel_event()`.
        - Manually by you at any time if you need the precise current state for visualization.

3.  **`on_event_received(self, event)` (Optional Override)**
    - **Purpose:** Defines how an agent reacts to events generated by *other* agents it is subscribed to. This is the foundation of inter-agent communication.
    - **When it's called:** Automatically by the engine whenever a subscribed event occurs, based on the `SubscriptionConfig` you provided.

To make an agent perform an action, you schedule an event using `self.schedule_event(...)`.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.