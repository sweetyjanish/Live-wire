import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

#connected components
num_components, labels = connected_components(newarr)
print("Number of connected components:", num_components)
print("Labels of connected components:", labels)

#dijkstra
print(dijkstra(newarr, return_predecessors=True, indices=0))