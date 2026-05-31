'''
🟠 NumPy Problem 8 — Matrix Operations
Create problem8.py

🎯 Task:
Given these two matrices:
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7,  8],
              [9,  10],
              [11, 12]])

Print the shape of both matrices
Perform matrix multiplication of A and B and print the result
Print the shape of the result
Print the transpose of the result


Expected Output:
Shape of A: (2, 3)
Shape of B: (3, 2)

Matrix Multiplication (A @ B):
[[ 58  64]
 [139 154]]

Shape of Result: (2, 2)

Transpose of Result:
[[ 58 139]
 [ 64 154]]

Hint: Remember @ is matrix multiplication — the number of columns in A must equal the number of rows in B! 😉
'''

import numpy as np

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])

print(f'Shape of A: {A.shape}')
print(f'Shape of B: {B.shape}')
mul = A @ B
print(f'Matrix Multiplication (A @ B):\n{mul}')
print(f'Shape of Result: {mul.shape}')
print(f'Transpose of Result:\n{mul.T}')