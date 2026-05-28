import numpy as np

m = np.arange(1, 25).reshape(4, 6)

print("Matrix:")
print(m)
print()

# Indexing
print("m[1,3]:")
print(m[1,3])
print()

# Column slicing
print("m[:,2]:")
print(m[:,2])
print()

# Submatrix slicing
print("m[1:3,2:5]:")
print(m[1:3,2:5])
print()

# Boolean masking
print("m[m > 12]:")
print(m[m > 12])
print()

# Flatten
print("Flattened:")
print(m.flatten())
print()

# Reshape
a = np.arange(1,11)

print("Reshaped:")
print(a.reshape(2,5))