import numpy as np

arr = np.array([11, 2, 3, 40, 5, 42, 4, 7])

# x = np.where(arr%2 == 0)
x = np.searchsorted(arr, 4, side='right')

print(x)