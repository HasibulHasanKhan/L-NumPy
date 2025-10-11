import numpy as np

# arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# arr2 = np.array([])

# for x in arr:
#     for y in x:
#         arr2 = np.append(arr2, y)


## without loop : new array : 
# arr2 = arr.flatten()

## Numpy N-Dimensional Iterator :

# newarr = np.nditer(arr2)
# print(newarr)

# for x in np.nditer(arr2):
#     print(x)

# for x in np.nditer(arr2[:, ::2]):
#     print(x)

# for idx, x in np.ndenumerate(arr2):
#     print(idx, x)

# print(arr2)