# arithmetic

import numpy as np

array = np.array([1,2,3,4,5])

print(array + 2)  
# Output: [3 4 5 6 7]
# NumPy adds 2 to every element
# Normal Python list: [1,2,3,4,5] + 2 gives TypeError
# But [1,2,3] + [4,5] concatenates lists [1,2,3,4,5]

print(array - 2)  
# Output: [-1  0  1  2  3]
# NumPy subtracts 2 from every element
# Normal Python list: [1,2,3] - 2 gives TypeError

print(array * 2)  
# Output: [ 2  4  6  8 10]
# NumPy multiplies every element by 2
# Normal Python list: [1,2,3] * 2 repeats the list
# Output: [1,2,3,1,2,3]

print(array / 2)  
# Output: [0.5 1.  1.5 2.  2.5]
# NumPy divides every element by 2
# Normal Python list: [1,2,3] / 2 gives TypeError

print(array ** 2)  
# Output: [ 1  4  9 16 25]
# NumPy squares every element
# Normal Python list: [1,2,3] ** 2 gives TypeError

#vectorized math functions
arr=np.array([1.3,2.5,3.9])
print(np.sqrt(arr))  
# Output: [1.         1.41421356 1.73205081 2.         2.23606798]
# NumPy finds square root of every element
# Normal Python needs math.sqrt() with a loop or list comprehension
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))
print(np.pi)


radii=np.array([1,3,4,5])
print(np.pi * radii**2)

#element wise arithematic
array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1 + array2)  # Output: [5 7 9]
print(array1 - array2)  # Output: [-3 -3 -3]
print(array1 * array2)  # Output: [ 4 10 18]
print(array1 / array2)  # Output: [0.25 0.4 0.5]

#comparison operators
scores= np.array([100,90,80,33])
print(scores==100)
print(scores>=90)
scores[scores<60]=0
print(scores)