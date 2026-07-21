import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.zeros(4, int)
c = np.arange(1, 10)

d = np.array([2, 4, 5, 0, -1, 3])

print(a.shape)                                  # shape of an array
print(a[0][1])                                  # individual element of an array
print(a)                                        # from begin to end of an array
print(np.sort(d[:], kind='mergesort'))          # sort array (using 'kind' specifier) and print from begin to end of an array
print(a.ndim)                                   # dimension of an array
print(np.reshape(c, [3, 3]))              # reshape arrays
print(np.flip(d))                               # reverse an array
print(a[0:2])                                   # array slicing by row
print(a[0:2, 0:2])                                 # array slicing by column
