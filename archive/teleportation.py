from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer.noise import NoiseModel, depolarizing_error



#  we create 3 qubits
# 2 classical bits for yuvraj's measurements + 1 classical bit for Bob's final measurement

qc = QuantumCircuit(3, 3)
qc4= QuantumCircuit(4, 3)  #we introduce a new qubit for experiment 4

#we prepare message qubit in superposition state |+> = (|0> + |1>)/sqrt(2)
# Qubit 0 = message qubit
# Put it into superposition

qc.ry(1.20, 0)

# Barrier for readability
qc.barrier()



# we create bell pair ,Entangle qubit 1 and qubit 2

qc.h(1)
qc.cx(1, 2)

qc.barrier()



# we do yuvraj teleportation operations, yuvraj owns qubit 0 and qubit 1

qc.cx(0, 1)
qc.h(0)

qc.barrier()


#measure yuvraj quibit

qc.measure(0, 0)
qc.measure(1, 1)

qc.barrier()

#Pratap attack
qc.h(2)
qc.cx(2, 3)
qc.barrier()

#Harsh applyies corrections

# If qubit 1 measured 1 -> apply X
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)

# If qubit 0 measured 1 -> apply Z
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

qc.barrier()


#final measurement
qc.measure(2, 2)


# printing the circuit

print("\n=== QUANTUM TELEPORTATION CIRCUIT ===\n")
print(qc.draw('text'))


#statevector of the circuit before measurement, to see the state of the system after all operations but before measurement

# Create separate circuit without measurements
state_circuit = QuantumCircuit(3)

state_circuit.ry(1.20, 0)

state_circuit.h(1)
state_circuit.cx(1, 2)

state_circuit.cx(0, 1)
state_circuit.h(0)

# Get statevector
state = Statevector.from_instruction(state_circuit)

print("\n=== STATEVECTOR ===\n")
print(state)

# we introduce noise to the circuit to see how it affects the teleportation process

noise_model = NoiseModel()

# single-qubit noise
error_1 = depolarizing_error(0.02, 1)

# two-qubit noise
error_2 = depolarizing_error(0.05, 2)

noise_model.add_all_qubit_quantum_error(error_1, ['h', 'ry'])
noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

# simulation sprinting ( i wanna say running lol)

simulator = AerSimulator(noise_model=noise_model)

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)

result = job.result()

counts = result.get_counts()


# measurement results

print("\n=== MEASUREMENT RESULTS ===\n")

total_shots = sum(counts.values())

for outcome, count in counts.items():
    probability = count / total_shots
    print(f"State {outcome} : {count} counts | Probability = {probability:.4f}")

harsh_0 = 0
harsh_1 = 0

for outcome, count in counts.items():

    # rightmost bit = Harsh's qubit
    harsh_bit = outcome[0]

    if harsh_bit == '0':
        harsh_0 += count
    else:
        harsh_1 += count

print("\n=== HARSH QUBIT ANALYSIS ===\n")

total = harsh_0 + harsh_1

print(f"Harsh measured 0 : {harsh_0} times | Probability = {harsh_0/total:.4f}")
print(f"Harsh measured 1 : {harsh_1} times | Probability = {harsh_1/total:.4f}")


# histogram of the results
print("\nTeleportation simulation completed successfully.")
print("\nDisplaying histogram...\n")


plot_histogram(counts)

plt.show()