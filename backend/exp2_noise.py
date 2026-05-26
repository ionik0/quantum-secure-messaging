from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit_aer.noise import NoiseModel, depolarizing_error
import matplotlib.pyplot as plt


# ============================================================
# EXPERIMENT 2
# QUANTUM TELEPORTATION WITH NOISE
# ============================================================

qc = QuantumCircuit(3, 3)


# ============================================================
# PREPARE MESSAGE QUBIT
# ============================================================

qc.ry(1.20, 0)

qc.barrier()


# ============================================================
# CREATE BELL PAIR
# ============================================================

qc.h(1)
qc.cx(1, 2)

qc.barrier()


# ============================================================
# YUVRAJ TELEPORTATION OPERATIONS
# ============================================================

qc.cx(0, 1)
qc.h(0)

qc.barrier()


# ============================================================
# YUVRAJ MEASURES HIS QUBITS
# ============================================================

qc.measure(0, 0)
qc.measure(1, 1)

qc.barrier()


# ============================================================
# HARSH APPLIES CORRECTIONS
# ============================================================

with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

qc.barrier()


# ============================================================
# FINAL MEASUREMENT
# ============================================================

qc.measure(2, 2)


# ============================================================
# PRINT CIRCUIT
# ============================================================

print("\n=== QUANTUM TELEPORTATION CIRCUIT ===\n")
print(qc.draw('text'))


# ============================================================
# STATEVECTOR
# ============================================================

state_circuit = QuantumCircuit(3)

state_circuit.ry(1.20, 0)

state_circuit.h(1)
state_circuit.cx(1, 2)

state_circuit.cx(0, 1)
state_circuit.h(0)

state = Statevector.from_instruction(state_circuit)

print("\n=== STATEVECTOR ===\n")
print(state)


# ============================================================
# CREATE NOISE MODEL
# ============================================================

noise_model = NoiseModel()

# Single qubit depolarizing noise
error_1 = depolarizing_error(0.02, 1)

# Two qubit depolarizing noise
error_2 = depolarizing_error(0.05, 2)

noise_model.add_all_qubit_quantum_error(error_1, ['h', 'ry'])
noise_model.add_all_qubit_quantum_error(error_2, ['cx'])


# ============================================================
# RUN NOISY SIMULATION
# ============================================================

simulator = AerSimulator(noise_model=noise_model)

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)

result = job.result()

counts = result.get_counts()


# ============================================================
# MEASUREMENT RESULTS
# ============================================================

print("\n=== MEASUREMENT RESULTS ===\n")

total_shots = sum(counts.values())

for outcome, count in counts.items():
    probability = count / total_shots
    print(f"State {outcome} : {count} counts | Probability = {probability:.4f}")


# ============================================================
# HARSH QUBIT ANALYSIS
# ============================================================

harsh_0 = 0
harsh_1 = 0

for outcome, count in counts.items():

    harsh_bit = outcome[0]

    if harsh_bit == '0':
        harsh_0 += count
    else:
        harsh_1 += count

print("\n=== HARSH QUBIT ANALYSIS ===\n")

total = harsh_0 + harsh_1

print(f"Harsh measured 0 : {harsh_0} times | Probability = {harsh_0/total:.4f}")
print(f"Harsh measured 1 : {harsh_1} times | Probability = {harsh_1/total:.4f}")


# ============================================================
# DISPLAY HISTOGRAM
# ============================================================

print("\nTeleportation simulation completed successfully.")
print("\nDisplaying histogram...\n")

plot_histogram(counts)

plt.show()