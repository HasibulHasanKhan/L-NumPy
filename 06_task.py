# NumPy aims to provide an array object that is up to 5ox faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np

# arr = np.array((1,2,3,4,5))
arr2 = np.array([1, 2 ,3 ,4 ,5])
arr3 = np.array([[1,2,3], [4,5,6]])
arr4 = np.array([[[1,2],[4,5]], [[6,7], [8,9]]])


## [start:end:step]
# print(arr2[0:5:2])
# print(arr2[::2])
# print(arr3[1, 1:4])

# print(arr4[1, 0, 1])
# print(arr3[1, 2])
# print(arr[2] + arr[3])
# print(arr.ndim)
# print(np.__version__)