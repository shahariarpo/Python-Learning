import numpy as np

a = np.array([[1, 2, 3]])

b = np.array([[1], [2], [3], [4]])

# either both of the number of the shape must match or either of the number is 1

print(a.shape)
print(b.shape)

print(a * b)