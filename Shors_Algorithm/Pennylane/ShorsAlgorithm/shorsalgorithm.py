import pennylane as qml
from pennylane import numpy as np

# Importing PennyLane and its numpy module for quantum computing operations

# Define the quantum circuit for Quantum Phase Estimation (QPE)
def qpe_circuit(n, target):
    # Initialize the quantum device with 'n' qubits plus one ancillary qubit
    dev = qml.device('default.qubit', wires=n+1)  

    # Define a quantum node (circuit) using the initialized device
    @qml.qnode(dev)
    def circuit():
        # Create the qubit registers: one for the phase estimation (qpe) and 'n' for the input state
        qpe = qml.Wires(0)  # Ancillary qubit for phase estimation
        qubits = [qml.Wires(i) for i in range(1, n+1)]  # Input qubits

        # Apply a Hadamard gate to the ancillary qubit to create a superposition
        qml.Hadamard(wires=qpe)

        # Apply controlled unitary operations to each input qubit, controlled by the ancillary qubit
        for qubit in qubits:
            qml.ControlledPhase(target, wires=[qubit, qpe])  # Controlled phase shift

        # Apply the inverse Quantum Fourier Transform (QFT) to the ancillary qubit
        qml.QFT(wires=qpe).inv()  # Inverse QFT for phase estimation

        # Return the ancillary qubit as the output of the circuit
        return qpe

    # Return the defined quantum node (circuit)
    return circuit()

# Define the main function for Shor's algorithm
def shors_algorithm(n, target):
    # Generate the quantum circuit for phase estimation
    qpe = qpe_circuit(n, target)

    # Measure the ancillary qubit to obtain the phase estimation result
    # This step is abstracted in PennyLane as qml.probs(), which returns the probabilities of measuring each basis state
    return qml.probs(wires=qpe)  # Measure the ancillary qubit

# Set the number to factorize and the target factor
N = 15  # Number to factorize
target = 7  # Target factor

# Run Shor's algorithm to find the factors of N
# Note: The number of qubits 'n' is determined by the ceiling of the logarithm base 2 of N, rounded up to the nearest integer
result = shors_algorithm(int(np.ceil(np.log2(N))), target)
print(result)
