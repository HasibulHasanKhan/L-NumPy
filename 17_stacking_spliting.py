import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.hstack((a, b)))
print(np.vstack((a, b)))

mat = np.array([[1,2,3],[4,5,6]])
print(np.hsplit(mat, 3))
