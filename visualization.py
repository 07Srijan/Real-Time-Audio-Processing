import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

def plot_fft(signal, fs, title):
    """Plot FFT spectrum of a signal."""
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1/fs)  # Correct frequency axis
    fft_signal = np.abs(fft(signal))

    plt.figure(figsize=(10, 4))
    plt.plot(freq[:N//2], fft_signal[:N//2])  # Plot only positive frequencies
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()

# ✅ Load noisy signal
fs, noisy_signal = wavfile.read(r"C:\Users\srija\Real-Time-Audio-processing\datasets\input_audio.wav")
fs, filtered_signal = wavfile.read(r"C:\Users\srija\Real-Time-Audio-processing\datasets\filtered_audio.wav")

# ✅ Convert Stereo to Mono if needed
if len(noisy_signal.shape) > 1:
    noisy_signal = np.mean(noisy_signal, axis=1).astype(np.int16)

if len(filtered_signal.shape) > 1:
    filtered_signal = np.mean(filtered_signal, axis=1).astype(np.int16)

# ✅ Plot FFT before and after filtering
plot_fft(noisy_signal, fs, "Before Noise Filtering")
plot_fft(filtered_signal, fs, "After Noise Filtering")

