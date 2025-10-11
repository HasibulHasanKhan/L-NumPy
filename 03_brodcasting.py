## Broascasting = automatic expansion of smaller arrays to match dimensions.

import numpy as np

a = np.array([1,2,3])
b = 2
print(a + b)

A = np.array([[1],[2],[3]])
B = np.array([10,20,30])

print(A + B)