## **Numpy Notes**
refer to [Test.py](../phase1-numpy/test.py)
## **Topic 1: Arrays & Array Creation**

**What is an array?**
An Numpy array is like a python list but supercharged. Its the fundamental building block of everything in ML.

```
 # Python list
 my_list = [1,2,3,4,5]

 # NumPy array - same data, but way more powerful
 import numpy as np
 my_array = np.array([1,2,3,4,5])
```

**Why not just use a Python list?**
```
# Python list - can't do math directly
a = [1,2,3]
b = [4,5,6]
a + b # [1,2,3,4,5,6] <- just joins them!

# NumPy array - math works element wise
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b # [5,7,9] <- actual addition! ✅
```

## **1️⃣ Creating arrays**
from a Python list
```
import numpy as np

# 1D array
arr = np.array([1,2,3,4,5])
print(arr) #[1,2,3,4,5]

# 2D array (matrix - rows and columns)
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
#[1,2,3]
#[4,5,6]

#3D array (like a cube)
cube = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print(cube)
# 1  2  3
# 4  5  6
# 7  8  9
# 10 11 12
```

**Shortcut Creation Functions**
```
#All Zeros
np.zeros((3,3))
#[[0. 0. 0.]
#[0. 0. 0.]
#[0. 0. 0.]]

#All ones
np.ones((2,4))
#[[1. 1. 1. 1.]
#[1. 1. 1. 1.]]

#Like range - arrange(start,stop,step)
np.arrange(0, 10, 2) #[0 2 4 6 8]
np.arrange(1, 6) #[1 2 3 4 5]

#Evenly spaced between two numbers
np.linspace(0, 1, 5) #[0.   0.25 0.5   0.75 1. ]

#Identity matrix (diagonal 1s,  rest 0s)
np.eye(3)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]

#Fill with a specific value
np.full((2,3), 7)
#[[7 7 7]
# [7 7 7]]
```

**💡 Fact:** ```np.zeros``` and ```np.ones``` are used in ML to initialise weights. ```np.arrange``` and ```np.linspace``` are used to generate data points.

## **2️⃣ Array Properties**

Every NumPy array has properties that tell you about its structure:
```
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape) # (2, 3) -> 2 rows and 3 columns
print(arr.ndim) # 2 -> number of dimensions
print(arr.size) # 6 -> total elements
print(arr.dtype) # int64 -> data type
```

**Visualizing Dimensions**
```
1D array -> [1,2,3,4]           shape = (4,)
2D array -> [[1,2,3],           shape = (2,3)
            [4,5,6]]
3D array -> [[[1,2], [3,4]],    shape = (2,2,2) # length, breadth/width, height
            [[5,6],[7,8]]]
```

**💡 Fact:** In ML, 1D = a single data point, 2D = a dataset (rows = samples, columns = features), 3D = images or sequences

## **3️⃣ Data Types**

NumPy arrays are strict - all elements must be of the same type:
```
int_arr = np.array([1, 2, 3])
floar_arr = np.array([1.0, 2.0, 3.0])
bool_arr = np.array([True, False])

# Specify type explicitly
arr = np.array([1,2,3], d_type = float) # [1. 2. 3.]

# Convert type
arr.astype(int) # back to int
arr.astype(str) # converted to string ['1.0', '2.0', '3.0']
```

**💡 Fact:** If you mix types, NumPy upcasts silently:
```
np.array([1, 2, 3.0]) # becomes float64 - the int 1 becomes float 1.0
np.array([1, 2, True]) # becomes int64 - True becomes 1
```

## **4️⃣ Indexing and Slicing**
Just like the Python lists, but extended to multiple dimensions

```
arr = np.array([10, 20, 30, 40, 50])

arr[0]      # 10 - first element
arr[-1]     # 50 - last element
arr[1:4]    # [20, 30, 40] 
arr[::2]    # [10, 30, 50] - every 2nd element
arr[::-1]   # [50, 40, 30, 20, 10] - reversed
```

**2D Indexing** - [row, column]
```
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

matrix[0,0]     # 1 = row -> 0, col -> 0
matrix[1,2]     # 6 = row -> 1, col -> 2 
matrix[0, :]    # [1, 2, 3] - entire first row
matrix[:, 1]    # [2, 5, 8] - entire second column
matrix[0:2, 1:] # [[2,3], [5, 6]] - submatrix
```
**💡 Fact:** matrix[:, 0] - extracting a full column - is something you'll do constantly in ML to grab a specific feature from a dataset!

## **5️⃣ Array Math**
```
a = np.array([1,2,3,4,5])

# Scalar operations - applies to every element
a + 10  # [11, 12, 13, 14, 15]
a * 2   # [2, 4, 6, 8, 10]
a ** 2  # [1, 4, 9, 16, 25]

# Element-wise with another array
b = np.array([10,20,30,40,50])
a + b   # [11, 22, 33, 44, 55]
a * b   # [10, 40, 90, 160, 250]

# Aggregate functions
np.sum(a)   # 15
np.mean(a)  # 3.0
np.max(a)   # 5
np.min(a)   # 1
np.std(a)   # standard deviation -> 1.41
```
**💡 Fact:** Remember @ is matrix multiplication — the number of columns in A must equal the number of rows in B!

## **6️⃣ Reshape & Transpose**
```
arr = np.arrange(1,7)       # [1,2,3,4,5,6]

# Reshape into 2d
arr.reshape(2,3)            # [[1,2,3],[4,5,6]]

# -1 means "figure out this dimension automatically"
arr.reshape(-1,2)           # (3,2) -> NumPy calculates 3
arr.reshape(2,-1)           # (2,3) -> NumPy calculates 3

matrix = np.array([[1,2,3],[4,5,6]])
matrix.T [[1,4],[2,5],[3,6]]
```

## **7️⃣ Boolean Masking**
```
arr = np.array([10,25, 3, 47, 8, 30])

# Filter elements greater than 15
arr[arr > 15]                   # [25 47 30]

# Multiple conditions
arr[(arr > 10) & (arr < 40)]    # [25 30]

# Where function - return indices
np.where(arr > 15)              # (array([1,3,5]),)
```

## **8️⃣ Random Module**
```
np.random.seed(42)                  # fix randomness - reproducible results
np.random.rand(3)                   # [0.37 0.95 0.73] - 0 to 1
np.random.rand(2,3)                 # 2x3 matrix, values 0 to 1
np.random.randn(3)                  # normal distribution (mean = 0, std = 1) basically all integers
np.random.randint(0,10,5)           # 5 random ints between 0-9 (start, end(excluded), number of numbers)
np.random.choice([10,20,30,40,50])  # random pick from array
```

## **🧠 Key Things to Remember**
```
np.array()          -> create array
np.shape()          -> dimensions
np.dtype()          -> data type
np.reshape()        -> change shape
np.T                -> transpose
np.arr[arr > x]     -> boolean masking
np.sum/mim/max      -> aggreagation
@                   -> matrix multiply
*                   -> element-wise multiply
```