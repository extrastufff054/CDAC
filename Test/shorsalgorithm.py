import pennylane as qml
import numpy as np
from math import gcd
from pennylane.templates import QuantumFourierTransform
from pennylane.templates import ControlledPhaseShift
from pennylane.templates import QuantumPhase
from pennylane.templates import MultiControlledXGate


def continued_fraction_expansion(x, max_iterations=1000):
    """
    Compute the continued fraction expansion of a number.
    
    Args:
        x (float): The number to compute the continued fraction expansion for.
        max_iterations (int): The maximum number of iterations to perform.
        
    Returns:
        list: The continued fraction expansion of x.
    """
    a = []
    for _ in range(max_iterations):
        a.append(int(x))
        if a[-1] == 0:
            break
        x = 1 / (x - a[-1])
    return a

def find_period(a, N):
    """
    Find the period of the modular exponentiation function.
    
    Args:
        a (int): The base of the exponentiation.
        N (int): The modulus.
        
    Returns:
        int: The period of the modular exponentiation function.
    """
    x = a
    a_list = continued_fraction_expansion(x)
    
    for r in range(1, len(a_list)):
        if (a ** a_list[r]) % N == 1:
            return a_list[r]
    
    return None

def shor_algorithm(N, a):
    """
    Implement Shor's algorithm.
    
    Args:
        N (int): The number to be factored.
        a (int): The base of the exponentiation.
    """
    # Determine the number of qubits needed
    n_qubits = 2 * qml.math.ceil(qml.math.log2(N))
    
    # Create the modular exponentiation circuit
    mod_exp_circuit = modular_exponentiation(a, N, n_qubits)
    
    # Execute the circuit and measure the output
    result = qml.execute(mod_exp_circuit, qml.device('default.qubit', wires=n_qubits))
    
    # Perform the classical post-processing steps
    period = find_period(a, N)
    
    # Find the factors of N
    if period is not None:
        if period % 2 == 0:
            x = (a ** (period // 2)) % N
            factors = [gcd(x - 1, N), gcd(x + 1, N)]
            return factors
    
    return None

N = 15
a = 7
factors = shor_algorithm(N, a)
if factors:
    print(f"The factors of {N} are: {factors}")
else:
    print(f"Failed to find factors for {N}")




