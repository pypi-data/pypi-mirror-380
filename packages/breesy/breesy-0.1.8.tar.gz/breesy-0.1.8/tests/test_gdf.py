import mne

from breesy.load import load_gdf

filename = "tests/bci_competition_2b/B0101T.gdf"

file = load_gdf(filename)

file_mne = mne.io.read_raw_gdf(filename, )

print("====== Breesy file ======")
print(file)
print("====== MNE file ======")
print(file_mne)