import numpy as np

integers = np.array([1,2,3])

#print(integers)

print(type(integers))

integers = np.array([[1,2,3],[4,5,6]])

print(integers.dtype)

print(integers.ndim)

print(integers.shape) # number of dimensions

print(integers.size) # number of elements in the array

print(integers.itemsize) # amount of space that it takes = 4 kilobytes 

for row in integers:
    print(row)
    print()

    for col in row:
        print(col)
    print()


for i in integers.flat:
    print(i, end=' ')

print(np.zeros(5)) # creat an array of 5 0's 

print(np.ones(5)) # create an array of 5 1's 
print()
print()
print()
print()

array1 = np.ones((2,4), dtype = int)
print(array1)

array2 = np.full((3,5), 13)  # create an array of 3 rows and 5
                             # columns of the number 13

print(array2)

print(np.arange(5))

print(np.arange(5, 10))

print(np.arange(10, 1, -1))

print(np.linspace(0.0, 1.0, num = 5))  # 최소, 최대값 둘다 포함


array1 = np.arange(1,21)
print(array1)

array2 = array1.reshape(4,5)
print(array2)



array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)

print(array4)

numbers = np.arange(1, 6)

print(numbers * 2)

print(numbers) # original number not affected 

numbers += 10

print(numbers) # original number affected

print(numbers ** 3)


numbers = np.arange(1,6)
print(numbers * 2)
print(numbers)

numbers *= 2

print(numbers)


print(numbers >= 13)
numbers2 = np.arange(5, 10)

print(numbers2 > numbers)
print(numbers)
print(numbers2)

print(numbers == numbers2)

















