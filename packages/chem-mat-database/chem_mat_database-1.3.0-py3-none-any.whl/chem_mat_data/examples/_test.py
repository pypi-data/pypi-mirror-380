from chem_mat_data import load_smiles_dataset

dataset = load_smiles_dataset("zinc250")
print(dataset.head())
print(len(dataset))




