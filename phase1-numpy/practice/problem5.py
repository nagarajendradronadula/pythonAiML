'''
🟡 NumPy Problem 5 — Reshape & Transpose
Create problem5.py

🎯 Task:
Given this array:
pythonarr = np.arange(1, 13)   # [1 2 3 4 5 6 7 8 9 10 11 12]

Reshape it into a 3x4 matrix and print it
Reshape it into a 4x3 matrix and print it
Reshape it using -1 into a matrix with 6 columns and print it
Print the transpose of the 3x4 matrix


Expected Output:
3x4 Matrix:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

4x3 Matrix:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

-1 Reshape (6 cols):
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]

Transpose of 3x4:
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]

Hint: Remember reshape(-1, n) means "figure out the rows automatically"! 😉
'''

import numpy as np

pythonarr = np.arange(1,13)

arr = pythonarr.reshape(3,4)
print(f'3x4 Matrix: \n{arr}')
print(f'4x3 Matrix: \n{pythonarr.reshape(4,3)}')
print(f'-1 Reshape (6 cols): \n{pythonarr.reshape(-1,6)}')
print(f'Transpose of 3x4: \n{arr.T}')
