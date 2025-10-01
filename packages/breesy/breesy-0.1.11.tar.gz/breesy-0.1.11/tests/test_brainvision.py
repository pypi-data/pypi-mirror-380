"""
Test script for loading ThingsEEG dataset files with Breesy.

Usage:
    1. Update the DATASET_PATH to point to your ThingsEEG data directory
    2. Run this script
"""

from os import path

from breesy.load import load_brainvision_eeg
from breesy.plots import plot_recording
from breesy.processing import mean_centering, remove_powerline_noise, remove_slow_drift

# Configuration
DATASET_PATH = "thingseeg_subj1/ses-01/eeg"  # Update this path
FILENAME = "sub-01_ses-01_task-test_eeg.vhdr"  # Or any other ThingsEEG file

file_path = path.join(DATASET_PATH, FILENAME)
recording = load_brainvision_eeg(file_path)

if recording.events:
    print("\nFirst 5 events:")
    for i, event in enumerate(recording.events[:5]):
        print(f"  Event {i + 1}: {event.name} at index {event.index}")
else:
    print("\nNo events in recording")

# Mean centering
print("Applying mean centering...")
centered = mean_centering(recording)

# Remove powerline noise
print("Detecting and removing powerline noise...")
filtered = remove_powerline_noise(centered)

# Remove slow drift
print("Removing slow drift...")
final = remove_slow_drift(filtered)

plot_recording(final, duration=5.0)