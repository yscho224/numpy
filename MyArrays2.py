import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90],
                     [94, 77, 90], [100, 81, 82]])

print(grades)
print(grades.sum())

print(grades.min())

print(grades.max())

print(grades.mean())

print(grades.std())

print(grades.var())

print(grades.mean(axis=0)) # average score of a first test (column)

print(grades.mean(axis=1)) # average of all students (row) y축을기준으로다더함

numbers = np.array([1,4,9,16,25,36])

print(np.sqrt(numbers))

grades = np.array([[87, 96, 70], [100, 87, 90],
                     [94, 77, 90], [100, 81, 82]])

print(grades[0,1])  #96

print(grades[1])

print(grades[0:2])
print()
print()
print()
print()

#print(grades[1,2]) # addressing the value 
#print(grades[[1,3]]) # specifiying the row, 2brackets = row 
#print()
#print()
#print()
#print(grades[:,0])  # all the rows but first column 
#print(grades[:,1:3])

# shallow copy , views allow you to look across multiple tables, just look
# into data , it affects the original array as well. 
numbers = np.arange(1,6)
number2 = numbers.view()

#print(number2)
numbers[1] *= 10
#print(number2)
#print(numbers)


number2[1] /= 10
#print(number2) 

numbers2 = numbers[0:3]
#print(numbers2)
numbers[1] *= 20
#print(numbers)

# deep copies, makes a copy of array and it has two separate arrays

numbers2 = numbers.copy()

grades = np.array([[87,96,70], [100,87,90]])
#print(grades.reshape(1,6)) #reshape creates/is a shallow copy 
                           # or a view
#print(grades)
# grades.resize(1,6)

# print(grades)

flattened = grades.flatten()    # flattens it all out into one row
#print(flattened)
#print(grades)

raveled = grades.ravel() # 
#print(raveled)
#print(grades)

raveled[5] = 99 
#print(grades)

grades = np.array([[87,96,70], [100,87,90]])
grades2 = grades.T
#print(grades)


grades = np.array([[87,96,70], [100,87,90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades,grades2))
print(h_grades)

v_grades = np.vstack((grades,grades2))
print(v_grades)
