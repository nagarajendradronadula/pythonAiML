'''
🟢 NumPy Problem 1 — Create & Explore an Array
Create a file problem1.py inside phase1-numpy/practice/

🎯 Task:
1. Import NumPy
2. Create a 1D array of numbers from 1 to 10
3. Print the array
4. Print its shape
5. Print its data type


Expected Output:
Array: [ 1  2  3  4  5  6  7  8  9 10]
Shape: (10,)
Data Type: int64

Hint: Use np.arange() 😉
'''

import numpy as np

arr = np.arange(1,11)
print(arr)
print(arr.shape)
print(arr.dtype)
