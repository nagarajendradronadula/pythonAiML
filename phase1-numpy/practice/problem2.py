'''
🟢 NumPy Problem 2 — Zeros, Ones & Full
Create problem2.py

🎯 Task:

Create a 3x3 matrix of all zeros
Create a 2x4 matrix of all ones
Create a 3x3 matrix filled with 5s
Print all three


Expected Output:
Zeros:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

Ones:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]

Fives:
[[5 5 5]
 [5 5 5]
 [5 5 5]]
'''

import numpy as np

zeros = np.zeros((3,3))
ones = np.ones((2,4))
fives = np.full((3,3),5)

print(f'Zeroes: \n{zeros}')
print(f'Ones: \n{ones}')
print(f'Fives: \n{fives}')