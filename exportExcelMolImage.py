import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools

smiles = ['CCCCC', 'C(=O)CN', 'c1ccccc1']
df = pd.DataFrame({'NAME': ['A', 'B', 'C'], 'SMILES':smiles})

df['MolImage'] = [Chem.MolFromSmiles(s) for s in df['SMILES']]

# http://rdkit.org/docs/source/rdkit.Chem.PandasTools.html#SaveXlsxFromFrame
# IMPORTANT: it requires XlsxWriter to be installed (pip install XlsxWriter)
PandasTools.SaveXlsxFromFrame(df, '_export.xlsx', molCol='MolImage', size=(100, 200))