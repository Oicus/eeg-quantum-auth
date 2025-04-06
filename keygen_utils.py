from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram
import hashlib

def generate_quantum_nonce(entropy, n_qubits=2):
    """Kuantum nonce oluşturma."""
    n_qubits = max(2, int(entropy * 10))  # Entropiye göre qubit sayısını belirle
    qc = QuantumCircuit(n_qubits)
    for qubit in range(n_qubits):
        qc.h(qubit)  # Hadamard kapısı uygulama
    qc.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, simulator)
    qobj = assemble(compiled_circuit)
    result = simulator.run(qobj).result()
    counts = result.get_counts(qc)
    return counts

def derive_key_from_nonce(nonce, length=256):
    """Nonce'dan anahtar türetme."""
    nonce_str = ''.join([str(bit) for bit in nonce.keys()])
    hash_obj = hashlib.sha256(nonce_str.encode())
    key = hash_obj.hexdigest()[:length // 4]  # 256-bit anahtar
    return key

def save_key_to_file(key, filename='generated_keys.txt'):
    """Anahtarı dosyaya kaydetme."""
    with open(filename, 'a') as file:
        file.write(f"{key}\n")
