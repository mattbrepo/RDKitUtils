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