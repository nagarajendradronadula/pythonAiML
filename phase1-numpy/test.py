import numpy as np

print(np.__version__)
print("======================================================")

# 1D array in NumPy
arr = np.array([1,2,3,4,5,6])
print(arr)
print(arr.shape)
print("======================================================")

# 2D array in NumPy
matrix = np.array([[1,2,3], [4,5,6]])
print(matrix)
print(matrix.shape)
print("======================================================")

# 3D array in NumPy
cube = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(cube)
print(cube.shape)

