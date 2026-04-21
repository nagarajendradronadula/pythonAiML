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