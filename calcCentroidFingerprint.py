# %%
from rdkit import Chem, DataStructs
import rdkit.Chem.Descriptors as Descriptors
import numpy as np

# %%
# load data and calculate fingerprint
mySMILES = ['CCCCF', 'C1CCCCC1', 'C(=O)CN']
mols = [Chem.MolFromSmiles(SMILES) for SMILES in mySMILES]
fps = [Chem.rdMolDescriptors.GetMorganFingerprintAsBitVect(m, 3, 512) for m in mols]

# %%
# in case only a subset must be selected
cluster_idxs = [0, 1, 2]
cluster_fps = [fp for idx, fp in enumerate(fps) if idx in cluster_idxs]

#%% 
# calculate centroid of the fingerprint
np_cluster_fps = np.array([np.array(fp) for idx, fp in enumerate(fps) if idx in cluster_idxs])
np_centroid = np.mean(np_cluster_fps, axis=0)

#%% 
# calculate distances of each fingerprint from the centroid
np_distances = np.array([np.linalg.norm(arr - np_centroid) for arr in np_cluster_fps])
print(np_distances)