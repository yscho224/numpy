'''
use NumPy random-number generation to create an array of 
twelve random grades in the range 60 through 100, then
reshape the result into a 3-by-4 array. Calculate the average
of all the grades, the averages of the grades for each test
and the averages of the grades for each student. 
'''
import numpy as np
import random

grades = np.random.randint(60, 101, 12).reshape(3,4)
print(grades)

print('All grades', grades.mean())
print("AVG by each test", grades.mean(axis = 0))
print("AVG by each student", grades.mean(axis = 1))



