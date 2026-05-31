'''
🟡 NumPy Problem 6 — Boolean Masking
Create problem6.py

🎯 Task:
Given this array:
pythonarr = np.array([15, 3, 22, 8, 47, 11, 36, 5, 29, 18])

Print all elements greater than 15
Print all elements less than or equal to 10
Print all elements that are between 10 and 30 (inclusive)
Replace all elements greater than 30 with 0 and print the result


Expected Output:
Greater than 15:    [22 47 36 29 18]
Less than or equal to 10:  [ 3  8  5]
Between 10 and 30:  [15 22 11 29 18]
Replaced > 30 with 0: [15  3 22  8  0 11  0  5 29 18]

Hint: For task 4 use arr[condition] = 0 — but make a copy of the array first so the original doesn't change! 😉
'''

import numpy as np

pythonarr = np.array([15, 3, 22, 8, 47, 11, 36, 5, 29, 18])

print(f'Greater than 15: {pythonarr[(pythonarr > 15)]}')
print(f'Less than or equal to 10: {pythonarr[(pythonarr <= 10)]}')
print(f'Between 10 and 30: {pythonarr[(pythonarr > 10) & (pythonarr < 30)]}')
arr = pythonarr.copy()
arr[arr > 30] = 0
print(f'Replaced > 30 with 0: {arr}')