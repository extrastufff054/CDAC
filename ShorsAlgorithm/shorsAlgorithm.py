from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.tools.visualization import plot_histogram

backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots = 1000)
my_shor = Shor(N=15, a = 2, quantum_instance = quantum_circuit)

Shor.run(my_shor)

def c_amod15(a,power) :
    U = QuantumCircuit(4)
    for iteration in range(power) : 
        U.swap(2,3)
        U.swap(1,2)
        U.swap(0,1)
        for q in range(4):
            U.x(q)

    U = U.to_gate()
    U.name = "%i^%i mod 15" %(a.power)
    c_U = U.control()
    return c_U

n_count = 8
a = 7

def qft_dagger(n) : 
    q0 = QuantumCircuit(n)
    for qubit in range(n//2) :
        qc.swap(qubit, n-qubit-1)

    for j in range(n) : 
        for m in range(j) :
            qc.cul(-np.pi/float(2**(j-m), m, j))

    qc.name = "QFT dagger"
    return qc

qc = QuantumCircuit(n_count + 4, n_count)

for q in range(n_count) : 
    qc.h(q)

qc.x(3+n_count)

for q in range(n_count):
    qc.append(c_amod15(a, 2**q),[q]+[i+n_count for i in range(4)])

qc.append(qft_dagger(n_count), range(n_count))

qc.measure(range(n_count), range(n_count))
qc.draw('text')


