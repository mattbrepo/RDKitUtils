from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import AllChem
from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions
from IPython.display import SVG
import os

IMAGE_FILE_NAME = "molecule.png"

def _getMol(SMILES):
  mol = Chem.MolFromSmiles(SMILES)
  return mol
  
def _drawMol(mol):
  #fig = Draw.MolToMPL(m, size=(800, 600))
  #fig.savefig(IMAGE_FILE_NAME, dpi=100)
  MolDrawing.atomLabelFontSize = 18
  MolDrawing.atomLabelMinFontSize = 18
  # vedi __init__.py di rdkit
  Draw.MolToFile(mol, IMAGE_FILE_NAME, size=(1024, 768), fitImage=True)

# https://iwatobipen.wordpress.com/2017/02/25/draw-molecule-with-atom-index-in-rdkit/
def _mol_with_atom_index(mol, onlyIdxs):
  atoms = mol.GetNumAtoms()
  for idx in range(atoms):
    atomIdx = mol.GetAtomWithIdx(idx).GetIdx()
    if len(onlyIdxs) == 0 or atomIdx in onlyIdxs:
      mol.GetAtomWithIdx(idx).SetProp('molAtomMapNumber', str(atomIdx))
  return mol
    
def drawMol(SMILES):
  mol = _getMol(SMILES)
  _drawMol(mol)

def drawMolWithAtomIdx(SMILES, onlyIdxs = []):
  mol = _getMol(SMILES)
  mol = _mol_with_atom_index(mol, onlyIdxs)
  _drawMol(mol)

#
# Main
#

#drawMol('CN')
drawMolWithAtomIdx('CC(CC=C)C(C)CC(O)C(O)C1CCC2OC3CC4OC5C=C(C)CC6OC7CC8OC9CC%10OC(CCC%10OC9CCC8OC7CC6OC5CC4OC3CC2O1)C1CCC2OC3CC4OC5CC6OC7CCCOC7CC6OC5CCC4OC3CC2O1', [1, 2, 3, 5, 7, 8, 10, 12, 23, 36, 58]) # simplified maitotoxin

os.system("start " + IMAGE_FILE_NAME)