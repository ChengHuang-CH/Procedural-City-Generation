import os, sys
import pickle
import numpy as np
from scipy.spatial import Delaunay, ConvexHull
import pyvista as pv
import time

path = os.path.join(os.getcwd(), ("../../"))
sys.path.append(path)
print(path)

#  ----------------------- terrain ----------------------------------
with open(path + "procedural_city_generation/temp/stubs_height_15_15", "rb") as f:
    file = f.read()
    points, triangles = pickle.loads(file)

for point in points:
    if point[2] > -0.1:
        print(point)

# ----------------- how to generate the terrain ---------------------
from PIL import Image

img = Image.open(path + 'procedural_city_generation/inputs/heightmaps/stubs_height.png')

# TODO: set these numbers to some file where they can be edited easier
rsize = img.resize(((15 + 20) * 10, (15 + 20) * 10))
array = np.asarray(rsize)

from copy import copy

array = np.rot90(copy(array), k=3)

# If image is a jpeg, all values have to be divided by 255
array = array[::, :, 0] / 255.

import matplotlib.pyplot as plt

plt.figure()
plt.title('z as 2d heat map')
p = plt.imshow(array)
plt.colorbar(p)
plt.show()

# print(
#     "You have selected a heightmap which has no .txt file yet, OR the given .txt file has the wrong dimensions. The parameter heightDif will be used to describe the height difference between the lowest and the highest points on the map.")
# h = 2
# print("Processing image")
#
# # TODO: Find and Fix this Bug
# array *= abs(h)
# # Caused weird bugs when -=h was used.. I still can't explain them...
# array -= h + 0.01
#
# # Create all necessary stuff for the heightmap
# from scipy.spatial import Delaunay as delaunay
#
# indices = np.vstack(np.unravel_index(np.arange(array.shape[0] * array.shape[1]), array.shape)).T
# points = np.column_stack((indices, array[indices[:, 0], indices[:, 1]]))
#
# triangles = np.sort(delaunay(indices).simplices)
#
# # TODO: set thse numbers to some file where they can be edited easier
# points *= [0.1, 0.1, 1]
# points -= np.array([(15 + 20) / 2, (15 + 20) / 2, 0])
# points = points.tolist()

# ----------------------------------------------------------------------------

import pickle

# with open(path + "/temp/" + name[0:-4] + "_" + str(singleton.border[0]) + "_" + str(singleton.border[1]), "wb") as f:
#     f.write(pickle.dumps([points, triangles.tolist()]))

import pickle

# ----------------- load 2d polygons -----------------------------
with open(path + "procedural_city_generation/temp/mycity_polygons.txt", "rb") as f:
    polylist = pickle.loads(f.read())

# ----------------- load o3d polygons ----------------------------
with open(path + "procedural_city_generation/outputs/mycity.txt", 'rb') as f:
    polygons = pickle.loads(f.read())
    print()

print(f'poly num： {len(polygons)}')

# ========================================================================================================

verts, faces, texname, texscale, shrinkwrap = polygons[9]
print(f'verts num： {len(verts)}')
print(f'face length： {len(faces)}')
verts = np.asarray(verts)
# tmp_verts = verts[faces[14]]
# print(tmp_verts)

# Perform triangulation
# hull = Delaunay(tmp_verts)


# Create a point cloud from the coplanar points
# point_cloud = pv.PolyData(tmp_verts)
#
# # Triangulate the point cloud
# mesh = point_cloud.delaunay_2d()
#
# # Get the triangle indices
# triangle_indices = mesh.faces.reshape(-1, 4)[:, 1:]
#
# # # Print the triangle indices
# # for triangle in triangle_indices:
# #     print(triangle)
#
# # mesh.plot(show_edges=True)
# p = pv.Plotter()
# p.add_mesh(mesh, show_edges=True)
# p.show()
# ========================================================================================================
# p = pv.Plotter()
# for face_i in range(len(faces)):
#     tmp_verts = verts[faces[face_i]]
#     # Create a point cloud from the coplanar points
#     point_cloud = pv.PolyData(tmp_verts)
#
#     # Triangulate the point cloud
#     mesh = point_cloud.delaunay_2d()
#
#     # Get the triangle indices
#     triangle_indices = mesh.faces.reshape(-1, 4)[:, 1:]
#
#     # # Print the triangle indices
#     # for triangle in triangle_indices:
#     #     print(triangle)
#
#     # mesh.plot(show_edges=True)
#
#     p.add_mesh(mesh, show_edges=True)
# p.show()
# ========================================================================================================
# Plot the triangulation
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(projection='3d')
# ax.plot(tmp_verts[:,0], tmp_verts[:,1], tmp_verts[:,2], 'o')
# ax.plot_trisurf(tmp_verts[:, 0], tmp_verts[:, 1], tmp_verts[:, 2], triangles=triangle_indices)
#
# # plt.triplot(tmp_verts[:,0], tmp_verts[:,1], triangle_indices)
# plt.show()

# ========================================================================================================

# total_verts_num = 0
# all_verts_list = []
# all_tri_list = []
# for poly_i, poly in enumerate(polygons):
#     verts, faces, _, _, _ = poly
#     num_verts = len(verts)
#     num_faces = len(faces)
#
#     # print(f'poly {poly_i} --- num_verts: {num_verts}; num_faces: {num_faces}')
#
#     all_verts_list += verts
#
#     verts = np.asarray(verts)
#
#     for face_i, face in enumerate(faces):
#
#         if len(face) == 3:
#             new_tri = [vi + total_verts_num for vi in face]
#             # all_tri_list.append(new_tri)
#         else:
#             # print(f'Err: poly {poly_i} face {face_i} --- {len(face)}')
#             tmp_verts = verts[face]
#
#             point_cloud = pv.PolyData(tmp_verts)
#
#             # Triangulate the point cloud
#             mesh = point_cloud.delaunay_2d()
#
#             # Get the triangle indices
#             triangle_indices = mesh.faces.reshape(-1, 4)[:, 1:]
#
#             tri_indice = triangle_indices + total_verts_num
#             tri_indice_list = tri_indice.tolist()
#             all_tri_list += tri_indice_list
#
#             # try:
#             #     point_cloud = pv.PolyData(tmp_verts)
#             #
#             #     # Triangulate the point cloud
#             #     mesh = point_cloud.delaunay_2d()
#             #
#             #     # Get the triangle indices
#             #     triangle_indices = mesh.faces.reshape(-1, 4)[:, 1:]
#             #
#             #     tri_indice = triangle_indices + total_verts_num
#             #     tri_indice_list = tri_indice.tolist()
#             #     all_tri_list += tri_indice_list
#             # except:
#             #     print(f'Err: poly {poly_i} face {face_i} --- {len(face)} triangulation issue')
#
#             # print('other face length >3')
#
#     total_verts_num += num_verts
#
# print(len(all_verts_list), len(all_tri_list))
# ========================================================================================================

# ========================================================================================================
# t0 = time.time()
# for poly_i, poly in enumerate(polygons):
#     # if poly_i > 1:
#     #     continue
#     tri_list = []
#
#     verts, faces, _, _, _ = poly  # VERTS: nest list; faces: nest list
#     num_verts = len(verts)
#     num_faces = len(faces)
#
#     # print(f'poly {poly_i} --- num_verts: {num_verts}; num_faces: {num_faces}')
#
#     verts = np.asarray(verts)
#
#     for face_i, face in enumerate(faces):
#
#         if len(face) == 3:
#             tri_list.append(face)
#         else:
#             # print(f'Err: poly {poly_i} face {face_i} --- {len(face)}')
#
#             tmp_verts = verts[face]
#             # hull = ConvexHull(verts1, qhull_options='QJ')
#
#             # Create a point cloud from the coplanar points
#             point_cloud = pv.PolyData(tmp_verts)
#
#             # Triangulate the point cloud
#             mesh = point_cloud.delaunay_2d()
#
#             # Get the triangle indices
#             triangle_indices = mesh.faces.reshape(-1, 4)[:, 1:]
#             face = np.asarray(face)
#             tri_indice_list_org = face[triangle_indices]
#             tri_indice_list = tri_indice_list_org.tolist()
#             tri_list += tri_indice_list
#             # print(f'Err: poly {poly_i} face {face_i} --- {len(face)} triangulation issue')
#
# t1 = time.time()
# print(f't: {t1 - t0:.3f}s')

# 1.  get the bounding box of the scaled 3d mesh
# 2. reset the origin and camera view dynamically
# 3. build new coordinate system
# 4. generate the terrain map.
