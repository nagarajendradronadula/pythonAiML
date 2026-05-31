'''
🔴 NumPy Problem 10 — Real World Mini Challenge
Create problem10.py
This one simulates a real ML scenario — analyzing a student marks dataset! 🎓

🎯 Task:
# 5 students, 4 subjects (Maths, Science, English, History)
marks = np.array([[85, 92, 78, 90],
                  [70, 65, 88, 72],
                  [95, 98, 92, 96],
                  [60, 55, 70, 58],
                  [78, 82, 75, 80]])

Print the average marks of each student (row-wise)
Print the average marks of each subject (column-wise)
Print the highest scoring student's index
Print the lowest scoring subject's index
Find all students who have average marks above 80 and print their row indices
Normalize the marks between 0 and 1 using:

normalized = (marks - min) / (max - min)

Expected Output:
Average per Student:  [86.25 73.75 95.25 60.75 78.75]
Average per Subject:  [77.6 78.4 80.6 79.2]

Highest Scoring Student Index: 2
Lowest Scoring Subject Index:  0

Students with avg > 80: [0 2]

Normalized Marks:
[[0.58 0.86 0.53 0.84]
 [0.23 0.10 0.77 0.30]
 [1.00 1.00 0.88 1.00]
 [0.00 0.00 0.35 0.00]
 [0.42 0.63 0.49 0.51]]

Hints:

np.mean(marks, axis=1) → average per student
np.argmax() → returns index of maximum value
np.where() → returns indices where condition is true 😉
'''

import numpy as np

marks = np.array([[85, 92, 78, 90],
                  [70, 65, 88, 72],
                  [95, 98, 92, 96],
                  [60, 55, 70, 58],
                  [78, 82, 75, 80]])

maxAvg = np.average(marks, axis=1)
print(f'Average per Student: {maxAvg}')
print(f'Average per Student: {np.mean(marks, axis=1)}')

minAvg = np.average(marks, axis=0)
print(f'Average per Subject: {minAvg}')
print(f'Average per Subject: {np.mean(marks, axis=0)}')

maxMarks = np.max(maxAvg)
highScore = np.where(maxAvg == maxMarks)
print(f'Highest Scoring Student Index: {highScore[0][0]}')
print(f'Highest Scoring Student Index: {np.argmax(maxAvg)}')

minMarks = np.min(minAvg)
lowScore = np.where(minAvg == minMarks)
print(f'Lowest Scoring Student Index: {lowScore[0][0]}')
print(f'Lowest Scoring Student Index: {np.argmin(minAvg)}')

avg80 = np.where(maxAvg > 80)
print(f'Students with avg > 80: {avg80[0]}')
maxVal = np.max(marks)
minVal = np.min(marks)
print(f'max val: {maxVal} min val: {minVal}')
normalisedMarks = (marks - minVal) / (maxVal - minVal)
print(f'Normalized Marks:\n{np.round(normalisedMarks, 2)}')