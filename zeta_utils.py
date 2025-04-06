import numpy as np
from scipy.signal import welch

def compute_spectral_entropy(signal, sf, band):
    """
    Computes the spectral entropy of the given signal.

    Parameters:
    - signal: EEG signal data (1D numpy array)
    - sf: Sampling frequency (Hz)
    - band: Frequency band of interest (e.g., [8, 12] for alpha band)

    Returns:
    - spectral_entropy: Spectral entropy value
    """
    freqs, psd = welch(signal, sf, nperseg=256)
    psd = psd[(freqs >= band[0]) & (freqs <= band[1])]
    psd_norm = psd / np.sum(psd)
    spectral_entropy = -np.sum(psd_norm * np.log2(psd_norm))
    return spectral_entropy

def filter_eeg_signal(signal, low_cut, high_cut, sf):
    """
    Applies a bandpass filter to the EEG signal.

    Parameters:
    - signal: EEG signal data (1D numpy array)
    - low_cut: Low cutoff frequency (Hz)
    - high_cut: High cutoff frequency (Hz)
    - sf: Sampling frequency (Hz)

    Returns:
    - filtered_signal: Filtered EEG signal
    """
    from scipy.signal import butter, filtfilt

    nyquist = 0.5 * sf
    low = low_cut / nyquist
    high = high_cut / nyquist

    b, a = butter(1, [low, high], btype='band')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def simulate_eeg_signal(duration=10, sf=250):
    """
    Simulates an EEG signal for testing purposes.

    Parameters:
    - duration: Duration of the signal (seconds)
    - sf: Sampling frequency (Hz)

    Returns:
    - eeg_signal: Simulated EEG signal (1D numpy array)
    """
    t = np.arange(0, duration, 1/sf)
    eeg_signal = np.sin(2 * np.pi * 10 * t) + np.random.randn(len(t)) * 0.5
    return eeg_signal
