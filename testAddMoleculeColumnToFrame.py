# %%
from rdkit import Chem
from rdkit.Chem import PandasTools
from rdkit.Chem import rdMolDescriptors, Draw
import pandas as pd

# %%

df = pd.DataFrame({'SMILES': ['CC(=O)NCCC1=CNc2c1cc(OC)cc2', 'CCCCC', 'CC(=O)N', 'CCF']})
PandasTools.AddMoleculeColumnToFrame(df, 'SMILES', 'Molecule')

# %%
Draw.MolsToGridImage(df['Molecule'],
                     legends=df['SMILES'].tolist(), 
                     molsPerRow=3, subImgSize=(400, 400))
