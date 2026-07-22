import numpy as np

a = np.array([[17, 21, 33, 32, 16, 22],
              [24, 25, 36, 37, 14, 54]])

b = a[(a > 18)]
evens = a[a % 2 == 0]

print(a)        # preserves original
print(b)
print(evens)
