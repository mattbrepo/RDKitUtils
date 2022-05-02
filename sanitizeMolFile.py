from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem

def get_mol(SMILES):
  mol = Chem.MolFromSmiles(SMILES)
  return mol

#
# Main
#

# read molecules from a file
f = open('molecules.smi', "r")
lines = f.readlines()
f.close()
  
for smiles in lines:
  # get SMILES string
  smiles = smiles.replace('\n', '').replace('\r', '')
  # get RDKit molecule
  mol = get_mol(smiles)
  # sanitize molecule and convert it to SMILES
  smiles2 = Chem.MolToSmiles(mol)
  print(smiles2)