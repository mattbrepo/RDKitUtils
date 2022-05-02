from rdkit import Chem

def printChiralArr(mol, xs):
  if len(xs) <= 0:
    print('None')
  else:
    for x in xs:
      (atom_idx, chiral_type) = x
      atom = mol.GetAtomWithIdx(atom_idx)
      print(atom.GetSymbol() + '('+ str(atom_idx) + '): ' + chiral_type)

def printChiral(SMILES):
  mol = Chem.MolFromSmiles(SMILES)
  # https://www.rdkit.org/docs/source/rdkit.Chem.html
  print('')
  print('SMILES: ' + Chem.MolToSmiles(mol))
  print('Chiral standard')
  printChiralArr(mol, Chem.FindMolChiralCenters(mol))
  print('Chiral forced-includeUnassigned')
  printChiralArr(mol, Chem.FindMolChiralCenters(mol,force=True,includeUnassigned=True))
  print('Chiral includeUnassigned')
  printChiralArr(mol, Chem.FindMolChiralCenters(mol,includeUnassigned=True))

#
# Main
#

printChiral('[C@H](Cl)(F)Br')