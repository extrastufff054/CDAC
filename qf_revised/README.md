# Quantum Integer Factorization with Babai's and Schnorr's Algorithms

## Overview
This project implements a quantum algorithm for integer factorization by leveraging classical algorithms such as Babai's Nearest Plane Algorithm and Schnorr's Algorithm. The process involves solving the Closest Vector Problem (CVP) on a lattice using a Quantum Approximate Optimization Algorithm (QAOA) and refining the results through classical algorithms.

## Methodology

### Quantum Approximate Optimization Algorithm (QAOA)
QAOA is used to optimize the parameters of the Hamiltonian corresponding to the CVP on a lattice. This quantum algorithm helps find an initial approximate solution to the CVP by mapping the variables to Pauli-Z terms of quantum states.

### Babai's Nearest Plane Algorithm
Babai's algorithm provides an approximate solution to the CVP by projecting the target vector onto the lattice basis and rounding the coefficients to the nearest integers. This serves as the first step in our classical refinement process.

### Schnorr's Algorithm
Schnorr's algorithm refines the approximate solution obtained from Babai's algorithm. It uses lattice basis reduction techniques to improve the quality of the solution, ultimately leading to a more accurate factorization of the integer.

### Why Babai and Schnorr?
- **Babai's Algorithm**: Provides a quick and efficient approximate solution to the CVP, serving as a good starting point for further refinement.
- **Schnorr's Algorithm**: Enhances the approximate solution by applying advanced lattice reduction techniques, leading to a more accurate result.

## Implementation Guide

### 1. Prerequisites
Ensure you have Python and necessary libraries installed:
- Pennylane
- NumPy
- A lattice reduction library that supports LLL and Gram-Schmidt operations (e.g., fpylll, SageMath)(I've used Scipy)

### 2. File Structure
```
project_root/
├── babai.py
├── schnorr.py
├── main.py
├── README.md
```

### 3. Implement Babai's Algorithm
Create a file named `babai.py`:
```python
# babai.py
def babais_algorithm(lattice_basis, target_vector):
    #Implementation for Baibai's Algorithm
```

### 4. Implement Schnorr's Algorithm
Create a file named `schnorr.py`:
```python
# schnorr.py
def schnorr_algorithm(approx_vector):
    # Implement Schnorr's algorithm logic here
    refined_vector = ...  # Your implementation here
    return refined_vector
```

### 5. Quantum Circuit and Optimization
In `main.py`, implement the quantum circuit and integrate Babai's and Schnorr's algorithms

### 6. Running the Program
1. Ensure all dependencies are installed.
2. Run the `main.py` script:
```sh
python main.py
```

### 7. Understanding the Output
- The program will print the optimized parameters from the QAOA.
- The refined vector from the lattice reduction process will be displayed, which can be analyzed for integer factorization.

