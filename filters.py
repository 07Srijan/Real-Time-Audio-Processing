import os
import numpy as np
from scipy.signal import butter, filtfilt
from scipy.io.wavfile import read, write

# ✅ Bandpass Filter Design Function
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

# ✅ Apply Bandpass Filter to Signal
def apply_bandpass_filter(signal, fs, lowcut=300, highcut=3400):
    b, a = butter_bandpass(lowcut, highcut, fs)
    return filtfilt(b, a, signal)

# ✅ File Paths
input_file = r"C:\Users\srija\Real-Time-Audio-processing\datasets\input_audio.wav"
output_file = r"C:\Users\srija\Real-Time-Audio-processing\datasets\filtered_audio.wav"

# ✅ Ensure File Exists
if not os.path.exists(input_file):
    print(f"❌ Error: File '{input_file}' not found!")
    exit()

# ✅ Load Recorded Audio
fs, noisy_signal = read(input_file)

# ✅ Handle Stereo Audio (Convert to Mono)
if len(noisy_signal.shape) > 1:
    noisy_signal = np.mean(noisy_signal, axis=1).astype(np.int16)

# ✅ Apply Bandpass Filter
filtered_signal = apply_bandpass_filter(noisy_signal, fs)

# ✅ Save Filtered Output
write(output_file, fs, filtered_signal.astype(np.int16))
print(f"✅ Filtered audio saved at: {output_file}")
