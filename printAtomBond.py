from rdkit import Chem

def get_mol(SMILES):
  mol = Chem.MolFromSmiles(SMILES)
  return mol

def print_atom_bond(SMILES):
  mol = get_mol(SMILES)
  print('')
  print('SMILES: ' + Chem.MolToSmiles(mol))
  print_atom(mol)
  print_bond(mol)

def print_atom(mol):
  print('===== Atoms')
  for i in range(len(mol.GetAtoms())):
    atom = mol.GetAtomWithIdx(i)
    s = atom.GetSymbol() + '(' + str(i) + ')'
    #s = s + 'z: ' + str(atom.GetAtomicNum()) + ' '
    #s = s + 'hy: ' + str(atom.GetHybridization()) + ' '
    print(s)

def print_bond(mol):
  print('===== Bonds')
  bonds = mol.GetBonds()
  for i in range(len(bonds)):
    #[0].GetBondType())
    bond = bonds[i]
    a1 = bond.GetBeginAtomIdx()
    a2 = bond.GetEndAtomIdx()
    atom1 = mol.GetAtomWithIdx(a1)
    atom2 = mol.GetAtomWithIdx(a2)
    s = str(i) + ': ' + atom1.GetSymbol() + '(' + str(a1) + ')' + ' - ' + atom2.GetSymbol() + '(' + str(a2) + ')'
    print(s)

#
# Main
#

print_atom_bond('Brc1cc(ccc1NC(=O)Nc2ccc(nc2)C#N)[C@@H]3CNCCO3')