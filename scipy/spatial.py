#Triangulation
#Delaunay()
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()

#ConvexHull()
hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

#points = np.array([
    # [2, 4],
    # [3, 4],
    #[3, 0],
    #[2, 2],
    #[4, 1]
#])

#KDTrees
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

#Distance Matrix types

p1 = (1, 0)
p2 = (10, 2)


#Euclidean Distance
res = euclidean(p1, p2)
print("euclidiean: ",res)

#Cityblock Distance (Manhattan Distance)
#Is the distance computed using 4 degrees of movement.
#E.g. we can only move: up, down, right, or left, not diagonally.
res = cityblock(p1, p2)
print("cityblock: ",res)

#Cosine Distance
#Is the value of cosine angle between the two points A and B.
res = cosine(p1, p2)
print("cosine",res)

#Hamming Distance
# Is the proportion of bits where two bits are different.
# It's a way to measure distance for binary sequences.
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print("hamming",res)
# eg:
# 010 ⊕ 011 = 001, d(010, 011) = 1.

# 010 ⊕ 101 = 111, d(010, 101) = 3.

# 010 ⊕ 111 = 101, d(010, 111) = 2.