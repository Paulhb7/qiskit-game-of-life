"""
Quantum Game of Life
Exploratory integration of quantum computing concepts with classical cellular automaton simulations. It demonstrates the potential for quantum algorithms to influence initial conditions in complex systems simulations.
This Python implementation leverages Qiskit for quantum computation to initialize Conway's Game of Life with quantum randomness, introducing a novel approach to generating the initial state of this cellular automaton. The evolution of the game follows the traditional rules, with cell states visualized through a dynamic Matplotlib animation.
Dependencies: Qiskit, NumPy, Matplotlib
by Paul Barbaste
Feb 2024
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from qiskit import QuantumCircuit, execute, Aer

def quantum_grid(grid_size):
    backend = Aer.get_backend('qasm_simulator')
    live_cells = np.zeros((grid_size, grid_size))

    for row in range(grid_size):
        for col in range(grid_size):
            qc = QuantumCircuit(2, 2)
            # Create entanglement
            qc.h(0)
            qc.cx(0, 1)
            # Apply rotation to create varying probabilities
            if np.random.rand() > 0.5:
                qc.ry(np.pi/3, 0)
            else:
                qc.ry(np.pi/1.1, 1)
            qc.measure([0, 1], [0, 1])
            # Execute circuit
            result = execute(qc, backend, shots=1, memory=True).result()
            memory = result.get_memory()[0]
            # Determine cell state
            if memory in ['11', '00']:
                live_cells[row, col] = 1
            else:
                live_cells[row, col] = 0
    return live_cells

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for row in range(N):
        for col in range(N):
            # Compute the number of live neighbors
            total = int((grid[row, (col-1)%N] + grid[row, (col+1)%N] +
                         grid[(row-1)%N, col] + grid[(row+1)%N, col] +
                         grid[(row-1)%N, (col-1)%N] + grid[(row-1)%N, (col+1)%N] +
                         grid[(row+1)%N, (col-1)%N] + grid[(row+1)%N, (col+1)%N])/1)
            # Apply Conway's rules
            if grid[row, col]  == 1:
                if (total < 2) or (total > 3):
                    newGrid[row, col] = 0
            else:
                if total == 3:
                    newGrid[row, col] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Main function
if __name__ == '__main__':
    # Grid size
    N = 50
    
    # Initialize the grid
    grid = quantum_grid(N)

    # Setup the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=250,
                                  save_count=50)

    plt.show()
