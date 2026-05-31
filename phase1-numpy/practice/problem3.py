'''
🟢 NumPy Problem 3 — Indexing & Slicing
Create problem3.py

🎯 Task:
Given this matrix:
pythonmatrix = np.array([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12]])

Print the element at row 1, column 2
Print the entire second row
Print the entire third column
Print the submatrix of first 2 rows and last 2 columns


Expected Output:
Element: 7
Second Row: [5 6 7 8]
Third Column: [ 3  7 11]
Submatrix:
[[ 3  4]
 [ 7  8]]

Hint: Remember matrix[row, col] and : for selecting all! 😉
'''

import numpy as np

matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(f'Element: {matrix[1,2]}')
print(f'Second row: {matrix[1,:]}')
print(f'Third Column: {matrix[:, 2]}')
print(f'Submatrix: \n{matrix[:2,2:]}')