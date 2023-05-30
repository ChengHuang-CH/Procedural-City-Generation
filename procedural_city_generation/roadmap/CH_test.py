import os, sys
import pickle
import numpy as np

path = os.path.join(os.getcwd(), ("../../"))
sys.path.append(path)
print(path)

# with open(path + "procedural_city_generation/temp/stubs_height_30_15", "rb") as f:
#     file= f.read()
#     points, triangles = pickle.loads(file)
#     print()


# If the given image has no .txt yet, write the corresponding.txt

# Load image and resize
from PIL import Image

img = Image.open(path + 'procedural_city_generation/inputs/heightmaps/stubs_height.png')

# TODO: set these numbers to some file where they can be edited easier
rsize = img.resize(((15 + 20) * 10, (15 + 20) * 10))
array = np.asarray(rsize)
from copy import copy

array = np.rot90(copy(array), k=3)

# If image is a jpeg, all values have to be divided by 255
array = array[::, :, 0] / 255.

print(
    "You have selected a heightmap which has no .txt file yet, OR the given .txt file has the wrong dimensions. The parameter heightDif will be used to describe the height difference between the lowest and the highest points on the map.")
h = 2
print("Processing image")

# TODO: Find and Fix this Bug
array *= abs(h)
# Caused weird bugs when -=h was used.. I still can't explain them...
array -= h + 0.01

# Create all necessary stuff for the heightmap
from scipy.spatial import Delaunay as delaunay

indices = np.vstack(np.unravel_index(np.arange(array.shape[0] * array.shape[1]), array.shape)).T
points = np.column_stack((indices, array[indices[:, 0], indices[:, 1]]))

triangles = np.sort(delaunay(indices).simplices)

# TODO: set thse numbers to some file where they can be edited easier
points *= [0.1, 0.1, 1]
points -= np.array([(15 + 20) / 2, (15 + 20) / 2, 0])
points = points.tolist()

import pickle

# with open(path + "/temp/" + name[0:-4] + "_" + str(singleton.border[0]) + "_" + str(singleton.border[1]), "wb") as f:
#     f.write(pickle.dumps([points, triangles.tolist()]))