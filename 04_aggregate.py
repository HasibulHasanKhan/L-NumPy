## Aggregate function = sumarize data and typically return a single value.

import numpy as np

arr = np.array([[2, 4, 7],[2, 4, 7]])

# print(np.sum(arr))
# print(np.mean(arr))
# print(np.std(arr)) # standard deviation
# print(np.var(arr)) # variation
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr))
# print(np.argmax(arr))

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))