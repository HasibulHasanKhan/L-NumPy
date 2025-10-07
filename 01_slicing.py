import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

## arr[start:end:step]
# print(arr[::-1])

## Column selection : 
# print(arr[:, ::2]) ## every 2nd column.

# print(arr[:, ::-1]) ## reverse 

print(arr[0:2, 0:2])