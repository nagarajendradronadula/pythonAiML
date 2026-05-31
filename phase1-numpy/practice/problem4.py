'''
🟢 NumPy Problem 4 — Array Math
Create problem4.py

🎯 Task:
Given these two arrays:
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

Print a + b
Print a * b
Print a / b
Print the sum of array a
Print the mean of array b
Print the max of array a


Expected Output:
Addition:       [12 24 36 48 60]
Multiplication: [ 20  80 180 320 500]
Division:       [5. 5. 5. 5. 5.]
Sum of a:       150
Mean of b:      6.0
Max of a:       50
'''

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print(f'Addition: {a + b}')
print(f'Multiplication: {a * b}')
print(f'Division: {a / b}')
print(f'Sum of a: {np.sum(a)}')
print(f'Mean of b: {np.mean(b)}')
print(f'Max of a: {np.max(a)}')