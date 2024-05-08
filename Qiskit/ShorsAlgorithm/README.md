# Shor's Algorithm Implementation

This code is an implementation of Shor's algorithm, a quantum algorithm used to efficiently factor large integers. The code uses the Qiskit library, a popular open-source software development kit for working with quantum computers and quantum circuits.

## Shor's Algorithm

Shor's algorithm is a quantum algorithm that can efficiently factor large integers, a task that is considered computationally difficult for classical computers. The algorithm works by finding the period of a function related to the number being factored, and then using this information to find the factors.

## Pseudo-code

1. Choose a random number `a` that is coprime to the number `N` to be factored.
2. Compute the order `r` of `a` modulo `N` using the quantum part of the algorithm.
3. If `r` is even and `a^(r/2) ≡ -1 (mod N)`, then `gcd(a^(r/2) - 1, N)` and `gcd(a^(r/2) + 1, N)` are the factors of `N`. Otherwise, go back to step 1.

## Workflow

1. Import the necessary libraries and modules from Qiskit.
2. Set up the quantum backend and the quantum instance.
3. Create a Shor object with the number `N` to be factored and the chosen `a` value.
4. Run the Shor algorithm using the `run()` method.
5. Define the `c_amod15()` function, which creates a controlled version of the modular exponentiation operation.
6. Define the `qft_dagger()` function, which implements the inverse quantum Fourier transform.
7. Create a quantum circuit with `n_count + 4` qubits, where `n_count` is the number of qubits used for the period-finding part of the algorithm.
8. Initialize the first `n_count` qubits with Hadamard gates.
9. Apply the controlled modular exponentiation operations to the circuit.
10. Apply the inverse quantum Fourier transform to the first `n_count` qubits.
11. Measure the first `n_count` qubits and display the circuit.

The key steps in this implementation are:

1. Choosing a random `a` value that is coprime to `N`.
2. Implementing the controlled modular exponentiation operation using the `c_amod15()` function.
3. Applying the inverse quantum Fourier transform to the circuit using the `qft_dagger()` function.
4. Measuring the output of the circuit to obtain the period `r`, which is then used to factor the number `N`.

This implementation of Shor's algorithm demonstrates the power of quantum computing in solving computationally difficult problems, such as integer factorization, which has important applications in cryptography and other fields.
