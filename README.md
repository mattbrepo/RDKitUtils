# RDKitUtils
Utilities using [RDKit](https://www.rdkit.org/).

**Language: Python**

**Start: 2021**

## Why
I collected here a series of utilities using RDKit (Open-Source Cheminformatics Software, version originally used: Q32017):

- calcCentroidFingerprint: calculate the centroid of a set of fingerprints
- calcDescriptors: calculate some basic molecular descriptors
- drawMolecule: draw a molecule (even with atom index)
- exportExcelMolImage: export a Pandas dataframe with molecule image to Excel
- printAtomBond: print atoms and bonds of a molecule
- printChiral: print chirality information of a molecule
- printPeriodicTable: print periodic table information
- sanitizeMol: sanitize a SMILES molecule
- sanitizeMolFile: sanitize a molecular file
- testBulkTanimotoSimilarity: test of _BulkTanimotoSimilarity_ function while working on different Pandas dataset of molecules
- testAddMoleculeColumnToFrame: test of _AddMoleculeColumnToFrame_ function to add a Molecule column to a Pandas dataframe (also molecules shown using _Draw.MolsToGridImage_)
- testMaxMinPicker: test of diversity and similarity pickers functions (e.g., _HierarchicalClusterPicker_)
- testSmilesMolSupplier: test of the _SmilesMolSupplier_ function

## Code example

#### Load molecules and calculate fingerprints:
```python
mySMILES = ['CCCCF', 'C1CCCCC1', 'C(=O)CN']
mols = [Chem.MolFromSmiles(SMILES) for SMILES in mySMILES]
fps = [Chem.rdMolDescriptors.GetMorganFingerprintAsBitVect(m, 3, 512) for m in mols]
```

#### Calculate molecular descriptor MW:
```python
from rdkit.Chem import rdMolDescriptors
import rdkit.Chem.Descriptors as Descriptors
MW = Descriptors.ExactMolWt(mol)
```

#### Draw a molecule
```python
from rdkit.Chem import Draw
Draw.MolToFile(mol, IMAGE_FILE_NAME, size=(1024, 768), fitImage=True)
Draw.MolsToGridImage(mols, molsPerRow=3, subImgSize=(400, 400))
```

#### Loop on bonds
```python
bonds = mol.GetBonds()
for i in range(len(bonds)):
  bond = bonds[i]
  a1 = bond.GetBeginAtomIdx()
  a2 = bond.GetEndAtomIdx()
  atom1 = mol.GetAtomWithIdx(a1)
  atom2 = mol.GetAtomWithIdx(a2)
```

#### Sanitized and canonical SMILES
```python
mol = Chem.MolFromSmiles(SMILES, sanitize = True)
Chem.MolToSmiles(mol)
Chem.CanonSmiles(mol)
```

#### Compare two molecules
```python
mol1 = Chem.MolFromSmiles('Nc1ccccc1')
mol2 = Chem.MolFromSmiles('c1c(N)cccc1')
print(Chem.MolToSmiles(mol1) == Chem.MolToSmiles(mol2))
```

#### Export Excel file with molecule image

**IMPORTANT: XlsxWriter needs to be installed (pip install XlsxWriter)**
```python
df['MolImage'] = [Chem.MolFromSmiles(s) for s in df['SMILES']]
PandasTools.SaveXlsxFromFrame(df, 'export.xlsx', molCol='MolImage', size=(100, 200))
```
