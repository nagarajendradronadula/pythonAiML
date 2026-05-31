import numpy as np

# print(np.__version__)
# print("======================================================")

# NumPy Array Creation
# 1D array in NumPy
# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print(arr.shape)
# print("======================================================")

# 2D array in NumPy
# matrix = np.array([[1,2,3], [4,5,6]])
# print(matrix)
# print(matrix.shape)
# print("======================================================")

# 3D array in NumPy
# cube = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
# print(cube)
# print(cube.shape)
# print("======================================================")

#Shortcut Creation Functions
# print(np.zeros((3,3)))
# print(np.ones((2, 4)))
# print(np.arange(0, 10, 2))
# print(np.arange(1, 6))
# print(np.linspace(0, 1, 5))
# print(np.eye(6, 6))
# print(np.full((2,3), 5))
# print("======================================================")

# Indexing & Slicing
# arr = np.array([1,2,3,4,5])
# print(arr[0])
# print(arr[-1])
# print(arr[1:4])
# print(arr[::2])
# print(arr[::-1])

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[0,0])
# print(matrix[1,2])
# print(matrix[0, :])
# print(matrix[:, 1])
# print(matrix[0:2, 1:])
# print("======================================================")

# Array Math
a = np.array([1,2,3,4,5])
# print(a + 10)
# print(a * 2)
# print(a ** 2)

# b = np.array([10,20,30,40,50])
# print(a + b)
# print(a * b)
# print(a ** b)

# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.std(a))
# print("======================================================")

# Reshape and Transpose
# arr = np.arange(1,7)
# print(arr)

# print(arr.reshape(2,3))
# print(arr.reshape(-1, 2))
# print(arr.reshape(2, -1))
# matrix = np.array([[1,2,3],[4,5,6]])
# print(matrix)
# print(matrix.T)
# print("======================================================")

# Boolean Masking
# arr = np.array([10, 25, 3, 47, 8, 30])

# print(arr[arr < 15])
# print(arr[arr > 15])
# print(arr[(arr > 10) & (arr < 40)])
# print(np.where(arr > 15))
# print("======================================================")

# Random Module
# print(np.random.seed(42))
# print(np.random.rand(3))
# print(np.random.rand(2,3))
# print(np.random.randn(3))
# print(np.random.randint(0, 10, 5))
# print(np.random.choice([10,20,30,40,50]))
# print("======================================================")