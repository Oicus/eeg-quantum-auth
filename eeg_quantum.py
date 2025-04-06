import numpy as np
from scipy.signal import welch
from pylsl import StreamInlet, resolve_stream
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# EEG verilerini almak için LSL kullanarak bir akış çözün
print("Looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

def compute_spectral_entropy(signal, sf, band):
    """Spektral Entropi hesaplaması."""
    freqs, psd = welch(signal, sf, nperseg=256)
    psd = psd[(freqs >= band[0]) & (freqs <= band[1])]
    psd_norm = psd / np.sum(psd)
    spectral_entropy = -np.sum(psd_norm * np.log2(psd_norm))
    return spectral_entropy

def generate_quantum_nonce(entropy):
    """Kuantum nonce oluşturma."""
    n_qubits = int(entropy * 10)  # Entropiye göre qubit sayısını belirle
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

def main():
    """Ana fonksiyon."""
    sf = 250  # Örnekleme frekansı (Hz)
    band = [8, 12]  # Alfa bandı (Hz)
    print("Starting ζ-QGuard...")

    while True:
        chunk, _ = inlet.pull_chunk()
        if chunk:
            eeg_data = np.array(chunk)[:, 0]  # İlk kanal verisi
            entropy = compute_spectral_entropy(eeg_data, sf, band)
            print(f"ζ: {entropy:.2f}")
            nonce = generate_quantum_nonce(entropy)
            print(f"Nonce: {nonce}")

if __name__ == "__main__":
    main()
