'''
🟠 NumPy Problem 9 — Array Manipulation
Create problem9.py

🎯 Task:

Create two 1D arrays:

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

Stack them vertically (one on top of the other)
Stack them horizontally (side by side)
Split the vertical stack into 2 equal arrays and print each
Print the flattened version of the vertical stack


Expected Output:
Vertical Stack:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]

Horizontal Stack:
[ 1  2  3  4  5  6  7  8  9 10]

Split Arrays:
[1 2 3 4 5]
[6 7 8 9 10]

Flattened: [ 1  2  3  4  5  6  7  8  9 10]

Hint: Look into np.vstack(), np.hstack(), np.split() and .flatten()! 😉
'''

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

arr = np.vstack((a,b))
print(f'Vertical Stack:\n{arr}')
print(f'Horizontal Stack:\n{np.hstack((a,b))}')
parts = np.split(arr,2)
print('Split Arrays:')
for part in parts:
    print(part)
print(f'Flattened: {arr.flatten()}')