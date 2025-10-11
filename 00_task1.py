import numpy as np


## two dimension :

arr = np.array([

      ['A', 'B' ,'C'], 
      ['D', 'E', 'F'], 
      ['G', 'H', 'I']
    
    ])



print(arr.ndim)

## Three dimension : 

import numpy as np

arr = np.array([
    [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ],
    [
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R']
    ]
])

print(arr)
print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)

print(arr[0, 0, 2])