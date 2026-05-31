'''
🟡 NumPy Problem 7 — Random Arrays & Statistics
Create problem7.py

🎯 Task:

Set random seed to 42
Create a 4x4 matrix of random integers between 1 and 100
Print the matrix
Print the min, max, mean and standard deviation of the matrix
Print the sum of each row
Print the sum of each column


Expected Output:
Random Matrix:
[[52 93 15 72]
 [61 21 83 87]
 [75 75 88 24]
 [35 10 34 27]]

Min: 10
Max: 93
Mean: 53.25
Std Dev: 28.02

Row Sums:    [232 252 262 106]
Column Sums: [223 199 220 210]

Hint: For row and column sums look into np.sum(arr, axis=?) — axis=0 goes down columns, axis=1 goes across rows! 😉
'''

import numpy as np

np.random.seed(42)
matrix = np.random.randint(1, 101, 16)
print(f'Random Matrix: {matrix.reshape(4,4)}')
print(f'Min: {np.min(matrix)}\nMax: {np.max(matrix)}\nMean: {np.mean(matrix)}\nStd Dev: {np.std(matrix)})')
matrix = matrix.reshape(4,4)
rowSum = np.sum(matrix, axis=1)
print(f'Row Sums: {rowSum}')
colSum = np.sum(matrix, axis=0)
print(f'Colummn Sums: {colSum}')