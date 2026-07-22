import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(a))
print(np.mean(a))
print(np.std(a))
print(np.var(a))
print(np.min(a))
print(np.max(a))
print(np.argmin(a))
print(np.argmax(a))
print(np.sum(a, axis=1))