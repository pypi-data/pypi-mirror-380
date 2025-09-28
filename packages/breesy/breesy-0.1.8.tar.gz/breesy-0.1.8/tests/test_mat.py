from breesy.load import load_mat

filename = "tests/matlab_dataset_karolina/FADHD.mat"
filename2 = "tests/matlab_dataset_karolina/MADHD.mat"

file = load_mat(filename)
print("====== Breesy file 1 ======")
print(file)

file2 = load_mat(filename2)
print("====== Breesy file 2 ======")
print(file2)