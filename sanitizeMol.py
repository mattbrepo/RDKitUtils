from rdkit import Chem

def print_SMILES_std(SMILES):
  mol = Chem.MolFromSmiles(SMILES, sanitize = True) # note: sanitize would be True by default!
  print('SMILES: ' + Chem.MolToSmiles(mol))

#
# Main
#

print_SMILES_std('C[N-][N+]#N')
print_SMILES_std('CN=[N+]=[N-]')