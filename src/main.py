from qiskit import QuantumCircuit, execute, Aer
from qiskit.quantum_info import Statevector

from utils import approximate_x1, approximate_x0
from numpy import pi
import numpy as np

import pathlib
import typing
import os

def encode_x0(circuit : QuantumCircuit , x0) -> QuantumCircuit :
    """
    encode decimal representation to quantum circuit

    if a = [a1, a2, a3] , |psi> = |a1, a2, a3>

    params:
        circuit (qiskit.QuantumCircuit) : quantum circuit object
        x0 (float) : decimal to be approximated
    returns:
        circuit (qiskit.QuantumCircuit) : quantum circuit object after encoding
    """

    [ circuit.x(i) for i, a in enumerate(approximate_x0(x0)) if a == True ]
    circuit.barrier(label="encode x0")
    return circuit

def encode_x1(circuit : QuantumCircuit , x1) -> QuantumCircuit :
    """
    encode decimal representation to quantum circuit

    if b = [b1, b2, b3, b4] , |psi> = |b1, b2, b3, b4>

    params:
        circuit (qiskit.QuantumCircuit) : quantum circuit object
        x1 (float) : decimal to be approximated
    returns:
        circuit (qiskit.QuantumCircuit) : quantum circuit object after encoding
    """

    [ circuit.x(i + 3) for i, a in enumerate(approximate_x1(x1)) if a == True ]
    circuit.barrier(label="encode x1")
    return circuit


def add(circuit : QuantumCircuit) -> QuantumCircuit:
    """
    we can add the numbers on to the phase of the last qubit using conditional rotations where the rotation angle depends on the index of the qubit hopefully :)
    """
    
    [ circuit.crx(pi/(2**(i+1)), control_qubit=i, target_qubit=-1) for i in range(0, 3) ]  
    [ circuit.crx(pi/(2**(i+2)), control_qubit=i + 3, target_qubit=-1) for i in range(0, 3) ]    

    circuit.barrier(label="add")
    return circuit


def measure(circuit : QuantumCircuit) -> float:
    """
    state of last qubit |-1> = Rx(a0/2 + a1/4 + a2/8 + b0/4 + b1/8 + b2/16) |0> = Rx(a0/2 + (a1 + b0)/4 + (a2 + b1)/8 + b2/16)|0>
     = ( cos(theta/2)I -i sin(theta/2)X ) |0> = cos(theta/2) |0> -i sin(theta/2) |1>

     prob(|1>) = sin^2(theta/2)
     theta/2 = sin-1(prob(|1>))
    """
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(circuit, simulator).result()

    statevector = result.get_statevector(circuit)
    probs = Statevector(statevector).probabilities([7])
    print(probs)

    sum = np.arcsin(probs[-1]**0.5)/np.pi
    print(sum)
    print(abs(sum - (x0 + x1)))

    return sum

def workflow(file_path : typing.Union[str, os.PathLike]):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()

        lines = contents.split("\n")

        x0 = float(lines[0].replace(",", "."))
        x1 = float(lines[1].replace(",", "."))

        print("x0 =", x0)
        print("x1 =", x1)


        circuit = QuantumCircuit(8)
        circuit = encode_x0(circuit=circuit, x0=x0)
        print(circuit)
        circuit = encode_x1(circuit=circuit, x1=x1)
        print(circuit)

        circuit = add(circuit)
        print(circuit)
        measure(circuit)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

x0 = 0.375
x1 = 0.0075

circuit = QuantumCircuit(8)
circuit = encode_x0(circuit=circuit, x0=x0)
print(circuit)
circuit = encode_x1(circuit=circuit, x1=x1)
print(circuit)

circuit = add(circuit)

print(circuit)

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, simulator).result()

statevector = result.get_statevector(circuit)
probs = Statevector(statevector).probabilities([7])
print(probs)

sum = np.arcsin(probs[-1]**0.5)
print(sum)
print(abs(sum - (x0 + x1)))

workflow("../numbers.txt")

