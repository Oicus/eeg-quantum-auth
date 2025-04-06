# ζ-QGuard: Brainwave-Driven Quantum Security System

A real-time authentication and key generation system based on EEG signals and quantum randomness.  
Built using OpenBCI + Python + Qiskit.

## 🧠 What is ζ-QGuard?

ζ-QGuard computes the entropy of your brainwaves (EEG) and maps it to a ζ value,  
which dynamically configures a quantum circuit. The circuit measurement produces nonces,  
which are used to generate a secure session key. Your **mind is your password**.

## ⚙️ System Architecture

![Architecture](media/architecture_diagram.png)

- EEG input (OpenBCI Cyton / Ganglion via LSL)
- ζ-calculation (Spectral Entropy from alpha band)
- Quantum Nonce generation (Qiskit)
- SHA-256-based key derivation
- Real-time logging + privilege classification

## 🔬 Example ζ Tracking

![Zeta Tracking](media/zeta_graph.png)

## 🚀 Getting Started

```bash
pip install -r requirements.txt
python zqguard_realtime.py
