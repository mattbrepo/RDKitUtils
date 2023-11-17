from rdkit import Chem
from rdkit.Chem import rdmolfiles

# https://www.rdkit.org/docs/source/rdkit.Chem.rdmolfiles.html#rdkit.Chem.rdmolfiles.SmilesMolSupplier
suppl = rdmolfiles.SmilesMolSupplier('a.smi', nameColumn=0, titleLine=False)
for mol in suppl:
  print('SMILES: ' + Chem.MolToSmiles(mol) + ': ' + str(mol.GetNumAtoms()))
