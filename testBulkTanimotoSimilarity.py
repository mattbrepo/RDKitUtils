# %%
import pandas as pd
from rdkit import Chem, DataStructs
from rdkit.Chem import rdMolDescriptors

# %%
# load data
df = pd.read_csv('original.smi', sep='\t', header=None)
df['Run'] = 'Original'
df['RunIdx'] = list(range(1, len(df) + 1))

for idx in range(1, 5+1):
  df_idx = pd.read_csv('aB_' + str(idx) + '_run.smi', sep='\t', header=None, usecols=[0])
  df_idx['Run'] = str(idx)
  df_idx['RunIdx'] = list(range(1, len(df_idx) + 1))
  df = pd.concat([df, df_idx])

df.rename(columns={ df.columns[0]: "SMILES" }, inplace = True)

# %%
# check similarity
print('Molecules with Tanimoto distance 0')
ms = [Chem.MolFromSmiles(SMILES) for SMILES in df['SMILES']]
fps = [rdMolDescriptors.GetMorganFingerprintAsBitVect(m, 3, 2048) for m in ms]
count = 0
for idx_fp, fp in enumerate(fps): # not optimized!
  dists = DataStructs.BulkTanimotoSimilarity(fp, fps, returnDistance=True)
  for idx_dist, dist in enumerate(dists):
    if dist > 0 or idx_fp >= idx_dist:
      continue
    count = count + 1
    print(str(count) + ': Runs: ' + df.iloc[idx_fp].Run + ',' + df.iloc[idx_dist].Run +
          ' - Idxs: ' + str(df.iloc[idx_fp].RunIdx) + ',' + str(df.iloc[idx_dist].RunIdx))

print('Done')