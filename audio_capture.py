import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Define recording parameters
fs = 44100  # Sample rate
duration = 5  # Recording duration in seconds

# ✅ Define absolute file path
base_dir = r"C:\Users\srija\Real-Time-Audio-processing"
dataset_dir = os.path.join(base_dir, "datasets")
filename = os.path.join(dataset_dir, "input_audio.wav")

# ✅ Ensure 'datasets' folder exists
os.makedirs(dataset_dir, exist_ok=True)

print("🎤 Recording audio...")
audio_signal = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Wait until recording is finished
print("✅ Recording complete!")

# ✅ Debugging: Check if audio is recorded
if np.sum(audio_signal) == 0:
    print("❌ Error: No audio recorded! Check your microphone.")
else:
    # ✅ Save the recorded audio
    write(filename, fs, audio_signal)
    print(f"✅ Audio saved successfully at: {filename}")

# ✅ Verify file creation
if os.path.exists(filename):
    print("✅ File successfully created!")
else:
    print("❌ Error: File was NOT created!")
