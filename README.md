# Quantum Secure Messaging Using Quantum Teleportation Under Noise and Attack Conditions

## Overview

This project implements and analyzes a quantum secure communication system using **quantum teleportation** in IBM’s Qiskit framework. The study evaluates how quantum states behave under ideal conditions, environmental noise, and adversarial attack scenarios.

The goal is to investigate both the **capabilities and vulnerabilities** of quantum teleportation as a secure communication primitive.

---

## Key Concepts

- Quantum Teleportation
- Quantum Entanglement (Bell States)
- Depolarizing Noise Models
- Quantum Circuit Simulation (Qiskit Aer)
- Adversarial Quantum Attacks
  - Basis Disturbance (Hadamard Attack)
  - Entanglement Injection Attack

---

## Experiments

The project is structured into the following experiments:

### 1. Bell State Verification
- Generation of a Bell pair using Hadamard + CNOT
- Verification of entanglement through correlated measurement outcomes

### 2. Baseline Quantum Teleportation
- Standard 3-qubit teleportation protocol
- Ideal noiseless simulation
- Evaluation of reconstruction accuracy

### 3. Noisy Quantum Teleportation
- Depolarizing noise model applied to gates
- Analysis of fidelity degradation under realistic conditions

### 4. Hadamard Disturbance Attack
- Unauthorized basis transformation on receiver qubit
- Evaluation of teleportation corruption under external interference

### 5. Entanglement Injection Attack
- Introduction of attacker-controlled qubit
- Unauthorized entanglement with receiver system
- Study of indirect quantum channel manipulation

---

## Tech Stack

- Python
- Qiskit
- Qiskit Aer Simulator
- Matplotlib (for result visualization)
- NumPy

---

---

## Installation
git clone https://github.com/your-username/quantum-secure-messaging.git
cd quantum-secure-messaging
pip install -r requirements.txt

# Requirements
qiskit
qiskit-aer
numpy
matplotlib

# Install manually if needed:

pip install qiskit qiskit-aer numpy matplotlib

How to Run

Run experiments individually:

python src/bell_state.py
python src/teleportation_baseline.py
python src/noisy_model.py
python src/attack_hadamard.py
python src/attack_entanglement.py

Results

The experiments demonstrate:

Successful entanglement generation in Bell states
Accurate teleportation under ideal conditions
Degradation of fidelity under depolarizing noise
Severe disruption under basis disturbance attacks
Statistical corruption under entanglement injection attacks

All results are stored in the results/ directory.

Key Findings
Quantum teleportation is highly sensitive to environmental noise
Basis disturbances significantly corrupt reconstructed states
Unauthorized entanglement can alter receiver-side statistics without direct measurement
Quantum communication systems require strict entanglement integrity protection
Research Context

This project is intended as a simulation-based study of quantum communication security using currently available quantum computing frameworks.

It does not require physical quantum hardware and is fully executable on classical systems via simulation.

Future Work
Implementation on real IBM Quantum hardware
Fidelity measurement using density matrices
Advanced attack modeling
Quantum Key Distribution (QKD) integration
Multi-node quantum network simulation
Error correction enhanced teleportation
References
Qiskit Documentation
IBM Quantum Platform
Nielsen & Chuang: Quantum Computation and Quantum Information
Bennett et al. (1993): Quantum Teleportation Protocol


Author
Nikhil Kumar
