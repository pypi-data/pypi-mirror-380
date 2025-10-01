from breesy.load import load_bdf

filename = "tests/bdf_dataset_paula/sub-01_ses-EEG_task-inner_eeg.bdf"
recording = load_bdf(filename)

print("====== Paula file ======")
print(recording)

filename = "tests/bdf_dataset_monika/sub-001_ses-01_task-meditation_eeg.bdf"
recording = load_bdf(filename)

print("====== Monika file ======")
print(recording)
