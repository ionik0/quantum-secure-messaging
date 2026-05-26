from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import transpile
import matplotlib.pyplot as plt

# Create quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Apply CNOT gate
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Print circuit
print(qc)

# Simulate circuit
simulator = AerSimulator()

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1000)

result = job.result()

counts = result.get_counts()

# Print measurement results
print("\nMeasurement Results:")
print(counts)

# Plot histogram
plot_histogram(counts)

plt.show()