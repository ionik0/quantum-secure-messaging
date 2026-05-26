from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# ============================================================
# EXPERIMENT 4
# PRATAP ENTANGLEMENT ATTACK
# ============================================================

# We create:
# - 4 qubits
# - 3 classical bits
#
# Qubit ownership:
# q0 -> message qubit
# q1 -> Yuvraj's entangled qubit
# q2 -> Harsh's entangled qubit
# q3 -> Pratap's malicious ancilla qubit

qc = QuantumCircuit(4, 3)


# ============================================================
# STEP 1: PREPARE MESSAGE QUBIT
# ============================================================

# Prepare arbitrary quantum state

qc.ry(1.20, 0)

qc.barrier()


# ============================================================
# STEP 2: CREATE BELL PAIR
# ============================================================

# Entangle qubit 1 and qubit 2

qc.h(1)
qc.cx(1, 2)

qc.barrier()


# ============================================================
# STEP 3: YUVRAJ TELEPORTATION OPERATIONS
# ============================================================

qc.cx(0, 1)
qc.h(0)

qc.barrier()


# ============================================================
# STEP 4: YUVRAJ MEASURES HIS QUBITS
# ============================================================

qc.measure(0, 0)
qc.measure(1, 1)

qc.barrier()


# ============================================================
# STEP 5: PRATAP ENTANGLEMENT ATTACK
# ============================================================

# Pratap first creates superposition
# on his malicious ancilla qubit

qc.h(3)

# Pratap entangles his qubit
# with Harsh's qubit

qc.cx(2, 3)

qc.barrier()


# ============================================================
# STEP 6: HARSH APPLIES CLASSICAL CORRECTIONS
# ============================================================

with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

qc.barrier()


# ============================================================
# STEP 7: FINAL MEASUREMENT
# ============================================================

qc.measure(2, 2)


# ============================================================
# PRINT CIRCUIT
# ============================================================

print("\n=== QUANTUM TELEPORTATION CIRCUIT ===\n")
print(qc.draw('text'))


# ============================================================
# STATEVECTOR BEFORE MEASUREMENT
# ============================================================

state_circuit = QuantumCircuit(4)

state_circuit.ry(1.20, 0)

state_circuit.h(1)
state_circuit.cx(1, 2)

state_circuit.cx(0, 1)
state_circuit.h(0)

# Pratap attack

state_circuit.h(3)
state_circuit.cx(2, 3)

state = Statevector.from_instruction(state_circuit)

print("\n=== STATEVECTOR ===\n")
print(state)


# ============================================================
# RUN SIMULATION
# ============================================================

simulator = AerSimulator()

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

    # Rightmost classical bit corresponds to Harsh's qubit

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