## **Numpy Notes**
refer to ~test.py~
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

**1️⃣ Creating arrays**
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