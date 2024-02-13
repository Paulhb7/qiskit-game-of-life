# Quantum Game of Life

## Overview
The Quantum Game of Life is a simulation that combines the classic Conway's Game of Life with quantum computing principles. Using Qiskit, IBM's open-source quantum computing framework, this project initializes the game board with states determined by quantum randomness, introducing a new layer of complexity to the cellular automaton. This simulation demonstrates the interplay between quantum computing and classical simulation rules, visualized through a dynamic grid.

https://github.com/Paulhb7/qiskit-game-of-life/assets/42540782/a7dfac12-7bd3-4372-8d58-18197eba76dc


## Installation

### Prerequisites
- Python 3.x
- pip

### Dependencies
The project relies on the following Python libraries:
- Qiskit
- NumPy
- Matplotlib

To install the necessary dependencies, run the following command in your terminal:

```sh
pip install qiskit numpy matplotlib qiskit-aer
```

## Usage

To run the Quantum Game of Life, execute the main script from your terminal:

```sh
python QuantumLife.py
```

This command launches a window displaying the initial quantum-generated game board. The simulation progresses according to the classical Game of Life rules, with each cell's fate determined by its neighbors. The board evolves over time, showcasing the unique outcomes of quantum randomness.

## Features

- **Quantum Initialization**: Leverages quantum circuits to generate the initial states of cells, providing a unique starting point for each simulation.
- **Classical Game Dynamics**: Applies Conway's Game of Life rules to simulate the evolution of cells based on classical computational models.
- **Visualization**: Utilizes Matplotlib to animate the game's progression, allowing users to visually track the development of cellular patterns.
