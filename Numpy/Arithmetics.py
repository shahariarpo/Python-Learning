import numpy as np

a = np.array([1, 2, 3])
b = np.array([1.233, 2.314, 3.432])

# scaler arithmetic

print(a + 1)
print(a - 2)
print(a * 3)
print(a / 4)
print(a ** 5)


# vectorized arithmetic

print(np.sqrt(a))
print(np.floor(b))
print(np.ceil(b))


# element-based arithmetic

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)


# comparison operator

a[a == 1] = 0
print(a)