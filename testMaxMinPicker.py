# %%
from rdkit.SimDivFilters import rdSimDivPickers
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

#
# MAIN
#

# %%
n_items = 1000
n_samples = 10

np.random.seed(0)
points = np.random.rand(n_items, 2)

# Calculate the Euclidean distance matrix
dm_np = distance_matrix(points, points)
picker = rdSimDivPickers.MaxMinPicker()
picker_name = 'MaxMin'
if False:
  picker = rdSimDivPickers.HierarchicalClusterPicker(rdSimDivPickers.ClusterMethod.WARD)
  picker_name = 'Hi WARD'
elif False:
  picker = rdSimDivPickers.HierarchicalClusterPicker(rdSimDivPickers.ClusterMethod.CLINK)
  picker_name = 'Hi CLINK'

dm_cluster = dm_np[np.tril_indices(n_items, -1)]
picks = picker.Pick(dm_cluster, n_items, n_samples)

# Plot the points
plt.figure(figsize=(8, 6))
for i, point in enumerate(points):
    if i in picks:
        plt.scatter(point[0], point[1], color='red', alpha=1)
    else:
        plt.scatter(point[0], point[1], color='blue', alpha=0.1)

plt.title('Random Points - ' + picker_name)
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')

# Show the plot
plt.show()
