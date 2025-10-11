# NumPy aims to provide an array object that is up to 5ox faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# By default python have these data types
# strings 
# integers
# float
# boolean
# complex

## NumPy have some extra data type :
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type(void)

import numpy as np


# arr = np.array((1,2,3,4,5))
# arr = np.array([1.1, 2.1, 3.1])
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2 = np.array([1, 2 ,3 ,4 ,5])
arr3 = np.array([[1,2,3], [4,5,6]])
arr4 = np.array([[[1,2],[4,5]], [[6,7], [8,9]]])








# newarr = arr.reshape(4, 3)
# print(newarr)

# newarr2 = arr.reshape(2, 3, 2)
# print(newarr2)


# newarr3 = arr.reshape(-1)



# newarr = arr.astype('i')
# print(newarr)
# print(arr3.shape)
# x = arr2.copy()
# print(x)
# x2 = arr2.view()
# arr2[0] = 22
# print(x2)

## [start:end:step] ## slicing 
# print(arr2[0:5:2])
# print(arr2[::2])
# print(arr3[1, 1:4])
# print(arr3[0:2, 2]) ## take row 0:2 , 0 and 1 then show value 2 index .
# print(arr3[0:2, 1:4])
# print(arr.dtype)
# print(arr4[1, 0, 1])
# print(arr3[1, 2])
# print(arr[2] + arr[3])
# print(arr.ndim)
# print(np.__version__)